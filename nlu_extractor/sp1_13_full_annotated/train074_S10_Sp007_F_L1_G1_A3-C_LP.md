## train074_S10_Sp007_F_L1_G1_A3-C_LP
* greet:السلام علیکم
	- utter_salaam
* intent_find_by_cuisine:میں [دیسی](cuisine) کھانا کھانا چاہتی ہوں
	- slot{"cuisine":"دیسی"}
	- action_find_by_cuisine
* intent_find_by_location_price:میں [مہنگا](price) کھانا پسند کروں گی اور میں یہ [ڈی ایچ اے](location) سے منگوانا پسند کروں گی
	- slot{"cuisine":"دیسی"}
	- slot{"price":"مہنگا"}
	- slot{"location":"ڈی ایچ اے"}
	- action_find_by_location_cuisine_price
	- action_restart