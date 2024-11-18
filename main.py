from flask import Flask, render_template, request
import requests


app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    if request.method == 'POST':
        response = get_quote()
        quote = {
            'author': response['originator']['name'],
            'quote': response['content']
        }
        render_template('index.html',**quote)
    render_template('index.html')


def get_quote():
    url = "https://quotes15.p.rapidapi.com/quotes/random/"
    querystring = {"language_code": "ru"}
    headers = {
        "x-rapidapi-key": "687a5dd305mshdf51e853bac2d89p1827fajsnaaeb41738b48",
        "x-rapidapi-host": "quotes15.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()

if __name__ == '__main__':
    app.run(debug=True)