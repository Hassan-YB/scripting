## train135_S10_Sp010_F_L1_G1_A4-C_LP
* intent_find_by_cuisine:جی میں اس وقت بہت زیادہ بھوکی ہوں اور میں نے اپنے لیے [پیزا](cuisine) آرڈر کرنا ہے
	- slot{"cuisine":"پیزا"}
	- action_find_by_cuisine
* intent_find_by_location_cuisine:[فیروز پور روڈ](location) سے میں آرڈر کرنا چاہتی ہوں اور [سستا](price) کھانا آرڈر کرنا چاہتی ہوں
	- slot{"cuisine":"پیزا"}
	- slot{"location":"فیروز پور روڈ"}
	- slot{"price":"سستا"}
	- action_find_by_location_cuisine_price
	- action_restart