from flask_app import app
from flask_app.controllers import users
from flask_app.controllers import foods
from flask_app.controllers import activities
from flask_app.controllers import user_foods
from flask_app.controllers import user_activities

if __name__=="__main__":
    app.run(debug=True)