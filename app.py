from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>CI/CD Mastery Achieved!</h1><p>Build #4 is 100% Automated.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
