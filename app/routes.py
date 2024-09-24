

from flask import (
	jsonify,
	request
)





def create_routes(app) -> None:

	@app.route("/train", methods=["GET"])
	def train():
		return jsonify({"message":"this is the message from the endpoint /train"})
