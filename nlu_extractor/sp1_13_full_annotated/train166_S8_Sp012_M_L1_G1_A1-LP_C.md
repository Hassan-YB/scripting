## train166_S8_Sp012_M_L1_G1_A1-LP_C
* intent_find_by_location_price:جی میں اس وقت [سمن آباد](location) میں بیٹھا ہوا ہوں اور میری جیب میں اس وقت [پانچ سو](price) روپے ہے
	- slot{"location":"سمن آباد"}
	- slot{"price":"پانچ سو"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:[پیزا](cuisine) کھانا پسند کروں گا
	- slot{"location":"سمن آباد"}
	- slot{"price":"پانچ سو"}
	- slot{"cuisine":"پیزا"}
	- action_find_by_location_cuisine_price
	- action_restart