from flask import Flask
# noinspection PyUnresolvedReferences
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")

    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user.hashed_password = "cap"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.surname = "Stepanova"
    user.name = "Darya"
    user.age = 16
    user.position = "the second captain"
    user.speciality = "main system programmer"
    user.address = "module_1"
    user.email = "darya_ste@mars.org"
    user.hashed_password = "dadada"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.surname = "Ononas"
    user.name = "Ray"
    user.age = 19
    user.position = "captain"
    user.speciality = "gravity engineer"
    user.address = "module_4"
    user.email = "ray_on@mars.org"
    user.hashed_password = "ray"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.surname = "Lightwood"
    user.name = "Jeffrey"
    user.age = 29
    user.position = "main soldier"
    user.speciality = "weapon checker"
    user.address = "module_5"
    user.email = "jeffiewood@mars.org"
    user.hashed_password = "jeewoo"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    # app.run()


if __name__ == '__main__':
    main()