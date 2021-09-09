## 142_S8_SP33_M_L1_G1_A3-LP_C
* intent_find_by_location_price::م: میری لوکیشن اس ٹائم [یو ای ٹی](location) ہے اور میں [تھاؤزنڈ](price) کی رینج میں کوئی بھی چیز جو ہے نیئرسٹ کسی بھی ریسٹورنٹ سے کھانا چاہ رہا ہوں
	- slot{"price":"تھاؤزنڈ"}
	- slot{"location":"یو ای ٹی"}
	- action_find_by_location_and_price
* intent_find_by_location_price:[دیسی](cuisine)
	- slot{"price":"تھاؤزنڈ"}
	- slot{"location":"یو ای ٹی"}
	- slot{"cuisine":"دیسی"}
	- action_find_by_location_cuisine_price
	- action_restart