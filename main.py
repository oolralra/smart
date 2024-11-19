from api import PetAPI
from parser import parser_json

from flask import (
    Flask,
    jsonify,
    request,
    render_template,
    url_for,
)
from flask_restful import Api, Resource
from flask_cors import CORS

pet_api = PetAPI()
app = Flask(__name__)
cors = CORS(app, supports_credentials=True, origins="http://127.0.0.1:8080")
api = Api(app)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/result")
def result_page():
    keyword = request.args.get("keyword")
    category = request.args.get("category")

    kwargs = {"keyword": keyword}
    if category:
        kwargs["category"] = category

    response = pet_api.get_response(**kwargs)
    parsed_json = parser_json(response)

    if category == "":
        category = "전체"

    return render_template(
        "result.html",
        items=parsed_json,
        keyword=keyword,
        category=category,
    )


@app.route("/search-home", methods=["GET"])
def search():
    return render_template("search.html")


class SearchPlace(Resource):
    def post(self):
        keyword = request.json.get("keyword")

        if (keyword is None) or (keyword == ""):
            return jsonify({"error": "검색어를 입력해주세요."})

        return jsonify({"redirect": url_for("result_page")})


api.add_resource(SearchPlace, "/search")

if __name__ == "__main__":
    app.run("0.0.0.0", port=8080, debug=True)
