var http = require('http');
http.createServer(function (request,respose)
{
	respose.writeHead(200,{'Content-Type': 'text/plain'});
	respose.end('hello world\n')
}).listen(8888);
console.log('server running at http://127.0.0.1:8888/');
