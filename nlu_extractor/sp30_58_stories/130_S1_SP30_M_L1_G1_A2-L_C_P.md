## 130_S1_SP30_M_L1_G1_A2-L_C_P
* greet:السلام علیکم
	- utter_salaam
	- utter_help_urdu
* intent_find_by_location:میں کھانا کھانا چاہ رہا ہوں آس پاس کسی ایریا میں فی الوقت میں [فیصل ٹاؤن](location) والی سائیڈ پہ ہوں میں کچھ اچھا کھانا چاہ رہا ہوں
	- slot{"location":"فیصل ٹاؤن"}
	- action_find_by_location
* intent_find_by_cuisine:[دیسی](cuisine) کھانا چاہ رہا ہوں میم میں
	- slot{"location":"فیصل ٹاؤن"}
	- slot{"cuisine":"دیسی"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:[مناسب](price) کھانا چاہتا ہوں مگر اچھا کھانا چاہتا ہوں
	- slot{"location":"فیصل ٹاؤن"}
	- slot{"cuisine":"دیسی"}
	- slot{"price":"مناسب"}
	- action_find_by_location_cuisine_price
	- action_restart