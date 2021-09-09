## 287_S6_SP54_M_L1_G1_A2-C_L_P
* intent_find_by_cuisine:میں نے [چائنیز](cuisine) فوڈ کھانا ہے اور [چائنیز](cuisine) فوڈ کے اندر میں نوڈلز کھانا چاہتا ہوں
	- slot{"cuisine":"چائنیز"}
	- action_find_by_cuisine
* intent_find_by_location:میں لاہور میں [گلبرگ](location) سے کھانا کھانا چاہتا ہوں
	- slot{"cuisine":"چائنیز"}
	- slot{"location":"گلبرگ"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:میں [مناسب](price) کھانا کھانا چاہتا ہوں
	- slot{"cuisine":"چائنیز"}
	- slot{"location":"گلبرگ"}
	- slot{"price":"مناسب"}
	- action_find_by_location_cuisine_price
	- action_restart