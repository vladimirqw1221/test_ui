from faker import Faker
from data_project.fake_data import DataPerson

faker: Faker = Faker(locale='en_US')


def generator_data():
    yield DataPerson(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        post_code=faker.postcode()

    )
