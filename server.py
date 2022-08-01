from flask import Flask, render_template
from forms import SubmitObject

app = Flask(__name__)

app.secret_key = "39p4uhgau-ewvhoruawe4-9gfhap34u9bp-upsdzv923"

@app.route('/', methods=['POST'])
def index():
    """index Page"""

    return render_template('/login.html')

@app.route('/register', methods=['POST'])
def home():    
    return render_template('/register.html')

@app.route('/home', methods=['GET', 'POST'])
def home():    
    return render_template('/home.html')

@app.route('/create', methods=['POST'])
def home():    
    return render_template('/create.html')

@app.route('/edit', methods=['POST'])
def home():    
    return render_template('/edit.html')



if __name__ == "__main__":
    app.run()