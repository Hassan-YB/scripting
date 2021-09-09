## 161_S3_SP37_M_L1_G1_A1-C_P_L
* intent_find_by_cuisine:سپائسی [فاسٹ فوڈ](cuisine)
	- slot{"cuisine":"فاسٹ فوڈ"}
	- action_find_by_cuisine
* intent_find_by_price:[مناسب](price)
	- slot{"cuisine":"فاسٹ فوڈ"}
	- slot{"price":"مناسب"}
	- action_find_by_cuisine_and_price
* intent_find_by_location:[قذافی اسٹیڈیم](location) نیئر
	- slot{"cuisine":"فاسٹ فوڈ"}
	- slot{"price":"مناسب"}
	- slot{"location":"قذافی اسٹیڈیم"}
	- action_find_by_location_cuisine_price
	- action_restart