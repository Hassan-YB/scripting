## train069_S8_Sp007_F_L1_G1_A3-LP_C
* greet:ہیلو
	- utter_salaam
* intent_find_by_location_price:میں [ٹاؤن شپ](location) سے بات کر رہی ہوں میری پرائس رینج جو ہے وہ جسٹ [فائیو ہنڈرڈ ٹو ون تھاؤزنڈ](price) ہے اور مجھے بہت بھوک لگی ہے
	- slot{"location":"ٹاؤن شپ"}
	- slot{"price":"فائیو ہنڈرڈ ٹو ون تھاؤزنڈ"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:دیسی [دیسی](cuisine) کھانا
	- slot{"location":"ٹاؤن شپ"}
	- slot{"price":"فائیو ہنڈرڈ ٹو ون تھاؤزنڈ"}
	- slot{"cuisine":"دیسی"}
	- action_find_by_location_cuisine_price
	- action_restart