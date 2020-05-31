from app import app


def create_app():
    return app.run(host='0.0.0.0', debug=True)
