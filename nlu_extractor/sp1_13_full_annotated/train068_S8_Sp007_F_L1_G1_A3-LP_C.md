## train068_S8_Sp007_F_L1_G1_A3-LP_C
* greet:ہائے
	- utter_salaam
* intent_find_by_location_price:میں [ڈی ایچ اے](location) سے بات کر رہی ہوں اور مجھے بہت زیادہ بھوک لگی ہے میری پرائس رینج جو ہے وہ جسٹ [ون تھاؤزنڈ](price) ہے
	- slot{"location":"ڈی ایچ اے"}
	- slot{"price":"ون تھاؤزنڈ"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:میں [چائنیز](cuisine)
	- slot{"location":"ڈی ایچ اے"}
	- slot{"price":"ون تھاؤزنڈ"}
	- slot{"cuisine":"چائنیز"}
	- action_find_by_location_cuisine_price
	- action_restart