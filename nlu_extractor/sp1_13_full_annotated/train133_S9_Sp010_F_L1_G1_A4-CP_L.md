## train133_S9_Sp010_F_L1_G1_A4-CP_L
* intent_find_by_cuisine_price:یہ میرے پاس [ہزار](price) روپے ہیں اور میں نے کوئی [برگر](cuisine) آرڈر کرنا ہے اپنے لیے
	- slot{"price":"ہزار"}
	- slot{"cuisine":"برگر"}
	- action_find_by_cuisine_and_price
* intent_find_by_location:[لنک روڈ](location) سے
	- slot{"price":"ہزار"}
	- slot{"cuisine":"برگر"}
	- slot{"location":"لنک روڈ"}
	- action_find_by_location_cuisine_price
	- action_restart