## 248_S8_SP50_F_L1_G1_A2-LP_C
* intent_find_by_location_price:میں [جوہر ٹاؤن](location) میں ہوں اور میں [فائیو ہنڈرڈ](price) کا کھانا کھانا چاہ رہی ہوں
	- slot{"location":"جوہر ٹاؤن"}
	- slot{"price":"فائیو ہنڈرڈ"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:[چائنیز](cuisine)
	- slot{"location":"جوہر ٹاؤن"}
	- slot{"price":"فائیو ہنڈرڈ"}
	- slot{"cuisine":"چائنیز"}
	- action_find_by_location_cuisine_price
	- action_restart