## 151_S1_SP35_M_L1_G1_A5-L_C_P
* intent_find_by_location::م: مجھے [جوہر ٹاؤن](location) میں کوئی بھی اچھا سا ناشتے کے لیے ریسٹورنٹ چاہیے ہے
	- slot{"location":"جوہر ٹاؤن"}
	- action_find_by_location
* intent_find_by_price:[مہنگا](price)
	- slot{"location":"جوہر ٹاؤن"}
	- slot{"price":"مہنگا"}
	- action_find_by_location_and_cuisine
* intent_find_by_cuisine:[چائنیز](cuisine)
	- slot{"location":"جوہر ٹاؤن"}
	- slot{"price":"مہنگا"}
	- slot{"cuisine":"چائنیز"}
	- action_find_by_location_cuisine_price
	- action_restart