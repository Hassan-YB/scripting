## 209_S7_SP44_M_L1_G1_A5-LC_P
* intent_find_by_location_cuisine:السلام علیکم میں لاہور سے بات کر رہی ہوں [یو ای ٹی](location) کے پاس سے تو مجھے ابھی [زنگر برگر](cuisine) چاہیے
	- slot{"location":"یو ای ٹی"}
	- slot{"cuisine":"زنگر برگر"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:[سستا](price)
	- slot{"location":"یو ای ٹی"}
	- slot{"cuisine":"زنگر برگر"}
	- slot{"price":"سستا"}
	- action_find_by_location_cuisine_price
	- action_restart