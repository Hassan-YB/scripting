## train144_S7_Sp011_M_L1_G1_A1-LC_P
* intent_find_by_location_cuisine:میں [یو ای ٹی](location) میں ہوں اور مجھے [بریانی](cuisine) کھانی ہے
	- slot{"location":"یو ای ٹی"}
	- slot{"cuisine":"بریانی"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:[سستا](price)
	- slot{"location":"یو ای ٹی"}
	- slot{"cuisine":"بریانی"}
	- slot{"price":"سستا"}
	- action_find_by_location_cuisine_price
	- action_restart