## train014_S12_Sp002_F_L1_G2_A5-P_CL
* intent_find_by_price:میں [دو ہزار](price) روپیز میں کھانا کھانا چاہتی ہوں.
	- slot{"price":"دو ہزار"}
	- action_find_by_price
* intent_find_by_location_cuisine:میں [فاسٹ فوڈ](cuisine) کھانا کھانا چاہتی ہوں اور [ماڈل ٹاؤن](location) میں کھانا چاہتی ہوں۔
	- slot{"price":"دو ہزار"}
	- slot{"cuisine":"فاسٹ فوڈ"}
	- slot{"location":"ماڈل ٹاؤن"}
	- action_find_by_location_cuisine_price
	- action_restart