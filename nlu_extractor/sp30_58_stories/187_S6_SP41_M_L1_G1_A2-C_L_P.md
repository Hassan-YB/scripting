## 187_S6_SP41_M_L1_G1_A2-C_L_P
* intent_find_by_cuisine:میں [مٹن کڑاہی](cuisine) کھانا چاہتا ہوں
	- slot{"cuisine":"مٹن کڑاہی"}
	- action_find_by_cuisine
* intent_find_by_location:[جوہر ٹاؤن](location)
	- slot{"cuisine":"مٹن کڑاہی"}
	- slot{"location":"جوہر ٹاؤن"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:[مہنگا](price)
	- slot{"cuisine":"مٹن کڑاہی"}
	- slot{"location":"جوہر ٹاؤن"}
	- slot{"price":"مہنگا"}
	- action_find_by_location_cuisine_price
	- action_restart