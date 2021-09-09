## 221_S5_SP46_F_L1_G2_A3-L_P_C
* intent_find_by_location:میں [ماڈل ٹاؤن](location) سے کھانا کھانا چاہتی ہوں
	- slot{"location":"ماڈل ٹاؤن"}
	- action_find_by_location
* intent_find_by_price:سستا اور [مناسب](price) کھانا کھانا چاہتی ہوں
	- slot{"location":"ماڈل ٹاؤن"}
	- slot{"price":"مناسب"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:میں [فاسٹ فوڈ](cuisine) کھانا چاہتی ہوں
	- slot{"location":"ماڈل ٹاؤن"}
	- slot{"price":"مناسب"}
	- slot{"cuisine":"فاسٹ فوڈ"}
	- action_find_by_location_cuisine_price
	- action_restart