## train047_S1_Sp004_M_L1_G1_A3-L_C_P
* intent_find_by_location:السلام علیکم میں [کلمہ چوک](location) پر ہوں ۔مجھے اس وقت بہت بھوک لگی ہے اور میں کھانا کھانا چاہتا ہوں۔
	- slot{"location":"کلمہ چوک"}
	- action_find_by_location
* intent_find_by_cuisine:میں [برگر](cuisine) کھانا چاہتا ہوں۔
	- slot{"location":"کلمہ چوک"}
	- slot{"cuisine":"برگر"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:[مناسب](price) ہی ہوں.
	- slot{"location":"کلمہ چوک"}
	- slot{"cuisine":"برگر"}
	- slot{"price":"مناسب"}
	- action_find_by_location_cuisine_price
	- action_restart