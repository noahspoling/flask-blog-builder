from flask import Flask, render_template
from services.checkPackages import update_from_json_list
# <script src="https://unpkg.com/htmx.org@1.9.2" integrity="sha384-L6OqL9pRWyyFU3+/bjdSri+iIphTN/bvYyM37tICVyOJkWZLpP2vGn6VUEXgzg6h" crossorigin="anonymous"></script>

#Check JS Packages
update_from_json_list('config/jsPackages.json')

app = Flask(__name__)

'''
ROUTES
'''

@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/Posts')
def posts():
    return render_template("posts.html")

@app.route('/Projects')
def projects():
    return render_template("projects.html")
  
@app.route('/AboutMe')
def aboutMe():
    return render_template("about.html")

@app.route('/ContactMe')
def contactMe():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(debug=True)