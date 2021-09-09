## train025_S12_Sp002_F_L1_G2_A5-P_CL
* intent_find_by_price:[فائیو تھاؤزنڈ](price) کا کھانا چاہ رہی ہوں مہنگا
	- slot{"price":"فائیو تھاؤزنڈ"}
	- action_find_by_price
* intent_find_by_location_cuisine:میں [سیٹلائٹ ٹاؤن](location) سے [دیسی](cuisine) کھانا کھانا چاہتی ہوں
	- slot{"price":"فائیو تھاؤزنڈ"}
	- slot{"location":"سیٹلائٹ ٹاؤن"}
	- slot{"cuisine":"دیسی"}
	- action_find_by_location_cuisine_price
	- action_restart