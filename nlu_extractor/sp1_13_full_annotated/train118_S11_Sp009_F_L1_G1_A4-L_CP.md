## train118_S11_Sp009_F_L1_G1_A4-L_CP
* intent_find_by_location:میں [شالامار](location) کھڑی ہوں اور مجھے کچھ کھانا ہے
	- slot{"location":"شالامار"}
	- action_find_by_location
* intent_find_by_cuisine_price:میں [مناسب](price) منگوانا چاہوں گی اورمیں [مناسب](price) منگوانا چاہوں گی اور مجھے آپ [بریانی](cuisine) سینڈ کر دیں
	- slot{"location":"شالامار"}
	- slot{"price":"مناسب"}
	- slot{"cuisine":"بریانی"}
	- action_find_by_location_cuisine_price
	- action_restart