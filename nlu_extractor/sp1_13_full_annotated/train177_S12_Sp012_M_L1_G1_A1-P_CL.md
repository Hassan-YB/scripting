## train177_S12_Sp012_M_L1_G1_A1-P_CL
* intent_find_by_price:جی مجھے میرے پاس [پانچ سو](price) روپیہ ہے اور مجھے بہت بھوک لگ رہی ہے
	- slot{"price":"پانچ سو"}
	- action_find_by_price
* intent_find_by_location_cuisine:یہ میرا [دیسی](cuisine) کھانے کا دل کر رہا ہے اور میں [ٹاؤن شپ](location) سے بول رہا ہوں
	- slot{"price":"پانچ سو"}
	- slot{"cuisine":"دیسی"}
	- slot{"location":"ٹاؤن شپ"}
	- action_find_by_location_cuisine_price
	- action_restart