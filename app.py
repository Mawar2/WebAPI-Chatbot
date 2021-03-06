import os, flask, flask_socketio, flask_sqlalchemy
import models, chat

from chat import Chatbot

app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)
users = 0

@app.route('/')

def index():
    return flask.render_template('index.html')

@socketio.on('connect')
def on_connect():
    query()
    print ('Someone connected!')
    global users
    users += 1

    messages = models.Message.query.all()
    chat = [m.text + '\n' for m in messages]
    # flask_socketio.emit('update', {
    #     'data': 'Got your connection!',
    #     'previous_messages': chat
    # })

@socketio.on('disconnect')
def on_disconnect():
    global users
    users -= 1
    print ('Someone disconnected!')
    
    flask_socketio.emit('update', {
        'data': 'Disconnected'
    })

def query():
    messages = models.Message.query.all()
    chat = [m.text + '\n' for m in messages]
    socketio.emit('message received', {
        'message': chat
    })

#event handler
@socketio.on('new message')
def on_new_message(data):
    print('Data Recieved: ', data)
    new_message = models.Message(data['message'])
    models.db.session.add(new_message)
    models.db.session.commit()

    #print(data['message'], 'TEST PLEASE')
    #print(data)
    if data['message'][:2] == '!!':
        
        bot_response = Chatbot()
        response = bot_response.get_response(data['message'])

        # socketio.emit('Bot Message', {
        #     'message': response
        # })
        #print(response, 'THIS IS ALSO A TEST TO SEE WHERE DATA IS')


        # chat_message = data['message'] 
        # bot_response = chatbot.Chatbot()
        # print("Chatbot message: " + chat_message)
        # response = bot_response.get_response(chat_message[2:])
    query()


if __name__ == '__main__':
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8085)),
        debug=True
    )