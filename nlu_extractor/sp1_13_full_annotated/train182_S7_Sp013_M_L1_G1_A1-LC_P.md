## train182_S7_Sp013_M_L1_G1_A1-LC_P
* intent_find_by_location_cuisine:میں اس وقت [یو ای ٹی](location) میں ہوں اور میں [چائنیز](cuisine) کھانا کھانا چاہتا ہوں
	- slot{"location":"یو ای ٹی"}
	- slot{"cuisine":"چائنیز"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:میں یہ کھانا [مناسب](price) پرائس رینج میں کھانا چاہتا ہوں
	- slot{"location":"یو ای ٹی"}
	- slot{"cuisine":"چائنیز"}
	- slot{"price":"مناسب"}
	- action_find_by_location_cuisine_price
	- action_restart