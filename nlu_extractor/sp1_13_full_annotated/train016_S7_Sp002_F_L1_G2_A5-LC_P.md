## train016_S7_Sp002_F_L1_G2_A5-LC_P
* intent_find_by_location_cuisine:میں لاہور [ماڈل ٹاؤن](location) سے بول رہی ہوں میں [برگر](cuisine) کھانا چاہ رہی ہوں.
	- slot{"location":"ماڈل ٹاؤن"}
	- slot{"cuisine":"برگر"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:[مناسب](price) رینج میں.
	- slot{"location":"ماڈل ٹاؤن"}
	- slot{"cuisine":"برگر"}
	- slot{"price":"مناسب"}
	- action_find_by_location_cuisine_price
	- action_restart