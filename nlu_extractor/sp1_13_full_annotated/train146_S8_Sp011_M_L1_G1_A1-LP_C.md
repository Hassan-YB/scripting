## train146_S8_Sp011_M_L1_G1_A1-LP_C
* intent_find_by_location_price:میں [سمن آباد](location) میں رہتا ہوں مجھے سمن آباد کے ایریا میں [پانچ سو](price) کی رینج کے اندر میل چاہیے میل
	- slot{"location":"سمن آباد"}
	- slot{"price":"پانچ سو"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:مجھے [دیسی فوڈ](cuisine) چاہیے ہے
	- slot{"location":"سمن آباد"}
	- slot{"price":"پانچ سو"}
	- slot{"cuisine":"دیسی فوڈ"}
	- action_find_by_location_cuisine_price
	- action_restart