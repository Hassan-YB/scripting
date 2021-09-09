## train053_S9_Sp004_M_L1_G1_A3-CP_L
* intent_find_by_cuisine_price:السلام علیکم مجھے اس وقت بہت بھوک لگی ہے مجھے [بریانی](cuisine) کھانی ہے اور میرے پاس تقریباً [تین سو](price) روپے ہیں.
	- slot{"cuisine":"بریانی"}
	- slot{"price":"تین سو"}
	- action_find_by_cuisine_and_price
* intent_find_by_location:میں [ٹاؤن شپ](location) سے کھانا چاہتا ہوں.
	- slot{"cuisine":"بریانی"}
	- slot{"price":"تین سو"}
	- slot{"location":"ٹاؤن شپ"}
	- action_find_by_location_cuisine_price
	- action_restart