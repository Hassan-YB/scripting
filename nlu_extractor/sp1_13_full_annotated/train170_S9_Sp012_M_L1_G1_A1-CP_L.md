## train170_S9_Sp012_M_L1_G1_A1-CP_L
* intent_find_by_cuisine_price:میرا اس وقت [پیزا](cuisine) کھانے کو دل کر رہا ہے اور میری جیب میں اس وقت صرف اور صرف [پانچ ہزار](price) کا پڑا ہوا ہے
	- slot{"cuisine":"پیزا"}
	- slot{"price":"پانچ ہزار"}
	- action_find_by_cuisine_and_price
* intent_find_by_location:[واپڈا ٹاؤن](location) سے
	- slot{"cuisine":"پیزا"}
	- slot{"price":"پانچ ہزار"}
	- slot{"location":"واپڈا ٹاؤن"}
	- action_find_by_location_cuisine_price
	- action_restart