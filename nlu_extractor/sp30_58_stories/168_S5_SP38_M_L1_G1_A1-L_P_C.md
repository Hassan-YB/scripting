## 168_S5_SP38_M_L1_G1_A1-L_P_C
* intent_find_by_location:[مغلپورہ](location) والی سائیڈ سے کھانا چاہتا ہوں کھانا
	- slot{"location":"مغلپورہ"}
	- action_find_by_location
* intent_find_by_price:سستا اور [مناسب](price)
	- slot{"location":"مغلپورہ"}
	- slot{"price":"مناسب"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:[چائنیز](cuisine)
	- slot{"location":"مغلپورہ"}
	- slot{"price":"مناسب"}
	- slot{"cuisine":"چائنیز"}
	- action_find_by_location_cuisine_price
	- action_restart