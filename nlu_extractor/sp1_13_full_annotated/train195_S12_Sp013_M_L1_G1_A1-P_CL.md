## train195_S12_Sp013_M_L1_G1_A1-P_CL
* intent_find_by_price:میرے پاس صرف [پانچ سو](price) روپے ہیں اور مجھے بہت بھوک لگ رہی ہے میں کچھ کھانا کھانا چاہتا ہوں
	- slot{"price":"پانچ سو"}
	- action_find_by_price
* intent_find_by_location_cuisine:میں [فاسٹ فوڈ](cuisine) کھانا چاہتا ہوں اور میری لوکیشن [ڈی ایچ اے](location) لاہور ہے
	- slot{"price":"پانچ سو"}
	- slot{"cuisine":"فاسٹ فوڈ"}
	- slot{"location":"ڈی ایچ اے"}
	- action_find_by_location_cuisine_price
	- action_restart