"""
file to run tests
"""
import unittest

import sign_in.GET_request as GET_sign_in
import sign_in.POST_request as POST_sign_in


class TestRequests(unittest.TestCase):
    def test_sign_in_request(self):
        GET_sign_in.get_request()
        GET_sign_in.GET_request_google_page()
        POST_sign_in.post_short_email()
        POST_sign_in.post_valid_data()

    def test_sign_up_request(self):
        # GET_sign_up.get_request()
        pass


if __name__ == '__main__':
    unittest.main()


#
# if __name__ == "__main__":
#     GET_sign_in.get_request()
#     GET_sign_in.GET_request_google_page()
