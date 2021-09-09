## 246_S7_SP50_F_L1_G1_A2-LC_P
* intent_find_by_location_cuisine:میں [مغلپورہ](location) میں ہوں اور میں [چائنیز](cuisine) کھانا چاہ رہی ہوں
	- slot{"cuisine":"چائنیز"}
	- slot{"location":"مغلپورہ"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:[مناسب](price)
	- slot{"cuisine":"چائنیز"}
	- slot{"location":"مغلپورہ"}
	- slot{"price":"مناسب"}
	- action_find_by_location_cuisine_price
	- action_restart