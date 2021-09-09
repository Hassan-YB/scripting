## 249_S5_SP50_F_L1_G1_A2-L_P_C
* intent_open:میں کھانا کھانا چاہ رہی ہوں
	- utter_ask_location
* intent_find_by_location:[مغلپورہ](location) سے
	- slot{"location":"مغلپورہ"}
	- action_find_by_location
* intent_find_by_price:[مناسب](price) قیمت
	- slot{"location":"مغلپورہ"}
	- slot{"price":"مناسب"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:[چائنیز](cuisine)
	- slot{"location":"مغلپورہ"}
	- slot{"price":"مناسب"}
	- slot{"cuisine":"چائنیز"}
	- action_find_by_location_cuisine_price
	- action_restart