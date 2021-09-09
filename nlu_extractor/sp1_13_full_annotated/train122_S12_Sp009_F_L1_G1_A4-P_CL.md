## train122_S12_Sp009_F_L1_G1_A4-P_CL
* intent_find_by_price:میرے پاس [ہزار](price) روپے ہیں اور مجھے بہت بھوک لگی ہے
	- slot{"price":"ہزار"}
	- action_find_by_price
* intent_find_by_location_cuisine:میں یہ کھانا [لنک روڈ](location) سے منگوانا پسند کروں گی اور مجھے [فاسٹ فوڈ](cuisine) کھانا ہے
	- slot{"price":"ہزار"}
	- slot{"location":"لنک روڈ"}
	- slot{"cuisine":"فاسٹ فوڈ"}
	- action_find_by_location_cuisine_price
	- action_restart