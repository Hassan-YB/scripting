## train041_S13_SP003_F_L1_G1_A5-LCP
* greet:السلام و علیکم
	- utter_salaam
* intent_find_by_location_cuisine_price:جی میں لاہور [اچھرہ](location) میں کھڑی ہوں۔میرے پاس [پانچ سو](price) روپے ہیں۔اور میں کوئی [دیسی](cuisine) اچھا سا فوڈ کھانا چاہتی ہوں مجھے بہت زیادہ بھوک لگی ہوئی ہے۔
	- slot{"location":"اچھرہ"}
	- slot{"price":"پانچ سو"}
	- slot{"cuisine":" دیسی"}
	- action_find_by_location_cuisine_price
	- action_restart