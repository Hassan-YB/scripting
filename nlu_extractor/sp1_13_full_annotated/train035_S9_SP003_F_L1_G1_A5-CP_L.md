## train035_S9_SP003_F_L1_G1_A5-CP_L
* intent_find_by_cuisine_price:السلام و علیکم. دیکھیں میں کھانا کھانا چاہتی ہوں اور جو [پانچ سو](price) کی رینج سے زیادہ نہ ہو اور میں [فاسٹ فوڈ](cuisine) لینا چاہتی ہوں.
	- slot{"price":"پانچ سو"}
	- slot{"cuisine":"فاسٹ فوڈ"}
	- action_find_by_cuisine_and_price
* intent_find_by_location:میں فیز فائیو سے [ڈیفنس](location) سے بات کر رہی ہوں۔
	- slot{"price":"پانچ سو"}
	- slot{"cuisine":"فاسٹ فوڈ"}
	- slot{"location":"ڈیفنس"}
	- action_find_by_location_cuisine_price
	- action_restart