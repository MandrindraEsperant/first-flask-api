from flask import Flask # type: ignore
from routes.user_route import user_bp

app = Flask(__name__)

# register routes
app.register_blueprint(user_bp, url_prefix="/api/users")

@app.route("/")
def home():
    return {"message": "Welcome to First Flask API"}

if __name__ == "__main__":
    app.run(debug=True)