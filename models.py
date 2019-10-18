import os, flask, flask_socketio, flask_sqlalchemy, psycopg2, app, chat

#app = flask.Flask(__name__)
#socketio = flask_socketio.SocketIO(app)

#app.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://leaky:admin@localhost/postgres' 
app.app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
db = flask_sqlalchemy.SQLAlchemy(app.app)
# creates a database objectç


class Message(db.Model): 
    #__tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    
    def __init__(self, text):
        self.text = text
        
    def __repr__(self):
        return '<Message text: %s>' % self.text 