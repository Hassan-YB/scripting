## 222_S4_SP46_F_L1_G2_A3-P_L_C
* intent_find_by_price:مجھے [پانچ سو](price) روپے کے اندر اندر اچھا اور مناسب کھانا چاہیے
	- slot{"price":"پانچ سو"}
	- action_find_by_price
* intent_find_by_location:میں لاہور میں [ماڈل ٹاؤن](location) سے کھانا کھانا چاہتی ہوں
	- slot{"price":"پانچ سو"}
	- slot{"location":"ماڈل ٹاؤن"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:میں [دیسی](cuisine) کھانا کھانا چاہتی ہوں
	- slot{"price":"پانچ سو"}
	- slot{"location":"ماڈل ٹاؤن"}
	- slot{"cuisine":"دیسی"}
	- action_find_by_location_cuisine_price
	- action_restart