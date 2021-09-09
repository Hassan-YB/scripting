## train174_S11_Sp012_M_L1_G1_A1-L_CP
* intent_find_by_location:میں [مسلم ٹاؤن](location) میں کھڑا ہوا ہوں اور میرے مجھے بہت بھوک لگ رہی ہے میرا کچھ کھانے کو دل کر رہا ہے
	- slot{"location":"مسلم ٹاؤن"}
	- action_find_by_location
* intent_find_by_cuisine_price:میرا [بریانی](cuisine) کھانے کو دل کر رہا ہے اور [ہزار](price) روپے کے میری پرائس رینج ہے
	- slot{"location":"مسلم ٹاؤن"}
	- slot{"cuisine":"بریانی"}
	- slot{"price":"ہزار"}
	- action_find_by_location_cuisine_price
	- action_restart