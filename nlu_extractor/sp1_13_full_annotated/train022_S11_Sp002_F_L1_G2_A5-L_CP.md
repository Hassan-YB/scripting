## train022_S11_Sp002_F_L1_G2_A5-L_CP
* intent_find_by_location:میں [سیٹلائٹ](location) لاہور سے بول رہی ہوں
	- slot{"location":"سیٹلائٹ"}
	- action_find_by_location
* intent_find_by_cuisine_price:میں [چائنیز](cuisine) کھانا چاہ رہی ہوں اور [تھری تھاؤزنڈ](price) میں کھانا چاہ رہی ہوں۔
	- slot{"location":"سیٹلائٹ"}
	- slot{"cuisine":"چائنیز"}
	- slot{"price":"تھری تھاؤزنڈ"}
	- action_find_by_location_cuisine_price
	- action_restart