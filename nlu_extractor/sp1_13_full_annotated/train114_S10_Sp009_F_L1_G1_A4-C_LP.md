## train114_S10_Sp009_F_L1_G1_A4-C_LP
* intent_find_by_cuisine:مجھے بہت بھوک لگی ہے اور میں کھانا کھانا چاہتی ہوں تو کیا مجھے [بریانی](cuisine) مل سکتی ہے
	- slot{"cuisine":"بریانی"}
	- action_find_by_cuisine
* intent_find_by_location_price:میں [ٹاؤن شپ ایریا](location) سے منگوانا پسند کروں گی اور [تھری ہنڈرڈ](price) پرائس ہو
	- slot{"cuisine":"بریانی"}
	- slot{"location":"ٹاؤن شپ ایریا"}
	- slot{"price":"تھری ہنڈرڈ"}
	- action_find_by_location_cuisine_price
	- action_restart