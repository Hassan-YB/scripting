## 257_S2_SP51_F_L1_G1_A1-P_C_L
* intent_find_by_price:السلام علیکم میرے پاس [ہزار](price) روپیہ ہے اور مجھے بہت بھوک لگی ہوئی ہے مجھے کھانا کھانا ہے  پلیز مجھے کسی ریسٹورنٹ کے بارے میں بتائیں
	- slot{"price":"ہزار"}
	- action_find_by_price
* intent_find_by_cuisine::م: میں [چائنیز](cuisine) کھانا کھانا چاہتی ہوں
	- slot{"price":"ہزار"}
	- slot{"cuisine":"چائنیز"}
	- action_find_by_cuisine_and_price
* intent_find_by_location:میں [لنک روڈ](location) والی سائیڈ پر موجود ہوں تو مجھے تو ادھر ہی کوئی ریسٹورنٹ بتا دیں
	- slot{"price":"ہزار"}
	- slot{"cuisine":"چائنیز"}
	- slot{"location":"لنک روڈ"}
	- action_find_by_location_cuisine_price
	- action_restart