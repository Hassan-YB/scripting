## train188_S9_Sp013_M_L1_G1_A1-CP_L
* intent_find_by_cuisine_price:میں مجھے بہت بھوک لگ رہی ہے اور اس وقت میرا لنچ ٹائم ہے میں [پیزا](cuisine) کھانا چاہتا ہوں [دو ہزار](price) کی پرائس رینج میں
	- slot{"cuisine":"پیزا"}
	- slot{"price":"دو ہزار"}
	- action_find_by_cuisine_and_price
* intent_find_by_location:میں یہ کھانا لاہور میں [اقبال ٹاؤن](location) سے آرڈر کرنا چاہوں گا
	- slot{"cuisine":"پیزا"}
	- slot{"price":"دو ہزار"}
	- slot{"location":"اقبال ٹاؤن"}
	- action_find_by_location_cuisine_price
	- action_restart