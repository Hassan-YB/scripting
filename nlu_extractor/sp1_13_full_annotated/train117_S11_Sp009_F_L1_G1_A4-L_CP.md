## train117_S11_Sp009_F_L1_G1_A4-L_CP
* intent_find_by_location:میں [ایجو کیشن یونیورسٹی](location) میں کھڑی ہوں اور میں کچھ کھانا چاہتی ہوں
	- slot{"location":"ایجو کیشن یونیورسٹی"}
	- action_find_by_location
* intent_find_by_cuisine_price:میں [مناسب](price) رینج میں کھانا پسند کروں گی اور میں [برگر](cuisine) کھانا پسند کروں گی
	- slot{"location":"ایجو کیشن یونیورسٹی"}
	- slot{"price":"مناسب"}
	- slot{"cuisine":"برگر"}
	- action_find_by_location_cuisine_price
	- action_restart