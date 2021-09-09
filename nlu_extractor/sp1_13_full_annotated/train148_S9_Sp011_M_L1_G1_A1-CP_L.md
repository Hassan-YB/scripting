## train148_S9_Sp011_M_L1_G1_A1-CP_L
* intent_find_by_cuisine_price:میرے پاس [پانچ سو](price) روپے ہیں اور مجھے [برگر](cuisine) کھانا ہے
	- slot{"price":"پانچ سو"}
	- slot{"cuisine":"برگر"}
	- action_find_by_cuisine_and_price
* intent_find_by_location:مجھے یہاں [شالیمار](location) کے ایریا میں کوئی جگہ چاہیے کھانے پینے کے لیے
	- slot{"price":"پانچ سو"}
	- slot{"cuisine":"برگر"}
	- slot{"location":"شالیمار"}
	- action_find_by_location_cuisine_price
	- action_restart