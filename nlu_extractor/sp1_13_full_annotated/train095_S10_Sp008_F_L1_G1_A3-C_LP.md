## train095_S10_Sp008_F_L1_G1_A3-C_LP
* intent_find_by_cuisine:مجھے نا بہت بھوک لگی ہے تو میں [کڑاہی](cuisine) کھانا چاہتی ہوں
	- slot{"cuisine":"کڑاہی"}
	- action_find_by_cuisine
* intent_find_by_location_price:[ہزار سے پندرہ سو](price) تک میں [ڈی ایچ اے یا ٹاؤن شپ](location) سے
	- slot{"cuisine":"کڑاہی"}
	- slot{"price":"ہزار سے پندرہ سو"}
	- slot{"location":"ڈی ایچ اے یا ٹاؤن شپ"}
	- action_find_by_location_cuisine_price
	- action_restart