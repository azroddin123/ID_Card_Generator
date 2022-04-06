
from googletrans import Translator
translator = Translator()
occupation_list = ["student" ,"medical","doctor","finance","lawyer","Engineer","designer","bannking","IT Professionals","Driver","Education","Airline","marketing","Farmer"]
ar_occupation =   ['طبي', 'طبيب', 'المالية', 'محامي', 'مهندس', 'مصمم', 'الخدمات المصرفية', 'مهنيات تكنولوجيا المعلومات', 'سائق', 'تعليم', 'شركة طيران', 'تسويق', 'مزارع', 'طالب علم', 'طبي', 'طبيب', 'المالية', 'محامي', 'مهندس', 'مصمم', 'الخدمات المصرفية', 'مهنيات تكنولوجيا المعلومات', 'سائق', 'تعليم', 'شركة طيران', 'تسويق', 'مزارع']

for i in range(len(occupation_list)) :
    ar_name=translator.translate(occupation_list[i],dest="ar")
    ar_occupation.append(ar_name.text)
    
print(ar_occupation)



with open("./data/ar_occupaion_names.text","w") as file:
    for i in range(len(occupation_list)) :
            file.write(f"{ar_occupation[i]} \n")
  



with open("./data/en_occupaion_names.text","w") as file:
    for i in range(len(occupation_list)) :
            file.write(f"{occupation_list[i]} \n")