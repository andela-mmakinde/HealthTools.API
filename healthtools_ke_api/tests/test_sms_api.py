from unittest import TestCase
from healthtools_ke_api import app
from healthtools_ke_api.views.sms_handler import build_query_response, send_sms


class TestSmsApi(TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_sms_requires_message_and_number(self):
        response = self.client.get("/sms")
        message = "The url parameters 'message' and 'phoneNumber' are required."
        self.assertEqual(message, response.data)

    def test_query_response(self):
        response = build_query_response('nurse mary')
        self.assertTrue(len(response[0]) > 0)

    def test_send_sms(self):
        message = build_query_response('nurse mary')
        response = self.client.get("/sms", query_string={"phoneNumber": "+254726075080", "message": message[0]})
        self.assertEqual(200, response.status_code)
