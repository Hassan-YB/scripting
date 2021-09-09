## train132_S9_Sp010_F_L1_G1_A4-CP_L
* intent_find_by_cuisine_price:میرے پاس [دو ہزار](price) موجود ہیں اور میں نے [پیزا](cuisine) آرڈر کرنا ہے
	- slot{"price":"دو ہزار"}
	- slot{"cuisine":"پیزا"}
	- action_find_by_cuisine_and_price
* intent_find_by_location:[چوبرجی](location) سے
	- slot{"price":"دو ہزار"}
	- slot{"cuisine":"پیزا"}
	- slot{"location":"چوبرجی"}
	- action_find_by_location_cuisine_price
	- action_restart