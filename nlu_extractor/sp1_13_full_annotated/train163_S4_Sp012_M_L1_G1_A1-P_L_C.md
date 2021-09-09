## train163_S4_Sp012_M_L1_G1_A1-P_L_C
* intent_find_by_price:میرے پاس [پانچ سو](price) روپے ہیں میں نے کچھ کھانا ہے مجھے بھوک لگی ہے
	- slot{"price":"پانچ سو"}
	- action_find_by_price
* intent_find_by_location:میں اس وقت [اقبال ٹاؤن](location) میں کھڑا ہوں
	- slot{"price":"پانچ سو"}
	- slot{"location":"اقبال ٹاؤن"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:میں [برگر](cuisine) کھانا پسند کروں گا
	- slot{"price":"پانچ سو"}
	- slot{"location":"اقبال ٹاؤن"}
	- slot{"cuisine":"برگر"}
	- action_find_by_location_cuisine_price
	- action_restart