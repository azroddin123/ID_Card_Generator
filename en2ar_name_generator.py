from faker import Faker 

from googletrans import Translator
from numpy import full
faker = Faker()
translator = Translator()

n=int(input("Enter How Many Names You wants to generate : \t"))

en_names = []
ar_names = [] 


for i in range(n) :
    en_name = faker.name()
    first_name = faker.first_name()
    full_name ="Name: " + first_name +" " +en_name
    en_names.append(full_name)
    print(full_name)
    ar_name = translator.translate(full_name,dest="ar")
    ar_names.append(ar_name.text)
    
with open("english_names_50.text","w") as file:
    for i in range(len(en_names)) :
        file.write(f"{en_names[i]}\n")   
        
with open("arabic_names.text_50","w") as file:
    for i in range(len(ar_names)) :
        file.write(f"{ar_names[i]}\n") 
        
file.close()
file.close()