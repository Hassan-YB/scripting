## train012_S11_Sp002_F_L1_G2_A5-L_CP
* intent_find_by_location:میں لاہور [ماڈل ٹاؤن](location) سے بات کر رہی ہوں.
	- slot{"location":"ماڈل ٹاؤن"}
	- action_find_by_location
* intent_find_by_cuisine_price:میں تھوڑا [سستا](price) [چائنیز](cuisine) کھانا کھانا چاہتی ہوں۔
	- slot{"location":"ماڈل ٹاؤن"}
	- slot{"price":"سستا"}
	- slot{"cuisine":"چائنیز"}
	- action_find_by_location_cuisine_price
	- action_restart