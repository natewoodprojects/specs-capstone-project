from flask import Flask, render_template

app = Flask(__name__)

app.secret_key = "39p4uhgau-ewvhoruawe4-9gfhap34u9bp-upsdzv923"

@app.route('/')
def index():
    """index Page"""

    return render_template('/index.html')

@app.route('/homepage')
def home():

    return render_template('/homepage.html')

if __name__ == "__main__":
    app.run()