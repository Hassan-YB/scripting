## train155_S10_Sp011_M_L1_G1_A1-C_LP
* intent_find_by_cuisine:مجھے بہت بھوک لگی ہے میں نے [دیسی](cuisine) کھانا کھانا ہے
	- slot{"cuisine":"دیسی"}
	- action_find_by_cuisine
* intent_find_by_location_price:میں [یو ای ٹی](location) میں [پانچ سو](price) روپے میں اپنا کھانا کھانا چاہتا ہوں
	- slot{"cuisine":"دیسی"}
	- slot{"location":"یو ای ٹی"}
	- slot{"price":"پانچ سو"}
	- action_find_by_location_cuisine_price
	- action_restart