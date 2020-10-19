from flask_script import Manager 
from app import create_app, db  

app = create_app

if __name__ == "__main__":
    db.create_all()
    manager = Manager(app)
    manager.run()
