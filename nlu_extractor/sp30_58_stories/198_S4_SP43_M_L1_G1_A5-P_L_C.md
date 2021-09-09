## 198_S4_SP43_M_L1_G1_A5-P_L_C
* intent_find_by_price:السلام علیکم میں ایکچوئلی میکسیمم ود ان [تھاؤزنڈ](price) میں کھانا کھانا چاہ رہا ہوں کچھ
	- slot{"price":"تھاؤزنڈ"}
	- action_find_by_price
* intent_find_by_location:میں :م: [کینٹ](location) ایریا میں کھانا چاہتا ہوں
	- slot{"price":"تھاؤزنڈ"}
	- slot{"location":"کینٹ"}
	- action_find_by_location_and_price
* intent_find_by_price:میں [چائنیز](cuisine) کھانا چاہوں گا
	- slot{"price":"تھاؤزنڈ"}
	- slot{"location":"کینٹ"}
	- slot{"cuisine":"چائنیز"}
	- action_find_by_location_cuisine_price
	- action_restart