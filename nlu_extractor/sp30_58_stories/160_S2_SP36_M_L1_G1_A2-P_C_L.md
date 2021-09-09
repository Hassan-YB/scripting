## 160_S2_SP36_M_L1_G1_A2-P_C_L
* intent_find_by_price:السلام علیکم میری رینج ہے [ون تھاؤزنڈ](price) میں اس میں کھانا کھانا چاہتا ہوں
	- slot{"price":"ون تھاؤزنڈ"}
	- action_find_by_price
* intent_find_by_cuisine:میں [دیسی](cuisine) کھانا کھانا چاہوں گا
	- slot{"price":"ون تھاؤزنڈ"}
	- slot{"cuisine":"دیسی"}
	- action_find_by_cuisine_and_price
* intent_find_by_location:میں لاہور میں [جوہر ٹاؤن](location) سے کھانا چاہوں
	- slot{"price":"ون تھاؤزنڈ"}
	- slot{"cuisine":"دیسی"}
	- slot{"location":"جوہر ٹاؤن"}
	- action_find_by_location_cuisine_price
	- action_restart