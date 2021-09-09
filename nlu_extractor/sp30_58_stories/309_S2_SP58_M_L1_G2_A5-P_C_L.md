## 309_S2_SP58_M_L1_G2_A5-P_C_L
* intent_find_by_price::م: میری رینج [ٹو ففٹی](price) کے اراؤنڈ اباوٹ ہے
	- slot{"price":"ٹو ففٹی"}
	- action_find_by_price
* intent_find_by_cuisine:[اٹالیئن](cuisine)
	- slot{"price":"ٹو ففٹی"}
	- slot{"cuisine":"اٹالیئن"}
	- action_find_by_cuisine_and_price
* intent_find_by_location:میں لاہور سے :م: [ماڈل ٹاؤن](location) سے
	- slot{"price":"ٹو ففٹی"}
	- slot{"cuisine":"اٹالیئن"}
	- slot{"location":"ماڈل ٹاؤن"}
	- action_find_by_location_cuisine_price
	- action_restart