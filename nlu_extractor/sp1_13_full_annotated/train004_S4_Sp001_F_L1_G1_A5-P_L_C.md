## train004_S4_Sp001_F_L1_G1_A5-P_L_C
* intent_find_by_price:میں کھانا کھانا چاہتی ہوں اور میں چاہتی ہوں کہ میرا یہ کھانا [تین ہزار](price) روپیز میں ہو جائے.
	- slot{"price":"تین ہزار"}
	- action_find_by_price
* intent_find_by_location:میں لاہور میں [ہربنس پورہ](location) سے کھانا کھانا چاہتی ہوں۔
	- slot{"price":"تین ہزار"}
	- slot{"location":"ہربنس پورہ"}
	- action_find_by_location_and_price
* intent_find_by_cuisine:میں [دیسی](cuisine) کھانا کھانا چاہتی ہوں.
	- slot{"price":"تین ہزار"}
	- slot{"location":"ہربنس پورہ"}
	- slot{"cuisine":"دیسی"}
	- action_find_by_location_cuisine_price
	- action_restart