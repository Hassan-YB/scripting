## train094_S9_Sp008_F_L1_G1_A3-CP_L
* intent_find_by_cuisine_price:میرے پاس [ہزار](price) روپے ہیں میں [برگر](cuisine) کھانا پسند کروں گی
	- slot{"price":"ہزار"}
	- slot{"cuisine":"برگر"}
	- action_find_by_cuisine_and_price
* intent_find_by_location:[ٹاؤن شپ](location) سے
	- slot{"price":"ہزار"}
	- slot{"cuisine":"برگر"}
	- slot{"location":"ٹاؤن شپ"}
	- action_find_by_location_cuisine_price
	- action_restart