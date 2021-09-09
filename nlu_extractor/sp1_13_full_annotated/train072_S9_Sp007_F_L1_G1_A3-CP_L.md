## train072_S9_Sp007_F_L1_G1_A3-CP_L
* intent_find_by_cuisine_price:اچھا جی مجھے بہت بھوک لگی ہے اور میں [چائنیز](cuisine) کھانا چاہتی ہوں اور میری پرائس رینج جو ہے وہ جسٹ [ون تھاؤزنڈ](price) ہے
	- slot{"cuisine":"چائنیز"}
	- slot{"price":"ون تھاؤزنڈ"}
	- action_find_by_cuisine_and_price
* intent_find_by_location:میں یہ کھانا [لنک روڈ](location) سے آرڈر کرنا پسند کروں گی
	- slot{"cuisine":"چائنیز"}
	- slot{"price":"ون تھاؤزنڈ"}
	- slot{"location":"لنک روڈ"}
	- action_find_by_location_cuisine_price
	- action_restart