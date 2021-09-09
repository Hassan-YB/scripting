## train157_S11_Sp011_M_L1_G1_A1-L_CP
* intent_find_by_location:میں [سمن آباد](location) میں رہتا ہوں اور مجھے کھانا کھانا ہے اور مجھے بہت شدید بھوک لگی ہوئی ہے
	- slot{"location":"سمن آباد"}
	- action_find_by_location
* intent_find_by_cuisine_price:میں [دیسی](cuisine) کھانا کھانا چاہتا ہوں اور میری رینج [ہزار](price) روپیہ ہے
	- slot{"location":"سمن آباد"}
	- slot{"cuisine":"دیسی"}
	- slot{"price":"ہزار"}
	- action_find_by_location_cuisine_price
	- action_restart