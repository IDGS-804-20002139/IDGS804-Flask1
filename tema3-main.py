from flask import Flask


app=Flask(__name__)

@app.route("/")
def index():
    return "!Hola mundo!"

#Pasamos un string
@app.route("/user/<string:user>")
def user(user):
    return "Hola " + user
    
#Pasamos parametros int
@app.route("/numero/<int:n>")
def numero(n):
    return "Numero: {} ".format(n)

#Pasamos mas de un parametro
@app.route("/user/<int:id>/<string:username>")
def usern(id,username):
    return "Id: {} nombre: {}".format(id,username)


#Pasamos parametros float
@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return "La suma es: {} + {}".format(n1,n2)

if __name__ == "__main__":
    app.run(debug=True,port=3000)
    