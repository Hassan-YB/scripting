## train167_S7_Sp012_M_L1_G1_A1-LC_P
* intent_find_by_location_cuisine:جی میں اس وقت [اچھرہ](location) میں بیٹھا ہوا ہوں اور میرا [پلاؤ](cuisine) کھانے کا دل کر رہا ہے
	- slot{"location":"اچھرہ"}
	- slot{"cuisine":"پلاؤ"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:جی میں میری جیب میں اس وقت [تین سو](price) روپے ہیں
	- slot{"location":"اچھرہ"}
	- slot{"cuisine":"پلاؤ"}
	- slot{"price":"تین سو"}
	- action_find_by_location_cuisine_price
	- action_restart