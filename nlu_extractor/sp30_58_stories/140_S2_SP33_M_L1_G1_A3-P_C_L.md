## 140_S2_SP33_M_L1_G1_A3-P_C_L
* intent_find_by_price:جی [فائیو ہنڈرڈ](price) کی رینج میں کوئی بھی کھانا اویل ایبل ہے
	- slot{"price":"فائیو ہنڈرڈ"}
	- action_find_by_price
* intent_find_by_cuisine:[فاسٹ فوڈ](cuisine)
	- slot{"price":"فائیو ہنڈرڈ"}
	- slot{"cuisine":"فاسٹ فوڈ"}
	- action_find_by_cuisine_and_price
* intent_find_by_location::م: [مغلپورہ](location)
	- slot{"price":"فائیو ہنڈرڈ"}
	- slot{"cuisine":"فاسٹ فوڈ"}
	- slot{"location":"مغلپورہ"}
	- action_find_by_location_cuisine_price
	- action_restart