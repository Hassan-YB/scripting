## 211_S7_SP45_F_L1_G1_A5-LC_P
* intent_find_by_location_cuisine::م: مجھے [پنجابی](cuisine)  کھانا کھانا ہے اور [یو ای ٹی](location) کے پاس کوئی بھی ہے ریسٹورنٹ تو مجھے بتا دیں
	- slot{"location":"یو ای ٹی"}
	- slot{"cuisine":"پنجابی"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:[سستا](price) ہو
	- slot{"location":"یو ای ٹی"}
	- slot{"cuisine":"پنجابی"}
	- slot{"price":"سستا"}
	- action_find_by_location_cuisine_price
	- action_restart