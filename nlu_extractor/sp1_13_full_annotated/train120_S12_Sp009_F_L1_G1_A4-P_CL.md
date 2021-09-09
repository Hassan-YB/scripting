## train120_S12_Sp009_F_L1_G1_A4-P_CL
* intent_find_by_price:میرے پاس کم پیسے ہیں مجھے بہت بھوک لگی ہے تو آپ کوئی [سستا](price) کھانا بتا سکتے ہیں
	- slot{"price":"سستا"}
	- action_find_by_price
* intent_find_by_location_cuisine:میں یہ کھانا [لنک روڈ](location) سے منگوانا پسند کروں گی اور میں [چائنیز](cuisine) کھانا پسند کروں گی
	- slot{"price":"سستا"}
	- slot{"location":"لنک روڈ"}
	- slot{"cuisine":"چائنیز"}
	- action_find_by_location_cuisine_price
	- action_restart