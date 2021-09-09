## 139_S6_SP33_M_L1_G1_A3-C_L_P
* intent_find_by_cuisine:جی [فاسٹ فوڈ](cuisine) کھانا چاہ رہا ہوں میں
	- slot{"cuisine":"فاسٹ فوڈ"}
	- action_find_by_cuisine
* intent_find_by_location::م: نیئرسٹ [شالیمار](location)
	- slot{"cuisine":"فاسٹ فوڈ"}
	- slot{"location":"شالیمار"}
	- action_find_by_location_and_cuisine
* intent_find_by_price:[نارمل](price)
	- slot{"cuisine":"فاسٹ فوڈ"}
	- slot{"location":"شالیمار"}
	- slot{"price":"نارمل"}
	- action_find_by_location_cuisine_price
	- action_restart