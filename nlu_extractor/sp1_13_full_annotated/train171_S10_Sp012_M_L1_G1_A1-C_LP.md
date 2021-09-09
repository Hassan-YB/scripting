## train171_S10_Sp012_M_L1_G1_A1-C_LP
* intent_find_by_cuisine:اس وقت موسم بہت اچھا ہو رہا ہے اور میرا [پکوڑے](cuisine) کھانے کو دل کر رہا ہے
	- slot{"cuisine":"پکوڑے"}
	- action_find_by_cuisine
* intent_find_by_location_price:جی [سمن آباد](location) سے کھانا چاہتا ہوں اور تقریباً میری جیب میں [دو ہزار](price) روپے ہیں
	- slot{"cuisine":"پکوڑے"}
	- slot{"location":"سمن آباد"}
	- slot{"price":"دو ہزار"}
	- action_find_by_location_cuisine_price
	- action_restart