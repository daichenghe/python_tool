const SerialPort = require('serialport');
const net = require('net');

const buffer = require('buffer');
buffer.INSPECT_MAX_BYTES = 1500;

// serialport config
const ComName = 'com23';
let serialPortBuf = Buffer.alloc(0);
const GGADELIMITER = Buffer.from('\r\n');

// ntripcaster config
/*
const host = 'rtk.aceinna.com';
const port = '2201';
const mountPoint = 'RTK';
const userAgent = 'NTRIP Aceinna CloudRTK 1.0';
const username = 'aceinna';
const password = 'GWQOCSILH4WPM4XSNE2M';
*/
const host = 'rtk.aceinna.com';
const port = '2201';
const mountPoint = 'RTK';
const userAgent = 'NTRIP Aceinna CloudRTK 1.0';
const username = 'aceinna';
const password = 'TEL8IOZTBJVVJ0IT';

// serialPort object
let serialPort = null;
// ntrip object
let ntripClient = null;

// ntrip status
let ntripIsReady = false;
// serialport status
let portIsReady = false;

// app start
function start() {
  connectSerialPort();
  connectNtripcaster();
}

start();

// make a do once function
function doOnce(func) {
  let done = false;
  return function innerOnce() {
    if (done) {
      return;
    }
    done = true;
    func.call(this);
  };
}

// sleep function
function sleep(ms) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve();
    }, ms);
  });
}


// init serialport
function connectSerialPort() {
  if (serialPort) {
    serialPort.removeAllListeners();
    serialPort = null;
  }

  serialPort = new SerialPort(ComName, {
    baudRate: 460800, 
    dataBits: 8, 
    parity: 'none', 
    stopBits: 1, 
    flowControl: false
  });
  
  serialPort.on('open', () => {
    portIsReady = true;
    console.log('serialport is open');
  });
  
  serialPort.on('data', data => {
    serialPortBuf = Buffer.concat([serialPortBuf, data]);
    while(true) {
      const idx = serialPortBuf.indexOf(GGADELIMITER);
      if (idx < 0) {
        return;
      }
      const gga = serialPortBuf.slice(0, idx + GGADELIMITER.length);
      writeToNtrip(gga);
      serialPortBuf = serialPortBuf.slice(idx + GGADELIMITER.length);
    }
  });

  const doneOnce = doOnce(async () => {
    await sleep(1000);
    connectSerialPort();
  });
  
  serialPort.on('close', () => {
    portIsReady = false;
    console.log('serialport is close');
    doneOnce();
  });
  
  serialPort.on('error', err => {
    portIsReady = false;
    console.error('serialport error', err);
    doneOnce();
  });
}

// init ntripcaster connect
function connectNtripcaster() {
  if (ntripClient) {
    ntripClient.removeAllListeners();
    ntripClient = null;
  }

  ntripClient = net.createConnection({
    host,
    port
  }, () => {
    const authorization = Buffer.from(
      username + ':' + password,
      'utf8'
    ).toString('base64');
    const data = `GET /${mountPoint} HTTP/1.0\r\nUser-Agent: ${userAgent}\r\nAuthorization: Basic ${authorization}\r\n\r\n`;
    ntripClient.write(data);
  });
  
  ntripClient.on('data', data => {
    if (ntripIsReady) {
      writeToPort(data);
      return;
    }
  
    if (data.toString() === 'ICY 200 OK\r\n\r\n') {
      ntripIsReady = true;
    }
  });

  const doneOnce = doOnce(async () => {
    await sleep(1000);
    connectNtripcaster();
  });
  
  ntripClient.on('close', () => {
    ntripIsReady = false;
    console.log('ntripclient is close');
    doneOnce();
  });
  
  ntripClient.on('error', err => {
    ntripIsReady = false;
    console.error('ntripclient error', err);
    doneOnce();
  });  
}

// write data to ntripcaster
function writeToNtrip(data) {
  if (!ntripIsReady && ntripClient) {
    console.log('ntripclient is not ready');
    return;
  }
  console.log(data.toString());
  ntripClient.write(data);
}

// write data to serialport
function writeToPort(data) {
  if (!portIsReady && serialPort) {
    console.log('serialport is not ready');
    return;
  }
  console.log(data);
  serialPort.write(data);
}
