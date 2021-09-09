## 190_S1_SP42_M_L1_G1_A5-L_C_P
* intent_open:میں کھانا کھانا چاہتا ہوں
	- utter_ask_location
* intent_find_by_location:میں لاہور میں [ماڈل ٹاؤن](location) سے کھانا کھانا چاہتا ہوں
	- slot{"location":"ماڈل ٹاؤن"}
	- action_find_by_location
* intent_find_by_cuisine:میں [فاسٹ فوڈ](cuisine) کھانا چاہتا ہوں
	- slot{"location":"ماڈل ٹاؤن"}
	- slot{"cuisine":"فاسٹ فوڈ"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:میں [مناسب](price) کھانا کھانا چاہتا ہوں
	- slot{"location":"ماڈل ٹاؤن"}
	- slot{"cuisine":"فاسٹ فوڈ"}
	- slot{"price":"مناسب"}
	- action_find_by_location_cuisine_price
	- action_restart