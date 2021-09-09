## train103_S2_Sp008_F_L1_G1_A3-P_C_L
* intent_find_by_price:میرے پاس [دو ہزار](price) روپے ہیں مجھے بھوک لگی ہے
	- slot{"price":"دو ہزار"}
	- action_find_by_price
* intent_find_by_cuisine:میں [پیزا](cuisine) کھانا پسند کروں گی
	- slot{"price":"دو ہزار"}
	- slot{"cuisine":"پیزا"}
	- action_find_by_cuisine_and_price
* intent_find_by_location:[ڈی ایچ اے](location) سے
	- slot{"price":"دو ہزار"}
	- slot{"cuisine":"پیزا"}
	- slot{"location":"ڈی ایچ اے"}
	- action_find_by_location_cuisine_price
	- action_restart