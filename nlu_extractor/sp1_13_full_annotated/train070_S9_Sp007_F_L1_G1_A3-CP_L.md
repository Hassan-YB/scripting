## train070_S9_Sp007_F_L1_G1_A3-CP_L
* intent_find_by_cuisine_price:میں [چائنیز](cuisine) کھانا چاہتی ہوں اور میری فوڈ کی لائک پرائس رینج جو ہے وہ جسٹ [ون تھاؤزنڈ](price) ہے
	- slot{"cuisine":"چائنیز"}
	- slot{"price":"ون تھاؤزنڈ"}
	- action_find_by_cuisine_and_price
* intent_find_by_location:میں [ڈی ایچ اے](location) سے
	- slot{"cuisine":"چائنیز"}
	- slot{"price":"ون تھاؤزنڈ"}
	- slot{"location":"ڈی ایچ اے"}
	- action_find_by_location_cuisine_price
	- action_restart