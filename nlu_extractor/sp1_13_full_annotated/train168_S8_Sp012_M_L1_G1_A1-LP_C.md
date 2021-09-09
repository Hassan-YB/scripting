## train168_S8_Sp012_M_L1_G1_A1-LP_C
* intent_find_by_location_price:جی میں اس وقت [ماڈل ٹاؤن](location) میں بیٹھا ہوا ہوں اور میری جیب میں [پانچ سو](price) روپیہ ہے
	- slot{"location":"ماڈل ٹاؤن"}
	- slot{"price":"پانچ سو"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:جی میں [دیسی](cuisine) کھانا پسند کروں گا
	- slot{"location":"ماڈل ٹاؤن"}
	- slot{"price":"پانچ سو"}
	- slot{"cuisine":"دیسی"}
	- action_find_by_location_cuisine_price
	- action_restart