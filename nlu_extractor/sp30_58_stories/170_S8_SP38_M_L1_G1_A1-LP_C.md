## 170_S8_SP38_M_L1_G1_A1-LP_C
* greet:السلام علیکم
	- utter_salaam
	- utter_help_urdu
* intent_find_by_location_price::م: میں دراصل :م: [مغلپورہ چوک](location) پہ کھڑا ہوں تو مجھے :م: [تھاؤزنڈ](price) کی رینج میں کھانا چاہیے
	- slot{"location":"مغلپورہ چوک"}
	- slot{"price":"تھاؤزنڈ"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:میں [دیسی](cuisine) کھانا کھانا چاہتا ہوں
	- slot{"location":"مغلپورہ چوک"}
	- slot{"price":"تھاؤزنڈ"}
	- slot{"cuisine":"دیسی"}
	- action_find_by_location_cuisine_price
	- action_restart