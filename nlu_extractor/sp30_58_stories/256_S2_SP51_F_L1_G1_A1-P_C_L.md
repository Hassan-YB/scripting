## 256_S2_SP51_F_L1_G1_A1-P_C_L
* intent_find_by_price::م: مجھے بھوک لگی ہے اور میرے پاس [ہزار](price) روپے ہیں اور
	- slot{"price":"ہزار"}
	- action_find_by_price
* intent_find_by_cuisine::م: میں [چائنیز](cuisine)
	- slot{"price":"ہزار"}
	- slot{"cuisine":"چائنیز"}
	- action_find_by_cuisine_and_price
* intent_find_by_location:میں لاہور میں [لنک روڈ](location) والی سائیڈ پہ ہوں تو ادھر کوئی ریسٹورنٹ ہو تو ادھر کوئی ریسٹورنٹ ہو
	- slot{"price":"ہزار"}
	- slot{"cuisine":"چائنیز"}
	- slot{"location":"لنک روڈ"}
	- action_find_by_location_cuisine_price
	- action_restart