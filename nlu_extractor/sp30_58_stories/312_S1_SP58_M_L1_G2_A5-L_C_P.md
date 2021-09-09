## 312_S1_SP58_M_L1_G2_A5-L_C_P
* intent_find_by_location:میں [گلبرگ](location) والی سائیڈ سے کھانا کھانا چاہتا ہوں
	- slot{"location":"گلبرگ"}
	- action_find_by_location
* intent_find_by_cuisine:میں [دیسی](cuisine) کھانا کھانا چاہتا ہوں
	- slot{"location":"گلبرگ"}
	- slot{"cuisine":"دیسی"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:میں [مناسب](price) اور سستا کھانا کھانا چاہتا ہوں
	- slot{"location":"گلبرگ"}
	- slot{"cuisine":"دیسی"}
	- slot{"price":"مناسب"}
	- action_find_by_location_cuisine_price
	- action_restart