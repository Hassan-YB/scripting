## train102_S12_Sp008_F_L1_G1_A3-P_CL
* intent_find_by_price:میرے پاس [ہزار](price) روپے ہیں مجھے بہت بھوک لگی ہے
	- slot{"price":"ہزار"}
	- action_find_by_price
* intent_find_by_location_cuisine:میں [جوہر ٹاؤن](location) سے [گول گپے](cuisine) کھانا پسند کروں گی
	- slot{"price":"ہزار"}
	- slot{"location":"جوہر ٹاؤن"}
	- slot{"cuisine":"گول گپے"}
	- action_find_by_location_cuisine_price
	- action_restart