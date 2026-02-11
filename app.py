from flask Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Madhusudan's DevOps Portfolio</h1><p>Status: CI/CD Pipeline Active</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
