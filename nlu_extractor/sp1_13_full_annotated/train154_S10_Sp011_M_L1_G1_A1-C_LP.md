## train154_S10_Sp011_M_L1_G1_A1-C_LP
* intent_find_by_cuisine:مجھے [برگر](cuisine) بہت پسند ہے میں [برگر](cuisine) کھانا پسند کرتا ہوں اور مجھے [برگر](cuisine) کھانا ہے
	- slot{"cuisine":"برگر"}
	- action_find_by_cuisine
* intent_find_by_location_price:مجھے [پانچ سو](price) روپے میں [سمن آباد](location) کی لوکیشن کے اندر برگر کھانا ہے
	- slot{"cuisine":"برگر"}
	- slot{"price":"پانچ سو"}
	- slot{"location":"سمن آباد"}
	- action_find_by_location_cuisine_price
	- action_restart