## train073_S10_Sp007_F_L1_G1_A3-C_LP
* greet:ہیلو
	- utter_salaam
* intent_find_by_cuisine:میں [چائنیز](cuisine) کھانا چاہتی ہوں
	- slot{"cuisine":"چائنیز"}
	- action_find_by_cuisine
* intent_find_by_location_price:میں [مناسب](price) کھانا پسند کروں گی اور اگر [لنک روڈ](location) سے ہو جائے تو بہت اچھا ہو گا
	- slot{"cuisine":"چائنیز"}
	- slot{"location":"لنک روڈ"}
	- slot{"price":"مناسب"}
	- action_find_by_location_cuisine_price
	- action_restart