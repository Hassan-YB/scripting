## train153_S10_Sp011_M_L1_G1_A1-C_LP
* intent_find_by_cuisine:مجھے [برگر](cuisine) بہت پسند ہے مجھے [برگر](cuisine) کھانا ہے
	- slot{"cuisine":"برگر"}
	- action_find_by_cuisine
* intent_find_by_location_price:میں [سمن آباد](location) سے منگوانا چاہتا ہوں اور [مناسب](price) قیمت میں اسے حاصل کرنا چاہتا ہوں
	- slot{"cuisine":"برگر"}
	- slot{"location":"سمن آباد"}
	- slot{"price":"مناسب"}
	- action_find_by_location_cuisine_price
	- action_restart