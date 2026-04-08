from flask import Flask, render_template, redirect
from data.jobs import Jobs
from data import db_session
from forms.user import RegisterForm
from data.users import User
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/jobs')
def jobs_():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return render_template('jobs.html', jobs=jobs)

def main():
    db_session.global_init("db/mars_explorer.db")
    db_sess = db_session.create_session()
    app.run(debug=True)

if __name__ == '__main__':
    main()
