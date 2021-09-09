## train040_S11_SP003_F_L1_G1_A5-L_CP
* greet:السلام و علیکم
	- utter_salaam
* intent_find_by_location:جی میں [ڈیفنس](location) سے فیز فائیو سے بات کر رہی ہوں.
	- slot{"location":"ڈیفنس"}
	- action_find_by_location
* intent_find_by_cuisine_price:جی میں [دیسی](cuisine) کھانا کھانا چاہتی ہوں بہت لائٹ سااور سموتھ سا ہو.اوراس کی رینج [فائیو تھاؤزنڈ](price)
	- slot{"location":"ڈیفنس"}
	- slot{"cuisine":"دیسی"}
	- slot{"price":"فائیو تھاؤزنڈ"}
	- action_find_by_location_cuisine_and_price
	- action_restart