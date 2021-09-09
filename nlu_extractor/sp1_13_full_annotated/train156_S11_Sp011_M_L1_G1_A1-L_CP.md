## train156_S11_Sp011_M_L1_G1_A1-L_CP
* intent_find_by_location:میں [یو ای ٹی](location) کے آس پاس ہوں اور مجھے کھانا کھانا ہے
	- slot{"location":"یو ای ٹی"}
	- action_find_by_location
* intent_find_by_cuisine_price:میں [دیسی](cuisine) کھانا پسند کرتا ہوں اور مجھے [ہزار](price) روپے کی رینج کے اندر کھانا کھانا ہے
	- slot{"location":"یو ای ٹی"}
	- slot{"cuisine":"دیسی"}
	- slot{"price":"ہزار"}
	- action_find_by_location_cuisine_price
	- action_restart