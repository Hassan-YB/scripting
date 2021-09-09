## 191_S9_SP42_M_L1_G1_A5-C_P_L
* intent_open:میں کھانا کھانا چاہتا ہوں
	- utter_ask_cuisine
* intent_find_by_cuisine:میں [چائنیز](cuisine) کھانا کھانا چاہتا ہوں
	- slot{"cuisine":"چائنیز"}
	- action_find_by_cuisine
* intent_find_by_price:میں [سستا](price) کھانا کھانا چاہتا ہوں
	- slot{"cuisine":"چائنیز"}
	- slot{"price":"سستا"}
	- action_find_by_cuisine_and_price
* intent_find_by_location:میں لاہور میں [انارکلی](location) سے کھانا کھانا چاہتا ہوں
	- slot{"cuisine":"چائنیز"}
	- slot{"price":"سستا"}
	- slot{"location":"انارکلی"}
	- action_find_by_location_cuisine_price
	- action_restart