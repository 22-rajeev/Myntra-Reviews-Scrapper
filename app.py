from flask import Flask, render_template, request ,send_file
from flask_cors import cross_origin
from src.scrapper.scrape import ScrapeReviews

app = Flask(__name__)
@app.route("/", methods=["GET"])
@cross_origin()
def index():
    return render_template("index.html")


@app.route("/review", methods=["POST", "GET"])
@cross_origin()
def review():
    if request.method == "POST":
        query = request.form.get("content")
        no_of_products = request.form.get("prod_no", type=int)

        try:
            scrape = ScrapeReviews(query, no_of_products)
            columns, data = scrape.get_review_data()
            return render_template("results.html", titles=columns, rows=data, error=None)
        except Exception as e:
            # Pass a clean error string to the template
            return render_template(
                "results.html", titles=[], rows=[], error=str(e)
            )

    return render_template("results.html", titles=[], rows=[], error=None)


@app.route("/download", methods=["GET"])
def download():
    try:
        return send_file("data.csv", as_attachment=True, download_name="reviews.csv")
    except Exception as e:
        return str(e), 500
    
if __name__ == "__main__":
    app.run(debug=True)