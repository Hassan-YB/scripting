## 215_S6_SP45_F_L1_G1_A5-C_L_P
* intent_find_by_cuisine:مجھے [چکن سموسہ](cuisine) کھانا ہے
	- slot{"cuisine":"چکن سموسہ"}
	- action_find_by_cuisine
* intent_find_by_location:میں [یو ای ٹی](location)
	- slot{"cuisine":"چکن سموسہ"}
	- slot{"location":"یو ای ٹی"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:[سستا ](price)
	- slot{"cuisine":"چکن سموسہ"}
	- slot{"location":"یو ای ٹی"}
	- slot{"price":"سستا "}
	- action_find_by_location_cuisine_price
	- action_restart