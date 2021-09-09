## 132_S8_SP31_M_L2_G1_A1-LP_C
* greet:السلام علیکم میم
	- utter_salaam
	- utter_help_urdu
* intent_find_by_location_price:میم میرے پاس تقریبا کوئی [سیون ہنڈرڈ](price) روپیز ہیں :م: اس وقت میں [ماڈل ٹاؤن](location) والے ایریا میں ہوں میں کچھ اچھا کھانا چاہ رہا ہوں
	- slot{"location":"ماڈل ٹاؤن"}
	- slot{"price":"سیون ہنڈرڈ"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:میم تھوڑا سپائسی [چائنیز](cuisine) ٹائپ
	- slot{"location":"ماڈل ٹاؤن"}
	- slot{"price":"سیون ہنڈرڈ"}
	- slot{"cuisine":"چائنیز"}
	- action_find_by_location_cuisine_price
	- action_restart