## train107_S7_Sp009_F_L1_G1_A4-LC_P
* intent_find_by_location_cuisine:میں اس وقت [گرین ٹاؤن](location) ایریا میں ہوں اور مجھے بہت بھوک لگی ہے تو میں [برگر](cuisine) کھانا چاہتی ہوں.
	- slot{"location":"گرین ٹاؤن"}
	- slot{"cuisine":"برگر"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:میں [مناسب](price) قیمت میں کھانا پسند کروں گی
	- slot{"location":"گرین ٹاؤن"}
	- slot{"cuisine":"برگر"}
	- slot{"price":"مناسب"}
	- action_find_by_location_cuisine_price
	- action_restart