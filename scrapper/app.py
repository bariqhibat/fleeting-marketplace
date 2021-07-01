from flask import Flask, jsonify
from service import CarousellScrapper
import logging

app = Flask(__name__)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


@app.route("/products/", methods=["GET"])
def get_recent_products():
    scrapper = CarousellScrapper()

    products = scrapper.get_recent_products()

    logger.debug(products)

    return jsonify(products)

if __name__ == "__main__":
    app.run(host="localhost", port=8000)

