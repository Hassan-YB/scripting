## 267_S6_SP52_M_L3_G1_A2-C_L_P
* intent_find_by_cuisine:السلام علیکم میرا اس وقت کچھ [چائنیز](cuisine) کھانے کو دل کر رہا ہے
	- slot{"cuisine":"چائنیز"}
	- action_find_by_cuisine
* intent_find_by_location:میں لاہور میں [گلبرگ](location)
	- slot{"cuisine":"چائنیز"}
	- slot{"location":"گلبرگ"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:میں [مناسب](price) کھانا کھانا چاہتا ہوں
	- slot{"cuisine":"چائنیز"}
	- slot{"location":"گلبرگ"}
	- slot{"price":"مناسب"}
	- action_find_by_location_cuisine_price
	- action_restart