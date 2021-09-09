## 207_S5_SP44_M_L1_G1_A5-L_P_C
* intent_find_by_location:میری کرنٹ لوکیشن میں [جوہر ٹاؤن](location) میں موجود ہوں
	- slot{"location":"جوہر ٹاؤن"}
	- action_find_by_location
* intent_find_by_price:[مناسب](price) کھانا کھانا چاہتا ہوں
	- slot{"location":"جوہر ٹاؤن"}
	- slot{"price":"مناسب"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:[دیسی](cuisine)
	- slot{"location":"جوہر ٹاؤن"}
	- slot{"price":"مناسب"}
	- slot{"cuisine":"دیسی"}
	- action_find_by_location_cuisine_price
	- action_restart