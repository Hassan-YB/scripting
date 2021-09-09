## train116_S10_Sp009_F_L1_G1_A4-C_LP
* intent_find_by_cuisine:بارش ہو رہی ہے اور میں جو ہوں [پکوڑے](cuisine) کھانا چاہتی ہوں
	- slot{"cuisine":"پکوڑے"}
	- action_find_by_cuisine
* intent_find_by_location_price:میں [فیصل ٹاؤن](location) ایریا سے کھانا پسند کروں گی [فائیو ہنڈرڈ](price) تک کی رینج میں
	- slot{"cuisine":"پکوڑے"}
	- slot{"location":"فیصل ٹاؤن"}
	- slot{"price":"فائیو ہنڈرڈ"}
	- action_find_by_location_cuisine_price
	- action_restart