## train192_S11_Sp013_M_L1_G1_A1-L_CP
* intent_find_by_location:میں اس وقت [سمن آباد](location) لاہور میں موجود ہوں اور یہاں پر ٹریفک بہت ہے اور میں کچھ کھانا کھانا چاہتا ہوں
	- slot{"location":"سمن آباد"}
	- action_find_by_location
* intent_find_by_cuisine_price:میں [فاسٹ فوڈ](cuisine) کھانا چاہتا ہوں اور میری پرائس رینج [مناسب](price) ہے
	- slot{"location":"سمن آباد"}
	- slot{"cuisine":"فاسٹ فوڈ"}
	- slot{"price":"مناسب"}
	- action_find_by_location_cuisine_price
	- action_restart