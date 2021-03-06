const SerialPort = require('serialport');
const net = require('net');
const fs = require('fs');


const buffer = require('buffer');
buffer.INSPECT_MAX_BYTES = 1500;

// serialport config
const ComName = 'com92';
let serialPortBuf = Buffer.alloc(0);
const GGADELIMITER = Buffer.from('\r\n');

// ntripcaster config
//const host =  '10.0.4.126';
const host = '47.116.1.17';
//'rtk.aceinna.com';//'10.0.20.21';//'106.12.40.121';
const port = '2201';
const mountPoint = 'RTKBASE';
const userAgent = 'NTRIP Aceinna CloudRTK 1.0';
const username = 'yundong';
const password = 'TEL8IOZTBJVVJ0IT';

// serialPort object
let serialPort = null;
// ntrip object
let ntripClient = null;

// ntrip status
let ntripIsReady = false;
// serialport status
let portIsReady = false;
// file log source
const logFile = writeFile();
//const log_data = write_data_to_file();


// write file
function writeFile() {
  const date = new Date();
  const year = date.getFullYear();
  const month = date.getMonth() + 1;
  const day = date.getDate();
  const hours = date.getHours();
  const minutes = date.getMinutes();
  const seconds = date.getSeconds();
  const filename = `${year}-${month}-${day}-${hours}-${minutes}-${seconds}.log`;

  return function write(data) {
    fs.writeFileSync(filename, data, {
      flag: 'a+'
    });
  };
}

// app start
function start() {
  //connectSerialPort();
  connectNtripcaster();
}

start();

// do log
function doLog(...args) {
  const newArgs = Array.from(args);
  if (newArgs.length <= 0) {
    return;
  }
  newArgs[0] = `%s ${newArgs[0]}`;
  newArgs.splice(1, 0, new Date().toUTCString());
  Reflect.apply(console.log, console, newArgs);
  logFile(newArgs);
}




var fs_data = require('fs');

function log_data(data)
{
	fs_data.appendFileSync("data.bin", data,  "binary",'a+',function(err) {
		if(err) {
			console.log(err);
		}
	});
}

// make a do once function
function doOnce(func) {
  let done = false;
  return function innerOnce(...args) {
    if (done) {
      return;
    }
    done = true;
    Reflect.apply(func, this, args);
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
  doLog('Starting connect serialport');

  serialPort = new SerialPort(ComName, {
    baudRate: 460800, 
    dataBits: 8, 
    parity: 'none', 
    stopBits: 1, 
    flowControl: false
  });
  
  serialPort.on('open', () => {
    portIsReady = true;
    doLog('Serialport is connected');
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
    doLog('serialport is close');
    doneOnce();
  });
  
  serialPort.on('error', err => {
    portIsReady = false;
    doLog('serialport error: %s', err);
    doneOnce();
  });
}

// init ntripcaster connect
function connectNtripcaster() {
  if (ntripClient) {
    ntripClient.removeAllListeners();
    ntripClient = null;
  }
  doLog('Starting connect ntripcaster');

  ntripClient = net.createConnection({
    host,
    port
  }, () => {
    doLog('Ntripcaster is connected');
    const authorization = Buffer.from(
      username + ':' + password,
      'utf8'
    ).toString('base64');
    const data = `GET /${mountPoint} HTTP/1.0\r\nUser-Agent: ${userAgent}\r\nAuthorization: Basic ${authorization}\r\n\r\n`;
	console.log(data);
    ntripClient.write(data);
  });
  
  ntripClient.on('data', data => {
    if (ntripIsReady) {
      writeToPort(data);
	  log_data(data);
      return;
    }
  
    if (data.toString().startsWith('ICY 200 OK')) {
      ntripIsReady = true;
    }
  });

  const doneOnce = doOnce(async () => {
    await sleep(1000);
    connectNtripcaster();
  });
  
  ntripClient.on('close', () => {
    ntripIsReady = false;
    doLog('ntripcaster is close');
    doneOnce();
  });
  
  ntripClient.on('error', err => {
    ntripIsReady = false;
    doLog('ntripcaster error: %s', err);
    doneOnce();
  });  
}

// write data to ntripcaster
function writeToNtrip(data) {
  if (!ntripIsReady && ntripClient) {
    doLog('ntripcaster is not ready');
    return;
  }
  doLog(data.toString());
  ntripClient.write(data);
}

// write data to serialport
function writeToPort(data) {
  if (!portIsReady && serialPort) {
    doLog('serialport is not ready');
    return;
  }
 // doLog('write ntrip data to serialport');
 // console.log(data);

  //serialPort.write(data);
}
