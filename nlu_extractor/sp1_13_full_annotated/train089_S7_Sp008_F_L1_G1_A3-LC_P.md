## train089_S7_Sp008_F_L1_G1_A3-LC_P
* intent_find_by_location_cuisine:میں [یو ای ٹی](location) سے بات کر رہی ہوں میں [برگر](cuisine) کھانا پسند کروں گی
	- slot{"location":"یو ای ٹی"}
	- slot{"cuisine":"برگر"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:[مناسب](price)
	- slot{"location":"یو ای ٹی"}
	- slot{"cuisine":"برگر"}
	- slot{"price":"مناسب"}
	- action_find_by_location_cuisine_price
	- action_restart