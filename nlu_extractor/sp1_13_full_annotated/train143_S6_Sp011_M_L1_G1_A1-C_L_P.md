## train143_S6_Sp011_M_L1_G1_A1-C_L_P
* intent_find_by_cuisine:مجھے بھوک لگی ہے مجھے [برگر](cuisine) کھانا ہے
	- slot{"cuisine":"برگر"}
	- action_find_by_cuisine
* intent_find_by_location:[سمن آباد](location) سے
	- slot{"cuisine":"برگر"}
	- slot{"location":"سمن آباد"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:[مناسب](price)
	- slot{"cuisine":"برگر"}
	- slot{"location":"سمن آباد"}
	- slot{"price":"مناسب"}
	- action_find_by_location_cuisine_price
	- action_restart