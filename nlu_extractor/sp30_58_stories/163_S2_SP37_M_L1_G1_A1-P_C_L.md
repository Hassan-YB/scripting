## 163_S2_SP37_M_L1_G1_A1-P_C_L
* intent_find_by_price::م: مجھے تقریبا [فائیو ہنڈرڈ](price) کی رینج میں کوئی ریسٹورنٹ بتا دیں
	- slot{"price":"فائیو ہنڈرڈ"}
	- action_find_by_price
* intent_find_by_cuisine:[دیسی](cuisine)
	- slot{"price":"فائیو ہنڈرڈ"}
	- slot{"cuisine":"دیسی"}
	- action_find_by_cuisine_and_price
* intent_find_by_location:میں لاہور میں [ای ایم ای](location) سے کھانا چاہتا ہوں
	- slot{"price":"فائیو ہنڈرڈ"}
	- slot{"cuisine":"دیسی"}
	- slot{"location":"ای ایم ای"}
	- action_find_by_location_cuisine_price
	- action_restart