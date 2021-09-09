## train126_S3_Sp010_F_L1_G1_A4-C_P_L
* intent_find_by_cuisine:مجھے [برگر](cuisine) کھانا ہے
	- slot{"cuisine":"برگر"}
	- action_find_by_cuisine
* intent_find_by_price:[مناسب](price)
	- slot{"cuisine":"برگر"}
	- slot{"price":"مناسب"}
	- action_find_by_cuisine_and_price
* intent_find_by_location:[چوبرجی](location) سے
	- slot{"cuisine":"برگر"}
	- slot{"price":"مناسب"}
	- slot{"location":"چوبرجی"}
	- action_find_by_location_cuisine_price
	- action_restart