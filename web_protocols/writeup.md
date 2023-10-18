Crew drills: Web protocols
====================================

## Task
Ahoy, officer,

almost all interfaces of the ship's systems are web-based, so we will focus the exercise on the relevant protocols. Your task is to identify all webs on given server, communicate with them properly and assembly the control string from responses.

May you have fair winds and following seas!

The webs are running on server web-protocols.cns-jv.tcc.

## Solution
Ok, se let's see what is there:

	─$ curl -v http://web-protocols.cns-jv.tcc
	*   Trying 10.99.0.122:80...
	* connect to 10.99.0.122 port 80 failed: Connection refused
	* Failed to connect to web-protocols.cns-jv.tcc port 80 after 9 ms: Couldn't connect to server
	* Closing connection 0
	curl: (7) Failed to connect to web-protocols.cns-jv.tcc port 80 after 9 ms: Couldn't connect to server

Nothing running on TCP port 80, time for nmap:

	└─# nmap -p1-65535 web-protocols.cns-jv.tcc       
	Starting Nmap 7.93 ( https://nmap.org ) at 2023-10-18 08:47 EDT
	Nmap scan report for web-protocols.cns-jv.tcc (10.99.0.122)
	Host is up (0.0034s latency).
	Not shown: 65530 closed tcp ports (reset)
	PORT     STATE SERVICE
	5009/tcp open  airport-admin
	5011/tcp open  telelpathattack
	5020/tcp open  zenginkyo-1
	8011/tcp open  unknown
	8020/tcp open  intu-ec-svcdisc

	Nmap done: 1 IP address (1 host up) scanned in 4.92 seconds

5 open ports, now we test it with curl again:

	└─$ curl -v http://web-protocols.cns-jv.tcc:5009
	*   Trying 10.99.0.122:5009...
	* Connected to web-protocols.cns-jv.tcc (10.99.0.122) port 5009 (#0)
	> GET / HTTP/1.1
	> Host: web-protocols.cns-jv.tcc:5009
	> User-Agent: curl/7.86.0
	> Accept: */*
	> 
	* Mark bundle as not supporting multiuse
	< HTTP/1.1 400 Bad Request
	* no chunk, no close, no size. Assume close to signal end
	< 
	* Closing connection 0
	Unsupported protocol version

	┌──(kali㉿kali)-[~]
	└─$ curl -v http://web-protocols.cns-jv.tcc:5011 >/dev/null
	  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
	                                 Dload  Upload   Total   Spent    Left  Speed
	  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*   Trying 10.99.0.122:5011...
	* Connected to web-protocols.cns-jv.tcc (10.99.0.122) port 5011 (#0)
	> GET / HTTP/1.1
	> Host: web-protocols.cns-jv.tcc:5011
	> User-Agent: curl/7.86.0
	> Accept: */*
	> 
	* Mark bundle as not supporting multiuse
	* HTTP 1.0, assume close after body
	< HTTP/1.0 200 OK
	< Content-Type: text/html; charset=utf-8
	< Content-Length: 523172
	< Set-Cookie: SESSION=LXJ2YnEtYWJJ; Path=/
	< Server: Werkzeug/1.0.1 Python/3.10.13
	< Date: Wed, 18 Oct 2023 12:48:39 GMT
	< 
	{ [2364 bytes data]
	100  510k  100  510k    0     0  6290k      0 --:--:-- --:--:-- --:--:-- 6386k
	* Closing connection 0
	                                                                                                                                                                                                                                          
	┌──(kali㉿kali)-[~]
	└─$ curl -v http://web-protocols.cns-jv.tcc:5020 >/dev/null
	  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
	                                 Dload  Upload   Total   Spent    Left  Speed
	  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*   Trying 10.99.0.122:5020...
	* Connected to web-protocols.cns-jv.tcc (10.99.0.122) port 5020 (#0)
	> GET / HTTP/1.1
	> Host: web-protocols.cns-jv.tcc:5020
	> User-Agent: curl/7.86.0
	> Accept: */*
	> 
	* Mark bundle as not supporting multiuse
	* HTTP 1.0, assume close after body
	< HTTP/1.0 200 OK
	< Content-Type: text/html; charset=utf-8
	< Content-Length: 542004
	< Set-Cookie: SESSION=Ui00MzNBfQ==; Path=/
	< Server: Werkzeug/1.0.1 Python/3.10.13
	< Date: Wed, 18 Oct 2023 12:48:54 GMT
	< 
	{ [2364 bytes data]
	100  529k  100  529k    0     0  9713k      0 --:--:-- --:--:-- --:--:-- 9801k
	* Closing connection 0
	                                                                                                                                                                                                                                          
	┌──(kali㉿kali)-[~]
	└─$ curl -v http://web-protocols.cns-jv.tcc:8011 >/dev/null
	  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
	                                 Dload  Upload   Total   Spent    Left  Speed
	  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*   Trying 10.99.0.122:8011...
	* Connected to web-protocols.cns-jv.tcc (10.99.0.122) port 8011 (#0)
	> GET / HTTP/1.1
	> Host: web-protocols.cns-jv.tcc:8011
	> User-Agent: curl/7.86.0
	> Accept: */*
	> 
	* Mark bundle as not supporting multiuse
	< HTTP/1.1 200 OK
	< Server: nginx/1.22.1
	< Date: Wed, 18 Oct 2023 12:49:01 GMT
	< Content-Type: text/html; charset=utf-8
	< Content-Length: 523172
	< Connection: keep-alive
	< Set-Cookie: SESSION=LXJ2YnEtYWJJ; Path=/
	< 
	{ [11813 bytes data]
	100  510k  100  510k    0     0  8646k      0 --:--:-- --:--:-- --:--:-- 8808k
	* Connection #0 to host web-protocols.cns-jv.tcc left intact
	                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
	┌──(kali㉿kali)-[~]
	└─$ curl -v http://web-protocols.cns-jv.tcc:8020           
	*   Trying 10.99.0.122:8020...
	* Connected to web-protocols.cns-jv.tcc (10.99.0.122) port 8020 (#0)
	> GET / HTTP/1.1
	> Host: web-protocols.cns-jv.tcc:8020
	> User-Agent: curl/7.86.0
	> Accept: */*
	> 
	* Mark bundle as not supporting multiuse
	< HTTP/1.1 400 Bad Request
	< Server: nginx/1.22.1
	< Date: Wed, 18 Oct 2023 12:49:19 GMT
	< Content-Type: text/html
	< Content-Length: 255
	< Connection: close
	< 
	<html>
	<head><title>400 The plain HTTP request was sent to HTTPS port</title></head>
	<body>
	<center><h1>400 Bad Request</h1></center>
	<center>The plain HTTP request was sent to HTTPS port</center>
	<hr><center>nginx/1.22.1</center>
	</body>
	</html>
	* Closing connection 0
	                                                                                                                                                                                                                                          
	┌──(kali㉿kali)-[~]
	└─$ curl -v -k https://web-protocols.cns-jv.tcc:8020 >/dev/null
	  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
	                                 Dload  Upload   Total   Spent    Left  Speed
	  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*   Trying 10.99.0.122:8020...
	* Connected to web-protocols.cns-jv.tcc (10.99.0.122) port 8020 (#0)
	* ALPN: offers h2
	* ALPN: offers http/1.1
	{ [16 bytes data]
	* SSL connection using TLSv1.2 / ECDHE-RSA-AES256-GCM-SHA384
	* ALPN: server accepted h2
	* Server certificate:
	*  subject: C=US; ST=Oregon; L=Portland; O=Company Name; OU=Org; CN=www.example.com
	*  start date: Aug 20 19:33:36 2023 GMT
	*  expire date: Aug 19 19:33:36 2024 GMT
	*  issuer: C=US; ST=Oregon; L=Portland; O=Company Name; OU=Org; CN=www.example.com
	*  SSL certificate verify result: self-signed certificate (18), continuing anyway.
	* Using HTTP2, server supports multiplexing
	* Copying HTTP/2 data in stream buffer to connection buffer after upgrade: len=0
	* h2h3 [:method: GET]
	* h2h3 [:path: /]
	* h2h3 [:scheme: https]
	* h2h3 [:authority: web-protocols.cns-jv.tcc:8020]
	* h2h3 [user-agent: curl/7.86.0]
	* h2h3 [accept: */*]
	* Using Stream ID: 1 (easy handle 0x560224fef950)
	* TLSv1.2 (OUT), TLS header, Supplemental data (23):
	} [5 bytes data]
	> GET / HTTP/2
	> Host: web-protocols.cns-jv.tcc:8020
	> user-agent: curl/7.86.0
	> accept: */*
	> 
	* TLSv1.2 (IN), TLS header, Supplemental data (23):
	{ [5 bytes data]
	* Connection state changed (MAX_CONCURRENT_STREAMS == 128)!
	* TLSv1.2 (OUT), TLS header, Supplemental data (23):
	} [5 bytes data]
	* TLSv1.2 (IN), TLS header, Supplemental data (23):
	{ [5 bytes data]
	* TLSv1.2 (IN), TLS header, Supplemental data (23):
	{ [5 bytes data]
	< HTTP/2 200 
	< server: nginx/1.22.1
	< date: Wed, 18 Oct 2023 12:49:29 GMT
	< content-type: text/html; charset=utf-8
	< content-length: 542004
	< set-cookie: SESSION=Ui00MzNBfQ==; Path=/
	< 
	100  529k  100  529k    0     0  8307k      0 --:--:-- --:--:-- --:--:-- 8401k
	* Connection #0 to host web-protocols.cns-jv.tcc left intact

So, what we see? Server on port 5009 returns unsupported protocols. Servers on 5011, 5020 and 8011 works ok and returns a long string as a HTML. Server on 8020 also works but on HTTPS protocol. On that it even accept HTTP/2 and also returns a long string as text/html (redirected to /dev/null for this purpose). String looks like base64 string, if we decode it, we findout that it's PNG picture with drawen cat. On these 4 servers are 2 pictures (2 and 2 are the same). It seems that in picture is nothing interesting. But look on the headers returned in responses. Especially set-cookie header:

	set-cookie: SESSION=Ui00MzNBfQ==; Path=/
	Set-Cookie: SESSION=LXJ2YnEtYWJJ; Path=/
	Set-Cookie: SESSION=Ui00MzNBfQ==; Path=/
	Set-Cookie: SESSION=LXJ2YnEtYWJJ; Path=/

Like with pictures - 2 and 2 session identificators are same. Which is especially in session case weird. And like in picture, it seems like base64 string, so look what is inside:

	Ui00MzNBfQ== = R-433A}
	LXJ2YnEtYWJJ = -rvbq-abI

It seems like a part of FLAG. Now we just need to find out the rest. Go back again to server on port 5009. This one just returned unsupported protocol version. Well, HTTP has several version, common was HTTP/1.0, HTTP/1.1, HTTP/2 and HTTP/3. For HTTP/3 is SSL mandatory which is not this case. For HTTP/2 it's also very uncommon to be running on non-encrypted connection. And HTTP/1.0 and 1.1 returns this error. Google research tell us that first public HTTP version was 0.9. Let's try it:

	telnet web-protocols.cns-jv.tcc 5009 
	Trying 10.99.0.122...
	Connected to web-protocols.cns-jv.tcc.
	Escape character is '^]'.
	GET / HTTP/0.9
	HTTP/0.9 200 OK

	SESSION=RkxBR3trckx0; iVBORw0KGgoAAAA...(continuing with some PNG image :-) )

We can decode this session:

	FLAG{krLt

And now we have complete FLAG:

	FLAG{krLt-rvbq-abIR-433A}

(To be honest, I've struggled with this for a very long time. First - it didn't come to my mind as server was responding with HTTP/1.1. And even when I start searching about all HTTP versions, documentation which I found says, that in  HTTP/0.9 request was made without specifying version, e.g. `GET /` only. Specifying version 0.9 was my last resort after few days trying :-) )