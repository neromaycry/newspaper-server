from flask import Flask
# from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

PORT = 8000

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:/VScodeProjects/newspaper-server/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# api = Api(app)
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}

# api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    db.session.remove()
    db.create_all()
    app.run(debug=True, port=PORT, use_reloader=False)
