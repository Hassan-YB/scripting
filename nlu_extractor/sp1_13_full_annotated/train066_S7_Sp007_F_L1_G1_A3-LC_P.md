## train066_S7_Sp007_F_L1_G1_A3-LC_P
* greet:ہیلو
	- utter_salaam
* intent_find_by_location_cuisine:جی میں [ ٹاؤن شپ](location) سے بات کر رہی ہوں اور میں [چائنیز فوڈ](cuisine) آرڈر کرنا چاہتی ہوں
	- slot{"location":" ٹاؤن شپ"}
	- slot{"cuisine":"چائنیز فوڈ"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:میں مناسب کیونکہ میرے پاس اس وقت [فائیو ہنڈرڈ سے تھاؤزنڈ](price) روپیز ہیں
	- slot{"location":" ٹاؤن شپ"}
	- slot{"cuisine":"چائنیز فوڈ"}
	- slot{"price":"فائیو ہنڈرڈ سے تھاؤزنڈ"}
	- action_find_by_location_cuisine_price
	- action_restart