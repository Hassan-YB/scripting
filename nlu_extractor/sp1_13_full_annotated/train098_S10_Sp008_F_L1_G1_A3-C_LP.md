## train098_S10_Sp008_F_L1_G1_A3-C_LP
* intent_find_by_cuisine:مجھے نا بہت بھوک لگی ہے تو میں نے [چائنیز](cuisine) کھانا ہے
	- slot{"cuisine":"چائنیز"}
	- action_find_by_cuisine
* intent_find_by_location_price:[ ٹاؤن شپ](location) سے [ہزار](price) روپے میں
	- slot{"cuisine":"چائنیز"}
	- slot{"location":" ٹاؤن شپ"}
	- slot{"price":"ہزار"}
	- action_find_by_location_cuisine_price
	- action_restart