Miscellaneous: Naval chef's recipe
====================================

## Task
Ahoy, officer,

some of the crew started behaving strangely after eating the chef's speciality of the day - they apparently have hallucinations, because they are talking about sirens wailing, kraken on starboard, and accussed the chef being reptilian spy. Paramedics are getting crazy, because the chef refuses to reveal what he used to make the food. Your task is to find his secret recipe. It should be easy as the chef knows only security by obscurity and he has registered domain chef-menu.galley.cns-jv.tcc. May you have fair winds and following seas!

The chef's domain is chef-menu.galley.cns-jv.tcc.

## Solution
If you want to break surprise from solving task, start with curl :-)

	└─$ curl -v chef-menu.galley.cns-jv.tcc
	*   Trying 10.99.0.32:80...
	* Connected to chef-menu.galley.cns-jv.tcc (10.99.0.32) port 80 (#0)
	> GET / HTTP/1.1
	> Host: chef-menu.galley.cns-jv.tcc
	> User-Agent: curl/7.86.0
	> Accept: */*
	> 
	* Mark bundle as not supporting multiuse
	< HTTP/1.1 200 OK
	< Date: Thu, 19 Oct 2023 09:17:39 GMT
	< Server: Apache
	< X-Powered-By: PHP/8.2.10
	< Vary: Accept-Encoding
	< Content-Length: 562
	< Content-Type: text/html; charset=UTF-8
	< 
	<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
	<html><head>
	  <title>301 Moved Permanently</title>
	  <meta http-equiv="refresh" content="0;url=https://chef-menu.galley.cns-jv.tcc">
	</head><body>
	<h1>Moved Permanently</h1>
	<p>The document has moved <a href="https://chef-menu.galley.cns-jv.tcc">here</a>.</p>
	<p style="display: none">The secret ingredient is composed of C6H12O6, C6H8O6, dried mandrake, FLAG{ytZ6-Pewo-iZZP-Q9qz}, and C20H25N3O. Shake, do not mix.</p>
	<script>window.location.href='https://chef-menu.galley.cns-jv.tcc'</script>
	* Connection #0 to host chef-menu.galley.cns-jv.tcc left intact
	</body></html> 

As we see, in page is javascript redirect to other location. If you open it in browser, you won't see it, because browser immediately redirects on https site where this info is missing. But with curl it's done in two seconds :-)