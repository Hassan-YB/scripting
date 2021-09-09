## train173_S10_Sp012_M_L1_G1_A1-C_LP
* intent_find_by_cuisine:ناشتے کا وقت ہے اور میرا [نان چنے](cuisine) کھانے کا دل کر رہا ہے
	- slot{"cuisine":"نان چنے"}
	- action_find_by_cuisine
* intent_find_by_location_price:[اچھرہ](location) سے اور پرائس رینج میری پانچ [پانچ سو](price) ہے
	- slot{"cuisine":"نان چنے"}
	- slot{"location":"اچھرہ"}
	- slot{"price":"پانچ سو"}
	- action_find_by_location_cuisine_price
	- action_restart