## 259_S6_SP51_F_L1_G1_A1-C_L_P
* intent_find_by_cuisine:میں [چائنیز](cuisine) فوڈ کھانا چاہتی ہوں
	- slot{"cuisine":"چائنیز"}
	- action_find_by_cuisine
* intent_find_by_location:میں [لنک روڈ](location) والی سائیڈ پہ رہتی ہوں تو ادھر سے کھانا چاہتی ہوں
	- slot{"cuisine":"چائنیز"}
	- slot{"location":"لنک روڈ"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:میرے پاس [تھاؤزنڈ](price) روپیز ہے تو میں اس کی مناسبت سے کھانا چاہتی ہوں
	- slot{"cuisine":"چائنیز"}
	- slot{"location":"لنک روڈ"}
	- slot{"price":"تھاؤزنڈ"}
	- action_find_by_location_cuisine_price
	- action_restart