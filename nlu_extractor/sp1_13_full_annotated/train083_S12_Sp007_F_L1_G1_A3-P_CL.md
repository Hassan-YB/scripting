## train083_S12_Sp007_F_L1_G1_A3-P_CL
* intent_find_by_price:اچھا جی میرے پاس [بہت کم](price) پیسے ہیں اور مجھے بہت زیادہ بھوک لگی ہے
	- slot{"price":"بہت کم"}
	- action_find_by_price
* intent_find_by_location_cuisine:میں [چائنیز](cuisine) کھانا پسند کروں گی [ٹاؤن شپ](location) سے
	- slot{"price":"بہت کم"}
	- slot{"cuisine":"چائنیز"}
	- slot{"location":"ٹاؤن شپ"}
	- action_find_by_location_cuisine_price
	- action_restart