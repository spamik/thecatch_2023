Troubles on the bridge: Captain's password
====================================

## Task
Ahoy, officer,

our captain has had too much naval espresso and is temporary unfit for duty. The chief officer is in command now, but he does not know the captain's passwords for key ship systems. Good news is that the captain uses password manager and ship chief engineer was able to acquire captain's computer memory crash dump. Your task is to acquire password for signalization system.

May you have fair winds and following seas!

Download the database and memory dump.
(MD5 checksum: 7c6246d6e21bd0dbda95a1317e4ae2c9)

## Solution
In downloaded zip archive are 2 files: captain.kdbx and crashdump.dmp. captain.kdbx will be KeePass password database, other file probably will be memory dump from Windows OS. After little research I found vulnerability CVE-2023-32784 which tells us that several versions of KeePass software keep master password from database in memory under certain circumstances. And there are also proof of concept scripts which can reveal password. I like personally this one because it's in python with almost no dependencies: https://github.com/CMEPW/keepass-dump-masterkey

Script is included in this repository. Now we can run it:

	python3 poc.py crashdump.dmp 
	2023-10-18 15:34:36,700 [.] [main] Opened crashdump.dmp
	Possible password: ●)ssword4mypreciousship
	Possible password: ●assword4mypreciousship
	Possible password: ●:ssword4mypreciousship
	Possible password: ●|ssword4mypreciousship
	Possible password: ●Wssword4mypreciousship
	Possible password: ●5ssword4mypreciousship
	Possible password: ●rssword4mypreciousship

If we read description of this CVE, we find out that first 2 characters of passwords usually could not be recovered. So there is a possibility to crack it but in this case we can guess, that password will probably be `password4mypreciousship`. So now just open database with some keepass software with this password and look inside. In Internal ship systems is record with title `Main Flag System` and password:

	FLAG{pyeB-941A-bhGx-g3RI}
