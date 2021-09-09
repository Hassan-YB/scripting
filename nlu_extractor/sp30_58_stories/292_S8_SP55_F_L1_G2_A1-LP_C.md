## 292_S8_SP55_F_L1_G2_A1-LP_C
* intent_find_by_location_price:السلام علیکم :م: میں اس ٹائم [مال روڈ](location) لاہور پر کھڑی ہوں اور مجھے :م: کھانا کھانے کے لیے کسی اچھی جگہ کے :م: مجھے آپ نام بتا سکتیں ہیں جہاں میں [دو ہزار سے پچیس سو](price) کی رینج میں کھانا کھا سکوں
	- slot{"location":"مال روڈ"}
	- slot{"price":"دو ہزار سے پچیس سو"}
	- action_find_by_location_and_price
* intent_find_by_cuisine::م: [چائنیز](cuisine) فوڈ
	- slot{"location":"مال روڈ"}
	- slot{"price":"دو ہزار سے پچیس سو"}
	- slot{"cuisine":"چائنیز"}
	- action_find_by_location_cuisine_price
	- action_restart