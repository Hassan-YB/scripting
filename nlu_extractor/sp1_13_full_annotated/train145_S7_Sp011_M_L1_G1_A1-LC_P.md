## train145_S7_Sp011_M_L1_G1_A1-LC_P
* intent_find_by_location_cuisine:مجھے [یو ای ٹی](location) میں [بریانی](cuisine) کھانی ہے
	- slot{"location":"یو ای ٹی"}
	- slot{"cuisine":"بریانی"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:[مناسب](price)
	- slot{"location":"یو ای ٹی"}
	- slot{"cuisine":"بریانی"}
	- slot{"price":"مناسب"}
	- action_find_by_location_cuisine_price
	- action_restart