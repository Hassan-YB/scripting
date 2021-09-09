## 290_S4_SP55_F_L1_G2_A1-P_L_C
* intent_find_by_price::م: السلام علیکم :م: اس ٹائم کیونکہ کھانے کا ٹائم ہو رہا ہے تو آپ مجھے :م: [ون تھاؤزنڈ سے ففٹین ہنڈرڈ](price) کی رینج میں کوئی ریسٹورنٹ ریکومنڈ کر سکتیں ہیں جہاں پہ ہم جو کہ لنچ کر سکیں
	- slot{"price":"ون تھاؤزنڈ سے ففٹین ہنڈرڈ"}
	- action_find_by_price
* intent_find_by_location::م: [ڈفینس](location) جو ایریا ہے ڈے ایچ اے فیز تھری
	- slot{"price":"ون تھاؤزنڈ سے ففٹین ہنڈرڈ"}
	- slot{"location":"ڈفینس"}
	- action_find_by_location_and_price
* intent_find_by_cuisine::م: [چائنیز](cuisine) فوڈ
	- slot{"price":"ون تھاؤزنڈ سے ففٹین ہنڈرڈ"}
	- slot{"location":"ڈفینس"}
	- slot{"cuisine":"چائنیز"}
	- action_find_by_location_cuisine_price
	- action_restart