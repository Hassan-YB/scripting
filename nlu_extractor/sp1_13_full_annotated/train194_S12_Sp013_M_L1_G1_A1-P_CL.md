## train194_S12_Sp013_M_L1_G1_A1-P_CL
* intent_find_by_price:میرے پاس مجھے اس وقت بہت بھوک لگ رہی اور میرے پاس صرف [پانچ سو](price) روپے ہیں
	- slot{"price":"پانچ سو"}
	- action_find_by_price
* intent_find_by_location_cuisine:میں اس پرائس رینج میں [فاسٹ فوڈ](cuisine) کھانا چاہوں گا اور میں آرڈر [سمن آباد](location) لاہور سے کرنا چاہوں گا
	- slot{"price":"پانچ سو"}
	- slot{"cuisine":" فاسٹ فوڈ"}
	- slot{"location":"سمن آباد"}
	- action_find_by_location_cuisine_price
	- action_restart