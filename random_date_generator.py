from faker import Faker
faker = Faker()
dob = []
date = faker.date_between(start_date='today', end_date='+30y')

def dob_date_generator():
    new_date = faker.date_between(start_date='-40y', end_date='-10y')
    return new_date

def expiry_date_generator():
    expiry_date = faker.date_between(start_date='today', end_date='+10y')
    return expiry_date

for i in range(100) :
    dob = dob_date_generator()
    expiry = expiry_date_generator()
    print(dob,expiry)
    

