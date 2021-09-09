## 277_S6_SP53_M_L1_G1_A1-C_L_P
* intent_find_by_cuisine:میں [دیسی](cuisine) ٹائپ کھانا کھانا چاہتا ہوں
	- slot{"cuisine":"دیسی"}
	- action_find_by_cuisine
* intent_find_by_location:میں لاہور میں [گلبرگ](location) سے کھانا کھانا چاہتا ہوں
	- slot{"cuisine":"دیسی"}
	- slot{"location":"گلبرگ"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:میں [مناسب](price) کھانا کھانا چاہتا ہوں
	- slot{"cuisine":"دیسی"}
	- slot{"location":"گلبرگ"}
	- slot{"price":"مناسب"}
	- action_find_by_location_cuisine_price
	- action_restart