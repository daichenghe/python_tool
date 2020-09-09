const SerialPort = require('serialport');
const net = require('net');

const buffer = require('buffer');
buffer.INSPECT_MAX_BYTES = 1500;

// serialport config
//const ComName = '/dev/tty.usbserial-143201';
const ComName = 'com14';
let serialPortBuf = Buffer.alloc(0);
const GGADELIMITER = Buffer.from('\r\n');

// ntripcaster config
const host = '47.116.1.17';
const port = '2201';
const mountPoint = 'RTK';
const userAgent = 'NTRIP Aceinna CloudRTK 1.0';
const authorization = 'test';


let ntripIsReady = false;
let portIsReady = false;

// init serialport
const serialPort = new SerialPort(ComName, {
  baudRate: 115200, 
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

serialPort.on('close', () => {
  portIsReady = false;
  console.log('serialport is close');
});

serialPort.on('error', err => {
  portIsReady = false;
  console.error('serialport error', err);
});

// init ntripcaster connect
const ntripClient = net.createConnection({
  host,
  port
}, () => {
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

ntripClient.on('close', () => {
  ntripIsReady = false;
  console.log('ntripclient is close');
});

ntripClient.on('error', err => {
  ntripIsReady = false;
  console.error('ntripclient error', err);
});

// write data to ntripcaster
function writeToNtrip(data) {
  if (!ntripIsReady) {
    console.log('ntripclient is not ready');
    return;
  }
  console.log(data.toString());
  ntripClient.write(data);
}

// write data to serialport
function writeToPort(data) {
  if (!portIsReady) {
    console.log('serialport is not ready');
    return;
  }
  console.log(data);
  serialPort.write(data);
}
