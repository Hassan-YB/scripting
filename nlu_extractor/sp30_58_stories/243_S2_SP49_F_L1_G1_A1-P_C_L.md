## 243_S2_SP49_F_L1_G1_A1-P_C_L
* intent_find_by_price:میں نے [تھری ہنڈرڈ](price) کے اندر کچھ کھانا ہے
	- slot{"price":"تھری ہنڈرڈ"}
	- action_find_by_price
* intent_find_by_cuisine:[چائنیز](cuisine) فوڈ
	- slot{"price":"تھری ہنڈرڈ"}
	- slot{"cuisine":"چائنیز"}
	- action_find_by_cuisine_and_price
* intent_find_by_location::م: [مال روڈ](location)
	- slot{"price":"تھری ہنڈرڈ"}
	- slot{"cuisine":"چائنیز"}
	- slot{"location":"مال روڈ"}
	- action_find_by_location_cuisine_price
	- action_restart