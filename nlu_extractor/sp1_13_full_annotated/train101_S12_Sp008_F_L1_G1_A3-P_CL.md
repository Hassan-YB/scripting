## train101_S12_Sp008_F_L1_G1_A3-P_CL
* intent_find_by_price:میرے پاس نا صرف [ہزار](price) روپے ہیں اور مجھے بہت بھوک لگی ہے
	- slot{"price":"ہزار"}
	- action_find_by_price
* intent_find_by_location_cuisine:میں [گول گپے](cuisine) کھانا پسند کروں گی [جوہر ٹاؤن](location) سے
	- slot{"price":"ہزار"}
	- slot{"cuisine":"گول گپے"}
	- slot{"location":"جوہر ٹاؤن"}
	- action_find_by_location_cuisine_price
	- action_restart