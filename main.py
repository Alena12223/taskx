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

    captain = User()
    captain.surname = "Scott"
    captain.name = "Ridley"
    captain.age = 21
    captain.position = "captain"
    captain.speciality = "research engineer"
    captain.address = "module_1"
    captain.email = "scott_chief@mars.org"
    db_sess.add(captain)

    colonist1 = User()
    colonist1.surname = "surname1"
    colonist1.name = "name1"
    colonist1.age = 20
    colonist1.position = "position1"
    colonist1.speciality = "speciality1"
    colonist1.address = "address1"
    colonist1.email = "email1"
    db_sess.add(colonist1)

    colonist2 = User()
    colonist2.surname = "surname2"
    colonist2.name = "name2"
    colonist2.age = 20
    colonist2.position = "position2"
    colonist2.speciality = "speciality2"
    colonist2.address = "address2"
    colonist2.email = "email2"
    db_sess.add(colonist2)

    colonist3 = User()
    colonist3.surname = "surname3"
    colonist3.name = "name3"
    colonist3.age = 20
    colonist3.position = "position3"
    colonist3.speciality = "speciality3"
    colonist3.address = "address3"
    colonist3.email = "email3"
    db_sess.add(colonist3)

    job = Jobs()
    job.team_leader = 1
    job.job = "deployment of residential modules 1 and 2"
    job.work_size = 15
    job.collaborators = "2, 3"
    job.start_date = datetime.datetime.now()
    job.is_finished = False
    db_sess.add(job)

    db_sess.commit()

    app.run(debug=True)

if __name__ == '__main__':
    main()
