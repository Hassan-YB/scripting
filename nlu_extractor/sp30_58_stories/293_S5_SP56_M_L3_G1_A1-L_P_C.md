## 293_S5_SP56_M_L3_G1_A1-L_P_C
* intent_find_by_location:میں اس وقت [کریم بلاک](location) میں ہوں اور مجھے بھوک لگی ہے اور میں نے کولڈ کافی پینی ہے
	- slot{"location":"کریم بلاک"}
	- action_find_by_location
* intent_find_by_price:میں [نارمل](price) کھانا چاہتا ہوں
	- slot{"location":"کریم بلاک"}
	- slot{"price":"نارمل"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:[دیسی](cuisine)
	- slot{"location":"کریم بلاک"}
	- slot{"price":"نارمل"}
	- slot{"cuisine":"دیسی"}
	- action_find_by_location_cuisine_price
	- action_restart