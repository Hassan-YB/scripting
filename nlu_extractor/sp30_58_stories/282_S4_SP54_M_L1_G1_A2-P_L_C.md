## 282_S4_SP54_M_L1_G1_A2-P_L_C
* intent_find_by_price:مجھے بھوک لگی ہے اور میں :م: [سستے](price) میں کوئی چیز کھانا کھانا چاہتا ہوں
	- slot{"price":"سستے"}
	- action_find_by_price
* intent_find_by_location:میں لاہور میں [وحدت روڈ](location) سے کھانا کھانا چاہتا ہوں
	- slot{"price":"سستے"}
	- slot{"location":"وحدت روڈ"}
	- action_find_by_location_and_price
* intent_find_by_cuisine::م: میں [چائنیز](cuisine) کھانا کھانا چاہتا ہوں
	- slot{"price":"سستے"}
	- slot{"location":"وحدت روڈ"}
	- slot{"cuisine":"چائنیز"}
	- action_find_by_location_cuisine_price
	- action_restart