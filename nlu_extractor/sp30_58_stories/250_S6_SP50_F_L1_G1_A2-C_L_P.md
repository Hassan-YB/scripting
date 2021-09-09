## 250_S6_SP50_F_L1_G1_A2-C_L_P
* intent_find_by_cuisine:میں [چائنیز](cuisine) کھانا کھانا چاہ رہی ہوں
	- slot{"cuisine":"چائنیز"}
	- action_find_by_cuisine
* intent_find_by_location:[جوہر ٹاؤن](location) سے
	- slot{"cuisine":"چائنیز"}
	- slot{"location":"جوہر ٹاؤن"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:[مناسب](price) کھانا
	- slot{"cuisine":"چائنیز"}
	- slot{"location":"جوہر ٹاؤن"}
	- slot{"price":"مناسب"}
	- action_find_by_location_cuisine_price
	- action_restart