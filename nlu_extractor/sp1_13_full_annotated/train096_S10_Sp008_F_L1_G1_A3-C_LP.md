## train096_S10_Sp008_F_L1_G1_A3-C_LP
* intent_find_by_cuisine:مجھے نا بہت بھوک لگ رہی ہے تو میں نا [کڑاہی](cuisine) کھانا چاہ رہی ہوں
	- slot{"cuisine":"کڑاہی"}
	- action_find_by_cuisine
* intent_find_by_location_price:[جوہر ٹاؤن](location) سے [پندرہ سو](price) تک میں
	- slot{"cuisine":"کڑاہی"}
	- slot{"location":"جوہر ٹاؤن"}
	- slot{"price":"پندرہ سو"}
	- action_find_by_location_cuisine_price
	- action_restart