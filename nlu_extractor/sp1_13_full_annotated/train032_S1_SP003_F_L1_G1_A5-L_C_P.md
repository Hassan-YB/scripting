## train032_S1_SP003_F_L1_G1_A5-L_C_P
* greet:السلام و علیکم۔
	- utter_salaam
* intent_find_by_location:جی میں [ڈیفنس](location) سے فیز سکس سے بات کر رہی ہوں ٹھیک ہے میں کوئی بہترین فوڈ کھانا چاہتی ہوں.
	- slot{"location":"ڈیفنس"}
	- action_find_by_location
* intent_find_by_cuisine:میں [فاسٹ فوڈ](cuisine) کھانا چاہتی ہوں اور میں بہت ہی لائٹ پسند کرتی ہوں ٹھیک ہے۔
	- slot{"location":"ڈیفنس"}
	- slot{"cuisine":"فاسٹ فوڈ"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:میں [ون تھاؤزنڈ](price) کی رینج میں کھانا چاہتی ہوں.
	- slot{"location":"ڈیفنس"}
	- slot{"cuisine":"فاسٹ فوڈ"}
	- slot{"price":"ون تھاؤزنڈ"}
	- action_find_by_location_cuisine_price
	- action_restart