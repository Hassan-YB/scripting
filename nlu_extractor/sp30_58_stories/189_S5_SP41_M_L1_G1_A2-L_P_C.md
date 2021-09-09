## 189_S5_SP41_M_L1_G1_A2-L_P_C
* intent_open:میں کھانا کھانا چاہ رہا ہوں
	- utter_ask_location
* intent_find_by_location:میں لاہور میں [ماڈل ٹاؤن](location) سے کھانا کھانا چاہتا ہوں
	- slot{"location":"ماڈل ٹاؤن"}
	- action_find_by_location
* intent_find_by_price:میں [مناسب](price) کھانا کھانا چاہتا ہوں
	- slot{"location":"ماڈل ٹاؤن"}
	- slot{"price":"مناسب"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:میں [فاسٹ فوڈ](cuisine) کھانا چاہتا ہوں
	- slot{"location":"ماڈل ٹاؤن"}
	- slot{"price":"مناسب"}
	- slot{"cuisine":"فاسٹ فوڈ"}
	- action_find_by_location_cuisine_price
	- action_restart