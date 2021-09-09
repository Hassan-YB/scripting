## train071_S12_Sp007_F_L1_G1_A3-P_CL
* intent_find_by_price:مجھے بہت بھوک لگی ہےاور میں اپنے لیے [ون تھاؤزنڈ](price)کی رینج میں کچھ آرڈر کرنا چاہتی ہوں
	- slot{"price":"ون تھاؤزنڈ"}
	- action_find_by_price
* intent_find_by_location_cuisine:میں [لنک روڈ](location) سے [لنک روڈ](location) سے [چائنیز](cuisine)
	- slot{"price":"ون تھاؤزنڈ"}
	- slot{"location":"لنک روڈ"}
	- slot{"cuisine":"چائنیز"}
	- action_find_by_location_cuisine_price
	- action_restart