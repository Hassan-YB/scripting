## train006_S6_Sp001_F_L1_G1_A5-C_L_P
* intent_find_by_cuisine:مجھے بھوک لگی ہے اور میں [چائنیز](cuisine) کھانا کھانا چاہتی ہوں.
	- slot{"cuisine":"چائنیز"}
	- action_find_by_cuisine
* intent_find_by_location:میں لاہور میں [ماڈل ٹاؤن](location) سے کھانا کھانا چاہتی ہوں.
	- slot{"cuisine":"چائنیز"}
	- slot{"location":"ماڈل ٹاؤن"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:میں [مناسب](price) کھانا کھانا چاہتی ہوں.
	- slot{"cuisine":"چائنیز"}
	- slot{"location":"ماڈل ٹاؤن"}
	- slot{"price":"مناسب"}
	- action_find_by_location_cuisine_price
	- action_restart