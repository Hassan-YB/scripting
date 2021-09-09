## train013_S9_Sp002_F_L1_G2_A5-CP_L
* intent_find_by_cuisine_price:میں مناسب رینج میں جیسے کہ [پندرہ سو](price) روپے میں [دیسی](cuisine) کھانا کھانا چاہتی ہوں
	- slot{"price":"پندرہ سو"}
	- slot{"cuisine":"دیسی"}
	- action_find_by_cuisine_and_price
* intent_find_by_location:میں لاہور میں [ماڈل ٹاؤن](location) سے کھانا کھانا چاہتی ہوں۔
	- slot{"price":"پندرہ سو"}
	- slot{"cuisine":"دیسی"}
	- slot{"location":"ماڈل ٹاؤن"}
	- action_find_by_location_cuisine_price
	- action_restart