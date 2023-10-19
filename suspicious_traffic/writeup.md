Below deck troubles: Suspicious traffic
====================================

## Task
Ahoy, officer,

the chief security officer has told you, he came across a very suspicious event in ship's security logs on the occasion of a planned monthly log check. The event is related to accessing the secret file secret.db on server on cargo deck. Luckily, the ship is equipped with an automatic network traffic recorder, which was activated by the suspicious event and provided corresponding packet capture. Your task is to confirm that the mentioned file has been exfiltrated and to examine its contents.

May you have fair winds and following seas!

Download the pcap.
(MD5 checksum: 6e7cfe473b222ff766e04196e35df304)

## Solution
Open downloaded file in wireshark and let's quickly scroll what is there:
- some DNS queries, nothing interesting on first look
- some SMB traffic, working with files employees.db and history.db. We can export these files and look inside (it's sqlite database) but also nothing interesting
- some encrypted SMB3 traffic. We can see authentication request for user james_admin before that but don't know what is inside
- some HTTP traffic, but also no interesting data
- quite o lot of traffic on non standard high TCP ports

So, start with the traffic on non standard ports. Communication begins opening port 65021. Wireshark in bottom part of window show just some data. But if we click on follow TCP stream and open show it as ASCII we find something interesting:

	220 (vsFTPd 3.0.3)
	USER james
	331 Please specify the password.
	PASS james.f0r.FTP.3618995
	230 Login successful.
	SYST
	215 UNIX Type: L8
	TYPE I
	200 Switching to Binary mode.
	PORT 172,20,0,7,213,251
	200 PORT command successful. Consider using PASV.
	STOR home.tgz
	150 Ok to send data.
	226 Transfer complete.
	PORT 172,20,0,7,149,183
	200 PORT command successful. Consider using PASV.
	STOR etc.tgz
	150 Ok to send data.
	226 Transfer complete.
	QUIT
	221 Goodbye.

So, it's FTP on non standard port and the other traffic will be data. (Note: to be honest this was not first what I have tried. But I run string command on pcap file and grep it with james. And I saw that there is FTP login so I started searching where the FTP data are). We see that user pushed home.tgz and etc.tgz file to FTP server. We can tell wireshark that this traffic is FTP so it will starts showing it correctly. And then we can export files (I believe that file - export objects should work like it's working with SMB but for some reason on my system it didn't work. But following datastream and exporting it in raw form works). We can untar files and look inside but still no secrets.db.

Well, we have probably to deal with encrypted SMB3. Here is a great article about that: https://medium.com/maverislabs/decrypting-smb3-traffic-with-just-a-pcap-absolutely-maybe-712ed23ff6a2
TL;DR: We need user's password or NTLM hash to compute session encryption key. When we have it, we can decrypt traffic in our pcap file.

So, let's get user's password. We don't have it. But SMB3, same like SMB2, starts with NTLM authentication. That means that client tell server that he want to authenticate. Server sends challenge and client return back MD5 hash of challenge with his NTLM password hash. NTLM hash is just something like two MD4 hashes of password in UTF16LE. That means: bruteforcing password will cost us computing 2 MD4 and 1 MD5 hash for one attempt, which can be doable. And best message: hashcat can do it. So, prepare hash file for hashcat:

	└─# cat ntlm             
	james_admin::LOCAL.TCC:78c8f4fdf5927e58:8bc34ae8e76fe9b8417a966c2f632eb4:01010000000000003ab4fc1550e2d901b352a9763bdec89a00000000020018004100360037004600320042004100340045003800460032000100180041003600370046003200420041003400450038004600320004000200000003001800610036003700660032006200610034006500380066003200070008003ab4fc1550e2d901060004000200000008003000300000000000000000000000000000002581558b8f3cf059f3661e7cb3af60d9b63a7561b7f48607589fb37e551862b10a0010000000000000000000000000000000000009001e0063006900660073002f0073006d006200730065007200760065007200320000000000

It's just one line and all required info is in dump right prior to SMB3 encrypted traffic: username (james_admin), domain (LOCAL.TCC), NTLM Server challenge, NTProofStr and NTLMv2 Response (in dump, NTProofStr is in one string behind NTLMv2 response so just split it). We can try decode password with wordlist:

	hashcat -m 5600 ntlm /usr/share/wordlists/rockyou.txt

but without success. Let's get back to the FTP. Password for FTP is: `james.f0r.FTP.3618995` which seems like username, for in leet speak, service and quite short number. What if this user makes same stupid password for SMB? Let's try it:

	hashcat -m 5600 -a3 -1 ?u -2 ?d ntlm "james_admin.f0r.SMB.?2?2?2?2?2?2?2"

and this will reveal us password: james_admin.f0r.SMB.8089078

Now we can use python script from website above to calculate session encryption key. Bad thing is that script was written for Python2 which nowdays is obsolete and is problem to run it on modern system. So I updated it to be compatible with python3 and added script to this repository :-) 

	└─# python3 decrypt.py -u james_admin -d LOCAL.TCC -p james_admin.f0r.SMB.8089078 -n 8bc34ae8e76fe9b8417a966c2f632eb4 -k 4292dac3c7a0510f8b26c969e1ef0db9 -v

	USER WORK: b'J\x00A\x00M\x00E\x00S\x00_\x00A\x00D\x00M\x00I\x00N\x00'b'L\x00O\x00C\x00A\x00L\x00.\x00T\x00C\x00C\x00'
	PASS HASH: b'7cf87b641c657bf9e3f75d93308e6db3'
	RESP NT:   b'a154f31a5ecc711694c3e0d064bac78e'
	NT PROOF:  b'8bc34ae8e76fe9b8417a966c2f632eb4'
	KeyExKey:  b'6a1d3b41cdf3d40f15a6c15b80d567d0'
	Random SK: b'7a93dee25de4c2141657e7037dddb8f1'

Again, we have password and rest of required information is in dump. Now we have Random SK - encryption key for traffic. We notice session id from auth packets: 49b136b900000000 (after respecting byte order) and in wireshark click on protocol preferences -> SMB2 -> secret sessions key for decryption... In dialog fill session ID and session key and whoa, we have decrypted SMB3 traffic. Now we see file secret.db.enc and we can export it. But what the hack, it's not SQLite database! We run file on it:

	$ file secrets.db.enc 
	secrets.db.enc: openssl enc'd data with salted password

Great, it's encrypted. We can try several brute force method without success... and then, return to FTP :-) Untar home.tgz file which seems like home from linux system. File is encrypted by openssl, probably in command line. So we try the luck:

	$ cat home/.bash_history |grep openssl
	sudo aptitude search openssl
	openssl enc -aes-256-cbc -salt -pbkdf2 -in secret.db -out secret.db.enc -k R3alyStr0ngP4ss!

Good, now just repeat same command with -d argument:

	$ openssl enc -aes-256-cbc -salt -pbkdf2 -d -in secret.db.enc -out secret.db -k R3alyStr0ngP4ss!

And look inside SQLite database:

	$ sqlite3 secret.db 
	SQLite version 3.43.2 2023-10-10 12:14:04
	Enter ".help" for usage hints.
	sqlite> .tables
	secrets
	sqlite> select * from secrets;
	1|FLAG|FLAG{5B9B-lwPy-OfRS-4uEN}
	sqlite>