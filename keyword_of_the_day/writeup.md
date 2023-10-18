Troubles on the bridge: Keyword of the day
====================================

## Task
Ahoy, officer,

one of deck cadets (remember your early days onboard) had a simple task to prepare simple web application to announce keyword of the day. He claimed that the task is completed, but he forgot on which port the application is running. Unfortunately, he also prepared a lot of fake applications, he claims it was necessary for security reasons. Find the keyword of the day, so daily routines on ship can continue.

May you have fair winds and following seas!

The webs are running somewhere on server keyword-of-the-day.cns-jv.tcc.

## Solution
As it's said, we don't know on which port application is running. So we start with nmap (and for later use little shell magic to save only TCP ports to file for later use):

	nmap -p1-65535 keyword-of-the-day.cns-jv.tcc | grep "tcp open" | cut -d / -f1 > keyword_ports

So now in file keyword_ports is quite a lot of TCP port on which this server accept connection. I look what is on this site and open one of it, for example: http://keyword-of-the-day.cns-jv.tcc:60495. If I open it in browser, thare is some loading picture for some time and than it shows some emoji. So, page with some javascript, delay and so on. I've tried open some other port and there is (if you aren't lucky and open the right one by accident :-) ) same application. So, how to find the different one. Let's try something:

	└─$ curl http://keyword-of-the-day.cns-jv.tcc:60495|md5sum
	  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
	                                 Dload  Upload   Total   Spent    Left  Speed
	100  4202  100  4202    0     0   308k      0 --:--:-- --:--:-- --:--:--  315k
	a6c47c104200806a0337a662a7d82f06  -

When I repeat same command, MD5 hash is different. That's not good, it means, that althought application looks same, something in returned HTML/JS code is chaning. But when someone is just pressing up arrow with enter while thinking about other idea... something interesting happens: two consecutive requests in short time has same MD5 hash. So, apparently returned content depends on time. If we are fast, we receive same content. And as I already somewhere said, I'm lazy. So we can do something really nasty, stupid and simple:

	└─$ for i in `cat keyword_ports`; do crc=`curl -s http://keyword-of-the-day.cns-jv.tcc:${i} | md5sum`; echo "${crc} - ${i}"; done
	3621315927510c8dcbe9b98add35d090  - - 60000
	3621315927510c8dcbe9b98add35d090  - - 60004
	3621315927510c8dcbe9b98add35d090  - - 60009
	3621315927510c8dcbe9b98add35d090  - - 60010
	3621315927510c8dcbe9b98add35d090  - - 60011
	3621315927510c8dcbe9b98add35d090  - - 60015
	3621315927510c8dcbe9b98add35d090  - - 60018
	3621315927510c8dcbe9b98add35d090  - - 60019
	3621315927510c8dcbe9b98add35d090  - - 60020
	3621315927510c8dcbe9b98add35d090  - - 60021
	3621315927510c8dcbe9b98add35d090  - - 60023
	3621315927510c8dcbe9b98add35d090  - - 60029
	3621315927510c8dcbe9b98add35d090  - - 60030
	3621315927510c8dcbe9b98add35d090  - - 60031
	3621315927510c8dcbe9b98add35d090  - - 60032
	3621315927510c8dcbe9b98add35d090  - - 60033
	3621315927510c8dcbe9b98add35d090  - - 60035
	3621315927510c8dcbe9b98add35d090  - - 60036
	3621315927510c8dcbe9b98add35d090  - - 60037
	3621315927510c8dcbe9b98add35d090  - - 60038
	3621315927510c8dcbe9b98add35d090  - - 60041
	3621315927510c8dcbe9b98add35d090  - - 60042
	3621315927510c8dcbe9b98add35d090  - - 60045
	3621315927510c8dcbe9b98add35d090  - - 60047
	3621315927510c8dcbe9b98add35d090  - - 60051
	3621315927510c8dcbe9b98add35d090  - - 60052
	3621315927510c8dcbe9b98add35d090  - - 60058
	3621315927510c8dcbe9b98add35d090  - - 60059
	3621315927510c8dcbe9b98add35d090  - - 60060
	3621315927510c8dcbe9b98add35d090  - - 60063
	3621315927510c8dcbe9b98add35d090  - - 60064
	3621315927510c8dcbe9b98add35d090  - - 60066
	3621315927510c8dcbe9b98add35d090  - - 60068
	3621315927510c8dcbe9b98add35d090  - - 60069
	f7736f845722173b8b4af0ef75e5a7cc  - - 60071
	f7736f845722173b8b4af0ef75e5a7cc  - - 60074
	f7736f845722173b8b4af0ef75e5a7cc  - - 60075
	f7736f845722173b8b4af0ef75e5a7cc  - - 60076
	...

We try GET request on all ports we discovered in nmap, that are opened. Because we doing it in loop, it's quite fast and as it is visible on sample output, if we have suitaible internet connection, around 30 requests returns same MD5 hash. So now I just scrolled in terminal output and visually select that one line which is unique from all others:

	ba78fb78b670b1b1a4c15e525bc3000b  - - 60257

So, open http://keyword-of-the-day.cns-jv.tcc:60257/ in browser. There is loading page, but the image which is loaded tell us to go to URL /948cd06ca7. Do it and we have flag:

	Your flag is FLAG{DEIE-fiOr-pGV5-8MPc}