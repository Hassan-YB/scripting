## 197_S1_SP43_M_L1_G1_A5-L_C_P
* intent_find_by_location:السلام علیکم میں اس وقت :م: [کینٹ](location) ایریا کھڑا ہوں اور مجھے کھانا کھانا ہے تو کائنڈلی مجھے کچھ لوکیشنز بتائیے گا
	- slot{"location":"کینٹ"}
	- action_find_by_location
* intent_find_by_cuisine:مجھے [چائنیز](cuisine) کھانا کھانا ہے
	- slot{"location":"کینٹ"}
	- slot{"cuisine":"چائنیز"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:نہیں میں [مناسب](price) کھانا چاہوں گا
	- slot{"location":"کینٹ"}
	- slot{"cuisine":"چائنیز"}
	- slot{"price":"مناسب"}
	- action_find_by_location_cuisine_price
	- action_restart