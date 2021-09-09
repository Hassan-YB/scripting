## train111_S8_Sp009_F_L1_G1_A4-LP_C
* intent_find_by_location_price:میں [اقبال ٹاؤن](location) میں کھڑی ہوں اور مجھے بہت بھوک لگی ہے اور میرے پاس صرف [ہزار](price) روپے ہیں
	- slot{"location":"اقبال ٹاؤن"}
	- slot{"price":"ہزار"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:میں [چائنیز](cuisine) کھانا پسند کروں گی
	- slot{"location":"اقبال ٹاؤن"}
	- slot{"price":"ہزار"}
	- slot{"cuisine":"چائنیز"}
	- action_find_by_location_cuisine_price
	- action_restart