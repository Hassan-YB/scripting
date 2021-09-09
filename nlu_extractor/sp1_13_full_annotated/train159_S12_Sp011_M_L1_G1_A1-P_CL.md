## train159_S12_Sp011_M_L1_G1_A1-P_CL
* intent_find_by_price:میں [دو ہزار](price) میں کھانا کھانا چاہتا ہوں اور مجھے شدید بھوک لگی ہے
	- slot{"price":"دو ہزار"}
	- action_find_by_price
* intent_find_by_location_cuisine:میں [لکشمی چوک](location) سے [بریانی](cuisine) کھانا چاہتا ہوں
	- slot{"price":"دو ہزار"}
	- slot{"location":"لکشمی چوک"}
	- slot{"cuisine":"بریانی"}
	- action_find_by_location_cuisine_price
	- action_restart