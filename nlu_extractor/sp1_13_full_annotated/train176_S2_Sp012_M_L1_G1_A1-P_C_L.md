## train176_S2_Sp012_M_L1_G1_A1-P_C_L
* intent_find_by_price:جی میرے پاس اس وقت [ہزار](price) روپیہ ہے اور مجھے بہت بھوک لگ رہی ہے
	- slot{"price":"ہزار"}
	- action_find_by_price
* intent_find_by_cuisine:جی میرا [دیسی](cuisine) کھانے کو دل کر رہا ہے
	- slot{"price":"ہزار"}
	- slot{"cuisine":"دیسی"}
	- action_find_by_cuisine_and_price
* intent_find_by_location:[کلمہ چوک](location) سے
	- slot{"price":"ہزار"}
	- slot{"cuisine":"دیسی"}
	- slot{"location":"کلمہ چوک"}
	- action_find_by_location_cuisine_price
	- action_restart