## train045_S13_SP003_F_L1_G1_A5-LCP
* greet:السلام و علیکم
	- utter_salaam
* intent_find_by_location_cuisine_price:جی میرے پاس [پانچ سو](price) روپے ہیں میں لاہور [اچھرہ](location) میں کھڑی ہوں ٹھیک ہے مجھے کچھ [دیسی](cuisine) سا فوڈاچھا سا [پانچ سو](price) روپے کی رینج میں چاہیے.
	- slot{"price":"پانچ سو"}
	- slot{"location":"اچھرہ"}
	- slot{"cuisine":"دیسی"}
	- action_find_by_location_cuisine_price
	- action_restart