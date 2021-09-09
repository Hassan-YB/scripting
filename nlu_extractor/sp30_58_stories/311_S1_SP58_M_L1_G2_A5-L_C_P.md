## 311_S1_SP58_M_L1_G2_A5-L_C_P
* intent_find_by_location:میں لاہور سے [رنگ روڈ](location) سے کھانا کھانا چاہتا ہوں
	- slot{"location":"رنگ روڈ"}
	- action_find_by_location
* intent_find_by_cuisine:میں [دیسی](cuisine) کھانا کھانا چاہتا ہوں
	- slot{"location":"رنگ روڈ"}
	- slot{"cuisine":"دیسی"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:میں [مناسب](price) اور سستے والا کھانا کھانا چاہتا ہوں جو میری رینج میں ہے
	- slot{"location":"رنگ روڈ"}
	- slot{"cuisine":"دیسی"}
	- slot{"price":"مناسب"}
	- action_find_by_location_cuisine_price
	- action_restart