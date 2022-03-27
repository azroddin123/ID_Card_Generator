
from random import randint



def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def qatar_id_generator():
    n = 11
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


def uae_id_generator() :
    country_code = '784'
    second= str(randint(1000, 9999)) 
    third = str(random_with_N_digits(7))
    four = str(randint(0,9))
    return country_code+"-"+second+"-"+third+"-"+four


with open("UAE_card_number.text","a") as file:
    for i in range(100000) :
        id_card = uae_id_generator()
        file.write(f"{id_card} \n")

with open("katar_card_number.text","a") as file:
    for i in range(100000) :
        id_card = qatar_id_generator()
        file.write(f"{id_card} \n")