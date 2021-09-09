## train008_S8_Sp001_F_L1_G1_A5-LP_C
* intent_find_by_location_price:میں اس وقت لاہور [ماڈل ٹاؤن](location) میں ہوں اور میں [پانچ ہزار](price) روپے کا کھانا کھانا چاہتی ہوں۔
	- slot{"location":"ماڈل ٹاؤن"}
	- slot{"price":"پانچ ہزار"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:میں [چائنیز](cuisine) کھانا کھانا چاہتی ہوں۔
	- slot{"location":"ماڈل ٹاؤن"}
	- slot{"price":"پانچ ہزار"}
	- slot{"cuisine":"چائنیز"}
	- action_find_by_location_cuisine_price
	- action_restart