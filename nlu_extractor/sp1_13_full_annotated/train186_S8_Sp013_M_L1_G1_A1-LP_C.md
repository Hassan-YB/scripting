## train186_S8_Sp013_M_L1_G1_A1-LP_C
* intent_find_by_location_price:میں اس وقت [ماڈل ٹاؤن](location) میں ہوں اور میرے پاس [تین ہزار](price) روپے ہیں
	- slot{"location":"ماڈل ٹاؤن"}
	- slot{"price":"تین ہزار"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:میں اس پرائس رینج میں دیسی کھانا کھانا پسند کروں گا اور دیسی میں [کڑاہی](cuisine)
	- slot{"location":"ماڈل ٹاؤن"}
	- slot{"price":"تین ہزار"}
	- slot{"cuisine":"کڑاہی"}
	- action_find_by_location_cuisine_price
	- action_restart