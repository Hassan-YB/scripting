## train002_S2_Sp001_F_L1_G1_A5-P_C_L
* intent_find_by_price:مجھے بھوک لگی ہے اور میرے پاس [تھری تھاؤزنڈ](price) روپیز ہیں اور اتنے میں میں کھانا کھانا چاہتی ہوں.
	- slot{"price":"تھری"}
	- action_find_by_price
* intent_find_by_cuisine:[چائنیز](cuisine)
	- slot{"price":"تھری تھاؤزنڈ"}
	- slot{"cuisine":"چائنیز"}
	- action_find_by_cuisine_and_price
* intent_find_by_location:میں لاہور میں [جوہر ٹاؤن](location) سے کھانا کھانا چاہتی ہوں.
	- slot{"price":"تھری تھاؤزنڈ"}
	- slot{"cuisine":"چائنیز"}
	- slot{"location":"جوہر ٹاؤن"}
	- action_find_by_location_cuisine_price
	- action_restart