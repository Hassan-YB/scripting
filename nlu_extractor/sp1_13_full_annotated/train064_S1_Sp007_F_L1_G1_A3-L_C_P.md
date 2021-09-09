## train064_S1_Sp007_F_L1_G1_A3-L_C_P
* greet:السلام علیکم
	- utter_salaam
* intent_find_by_location:اچھا جی میں [یو ای ٹی](location) سے بات کر رہی ہوں تو مجھے بہت بھوک لگی ہے تو میں کچھ آرڈر کرنا چاہ رہی تھی
	- slot{"location":"یو ای ٹی"}
	- action_find_by_location
* intent_find_by_cuisine:میں [فاسٹ فوڈ](cuisine) لائک کرتی ہوں
	- slot{"location":"یو ای ٹی"}
	- slot{"cuisine":"فاسٹ فوڈ"}
	- action_find_by_location_and_cuisineمیرے پاس فی الحال [فائیو ہنڈرڈ](price) روپیز ہیں
	- slot{"location":"یو ای ٹی"}
	- slot{"cuisine":"فاسٹ فوڈ"}
	- slot{"price":"فائیو ہنڈرڈ"}
	- action_find_by_location_cuisine_price
	- action_restart