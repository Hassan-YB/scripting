## train031_S5_SP003_F_L1_G1_A5-L_P_C
* greet:السلام و علیکم۔
	- utter_salaam
* intent_find_by_location:جی میں کچھ بہترین فوڈ کھانا چاہتی ہوں.میں [ڈیفنس](location) سے فیز سکس سے بات کر رہی ہوں.
	- slot{"location":"ڈیفنس"}
	- action_find_by_location
* intent_find_by_price:میں [ون تھاؤزنڈ](price) کی رینج میں کھانا کھانا چاہتی ہوں.
	- slot{"location":"ڈیفنس"}
	- slot{"price":"ون تھاؤزنڈ"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:مجھے[فاسٹ فوڈ](cuisine) چاہیے.
	- slot{"location":"ڈیفنس"}
	- slot{"price":"ون تھاؤزنڈ"}
	- slot{"cuisine":" فاسٹ فوڈ"}
	- action_find_by_location_cuisine_price
	- action_restart