## train131_S8_Sp010_F_L1_G1_A4-LP_C
* intent_find_by_location_price:جی میں [لنک روڈ](location) پہ موجود ہوں اور میرے پاس صرف [پانچ سو](price)روپے ہیں مجھے بھوک لگی ہوئی ہے
	- slot{"location":"لنک روڈ"}
	- slot{"price":"پانچ سو"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:[فاسٹ فوڈ](cuisine) کھانا پسند کروں گی
	- slot{"location":"لنک روڈ"}
	- slot{"price":"پانچ سو"}
	- slot{"cuisine":"فاسٹ فوڈ"}
	- action_find_by_location_cuisine_price
	- action_restart