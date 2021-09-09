## train130_S7_Sp010_F_L1_G1_A4-LC_P
* intent_find_by_location_cuisine:جی میں اس وقت [مسلم ٹاؤن](location) کھڑی ہوں اور میں [برگر](cuisine) کھانا چاہتی ہوں
	- slot{"location":"مسلم ٹاؤن"}
	- slot{"cuisine":"برگر"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:[سستا](price) کھانا کھانا چاہتی ہوں
	- slot{"location":"مسلم ٹاؤن"}
	- slot{"cuisine":"برگر"}
	- slot{"price":"سستا"}
	- action_find_by_location_cuisine_price
	- action_restart