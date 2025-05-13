from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            km = float(request.form["km"])
            # Emision promedio: 0.192 kg C02 por km 
            huella = km * 0.192
            result = f"Tu huella semanal estimada es de {huella:.2f} kg de CO2 con {km}km"
        except ValueError:
            result = "Por favor, ingrese un numero valido."    

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
