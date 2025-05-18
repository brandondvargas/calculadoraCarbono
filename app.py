from flask import Flask, render_template, request
from azure.cosmos import CosmosClient
import os, uuid
from datetime import datetime

app = Flask(__name__)

COSMOS_URL = os.environ["COSMOS_URL"]
COSMOS_KEY = os.environ["COSMOS_KEY"]
DATABASE_NAME = os.environ["COSMOS_DATABASE"]
CONTAINER_NAME = os.environ["COSMOS_CONTAINER"]

client = CosmosClient(COSMOS_URL, COSMOS_KEY)
db = client.create_database_if_not_exists(DATABASE_NAME)
container = db.create_container_if_not_exists(CONTAINER_NAME, partition_key="/user_id")

def guardar_en_cosmos(km, huella):
    item = {
        "id": str(uuid.uuid4()),
        "user_id": "usuario1", 
        "km": km,
        "huella": huella,
        "timestamp": datetime.utcnow().isoformat()
    }
    container.create_item(body=item)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            km = float(request.form["km"])
            huella = km * 0.192
            result = f"Tu huella semanal estimada es de {huella:.2f} kg de CO2 con {km} km"
            guardar_en_cosmos(km, huella)
        except ValueError:
            result = "Por favor, ingrese un número válido."
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
