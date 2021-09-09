## train057_S10_Sp004_M_L1_G1_A3-C_LP
* intent_find_by_cuisine:السلام و علیکم مجھے اس وقت بہت زیادہ ہی بھوک لگی ہوئی ہے اور میں [برگر](cuisine) کھانا چاہتا ہوں.
	- slot{"cuisine":"برگر"}
	- action_find_by_cuisine
* intent_find_by_location_price:میں اس وقت جو ہوں وہ [ماڈل ٹاؤن](location) میں ہوں .اور میرے پاس [ہزار](price) روپے ہیں کیا آپ مجھے بتا سکتی ہیں کہ میں یہ کہاں سے کھا سکتا ہوں.
	- slot{"cuisine":"برگر"}
	- slot{"location":"ماڈل ٹاؤن"}
	- slot{"price":"ہزار"}
	- action_find_by_location_cuisine_price
	- action_restart