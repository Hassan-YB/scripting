## 273_S8_SP53_M_L1_G1_A1-LP_C
* intent_find_by_location_price:میں [گلبرگ](location) میں :م: کھانا چاہتا ہوں میری پرائس رینج ہے [تھاؤزنڈ ٹو تھاؤزنڈ](price) سم تھنگ
	- slot{"location":"گلبرگ"}
	- slot{"price":"تھاؤزنڈ ٹو تھاؤزنڈ"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:[دیسی](cuisine)
	- slot{"location":"گلبرگ"}
	- slot{"price":"تھاؤزنڈ ٹو تھاؤزنڈ"}
	- slot{"cuisine":"دیسی"}
	- action_find_by_location_cuisine_price
	- action_restart