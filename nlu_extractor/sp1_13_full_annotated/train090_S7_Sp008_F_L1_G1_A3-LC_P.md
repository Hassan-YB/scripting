## train090_S7_Sp008_F_L1_G1_A3-LC_P
* intent_find_by_location_cuisine:میں [ڈی ایچ اے](location) سے بات کر رہی ہوں میں [چائنیز](cuisine) کھانا پسند کروں گی
	- slot{"location":"ڈی ایچ اے"}
	- slot{"cuisine":"چائنیز"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:میں [مناسب](price) میں
	- slot{"location":"ڈی ایچ اے"}
	- slot{"cuisine":"چائنیز"}
	- slot{"price":"مناسب"}
	- action_find_by_location_cuisine_price
	- action_restart