## train129_S7_Sp010_F_L1_G1_A4-LC_P
* intent_find_by_location_cuisine:جی میں [اقبال ٹاؤن](location) موجود ہوں اور مجھے بہت تیز بھوک لگی ہے میں نے [دال چاول](cuisine) کھانی ہیں
	- slot{"location":"اقبال ٹاؤن"}
	- slot{"cuisine":"دال چاول"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:مناسب میرے پاس صرف [پانچ سو](price) روپے ہیں
	- slot{"location":"اقبال ٹاؤن"}
	- slot{"cuisine":"دال چاول"}
	- slot{"price":"پانچ سو"}
	- action_find_by_location_cuisine_price
	- action_restart