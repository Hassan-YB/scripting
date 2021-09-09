## train189_S10_Sp013_M_L1_G1_A1-C_LP
* intent_find_by_cuisine:میں [کڑاہی گوشت](cuisine) کھانا چاہتا ہوں
	- slot{"cuisine":"کڑاہی گوشت"}
	- action_find_by_cuisine
* intent_find_by_location_price:میں یہ کھانا [مناسب](price) پرائس رینج میں کھانا پسند کروں گا [اقبال ٹاؤن](location) سے
	- slot{"cuisine":"کڑاہی گوشت"}
	- slot{"price":"مناسب"}
	- slot{"location":"اقبال ٹاؤن"}
	- action_find_by_location_cuisine_price
	- action_restart