## 127_S4_SP30_M_L1_G1_A2-P_L_C
* greet:السلام علیکم
	- utter_salaam
	- utter_help_urdu
* intent_find_by_price:میں نے کھانے کے بارے میں جاننا تھا میری رینج ہے  [تھری تھاؤزنڈ سے فور تھاؤزنڈ](price) تو مجھے اس رینج میں کیا اچھے کھانے
	- slot{"price":"تھری تھاؤزنڈ سے فور تھاؤزنڈ"}
	- action_find_by_price
* intent_find_by_location:[سلامت پورہ](location) والی سائیڈ سے کھانا چاہتا ہوں
	- slot{"price":"تھری تھاؤزنڈ سے فور تھاؤزنڈ"}
	- slot{"location":"سلامت پورہ"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:[چائنیز](cuisine) فوڈ
	- slot{"price":"تھری تھاؤزنڈ سے فور تھاؤزنڈ"}
	- slot{"location":"سلامت پورہ"}
	- slot{"cuisine":"چائنیز"}
	- action_find_by_location_cuisine_price
	- action_restart