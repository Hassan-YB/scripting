## 135_S2_SP32_M_L1_G1_A1-P_C_L
* intent_find_by_price:السلام علیکم میں [فائیو ہنڈرڈ](price) کی رینج میں فوڈ پرچیز کرنا چاہ رہا ہوں
	- slot{"price":"فائیو ہنڈرڈ"}
	- action_find_by_price
* intent_find_by_cuisine:میں [فاسٹ فوڈ](cuisine) کھانا
	- slot{"price":"فائیو ہنڈرڈ"}
	- slot{"cuisine":"فاسٹ فوڈ"}
	- action_find_by_cuisine_and_price
* intent_find_by_location:میں لاہور میں [شاہدرہ](location) سے کھانا چاہ رہا ہوں
	- slot{"price":"فائیو ہنڈرڈ"}
	- slot{"cuisine":"فاسٹ فوڈ"}
	- slot{"location":"شاہدرہ"}
	- action_find_by_location_cuisine_price
	- action_restart