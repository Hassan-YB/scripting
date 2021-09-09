## train055_S10_Sp004_M_L1_G1_A3-C_LP
* intent_find_by_cuisine:مجھے اس وقت بہت زیادہ ہی بھوک لگی ہوئی ہے اور میں جو ہے وہ [پیزا](cuisine) کھانا چاہتا ہوں.
	- slot{"cuisine":"پیزا"}
	- action_find_by_cuisine
* intent_find_by_location_cuisine:میں تھوڑی دیر [ٹاؤن شپ](location) میں ہوں اور مجھے تقریباً [ون تھاؤزنڈ](price) کی رینج تک پیزا جو ہے نا وہ ملنا چاہیے.
	- slot{"cuisine":"پیزا"}
	- slot{"location":"ٹاؤن شپ"}
	- slot{"price":"ون تھاؤزنڈ"}
	- action_find_by_location_cuisine_price
	- action_restart