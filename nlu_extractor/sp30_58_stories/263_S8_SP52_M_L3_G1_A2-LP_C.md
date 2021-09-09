## 263_S8_SP52_M_L3_G1_A2-LP_C
* intent_find_by_location_price:السلام علیکم میں اس وقت [[ڈی ایچ اے](price)](location) میں ہوں اور میں :م: دو ہزار روپے کی رینج میں کچھ کھانا چاہتا ہوں تو آپ مجھے اپنا مینیو بتا سکتے ہیں
	- slot{"location":"ڈی ایچ اے"}
	- slot{"price":"دو ہزار"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:[چائنیز](cuisine)
	- slot{"location":"ڈی ایچ اے"}
	- slot{"price":"دو ہزار"}
	- slot{"cuisine":"چائنیز"}
	- action_find_by_location_cuisine_price
	- action_restart