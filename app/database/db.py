from flask_sqlalchemy import SQLAlchemy

# Separated from main to prevent circular dependency

db = SQLAlchemy()
