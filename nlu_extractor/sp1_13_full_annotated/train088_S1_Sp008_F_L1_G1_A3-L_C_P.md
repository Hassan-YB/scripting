## train088_S1_Sp008_F_L1_G1_A3-L_C_P
* intent_find_by_location:میں [یو ای ٹی](location) سے بات کر رہی ہوں
	- slot{"location":"یو ای ٹی"}
	- action_find_by_location
* intent_find_by_cuisine:[چائنیز](cuisine) کھانا پسند کروں گی
	- slot{"location":"یو ای ٹی"}
	- slot{"cuisine":"چائنیز"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:[مناسب](price)
	- slot{"location":"یو ای ٹی"}
	- slot{"cuisine":"چائنیز"}
	- slot{"price":"مناسب"}
	- action_find_by_location_cuisine_price
	- action_restart