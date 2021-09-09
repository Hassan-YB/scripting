## 195_S6_SP42_M_L1_G1_A5-C_L_P
* intent_find_by_cuisine:میں [چائنیز](cuisine) کھانا کھانا چاہتا ہوں
	- slot{"cuisine":"چائنیز"}
	- action_find_by_cuisine
* intent_find_by_location:میں لاہور میں [انارکلی](location) سے کھانا کھانا چاہتا ہوں
	- slot{"cuisine":"چائنیز"}
	- slot{"location":"انارکلی"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:میں [مناسب](price) کھانا کھانا چاہتا ہوں
	- slot{"cuisine":"چائنیز"}
	- slot{"location":"انارکلی"}
	- slot{"price":"مناسب"}
	- action_find_by_location_cuisine_price
	- action_restart