## train172_S10_Sp012_M_L1_G1_A1-C_LP
* intent_find_by_cuisine:موسم بڑا بہترین ہو رہا ہے اور اس وقت میرا [پکوڑے](cuisine) کھانے کا دل کر رہا ہے
	- slot{"cuisine":"پکوڑے"}
	- action_find_by_cuisine
* intent_find_by_location_price:جی [سبزہ زار](location) سے اور میری رینج [پانچ ہزار](price) ہے
	- slot{"cuisine":"پکوڑے"}
	- slot{"location":"سبزہ زار"}
	- slot{"price":"پانچ ہزار"}
	- action_find_by_location_cuisine_price
	- action_restart