## train046_S9_SP003_F_L1_G1_A5-CP_L
* greet:السلام و علیکم
	- utter_salaam
* intent_find_by_cuisine_price:جی میں لاہور سے بات کر رہی ہوں ٹھیک ہے مجھے [پانچ سو](price).[پانچ سو](price) کی رینج میں کوئی [فاسٹ فوڈ](cuisine) چاہیے.اور مجھے پرووائیڈ ہو سکتا [پانچ سو](price) کی رینج میں.
	- slot{"price":"پانچ سو"}
	- slot{"cuisine":"فاسٹ فوڈ"}
	- action_find_by_cuisine_and_price
* intent_find_by_location:میں لاہور میں. میں لاہور میں دربار کے پاس [داتا دربار](location) کے پاس سے  کھانا کھانا چاہتی ہوں.
	- slot{"price":"پانچ سو"}
	- slot{"cuisine":"فاسٹ فوڈ"}
	- slot{"location":"داتا دربار"}
	- action_find_by_location_cuisine_price
	- action_restart