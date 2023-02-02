from flask import Flask, render_template
from flask import request
import math

app=Flask(__name__)

@app.route("/dispunt")
def dispunt():
    return render_template("dispunt.html")


@app.route("/resultado2",methods=["POST"])
def resultado1():
    x1= float(request.form.get("x1"))
    x2= float(request.form.get("x2"))
    y1= float(request.form.get("y1"))
    y2= float(request.form.get("y2"))
    res = math.sqrt((x2-x1)**2 + (y2-y1)**2) 
    print (res)
    return render_template("resultado2.html",x1=x1,x2=x2,y1=y1,y2=y2,res=res)


if __name__ == "__main__":
    app.run(debug=True,port=3000)