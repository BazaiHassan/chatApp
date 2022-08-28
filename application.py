from crypt import methods
from flask import Flask, render_template
from wtform_fields import *
from models import *



# Config App
app = Flask(__name__)
app.secret_key = 'replace later'

# Config DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://syvzvfevwxgjyq:38bef637c3994b2d55bce0a3ef424d81f06ad77e31b783be9bd5a77c7ce895f5@ec2-34-225-159-178.compute-1.amazonaws.com:5432/ddrgq4ig9koesh'
db = SQLAlchemy(app)

@app.route("/",methods=['GET', 'POST'])
def index():
    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

        # Check username exists in the db
        user_object = User.query.filter_by(username = username).first()
        if user_object:
            return "The username has been taken by another one."
        
        user = User(username=username, password = password)
        db.session.add(user)
        db.session.commit()
        return "Inserted into DB"


    return render_template("index.html", form=reg_form)

if __name__ == "__main__":
    app.run(debug=True)