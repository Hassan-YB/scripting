## train134_S10_Sp010_F_L1_G1_A4-C_LP
* intent_find_by_cuisine:جی مجھے بہت تیز بھوک لگی ہے اور میں [کڑاہی](cuisine) آرڈر کرنا چاہتی ہوں
	- slot{"cuisine":"کڑاہی"}
	- action_find_by_cuisine
* intent_find_by_location_price:[مناسب](price) آرڈر کرنا چاہتی ہوں اور [اقبال ٹاؤن](location) سے کر دیں آرڈر
	- slot{"cuisine":"کڑاہی"}
	- slot{"price":"مناسب"}
	- slot{"location":"اقبال ٹاؤن"}
	- action_find_by_location_cuisine_price
	- action_restart