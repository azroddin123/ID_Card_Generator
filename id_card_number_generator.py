
from random import randint



def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


def uae_id_generator() :
    country_code = '784'
    second= str(randint(1000, 9999)) 
    third = str(random_with_N_digits(7))
    four = str(randint(0,9))
    return country_code+"-"+second+"-"+third+"-"+four


for i in range(100000) :
    id_number = uae_id_generator()
    print(id_number)