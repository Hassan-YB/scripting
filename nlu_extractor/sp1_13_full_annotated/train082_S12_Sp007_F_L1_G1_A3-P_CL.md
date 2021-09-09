## train082_S12_Sp007_F_L1_G1_A3-P_CL
* intent_find_by_price:مجھے بہت زیادہ بھوک لگی ہے اور میرے پاس جو ہے پرائس بہت ریزنیبل سی ہے لائک [ون تھاؤزنڈ](price)
	- slot{"price":"ون تھاؤزنڈ"}
	- action_find_by_price
* intent_find_by_location_cuisine:اچھا جگہ تو [لنک روڈ](location) ہو لائک [لنک روڈ](location) ہو اور کھانا کوئی مناسب ہو لائک کوئی [فاسٹ فوڈ](cuisine) ہو جائے
	- slot{"price":"ون تھاؤزنڈ"}
	- slot{"location":"لنک روڈ"}
	- slot{"cuisine":"فاسٹ فوڈ"}
	- action_find_by_location_cuisine_price
	- action_restart