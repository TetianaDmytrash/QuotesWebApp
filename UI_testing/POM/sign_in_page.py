"""
sign in page for testing
"""
import requests


class SignIn:
    """
    sign in
    """

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def sign_in_valid_email_password(self, user_email, password):
        """
        sign in with valid email and password (lu@gmail.com, 1q2w3E)
        :param user_email:
        :param password:
        :return:
        """
        login_url = "{}/sign-in".format(self.base_url)
        data = {"user_email": user_email, "password": password}
        response_get = self.session.get(login_url)
        assert response_get.status_code == 200
        response_post = self.session.post(login_url, data=data)
        assert response_post.status_code == 200
        return response_post
