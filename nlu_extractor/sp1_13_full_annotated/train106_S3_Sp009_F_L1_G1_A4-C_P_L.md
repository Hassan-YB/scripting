## train106_S3_Sp009_F_L1_G1_A4-C_P_L
* intent_find_by_cuisine:مجھے بہت بھوک لگی ہے اور مجھے [چائنیز](cuisine) کھانا کھانا ہے
	- slot{"cuisine":"چائنیز"}
	- action_find_by_cuisine
* intent_find_by_price:میں [مناسب](price) کھانا پسند کروں گی
	- slot{"cuisine":"چائنیز"}
	- slot{"price":"مناسب"}
	- action_find_by_cuisine_and_price
* intent_find_by_location:میں [یو ای ٹی](location) سے منگوانا پسند کروں گی
	- slot{"cuisine":"چائنیز"}
	- slot{"price":"مناسب"}
	- slot{"location":"یو ای ٹی"}
	- action_find_by_location_cuisine_price
	- action_restart