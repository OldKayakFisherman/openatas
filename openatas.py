import os
from app import create_app, db
from flask_migrate import Migrate
from dotenv import load_dotenv
from app.models import Role, User, OperatingDivision, CFDAMappings

load_dotenv()

app = create_app(os.getenv("FLASK.CONFIG"))
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db)
