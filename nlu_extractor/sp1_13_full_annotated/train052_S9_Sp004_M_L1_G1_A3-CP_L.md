## train052_S9_Sp004_M_L1_G1_A3-CP_L
* intent_find_by_cuisine_price:میں اس وقت جو ہے وہ [بریانی](cuisine)کھانا چاہتا ہوں اور جس کی پرائس تقریباً [پانچ سو](price) کا رینج ہو.
	- slot{"cuisine":"بریانی"}
	- slot{"price":"پانچ سو"}
	- action_find_by_location_cuisine_price
* intent_find_by_location:میں [ماڈل ٹاؤن](location) سے کھانا  چاہتا ہوں
	- slot{"cuisine":"بریانی "}
	- slot{"price":"پانچ سو"}
	- slot{"location":"ماڈل ٹاؤن"}
	- action_find_by_location_cuisine_price
	- action_restart