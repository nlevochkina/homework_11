import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone: str
    day: str
    month: str
    year: str
    subject: str
    picture: str
    picture_name: str
    address: str
    hobbies: str
    state: str
    city: str


user = User(
    first_name='Natalia',
    last_name='La',
    email='natalia@mail.ru',
    gender='Female',
    phone='1234567890',
    day='12',
    month='January',
    year='1990',
    subject='Computer Science',
    picture='tests/resources/sun.jpeg',
    picture_name='sun.jpeg',
    address='Moscow Street, 56, Moscow, Russia',
    hobbies='Sports',
    state='Haryana',
    city='Karnal'
)
