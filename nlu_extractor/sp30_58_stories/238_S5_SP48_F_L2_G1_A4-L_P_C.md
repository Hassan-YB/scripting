## 238_S5_SP48_F_L2_G1_A4-L_P_C
* intent_find_by_location:میری کرنٹ لوکیشن [غازی روڈ](location) ہے
	- slot{"location":"غازی روڈ"}
	- action_find_by_location
* intent_find_by_price:مجھے سستا اور [مناسب](price) کھانا چاہیے
	- slot{"location":"غازی روڈ"}
	- slot{"price":"مناسب"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:مجھے [ٹریڈیشنل](cuisine) کھانا چاہیے
	- slot{"location":"غازی روڈ"}
	- slot{"price":"مناسب"}
	- slot{"cuisine":"ٹریڈیشنل"}
	- action_find_by_location_cuisine_price
	- action_restart