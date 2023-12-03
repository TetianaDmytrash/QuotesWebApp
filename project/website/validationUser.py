from flask import flash
from logger import logger

LEN_EMAIL = 11
LEN_NAME = 3
LEN_PASSWORD = 6

class Validation:

	@staticmethod
	def validationGeneral(user, email, firstName, lastName, login, password, confirm):
		return not Validation.isUserCreated(user) \
			and Validation.validationEmail(email) \
			and Validation.validationFirstName(firstName) \
			and Validation.validationLastName(lastName) \
			and Validation.validationLogin(login) \
			and Validation.validationPassword(password) \
			and Validation.confirmPassword(password, confirm)

	@staticmethod
	def isUserCreated(user):
		if user:
			logger.warning(f"User: {user} is already exists")
			flash('Email already exists. Choice another email. ', category='error')
			return True
		return False

	@staticmethod
	def validationEmail(email):
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
	def validationLogin(login):
		if len(login) < LEN_NAME:
			logger.warning(f"login: {login} is so short")
			flash(f"login is so short", category='error')
			return False
		else:
			return True

	@staticmethod
	def validationFirstName(firstName):
		if len(firstName) < LEN_NAME:
			logger.warning(f"first Name: {firstName} is so short")
			flash(f"first Name is so short", category='error')
			return False
		else:
			return True

	@staticmethod
	def validationLastName(lastName):
		if len(lastName) < LEN_NAME:
			logger.warning(f"last Name: {lastName} is so short")
			flash(f"last Name is so short", category='error')
			return False
		else:
			return True

	@staticmethod
	def validationPassword(password):
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
	def confirmPassword(password, confirm):
		if password != confirm:
			logger.warning(f'password don`t match')
			flash('Password don`t match.', category='error')
			return False
		else:
			return True