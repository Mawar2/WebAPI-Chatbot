import app, unittest, flask_testing, requests

class ServerIntegrationTestCase(
    flask_testing.LiveServerTestCase
):
    def create_app(self):
        return app.app

    def test_server_send_message(self):
        response = requests.get(self.get_server_url())
        
        print(response.text)
        self.assertEquals(response.text, 'Server Message Sent.')

if __name__ == '__main__':
    unittest.main()