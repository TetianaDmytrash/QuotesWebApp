"""
This file used in validation new users
"""
import flask
from logs.logger import logger

LEN_EMAIL = 11
LEN_NAME = 3
LEN_PASSWORD = 6


class Validation:
    """
    Class for validation when user create new account
    """
    @staticmethod
    def validation_general(user, email, first_name, last_name, login, password, confirm):
        """
        Data validation before creating a new user
        :param user:
        :param email:
        :param first_name:
        :param last_name:
        :param login:
        :param password:
        :param confirm:
        :return:
        """
        return not Validation.is_user_created(user) \
            and Validation.validation_email(email) \
            and Validation.validation_first_name(first_name) \
            and Validation.validation_last_name(last_name) \
            and Validation.validation_login(login) \
            and Validation.validation_password(password) \
            and Validation.confirm_password(password, confirm)

    @staticmethod
    def is_user_created(user):
        """
        Checking whether the mail to which they are trying to register a new user exists in the system
        :param user:
        :return:
        """
        if user:
            logger.warning("User: {} is already exists".format(user))
            flask.flash('Email already exists. Choice another email. ', category='error')
            return True
        return False

    @staticmethod
    def validation_email(email):
        """
        Checking email length
        :param email:
        :return:
        """
        if len(email) < LEN_EMAIL:
            logger.warning("Email: {} must be greater than {} characters".format(email, LEN_EMAIL))
            flask.flash('Email must be greater than {} characters.'.format(LEN_EMAIL), category='error')
            return False
        elif '@hotmail.com' not in email and \
                '@gmail.com' not in email:
            logger.warning("Email: {} must have normal domain".format(email))
            flask.flash("Email must have normal domain.", category='error')
            return False
        return True

    @staticmethod
    def validation_login(login):
        """
        Checking login length
        :param login:
        :return:
        """
        if len(login) < LEN_NAME:
            logger.warning("login: {} is so short".format(login))
            flask.flash("login is so short", category='error')
            return False
        else:
            return True

    @staticmethod
    def validation_first_name(first_name):
        """
        Checking first name length
        :param first_name:
        :return:
        """
        if len(first_name) < LEN_NAME:
            logger.warning("first Name: {} is so short".format(first_name))
            flask.flash("first Name is so short", category='error')
            return False
        else:
            return True

    @staticmethod
    def validation_last_name(last_name):
        """
        Checking last name length
        :param last_name:
        :return:
        """
        if len(last_name) < LEN_NAME:
            logger.warning("last Name: {} is so short".format(last_name))
            flask.flash("last Name is so short", category='error')
            return False
        else:
            return True

    @staticmethod
    def validation_password(password):
        """
        Checking whether the password complies with the standard
        (number of characters, presence of uppercase letters, lowercase letters, numbers)
        :param password:
        :return:
        """
        import string

        # Checking the password length (must be at least LEN_PASSWORD characters)
        if len(password) < LEN_PASSWORD:
            return False

        # Create a set containing numbers
        digits = set(string.digits)
        # Create a set containing lowercase letters
        lowercase = set(string.ascii_lowercase)
        # Create a set containing capital letters
        uppercase = set(string.ascii_uppercase)

        # Checking for at least one digit in the password
        if not set(password).intersection(digits):
            return False

        # Checking for at least one lowercase letter in the password
        if not set(password).intersection(lowercase):
            return False

        # Checking for at least one capital letter in the password
        if not set(password).intersection(uppercase):
            return False

        # If all checks pass, return True
        return True

    @staticmethod
    def confirm_password(password, confirm):
        """
        Checking Password Matches
        :param password:
        :param confirm:
        :return:
        """
        if password != confirm:
            logger.warning("password don`t match")
            flask.flash("Password don`t match.", category='error')
            return False
        else:
            return True
