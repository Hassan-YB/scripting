## train108_S7_Sp009_F_L1_G1_A4-LC_P
* intent_find_by_location_cuisine:میں [جوہر ٹاؤن](location) ایریا سے بول رہی ہوں اور مجھے اس وقت بہت بھوک لگی ہے تو میں [دال چاول](cuisine) کھانا پسند کروں گی
	- slot{"location":"جوہر ٹاؤن"}
	- slot{"cuisine":"دال چاول"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:میں [مہنگا](price) کھانا پسند کروں گی
	- slot{"location":"جوہر ٹاؤن"}
	- slot{"cuisine":"دال چاول"}
	- slot{"price":"مہنگا"}
	- action_find_by_location_cuisine_price
	- action_restart