## 298_S5_SP56_M_L3_G1_A1-L_P_C
* intent_find_by_location:میں اس وقت [جوہر ٹاؤن](location) میں موجود ہوں
	- slot{"location":"جوہر ٹاؤن"}
	- action_find_by_location
* intent_find_by_price:میں [[مناسب](price)] کھانا چاہتا ہوں
	- slot{"location":"جوہر ٹاؤن"}
	- slot{"price":"مناسب"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:میں [چائنیز](cuisine) کھانا کھانا چاہتا ہوں
	- slot{"location":"جوہر ٹاؤن"}
	- slot{"price":"مناسب"}
	- slot{"cuisine":"چائنیز"}
	- action_find_by_location_cuisine_price
	- action_restart