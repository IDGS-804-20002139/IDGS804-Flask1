from flask import Flask, render_template
from flask import request

app = Flask(__name__)


@app.route("/")
def PICine():
    return render_template("pantallaCinepolis.html")


@app.route("/PRCine", methods=["GET", "POST"])
def PRCine():
    nombre = request.form.get("txtNombre")
    cCom = int(request.form.get("txtCanCom"))
    btnTar = request.form.get("btnTar")
    CanBoleta = int(request.form.get("txtCanBol"))
    presioBoleto = 12*CanBoleta
    canBolxPer = 7*cCom
    aviso = ""

    if CanBoleta > canBolxPer:
        aviso = "Por persona se puede comprar un maximo de 7 boletos."
        ValPagoTotal = ""
    else:
        if int(CanBoleta) > 5:
            if btnTar == '1':
                ValPago = presioBoleto - (presioBoleto * 0.15)
                ValPagoTotal = ValPago - (ValPago*0.10)
                aviso = "Cada boleta tiene un costo de $12.00,\n además se asigno un descuento del 15% por comprar más de 5 boletas, \n y un descuento del 10% por usar la tarjeta CINECO"
            else:
                ValPagoTotal = presioBoleto - (presioBoleto*0.15)
                aviso = "Cada boleta tiene un costo de $12.00,\n además se asigno un descuento del 15% por comprar más de 5 boletas."
        elif int(CanBoleta) == 3 or int(CanBoleta) == 4 or int(CanBoleta) == 5:
            if btnTar == "1":
                ValPago = presioBoleto-(presioBoleto*0.10)
                ValPagoTotal = ValPago - (ValPago*0.10)
                aviso = "Cada boleta tiene un costo de $12.00,\n además se asigno un descuento del 10% por comprar entre 3 y 5 boletas, \n y un descuento del 10% por usar la tarjeta CINECO"
            else:
                ValPagoTotal = presioBoleto-(presioBoleto*0.10)
                aviso = "Cada boleta tiene un costo de $12.00,\n además se asigno un descuento del 10% por comprar entre 3 y 5 boletas."
        elif int(CanBoleta) <= 2:
            if btnTar == "1":
                ValPagoTotal = presioBoleto - (presioBoleto*0.10)
                aviso = "Cada boleta tiene un costo de $12.00,\n además se asigno un descuento del 10% por usar la tarjeta CINECO"
            else:
                ValPagoTotal = presioBoleto
                aviso = "Cada boleta tiene un costo de $12.00"

    return render_template("respuestaCine1.html", nombre=nombre,  ValPagoTotal=ValPagoTotal, aviso=aviso, CanBoleta=CanBoleta)


@app.route("/Salir", methods=["POST"])
def Salir():
    return render_template("respuestaCine2.html")


if __name__ == "__main__":
    app.run(debug=True, port=3000)
