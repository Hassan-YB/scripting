## 217_S9_SP46_F_L1_G2_A3-CP_L
* intent_find_by_cuisine_price:میری پرائس رینج [ایک ہزار سے لے کر پندرہ سو](price) تک ہے میں دیسی کھانا آرڈر کرنا چاہ رہی ہوں کیا آپ لوگوں کے پاس [کباب تکے اور باربی کیو](cuisine) ہیں اس کے بارے میں پلیز مجھے معلومات دے دیجیئے
	- slot{"cuisine":"کباب تکے اور باربی کیو"}
	- slot{"price":"ایک ہزار سے لے کر پندرہ سو"}
	- action_find_by_cuisine_and_price
* intent_find_by_location:میں لاہور کے اندر :م: [گلبرگ](location) والے جگہ سے کھانا کھانا چاہتی ہوں اس کے آس پاس اگر کوئی ریسٹورنٹ ہے تو میں اس کو ترجیح دوں گی
	- slot{"cuisine":"کباب تکے اور باربی کیو"}
	- slot{"price":"ایک ہزار سے لے کر پندرہ سو"}
	- slot{"location":"گلبرگ"}
	- action_find_by_location_cuisine_price
	- action_restart