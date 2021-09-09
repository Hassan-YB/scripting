## train049_S8_Sp004_M_L1_G1_A3-LP_C
* intent_find_by_location_price:میں اس وقت [گارڈن ٹاؤن](location) میں ہوں اور میں میری جیب میں اس وقت[ چھ سو](price) ہیں میں کھانا کھانا چاہتا ہوں مجھے بہت بھوک لگی.
	- slot{"location":"گارڈن ٹاؤن"}
	- slot{"price":" چھ سو"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:میں [بریانی](cuisine) کھانا چاہتا ہوں۔
	- slot{"location":"گارڈن ٹاؤن"}
	- slot{"price":" چھ سو"}
	- slot{"cuisine":"بریانی"}
	- action_find_by_location_cuisine_price
	- action_restart