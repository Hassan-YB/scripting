## train151_S9_Sp011_M_L1_G1_A1-CP_L
* intent_find_by_cuisine_price:مجھے [مناسب](price) قیمت میں [برگر](cuisine) کھانا ہے
	- slot{"price":"مناسب"}
	- slot{"cuisine":"برگر"}
	- action_find_by_cuisine_and_price
* intent_find_by_location:میں[ سمن آباد](location) میں رہتا ہوں اور مجھے سمن آباد کے آس پاس کوئی جگہ چاہیے کھانے پینے کے لیے
	- slot{"price":"مناسب"}
	- slot{"cuisine":"برگر"}
	- slot{"location":" سمن آباد"}
	- action_find_by_location_cuisine_price
	- action_restart