## train097_S1_Sp008_F_L1_G1_A3-L_C_P
* intent_find_by_location:میں [ٹاؤن شپ](location) سے بات کر رہی ہوں
	- slot{"location":"ٹاؤن شپ"}
	- action_find_by_location
* intent_find_by_cuisine:مجھے [کڑاہی](cuisine) کھانی ہے
	- slot{"location":"ٹاؤن شپ"}
	- slot{"cuisine":"کڑاہی"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:ہزار [ہزار](price) تک میں
	- slot{"location":"ٹاؤن شپ"}
	- slot{"cuisine":"کڑاہی"}
	- slot{"price":" ہزار"}
	- action_find_by_location_cuisine_price
	- action_restart