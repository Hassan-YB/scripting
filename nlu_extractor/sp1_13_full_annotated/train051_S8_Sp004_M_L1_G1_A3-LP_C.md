## train051_S8_Sp004_M_L1_G1_A3-LP_C
* intent_find_by_location_price:السلام و علیکم جناب مجھے بہت بھوک لگ گئی ہے اور میرےاے ٹی ایم میں نا اس وقت [بارہ سو](price) ہیں. اور میں کھانا کھانا چاہتا ہوں اس وقت میں [ماڈل ٹاؤن](location) میں موجود ہوں
	- slot{"price":"بارہ سو"}
	- slot{"location":"ماڈل ٹاؤن"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:میں [پیزا](cuisine) کھانا چاہتا ہوں
	- slot{"price":"بارہ سو"}
	- slot{"location":"ماڈل ٹاؤن"}
	- slot{"cuisine":"پیزا"}
	- action_find_by_location_cuisine_price
	- action_restart