## train010_S10_Sp001_F_L1_G1_A5-C_LP
* intent_find_by_cuisine:میں [چائنیز](cuisine) کھانا کھانا چاہتی ہوں.
	- slot{"cuisine":"چائنیز"}
	- action_find_by_cuisine
* intent_find_by_location_price:میں لاہور میں [ماڈل ٹاؤن](location) سے کھانا کھانا چاہتی.اور [تین ہزار](price) روپیز میں کھانا چاہتی ہوں.
	- slot{"cuisine":"چائنیز"}
	- slot{"location":"ماڈل ٹاؤن"}
	- slot{"price":"تین ہزار"}
	- action_find_by_location_cuisine_price
	- action_restart