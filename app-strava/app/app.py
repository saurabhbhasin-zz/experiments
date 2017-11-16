from flask import Flask, request, render_template
from config import client_secret
from stravalib.client import Client
import csv

client_id = "15271"
redirect_uri = "http://localhost:5000/authorized"

app = Flask(__name__)
client = Client()


@app.route('/')
def homepage():
    url = make_authorization_url()
    return render_template('index.html', url=url)


def make_authorization_url():
    authorize_url = client.authorization_url(client_id=client_id, redirect_uri=redirect_uri)
    return authorize_url


@app.route('/authorized')
def authorized():
    code = request.args.get('code')
    access_token = client.exchange_code_for_token(client_id=client_id, client_secret=client_secret, code=code)
    client.access_token = access_token
    athlete = client.get_athlete()
    fname = athlete.firstname
    m_pic = athlete.profile_medium
    writeCSV(athlete)
    return render_template('authorized.html', name=fname, pic=m_pic)
    # "Hello, {} {}. You're now authorized.".format(athlete.firstname, athlete.lastname))


def writeCSV(athlete):
    with open("athletes.csv", 'a') as f:
        writer = csv.writer(f, delimiter=",")
        row = athlete.firstname, client.access_token, athlete.email, athlete.city, athlete.state, athlete.country
        writer.writerow(row)
        f.close()


if __name__ == '__main__':
    app.run(debug=True)
