## train021_S10_Sp002_F_L1_G2_A5-C_LP
* intent_find_by_cuisine:میں[ پیزا](cuisine) کھانا چاہ رہی ہوں
	- slot{"cuisine":"پیزا"}
	- action_find_by_cuisine
* intent_find_by_location_price:میں [ماڈل ٹاؤن](location) میں ہوں [ماڈل ٹاؤن](location) سے کھانا چاہ رہی ہوں اور [ٹوئنٹی فائیو ہنڈرڈ](price) میں۔
	- slot{"cuisine":"پیزا"}
	- slot{"location":"ماڈل ٹاؤن"}
	- slot{"price":"ٹوئنٹی فائیو ہنڈرڈ"}
	- action_find_by_location_cuisine_price
	- action_restart