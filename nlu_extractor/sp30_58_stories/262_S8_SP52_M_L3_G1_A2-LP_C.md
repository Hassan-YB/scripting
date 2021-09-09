## 262_S8_SP52_M_L3_G1_A2-LP_C
* intent_find_by_location_price:میں [ماڈل ٹاؤن](location) کی رینج میں ہوں اور اس وقت میں [پانچ سو](price) روپے کی :م: رینج میں کچھ کھانا چاہتا ہوں
	- slot{"location":"ماڈل ٹاؤن"}
	- slot{"price":"پانچ سو"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:میں [دیسی](cuisine) زیادہ پریفر کروں گا
	- slot{"location":"ماڈل ٹاؤن"}
	- slot{"price":"پانچ سو"}
	- slot{"cuisine":"دیسی"}
	- action_find_by_location_cuisine_price
	- action_restart