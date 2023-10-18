Troubles on the bridge: Signal flags
====================================

## Task
Ahoy, officer,

after a reboot at 2023-10-02 11:30:18 UTC, the On-board signal flag recognition system (OBSF-RS) has malfunctioned. The signal flags are no more recognized and the only working function is to generate and save schematic views, which are created every time a ship in the vicinity changes its signaling. We need to know what the surrounding ships signaled and if we have missed something important.

May you have fair winds and following seas!

Download the schematic views.
(MD5 checksum: c1820a3c41a0d6a0daacd84b69fd1b57)

## Solution
In downloaded archive is a lot of pictures of ships from different angles. Ships have some flags on it marked in green rectangle/target. And on left side is written timestamp, ship ID and some other information.

Obviously is needed to process picture... Which I don't like and never did that :-) But I'm lucky living in 21st century and we have chat gpt :-) So I've started writing python script and asking dump question.

In repository is ocr.py script which print almost solution. But the way to this script leads probably like this:
- I've read hint. It seems that I need to put together images from same ships and also sort all messages by timestamp.
- This can probably be done just by using OCR. So I've read text from images using pytesseract. Ship object ID identify same ships and timestamp can be used for sorting messages.
- What next? Still doesn't know where to get the message. What means that flags? Using google brings the answer: https://en.wikipedia.org/wiki/International_maritime_signal_flags
- So now I need to identify all flags on ship. Chat GPT generate some code using cv2 which quite works. I can separate all the flags inside. But we need text...
- So I try calculate MD5 hash from cropped sections. Too much results... but when I crop results with 20 pixels from each side it only generates something over 30 pictures. That good.
- I've opened all separated flags and wrote hash dict with MD5 sum and corresponding letter/number what that flags meant
- Because I'm lucky and countours from cv2 are ordered from bottom to top, I can wrote decoded messages.
- Ok, we have some characters. In output I can see text like "VERICH" so it seems good. But usually that is a mess... mess which in almost all cases starts with 0X. Weid... what it can be? I've opened ASCII table, starts looking... great, that makes sense
- Next version of script: if it starts with 0X, decode it as ASCII

This trying results in script in repository. Its result looks like this:

	VESSEL: 259798
	2023-10-02 11:30:18 HONEYMOON ./signalization_xidfjmtojrijkfhgxrkeepbfzrdioemt.png
	VESSEL: 304622
	2023-10-02 11:30:18 M ./signalization_fytnqqtmiflldhttljkhvwcooazamptj.png
	2023-10-02 11:37:45 CNS Josef ./signalization_dhtdlbfedfykcfjoqkyzvyaugichcpke.png
	2023-10-02 11:38:58  Verich,  ./signalization_jiaovotzbcnwdzgotxsbogondrzjnvlb.png
	2023-10-02 11:40:12 nice flag ./signalization_uforuecpbsvmvbcistxbqmhbjngdihbf.png
	2023-10-02 11:48:51 CNS Josef ./signalization_iuomilytqpucycidmkrtvcmifnqoprre.png
	2023-10-02 11:50:00  Verich,  ./signalization_brbezdorjcmststjxmvijsxmgsshmalm.png
	2023-10-02 11:51:08 is Mr. Ca ./signalization_zqgtpzirjdgstercodmhnknefdxrukfl.png
	2023-10-02 11:52:25 letka on  ./signalization_wkqnlgjqwsojeiamybkmcybusfpsuptm.png
	2023-10-02 11:53:28 board? ./signalization_tpbgtvdfmtmiofzdobtcnrnqrlvgwmqm.png
	2023-10-02 12:30:12 Have you  ./signalization_ryjypqpubwianhnzbavwthwoahjqirvi.png
	2023-10-02 12:31:27 seen Mr.  ./signalization_nqrddyppighaotgvnhymrckyleogsqbg.png
	2023-10-02 12:32:38 Caletka? ./signalization_aiaucdjpnsntplwncqozuymywjmhukwm.png
	VESSEL: 367676
	2023-10-02 11:30:18 X ./signalization_nueujtmhxwbqwjrradxhcyyrroefdszd.png
	2023-10-02 11:35:43 Party on th ./signalization_ajshslvsnbevfdnoncbpylqgspvplqur.png
	2023-10-02 11:36:42 e bridge at ./signalization_vgptsygrpaiosvgesiwjwcelwumalkdt.png
	2023-10-02 11:37:50  2100 ZULU. ./signalization_ikeosnxvfwqyhievhomuhjuwjnxosuil.png
	2023-10-02 11:43:15 Free pinot  ./signalization_askooyynbtnbsktiqcegkwfyfencnkim.png
	2023-10-02 11:44:17 gris for ev ./signalization_vlgbgamyiilvsyavsqhsadavcysqtuwr.png
	2023-10-02 11:45:11 eryone! ./signalization_jagbfhvsjomvplwzwjjkxnkcnxztyjra.png
	VESSEL: 487078
	2023-10-02 11:30:18 V ./signalization_anqmnnkdilsdfqlqbbrtjrrbqtalnrgl.png
	2023-10-02 11:32:47 57220636 ./signalization_qgqzzsupoikjhhsrhnqunnsaixirwlsh.png
	2023-10-02 11:33:52 6656520163 ./signalization_kkglwxloneopikuenkdskiitjhjnxyws.png
	2023-10-02 11:34:58 8695206973 ./signalization_jhwlxnkmestyepexockmlcurcsoneyoi.png
	2023-10-02 11:36:03 0627256E ./signalization_dfbcwuvrspgymxfanfixdsewullrmebg.png
	2023-10-02 11:37:11 07765205 ./signalization_naxonqjkhfmkcovdmbzmldmzpzuvvavy.png
	2023-10-02 11:38:18 5642061205 ./signalization_kiddxaeumfxjrijmscnwucgbeoatdieb.png
	2023-10-02 11:39:22 368619632E ./signalization_xskdiiwbwnkotcykqydqswbfdiaryxee.png
	2023-10-02 11:45:00 VF ./signalization_xqmdpcjxntzevzjazqfbchnytzuekclz.png
	VESSEL: 567874
	2023-10-02 11:30:18 E ./signalization_owyphcthfjiogtsskewqpqbqsufyekfs.png
	2023-10-02 11:40:00 K ./signalization_tldakfqlalagsnldvkfzemgznwocllhk.png
	2023-10-02 11:43:02  Hey, w ./signalization_rctgricoofibtwqyexzurafcoybmqzbz.png
	2023-10-02 11:44:14  hat is ./signalization_omubfbsfdsrbgfupwawqlpytytxftjrd.png
	2023-10-02 11:45:15   your  ./signalization_bgongwndgpxslbchkesjtuflpurvgcis.png
	2023-10-02 11:46:18  wifi P ./signalization_rgkkrjlqkcbakebcttotmjoxhrbzypno.png
	2023-10-02 11:47:21  ./signalization_ukcnmqdmqfjnutsafajpbagiabldavaj.png
	2023-10-02 11:48:19 ? ./signalization_gjdbcyxeqzufatqmbqxtdexbhtgwdqcx.png
	2023-10-02 12:41:24 Relay: ./signalization_ytythebnnuyfbdsnibjwtgwrkvddledg.png
	2023-10-02 12:42:18   Have  ./signalization_hltqwxlrqfpmdvwrefabnnctdrcwojzw.png
	2023-10-02 12:43:12  you se ./signalization_cwautabhaqfuunecnnjapvfhdvtsiaoe.png
	2023-10-02 12:44:09 en Mr. ./signalization_ciuemipqmmckmprwmmabuznirrqenriy.png
	2023-10-02 12:45:05   Calet ./signalization_xkarfwleyjvhkivzibqpboyuhvtunwol.png
	2023-10-02 12:46:01 ka? ./signalization_ffbyfhydersznxishwajuolbhceqtohw.png
	VESSEL: 627912
	2023-10-02 11:30:18 PE ./signalization_gwpmyzutwwuaneucbblckpgqsnvyiebx.png
	2023-10-02 12:33:00 Relay: H ./signalization_szrqzrcuyocbpmabxsyrocytlubcqftw.png
	2023-10-02 12:34:00 ave you  ./signalization_efohpauggoenqzhysleojdkwztyktsev.png
	2023-10-02 12:35:00 seen Mr. ./signalization_qbpdlxbtjdgboyrgkocxsrlgeiyckdkp.png
	2023-10-02 12:36:00  Caletka ./signalization_sgavctduqwsplbpvztkbjuxyxnbrffyk.png
	2023-10-02 12:37:00 ? ./signalization_lcsupmmrqnorcqekocpigpapxlslottg.png
	VESSEL: 717609
	2023-10-02 11:30:18 CNS J ./signalization_cmsnkxoklpmhiqgupphptwlbguuiopjr.png
	2023-10-02 11:30:20 osef  ./signalization_uxfvfxezfopmgljghgmvdyoflyuctong.png
	2023-10-02 11:31:22 VERICH ./signalization_qzsyhkpxvmowpqygwbmkpyuftatljypd.png
	2023-10-02 11:32:25 , are ./signalization_rnkwhtwrtzadigwrpswlxqjkmaixkrnk.png
	2023-10-02 11:33:27  your ./signalization_fwxjmwekxsvvooplbrfcetjumzorvebx.png
	2023-10-02 11:34:30  nets ./signalization_malytkmuxyyhoizzlrdslphxiebxgucf.png
	2023-10-02 11:35:32  ok,  ./signalization_jxiuguaiqfetbhccrsocxvhuihcbbgky.png
	2023-10-02 11:36:33 too?  ./signalization_zbindrcgpjnqcispavsrfuxmxydymkbf.png
	2023-10-02 11:37:36 ;-) ./signalization_nuyblkwgzodkbjhgjgfdmzrjlmqzlfdz.png
	2023-10-02 11:41:00 CNS J ./signalization_dzkkbyftmolajmgqyeiryyivrqoegekc.png
	2023-10-02 11:42:03 osef  ./signalization_cwxrnolhaezundjspjsvrjaqnhjpngyp.png
	2023-10-02 11:43:05 VERICH ./signalization_dwinjgndjrrwckmjjwagbufpnebvkvjo.png
	2023-10-02 11:44:07 , you ./signalization_buquypzjibuuqbmycjwzuqcanxmhdokk.png
	2023-10-02 11:45:09  can  ./signalization_ygwllzvvmeamixrqpviwkvxiaafctwfc.png
	2023-10-02 11:46:12 IMEROVE ./signalization_qccxgrxhvgnfandawbuwonpytkbrhjvf.png
	2023-10-02 11:47:14  them ./signalization_ktwtfrlfjsnoqukcysexvzghkxvrvlnh.png
	2023-10-02 11:48:17  by  ./signalization_eymcrjssbgwivpyxnbwiyriupuxidunq.png
	2023-10-02 11:49:18 RkxBR ./signalization_aqhzrefkuxdymavxvpkmzguvftaqzifz.png
	2023-10-02 11:50:21 3tsVH ./signalization_wkqiyufjejlddvrpdoyjairgychslbrv.png
	2023-10-02 11:51:23 JHLTN ./signalization_kzipwwkhjfttxumuwpdfkcfkobkydnen.png
	2023-10-02 11:52:25 vWG4t ./signalization_eufsdqatkmokqhpxtgzazfhlwzcmtnyl.png
	2023-10-02 11:53:28 YW9aT ./signalization_zzoubizlyyipumvijaqyoudbsnngrmks.png
	2023-10-02 11:54:32 i1aNH ./signalization_cimekmmmntzzeisntnmtkekkvifpblpn.png
	2023-10-02 11:55:35 FNfQ= ./signalization_srjbvbrmsvfsalrkzndhyijgrhpcztfz.png
	2023-10-02 11:56:39 = ! ./signalization_clibjjykcqqsxncqusveikakzoitfnea.png
	VESSEL: 745387
	2023-10-02 11:30:18 K ./signalization_qronxprykjntmvcwcihtxevtefglpcea.png
	2023-10-02 11:32:50 KL ./signalization_xhbbnbucjhrheenctftiicbloqzjbojz.png
	2023-10-02 11:35:08 Can you s ./signalization_eqxboejickzswuiivlmjyphhpeciqbfj.png
	2023-10-02 11:36:35 ell us so ./signalization_gxsfjwnfbtztajgmrmklrrkzpthwbcbh.png
	2023-10-02 11:38:02 me ipv4 a ./signalization_mmfutnnhmbuwikijmmxvafvoscaureed.png
	2023-10-02 11:39:56 ddresses? ./signalization_cenithsibphpqiyzelzsrmksqfnsljes.png
	2023-10-02 12:45:00 Relay: Ha ./signalization_gtzwweieommowkqgtvxkwbqndlzlpois.png
	2023-10-02 12:46:21 ve you se ./signalization_zzdkdzzmihnwplqldurdutuokyszakxg.png
	2023-10-02 12:47:52 en Mr. Ca ./signalization_wreirpozghydrwqjgtzmtqjjrxlyhtqw.png
	2023-10-02 12:49:28 letka? ./signalization_ucrcxftmrzpgvksdmkdupahttpwhebjg.png
	VESSEL: 782535
	2023-10-02 11:30:18 BV ./signalization_zvdaadtixobvgkvpxolkjlqolsjxoxxp.png
	2023-10-02 11:37:27  ./signalization_lmvaisoycxceyqholqthljfdhjgwiqar.png
	2023-10-02 11:38:32  ./signalization_urqlxpwijqjrbtexkqphvckibsjigsbp.png
	2023-10-02 11:39:40  ./signalization_faymrpjbajotiyqxwuiuakimuvzhgpun.png
	2023-10-02 11:40:44  ./signalization_qbtyjmwocjujdnhjkmsdqctuucngarts.png
	2023-10-02 11:50:31 BV ./signalization_omlrfmokmamoszvfopkgeemjvprtfhcw.png

We can see some readable text, great. Also we can see some undecoded signalisations. It's some very long singalisations and function findCountours return it as 1 countour with all flags instead one by one - because flags are too close to each other. Unfortunately at this point even chat GPT failed and I didn't convice it how to fix it :-) But in output is one interesting part:

	2023-10-02 11:49:18 RkxBR ./signalization_aqhzrefkuxdymavxvpkmzguvftaqzifz.png
	2023-10-02 11:50:21 3tsVH ./signalization_wkqiyufjejlddvrpdoyjairgychslbrv.png
	2023-10-02 11:51:23 JHLTN ./signalization_kzipwwkhjfttxumuwpdfkcfkobkydnen.png
	2023-10-02 11:52:25 vWG4t ./signalization_eufsdqatkmokqhpxtgzazfhlwzcmtnyl.png
	2023-10-02 11:53:28 YW9aT ./signalization_zzoubizlyyipumvijaqyoudbsnngrmks.png
	2023-10-02 11:54:32 i1aNH ./signalization_cimekmmmntzzeisntnmtkekkvifpblpn.png
	2023-10-02 11:55:35 FNfQ= ./signalization_srjbvbrmsvfsalrkzndhyijgrhpcztfz.png
	2023-10-02 11:56:39 = ! ./signalization_clibjjykcqqsxncqusveikakzoitfnea.png

It seems like base64. Let's try it:

	echo -n "RkxBR3tsVHJHLTNvWG4tYW9aTi1aNHFNfQ=="|base64 -d
	FLAG{lTrG-3oXn-aoZN-Z4qM}