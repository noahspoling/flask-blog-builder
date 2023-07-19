from app import create_app
import flask_sqlalchemy
print(flask_sqlalchemy.__version__)

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)