Sailor training center: Ship web server
====================================

## Task
Ahoy, deck cadet,

there are rumors that on the ship web server is not just the official presentation. Your task is to disprove or confirm these rumors.

May you have fair winds and following seas!

Ship web server is available at http://www.cns-jv.tcc.

## Solution
Open web in browser. It's redirected to HTTPS, with unknown CA. Ignoring certificate shows simple web on which is very interesting footer part:

	ver. RkxBR3sgICAgLSAgICAtICAgIC0gICAgfQ== 

Seems like base64 string so we try to decode it:

	~ $ echo -n "RkxBR3sgICAgLSAgICAtICAgIC0gICAgfQ== "|base64 -d
	FLAG{    -    -    -    }

Ok, it seems like good way. Website is HTTPS. Why? Let's examine certificate; first thing which came to my mind was what DNS alt names are in:

	─$ openssl s_client -connect www.cns-jv.tcc:443 -showcerts </dev/null | openssl x509 -text | grep DNS
	depth=0 C = CS, ST = CESNET, L = Maritime Communications, O = CNS Josef Verich, OU = Headquarters, CN = CESNET Maritime Communications
	verify error:num=18:self-signed certificate
	verify return:1
	depth=0 C = CS, ST = CESNET, L = Maritime Communications, O = CNS Josef Verich, OU = Headquarters, CN = CESNET Maritime Communications
	verify return:1
	DONE
	                DNS:www.cns-jv.tcc, DNS:documentation.cns-jv.tcc, DNS:home.cns-jv.tcc, DNS:pirates.cns-jv.tcc, DNS:structure.cns-jv.tcc

Good, can we look on other sites?

	└─$ curl http://documentation.cns-jv.tcc
	curl: (6) Could not resolve host: documentation.cns-jv.tcc

Nope, because these DNS names are not in DNS server. But when they are in certificate, web server probably knows them. From several options how to fix this let's add this to /etc/hosts:

	10.99.0.64      home.cns-jv.tcc documentation.cns-jv.tcc pirates.cns-jv.tcc structure.cns-jv.tcc

Now we can open all these sites in browser. Version string varies on all sites, by visiting documentation, pirates and structure website we can gather these:
	
	RkxBR3tlamlpLSAgICAtICAgIC0gICAgfQ==
	RkxBR3sgICAgLSAgICAtICAgIC1nTXdjfQ==
	RkxBR3sgICAgLSAgICAtUTUzQy0gICAgfQ==
	RkxBR3sgICAgLXBsbVEtICAgIC0gICAgfQ==

(Notice: don't forget on https prefix as on all sites, http virtual host returns redirect to https://www.cns-jv.tcc). On home website it's needed click on visit user button, on documentation website version is written via CSS (so string can be found in CSS stylesheet), on structure it's written over image - possible to copy it, it's just badly visible.

Decode these base64 strings:

	~ $ echo -n "RkxBR3tlamlpLSAgICAtICAgIC0gICAgfQ=="|base64 -d
	FLAG{ejii-    -    -    }
	~ $ echo -n "RkxBR3sgICAgLSAgICAtICAgIC1nTXdjfQ=="|base64 -d
	FLAG{    -    -    -gMwc}
	~ $ echo -n "RkxBR3sgICAgLSAgICAtUTUzQy0gICAgfQ=="|base64 -d
	FLAG{    -    -Q53C-    }
	~ $ echo -n "RkxBR3sgICAgLXBsbVEtICAgIC0gICAgfQ=="|base64 -d
	FLAG{    -plmQ-    -    }

Put it together:

	FLAG{ejii-plmQ-Q53C-gMwc}