## train158_S12_Sp011_M_L1_G1_A1-P_CL
* intent_find_by_price:مجھے [ہزار](price) روپے میں کھانا کھانا ہے
	- slot{"price":"ہزار"}
	- action_find_by_price
* intent_find_by_location_cuisine:میں [سمن آباد](location) میں [برگر](cuisine) کھانا چاہتا ہوں
	- slot{"price":"ہزار"}
	- slot{"location":"سمن آباد"}
	- slot{"cuisine":"برگر"}
	- action_find_by_location_cuisine_price
	- action_restart