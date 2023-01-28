# Agregar radio buttons


from flask import Flask
from flask import request


app=Flask(__name__)

# Con esto podemos indecar el tipo de metodos que vamos a utilizar
@app.route("/operacion",methods=["GET","POST"])
def operacion():
    if request.method == "POST":
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")
        if request.form.get('button') == '1':
            return "<h1> La suma es: {} </h1>".format(str(int(num1)+int(num2)))
        elif request.form.get('button') == '2':
            return "<h1> La resta es: {} </h1>".format(str(int(num1)-int(num2)))
        elif request.form.get('button') == '3':
            return "<h1> La multiplicacion es: {} </h1>".format(str(int(num1)*int(num2)))
        elif request.form.get('button') == '4':
            return "<h1> La division es: {} </h1>".format(str(int(num1)/int(num2)))
    else:
        return'''
        <form action = "/operacion" method="POST">
        <label>Eligue la operacion </label><br>
        <label>Suma </label>
        <input type="radio" name="button" value="1"><br><br>
        <label>Resta </label>
        <input type="radio" name="button" value="2"><br><br>
        <label>Multiplicacion </label>
        <input type="radio" name="button" value="3"><br><br>
        <label>Division </label>
        <input type="radio" name="button" value="4"><br><br>
        <label>N1: </label>
        <input type="text" name="num1"/><br><br>
        <label>N2: </label>
        <input type="text" name="num2"/><br><br>
        <input type="submit" name="Calcular"/>
        </form>
        '''

if __name__ == "__main__":
    app.run(debug=True,port=3000)