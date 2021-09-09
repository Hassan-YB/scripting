## train190_S10_Sp013_M_L1_G1_A1-C_LP
* intent_find_by_cuisine:میں [پیزا](cuisine) کھانا چاہتا ہوں
	- slot{"cuisine":"پیزا"}
	- action_find_by_cuisine
* intent_find_by_location_price:میں پیزا [ڈی ایچ اے](location) لاہور سے کھانا چاہتا ہوں اور میری پرائس رینج [دو ہزار](price) روپے ہے
	- slot{"cuisine":"پیزا"}
	- slot{"location":"ڈی ایچ اے"}
	- slot{"price":"دو ہزار"}
	- action_find_by_location_cuisine_price
	- action_restart