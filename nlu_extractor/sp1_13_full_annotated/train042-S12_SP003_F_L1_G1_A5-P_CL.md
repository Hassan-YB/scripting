## train042-S12_SP003_F_L1_G1_A5-P_CL
* greet:السلام و علیکم
	- utter_salaam
* intent_find_by_price:جی میرے پاس [پانچ سو](price) روپے ہیں.
	- slot{"price":"پانچ سو"}
	- action_find_by_price
* intent_find_by_location_price:میں لاہور [اچھرہ](location) میں جی ٹی روڈ پر کھڑی ہوں اور مجھے بہت زیادہ بھوک لگی ہے اور کچھ [دیسی](cuisine) اسپائسی سا کھانا چاہتی ہوں.
	- slot{"price":"پانچ سو"}
	- slot{"location":"اچھرہ"}
	- slot{"cuisine":"دیسی"}
	- action_find_by_location_cuisine_price
	- action_restart