## train091_S8_Sp008_F_L1_G1_A3-LP_C
* intent_find_by_location_price:میں [ٹاؤن شپ](location) سے بات کر رہی ہوں میرے پاس صرف [ہزار](price) روپے ہیں
	- slot{"location":"ٹاؤن شپ"}
	- slot{"price":"ہزار روپے"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:[چائنیز](cuisine)
	- slot{"location":"ٹاؤن شپ"}
	- slot{"price":"ہزار روپے"}
	- slot{"cuisine":"چائنیز"}
	- action_find_by_location_cuisine_price
	- action_restart