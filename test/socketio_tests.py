import unittest
import app
import flask_socketio


class SocketIOTestCase(unittest.TestCase):
    # test app.py connection and disconnection
    def test_on_connect(self):
        client = app.socketio.test_client(app.app)
            # make sure to target the root
        response = client.get_received('/')
        self.assertEquals(len(received), 1)
        message = received[0]
        self.assertEquals(message,'Test Successful!')
    
    def test_disconnect(self):
        socketio = flask_socketio.SocketIO(app.app)
        client = app.socketio.test_client(app.app)
        socketio.emit('disconnect')
        response = client.get_received()
        print(response)    
    # implement a test to make sure the server is emitting correctly
    def test_connection_server_emit(self):
        client = app.socketio.test_client(app.app)
        client.emit('new message', {  
            'user_message': 'Unit Test'   
        })

        
    # base
if __name__ == '__main__':
    unittest.main()