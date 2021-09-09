## 247_S7_SP50_F_L1_G1_A2-LC_P
* intent_find_by_location_cuisine:میں [ماڈل ٹاؤن](location) میں ہوں اور میں [دیسی](cuisine) کھانا کھانا چاہ رہی ہوں
	- slot{"location":"ماڈل ٹاؤن"}
	- slot{"cuisine":"دیسی"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:[مناسب](price) قیمت میں
	- slot{"location":"ماڈل ٹاؤن"}
	- slot{"cuisine":"دیسی"}
	- slot{"price":"مناسب"}
	- action_find_by_location_cuisine_price
	- action_restart