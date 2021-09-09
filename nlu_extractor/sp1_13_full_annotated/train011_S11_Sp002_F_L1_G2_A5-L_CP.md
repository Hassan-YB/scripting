## train011_S11_Sp002_F_L1_G2_A5-L_CP
* intent_find_by_location:میں لاہور [ہربنس پورہ](location) سے [ہربنس پورہ](location) میں ہوں اور میں کھانا کھانا چاہتی ہوں.
	- slot{"location":"ہربنس پورہ"}
	- action_find_by_location
* intent_find_by_cuisine_price:میں [دیسی](cuisine) کھانا کھانا چاہتی ہوں.اور [تین ہزار](price) روپیز میں کھانا چاہتی ہوں.
	- slot{"location":"ہربنس پورہ"}
	- slot{"cuisine":"دیسی"}
	- slot{"price":"تین ہزار"}
	- action_find_by_location_cuisine_price
	- action_restart