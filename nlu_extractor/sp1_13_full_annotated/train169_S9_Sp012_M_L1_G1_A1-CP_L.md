## train169_S9_Sp012_M_L1_G1_A1-CP_L
* intent_find_by_cuisine_price:میری جیب میں اس وقت [ہزار](price) روپیہ پڑا ہوا ہے اور میرا [پیزا](cuisine) کھانے کا دل کر رہا ہے
	- slot{"price":"ہزار"}
	- slot{"cuisine":"پیزا"}
	- action_find_by_cuisine_and_price
* intent_find_by_location:[ماڈل ٹاؤن](location) سے
	- slot{"price":"ہزار"}
	- slot{"cuisine":"پیزا"}
	- slot{"location":"ماڈل ٹاؤن"}
	- action_find_by_location_cuisine_price
	- action_restart