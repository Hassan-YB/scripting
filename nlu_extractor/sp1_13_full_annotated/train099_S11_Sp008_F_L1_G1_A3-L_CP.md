## train099_S11_Sp008_F_L1_G1_A3-L_CP
* intent_find_by_location:مجھے نا بہت بھوک لگ رہی ہے میں [ٹاؤن شپ](location) کے ایریا میں کھڑی ہوں
	- slot{"location":"ٹاؤن شپ"}
	- action_find_by_location
* intent_find_by_cuisine_price:میں [برگر](cuisine) کھانا پسند کروں گی [پانچ سو](price) تک میں
	- slot{"location":"ٹاؤن شپ"}
	- slot{"cuisine":"برگر"}
	- slot{"price":"پانچ سو"}
	- action_find_by_location_cuisine_price
	- action_restart