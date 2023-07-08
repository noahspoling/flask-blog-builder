from flask import Flask, render_template

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