## 245_S5_SP49_F_L1_G1_A1-L_P_C
* intent_find_by_location:میں [جوہر ٹاؤن](location) کے پاس ہوں
	- slot{"location":"جوہر ٹاؤن"}
	- action_find_by_location
* intent_find_by_price:میں [مناسب](price) کھانا کھانا چاہتی ہوں
	- slot{"location":"جوہر ٹاؤن"}
	- slot{"price":"مناسب"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:میں [چائنیز](cuisine) فوڈ کھانا چاہتی ہوں
	- slot{"location":"جوہر ٹاؤن"}
	- slot{"price":"مناسب"}
	- slot{"cuisine":"چائنیز"}
	- action_find_by_location_cuisine_price
	- action_restart