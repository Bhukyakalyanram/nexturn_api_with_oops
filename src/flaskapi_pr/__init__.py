# from flask import Flask, request, render_template

# app = Flask(__name__)


# @app.post("/handle_post")
# def handle_post():
#     data = request.json
#     print(data)
#     return data


# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Blueprint

user_bp = Blueprint("user_bp", __name__, url_prefix="/users")


@user_bp.get("/test")
def handle_user_test():
    return "Blueprint working"
