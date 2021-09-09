## train185_S8_Sp013_M_L1_G1_A1-LP_C
* intent_find_by_location_price:میں اس وقت [گلبرگ](location) میں ہوں اور میرے پاس [دو ہزار](price) روپے ہیں کیا اس میں کوئی مناسب کھانا مل سکتا ہے
	- slot{"location":"گلبرگ"}
	- slot{"price":"دو ہزار"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:میں اس پرائس رینج میں [دیسی](cuisine) کھانا کھانا پسند کروں گا
	- slot{"location":"گلبرگ"}
	- slot{"price":"دو ہزار"}
	- slot{"cuisine":"دیسی"}
	- action_find_by_location_cuisine_price
	- action_restart