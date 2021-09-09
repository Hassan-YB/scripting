## 304_S6_SP57_M_L1_G1_A1-C_L_P
* intent_find_by_cuisine:میں [فاسٹ فوڈ](cuisine) کھانا چاہتا ہوں
	- slot{"cuisine":"فاسٹ فوڈ"}
	- action_find_by_cuisine
* intent_find_by_location:[لبرٹی مارکیٹ ](location)
	- slot{"cuisine":"فاسٹ فوڈ"}
	- slot{"location":"لبرٹی مارکیٹ "}
	- action_find_by_location_and_cuisine
* intent_find_by_price:میں سستا اور [مناسب](price) کھانا پسند کرتا ہوں
	- slot{"cuisine":"فاسٹ فوڈ"}
	- slot{"location":"لبرٹی مارکیٹ "}
	- slot{"price":"مناسب"}
	- action_find_by_location_cuisine_price
	- action_restart