from models.customer import Customer
from faker import Faker
from random import choice, randint
import mlab

mlab.connect()

fake = Faker()

for i in range(50):
    print("Saving customer", i + 1, ".....")
    customer = Customer(name = fake.name(),
                        gender = randint(0,1),
                        email = fake.email(),
                        phone = fake.phone_number(),
                        job = fake.job(),
                        company = fake.company(),
                        address = fake.address(),
                        contacted = choice([True, False]),
                        measurements = [85, 63, 94])
    customer.save()
    # print(customer.to_mongo())
