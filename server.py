from flask import Flask, render_template
import requests

app = Flask(__name__)

blog_response = requests.get('https://api.npoint.io/c6fc8f9b4abb85408d41')
blogs = blog_response.json()

@app.route('/')
def home():
    return render_template('index.html', blogs=blogs)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:index>')
def post(index):
    for blog in blogs:
        if blog['id'] == index:
            return render_template('post.html', blog=blog)

if __name__ == '__main__':
    app.run(debug=True)