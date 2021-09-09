## train087_S5_Sp008_F_L1_G1_A3-L_P_C
* intent_find_by_location:میں [یو ای ٹی](location) سے بات  کر رہی ہوں مجھے بہت بھوک لگ رہی ہے تو میں کھانا کھانا چاہتی ہوں
	- slot{"location":"یو ای ٹی"}
	- action_find_by_location
* intent_find_by_price:[مناسب](price)
	- slot{"location":"یو ای ٹی"}
	- slot{"price":"مناسب"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:[دیسی](cuisine)
	- slot{"location":"یو ای ٹی"}
	- slot{"price":"مناسب"}
	- slot{"cuisine":"دیسی"}
	- action_find_by_location_cuisine_price
	- action_restart