## train119_S11_Sp009_F_L1_G1_A4-L_CP
* intent_find_by_location:میں [باغبان پورہ](location) کھڑی ہوں اور میں کچھ کھانا چاہتی ہوں
	- slot{"location":"باغبان پورہ"}
	- action_find_by_location
* intent_find_by_cuisine_price:میں مناسب آرڈر کرنا چاہوں گی اور میرے پاس اس وقت [ہزار](price) روپے ہیں تو میں [پیزا](cuisine) کھانا چاہوں گی
	- slot{"location":"باغبان پورہ"}
	- slot{"cuisine":"پیزا"}
	- slot{"price":"ہزار"}
	- action_find_by_location_cuisine_price
	- action_restart