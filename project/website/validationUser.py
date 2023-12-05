from flask import flash
from project.logger import logger

LEN_EMAIL = 11
LEN_NAME = 3
LEN_PASSWORD = 6


class Validation:

    @staticmethod
    def validation_general(user, email, first_name, last_name, login, password, confirm):
        return not Validation.is_user_created(user) \
            and Validation.validation_email(email) \
            and Validation.validation_first_name(first_name) \
            and Validation.validation_last_name(last_name) \
            and Validation.validation_login(login) \
            and Validation.validation_password(password) \
            and Validation.confirm_password(password, confirm)

    @staticmethod
    def is_user_created(user):
        if user:
            logger.warning(f"User: {user} is already exists")
            flash('Email already exists. Choice another email. ', category='error')
            return True
        return False

    @staticmethod
    def validation_email(email):
        if len(email) < LEN_EMAIL:
            logger.warning(f"Email: {email} must be greater than {LEN_EMAIL} characters")
            flash(f'Email must be greater than {LEN_EMAIL} characters.', category='error')
            return False
        elif '@hotmail.com' not in email and \
                '@gmail.com' not in email:
            logger.warning(f"Email: {email} must have normal domain")
            flash('Email must have normal domain.', category='error')
            return False
        return True

    @staticmethod
    def validation_login(login):
        if len(login) < LEN_NAME:
            logger.warning(f"login: {login} is so short")
            flash(f"login is so short", category='error')
            return False
        else:
            return True

    @staticmethod
    def validation_first_name(first_name):
        if len(first_name) < LEN_NAME:
            logger.warning(f"first Name: {first_name} is so short")
            flash(f"first Name is so short", category='error')
            return False
        else:
            return True

    @staticmethod
    def validation_last_name(last_name):
        if len(last_name) < LEN_NAME:
            logger.warning(f"last Name: {last_name} is so short")
            flash(f"last Name is so short", category='error')
            return False
        else:
            return True

    @staticmethod
    def validation_password(password):
        import string

        # Проверка длины пароля (должна быть не менее LEN_PASSWORD символов)
        if len(password) < LEN_PASSWORD:
            return False

        # Создаем множество, содержащее цифры
        digits = set(string.digits)
        # Создаем множество, содержащее строчные буквы
        lowercase = set(string.ascii_lowercase)
        # Создаем множество, содержащее заглавные буквы
        uppercase = set(string.ascii_uppercase)

        # Проверка наличия хотя бы одной цифры в пароле
        if not set(password).intersection(digits):
            return False

        # Проверка наличия хотя бы одной строчной буквы в пароле
        if not set(password).intersection(lowercase):
            return False

        # Проверка наличия хотя бы одной заглавной буквы в пароле
        if not set(password).intersection(uppercase):
            return False

        # Если все проверки пройдены, возвращаем True
        return True

    @staticmethod
    def confirm_password(password, confirm):
        if password != confirm:
            logger.warning(f'password don`t match')
            flash('Password don`t match.', category='error')
            return False
        else:
            return True
