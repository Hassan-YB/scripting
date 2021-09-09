## 157_S6_SP36_M_L1_G1_A2-C_L_P
* intent_find_by_cuisine:ہیلو السلام علیکم میں [فاسٹ فوڈ](cuisine) کھانا چاہتا ہوں
	- slot{"cuisine":"فاسٹ فوڈ"}
	- action_find_by_cuisine
* intent_find_by_location:میں لاہور میں [جوہر ٹاؤن](location) سائیڈ سے کھانا کھانا چاہتا ہوں
	- slot{"cuisine":"فاسٹ فوڈ"}
	- slot{"location":"جوہر ٹاؤن"}
	- action_find_by_cuisine_and_price
	- action_find_by_location_and_cuisine
* intent_find_by_price:میں :م: [مہنگا](price) کھانا کھانا چاہتا ہوں
	- slot{"cuisine":"فاسٹ فوڈ"}
	- slot{"location":"جوہر ٹاؤن"}
	- slot{"price":"مہنگا"}
	- action_find_by_location_cuisine_price
	- action_restart