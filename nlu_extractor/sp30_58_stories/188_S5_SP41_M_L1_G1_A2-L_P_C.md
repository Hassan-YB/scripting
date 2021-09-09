## 188_S5_SP41_M_L1_G1_A2-L_P_C
* intent_find_by_location:میں [باغبان پورہ](location) میں ہوں
	- slot{"location":"باغبان پورہ"}
	- action_find_by_location
* intent_find_by_price:سستا [مناسب](price) :م:
	- slot{"location":"باغبان پورہ"}
	- slot{"price":"مناسب"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:[برگر](cuisine)
	- slot{"location":"باغبان پورہ"}
	- slot{"price":"مناسب"}
	- slot{"cuisine":"برگر"}
	- action_find_by_location_cuisine_price
	- action_restart