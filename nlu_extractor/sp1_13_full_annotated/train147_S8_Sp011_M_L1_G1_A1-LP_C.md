## train147_S8_Sp011_M_L1_G1_A1-LP_C
* intent_find_by_location_price:مجھے [اقبال ٹاؤن](location) میں [مناسب](price) ریٹ پہ کھانا کھانا ہے
	- slot{"location":"اقبال ٹاؤن"}
	- slot{"price":"مناسب"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:[فاسٹ فوڈ](cuisine) کھانا پسند کرتا ہوں میں
	- slot{"location":"اقبال ٹاؤن"}
	- slot{"price":"مناسب"}
	- slot{"cuisine":"فاسٹ فوڈ"}
	- action_find_by_location_cuisine_price
	- action_restart