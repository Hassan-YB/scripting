## 129_S3_SP30_M_L1_G1_A2-C_P_L
* intent_find_by_cuisine:السلام علیکم میں [فاسٹ فوڈ](cuisine) کھانا چاہتا ہوں مجھے اس کے بارے میں گائیڈنس
	- slot{"cuisine":"فاسٹ فوڈ"}
	- action_find_by_cuisine
* intent_find_by_price:میں [مناسب](price) کھانا چاہتا ہوں
	- slot{"cuisine":"فاسٹ فوڈ"}
	- slot{"price":"مناسب"}
	- action_find_by_cuisine_and_price
* intent_find_by_location:میں [باغبان پورہ](location) سے کھانا
	- slot{"cuisine":"فاسٹ فوڈ"}
	- slot{"price":"مناسب"}
	- slot{"location":"باغبان پورہ"}
	- action_find_by_location_cuisine_price
	- action_restart