from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
CORS(app)


app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL','postgresql://sapcountdown_user:r8ViRzCTA5c61xUsB2Q5YGPo7H0P7SzF@dpg-d0shpec9c44c73f6euq0-a.oregon-postgres.render.com/sapcountdown')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app) 



class Frase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100))
    description = db.Column(db.Text)

    def to_dict(self):
        return {"id": self.id, "author": self.author, "description": self.description}

@app.route("/frases", methods=["GET"])
def get_frases():
    frases = Frase.query.all()
    return jsonify([q.to_dict() for q in frases])

"""@app.route("/quotes", methods=["POST"])
def create_quote():
    data = request.json
    new_quote = Quote(author=data["author"], description=data["description"])
    db.session.add(new_quote)
    db.session.commit()
    return jsonify(new_quote.to_dict()), 201

@app.route("/quotes/<int:quote_id>", methods=["PUT"])
def update_quote(quote_id):
    data = request.json
    quote = Quote.query.get(quote_id)
    if quote:
        quote.author = data["author"]
        quote.description = data["description"]
        db.session.commit()
        return jsonify(quote.to_dict())
    return jsonify({"error": "Not found"}), 404

@app.route("/quotes/<int:quote_id>", methods=["DELETE"])
def delete_quote(quote_id):
    quote = Quote.query.get(quote_id)
    if quote:
        db.session.delete(quote)
        db.session.commit()
        return jsonify({"message": "Deleted"})
    return jsonify({"error": "Not found"}), 404"""


if __name__ == "__main__":
    app.run(debug=True)


