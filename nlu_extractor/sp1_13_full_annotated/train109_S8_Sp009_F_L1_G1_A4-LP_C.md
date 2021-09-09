## train109_S8_Sp009_F_L1_G1_A4-LP_C
* intent_find_by_location_price:میں اس وقت [اقبال ٹاؤن](location) میں کھڑی ہوں اور میرے پاس [فائیو ہنڈرڈ](price) روپیز ہیں تو میں آپ مجھے کوئی قریب کا ریسٹورنٹ بتا سکتے ہیں جہاں سے میں اتنی رینج میں کھانا کھا سکوں
	- slot{"location":"اقبال ٹاؤن"}
	- slot{"price":"فائیو ہنڈرڈ"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:[فاسٹ فوڈ](cuisine)
	- slot{"location":"اقبال ٹاؤن"}
	- slot{"price":"فائیو ہنڈرڈ"}
	- slot{"cuisine":"فاسٹ فوڈ"}
	- action_find_by_location_cuisine_price
	- action_restart