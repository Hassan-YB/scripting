## 194_S7_SP42_M_L1_G1_A5-LC_P
* intent_find_by_location_cuisine:میں لاہور میں [ماڈل ٹاؤن](location) سے [دیسی](cuisine) کھانا کھانا چاہتا ہوں
	- slot{"location":"ماڈل ٹاؤن"}
	- slot{"cuisine":"دیسی"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:میں [مناسب](price) کھانا کھانا چاہتا ہوں
	- slot{"location":"ماڈل ٹاؤن"}
	- slot{"cuisine":"دیسی"}
	- slot{"price":"مناسب"}
	- action_find_by_location_cuisine_price
	- action_restart