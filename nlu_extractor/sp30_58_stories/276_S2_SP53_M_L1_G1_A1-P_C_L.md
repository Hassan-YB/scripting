## 276_S2_SP53_M_L1_G1_A1-P_C_L
* intent_find_by_price:رینج [ٹو تھاؤزنڈ](price) ہے
	- slot{"price":"ٹو تھاؤزنڈ"}
	- action_find_by_price
* intent_find_by_cuisine:میں [دیسی](cuisine) کھانا کھانا چاہتا ہوں
	- slot{"price":"ٹو تھاؤزنڈ"}
	- slot{"cuisine":"دیسی"}
	- action_find_by_cuisine_and_price
* intent_find_by_location:میں لاہور میں [باغبان پورہ](location) سے کھانا چاہتا ہوں
	- slot{"price":"ٹو تھاؤزنڈ"}
	- slot{"cuisine":"دیسی"}
	- slot{"location":"باغبان پورہ"}
	- action_find_by_location_cuisine_price
	- action_restart