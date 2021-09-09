## train113_S9_Sp009_F_L1_G1_A4-CP_L
* intent_find_by_cuisine_price:میرے پاس اس وقت جو ہے [ہنڈرڈ](price) روپیز ہیں اور مجھے بہت بھوک لگی ہے تو میں نے [فرائز](cuisine) کھانے ہیں
	- slot{"price":"ہنڈرڈ"}
	- slot{"cuisine":"فرائز"}
	- action_find_by_cuisine_and_price
* intent_find_by_location:میں یہ [گرین ٹاؤن](location) ایریا سے منگوانا پسند کروں گی
	- slot{"price":"ہنڈرڈ"}
	- slot{"cuisine":"فرائز"}
	- slot{"location":"گرین ٹاؤن"}
	- action_find_by_location_cuisine_price
	- action_restart