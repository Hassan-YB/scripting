## train180_S6_Sp013_M_L1_G1_A1-C_L_P
* intent_find_by_cuisine:مجھے بھوک لگ رہی ہے اور میں [چائنیز](cuisine) کھانا چاہتا ہوں
	- slot{"cuisine":"چائنیز"}
	- action_find_by_cuisine
* intent_find_by_location:میں لاہور میں کھانا [اقبال ٹاؤن](location) سے کھانا چاہتا ہوں
	- slot{"cuisine":"چائنیز"}
	- slot{"location":"اقبال ٹاؤن"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:[مناسب](price)
	- slot{"cuisine":"چائنیز"}
	- slot{"location":"اقبال ٹاؤن"}
	- slot{"price":"مناسب"}
	- action_find_by_location_cuisine_price
	- action_restart