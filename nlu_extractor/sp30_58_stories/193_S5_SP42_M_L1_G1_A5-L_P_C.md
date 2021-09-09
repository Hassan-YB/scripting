## 193_S5_SP42_M_L1_G1_A5-L_P_C
* intent_open:میں کھانا کھانا چاہتا ہوں
	- utter_ask_location
* intent_find_by_location:میں لاہور میں [ماڈل ٹاؤن](location) سے کھانا کھانا چاہتا ہوں
	- slot{"location":"ماڈل ٹاؤن"}
	- action_find_by_location
* intent_find_by_price:میں [مہنگا](price) کھانا کھانا چاہتا ہوں
	- slot{"location":"ماڈل ٹاؤن"}
	- slot{"price":"مہنگا"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:میں [دیسی](cuisine) کھانا کھانا چاہتا ہوں
	- slot{"location":"ماڈل ٹاؤن"}
	- slot{"price":"مہنگا"}
	- slot{"cuisine":"دیسی"}
	- action_find_by_location_cuisine_price
	- action_restart