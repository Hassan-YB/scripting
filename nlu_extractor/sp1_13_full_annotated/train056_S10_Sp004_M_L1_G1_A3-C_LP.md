## train056_S10_Sp004_M_L1_G1_A3-C_LP
* intent_find_by_cuisine:السلام و علیکم میں اس وقت جو ہے نا مجھے بہت زیادہ ہی بھوک لگی ہوئی ہے اور مجھے [برگر](cuisine) کھانا ہے.
	- slot{"cuisine":"برگر"}
	- action_find_by_cuisine
* intent_find_by_location_price:میں اس وقت [والٹن](location) میں ہوں اور میرے پاس جو ہیں وہ [آٹھ سو](price) روپے ہیں۔
	- slot{"cuisine":"برگر"}
	- slot{"location":"والٹن"}
	- slot{"price":"آٹھ سو"}
	- action_find_by_location_cuisine_price
	- action_restart