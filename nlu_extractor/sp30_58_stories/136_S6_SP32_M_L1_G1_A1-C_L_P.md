## 136_S6_SP32_M_L1_G1_A1-C_L_P
* intent_find_by_cuisine:جی میں [فاسٹ فوڈ](cuisine) کھانا کھانا چاہ رہا ہوں
	- slot{"cuisine":"فاسٹ فوڈ"}
	- action_find_by_cuisine
* intent_find_by_location:میں لاہور میں :م: [شاہدرہ](location) سے کھانا چاہ رہا ہوں
	- slot{"cuisine":"فاسٹ فوڈ"}
	- slot{"location":"شاہدرہ"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:میں [مناسب](price) ریٹ پہ کھانا چاہ رہا ہوں
	- slot{"cuisine":"فاسٹ فوڈ"}
	- slot{"location":"شاہدرہ"}
	- slot{"price":"مناسب"}
	- action_find_by_location_cuisine_price
	- action_restart