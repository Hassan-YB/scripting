## 181_S2_SP40_M_L1_G1_A1-P_C_L
* intent_find_by_price:میں نے رات کا کھانا کھانا ہے [تین ہزار](price) میں
	- slot{"price":"تین ہزار"}
	- action_find_by_price
* intent_find_by_cuisine:[باربی کیو](cuisine) ٹائپ ہو جائے
	- slot{"price":"تین ہزار"}
	- slot{"cuisine":"باربی کیو"}
	- action_find_by_cuisine_and_price
* intent_find_by_location::م: [شالیمار ٹاؤن](location) والی سائیڈ پہ
	- slot{"price":"تین ہزار"}
	- slot{"cuisine":"باربی کیو"}
	- slot{"location":"شالیمار ٹاؤن"}
	- action_find_by_location_cuisine_price
	- action_restart