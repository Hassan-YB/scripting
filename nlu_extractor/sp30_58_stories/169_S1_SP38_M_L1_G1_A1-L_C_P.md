## 169_S1_SP38_M_L1_G1_A1-L_C_P
* greet:ہیلو
	- utter_salaam
	- utter_help_urdu
* intent_find_by_location::م: اپنے [مغلپورہ](location) والے ایریا میں کھانا وغیرہ کھانا چاہتا ہوں
	- slot{"location":"مغلپورہ"}
	- action_find_by_location
* intent_find_by_cuisine:میں [دیسی](cuisine) کھانا کھانا چاہتا ہوں
	- slot{"location":"مغلپورہ"}
	- slot{"cuisine":"دیسی"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:[مناسب](price) کھانا کھانا چاہتا ہوں
	- slot{"location":"مغلپورہ"}
	- slot{"cuisine":"دیسی"}
	- slot{"price":"مناسب"}
	- action_find_by_location_cuisine_price
	- action_restart