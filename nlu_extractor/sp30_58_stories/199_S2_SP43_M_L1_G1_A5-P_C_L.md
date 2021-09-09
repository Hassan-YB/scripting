## 199_S2_SP43_M_L1_G1_A5-P_C_L
* intent_find_by_price:السلام علیکم ایکچوئلی میرے پاس فی الحال [ون تھاؤزنڈ](price) روپیز ہے اور میں اس رینج میں کچھ کھانا چاہ رہا ہوں
	- slot{"price":"ون تھاؤزنڈ"}
	- action_find_by_price
* intent_find_by_cuisine:میں [چائنیز](cuisine) فوڈ ٹرائے کرنا چاہتا ہوں
	- slot{"price":"ون تھاؤزنڈ"}
	- slot{"cuisine":"چائنیز"}
	- action_find_by_cuisine_and_price
* intent_find_by_location:میں [کینٹ](location) ایریا سے کھانا چاہتا ہوں
	- slot{"price":"ون تھاؤزنڈ"}
	- slot{"cuisine":"چائنیز"}
	- slot{"location":"کینٹ"}
	- action_find_by_location_cuisine_price
	- action_restart