## train003_S3_Sp001_F_L1_G1_A5-C_P_L
* intent_find_by_cuisine:میں مجھے بھوک لگی ہے اور میں [دیسی](cuisine) کھانا کھانا چاہتی ہوں.
	- slot{"cuisine":"دیسی"}
	- action_find_by_cuisine
* intent_find_by_price:میں [مناسب](price) کھانا کھانا چاہتی ہوں.
	- slot{"cuisine":"دیسی"}
	- slot{"price":"مناسب"}
	- action_find_by_cuisine_and_price
* intent_find_by_location:میں لاہور میں [ماڈل ٹاؤن](location) سے کھانا کھانا چاہتی ہوں.
	- slot{"cuisine":"دیسی"}
	- slot{"price":"مناسب"}
	- slot{"location":"ماڈل ٹاؤن"}
	- action_find_by_location_cuisine_price
	- action_restart