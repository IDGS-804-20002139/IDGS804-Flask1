from flask import Flask, render_template
from flask import request

app = Flask(__name__)


@app.route("/")
def Formulario():
    return render_template("formularioSignos.html")


@app.route("/pag2", methods=["GET", "POST"])
def Pag2():
    action = request.form.get("boton")

    if action == "limpiar":
        return render_template("formularioSignos.html")
    else:
        nombre = request.form.get("txtNombre")
        aPaterno = request.form.get("txtAPaterno")
        aMaterno = request.form.get("txtAMaterno")
        dia  = int(request.form.get("txtDia"))
        mes  = int(request.form.get("txtMes"))
        anio = int(request.form.get("txtAnio"))
        sexo = request.form.get("btnSexo")
        btnRes1 = request.form.get("btnPreg1")
        btnRes2 = request.form.get("btnPreg2")
        btnRes3 = request.form.get("btnPreg3")
        btnRes4 = request.form.get("btnPreg4")
        btnRes5 = request.form.get("btnPreg5")
        signo = ''
        edad = ''
        cali= ''
        img=''

        if mes > 2:
            edad = 2022 - anio
        else:
            edad = 2023 - anio

        if int(anio) == 1936 or int(anio) == 1948 or int(anio) == 1960 or int(anio) == 1972 or int(anio) == 1984 or int(anio) == 1996 or int(anio) == 2008 or int(anio) == 2020:
            signo = 'Rata'
            img = 'href = ../static/bootstrap/img/rata.png'
        elif int(anio) == 1937 or int(anio) == 1949 or int(anio) == 1961 or int(anio) == 1973 or int(anio) == 1985 or int(anio) == 1997 or int(anio) == 2009 or int(anio) == 2021:
            signo = 'Buey'
            img = '../static/bootstrap/img/buey.png'
        elif int(anio) == 1938 or int(anio) == 1950 or int(anio) == 1962 or int(anio) == 1974 or int(anio) == 1986 or int(anio) == 1998 or int(anio) == 2010 or int(anio) == 2022:
            signo = 'Tigre'
            img = '../static/bootstrap/img/tigre.png'
        elif int(anio) == 1939 or int(anio) == 1951 or int(anio) == 1963 or int(anio) == 1975 or int(anio) == 1987 or int(anio) == 1999 or int(anio) == 2011 or int(anio) == 2023:
            signo = 'Conejo'
            img = '../static/bootstrap/img/conejo.png'
        elif int(anio) == 1940 or int(anio) == 1952 or int(anio) == 1964 or int(anio) == 1976 or int(anio) == 1988 or int(anio) == 2000 or int(anio) == 2012:
            signo = 'Dragón'
            img = '../static/bootstrap/img/dragon.png'
        elif int(anio) == 1941 or int(anio) == 1953 or int(anio) == 1965 or int(anio) == 1977 or int(anio) == 1989 or int(anio) == 2001 or int(anio) == 2013:
            signo = 'Serpiente'
            img = '../static/bootstrap/img/serpiente.png'
        elif int(anio) == 1942 or int(anio) == 1954 or int(anio) == 1966 or int(anio) == 1978 or int(anio) == 1990 or int(anio) == 2002 or int(anio) == 2014:
            signo = 'Caballo'
            img = '../static/bootstrap/img/caballo.png'
        elif int(anio) == 1943 or int(anio) == 1955 or int(anio) == 1967 or int(anio) == 1979 or int(anio) == 1991 or int(anio) == 2003 or int(anio) == 2015:
            signo = 'Cabra'
            img = '../static/bootstrap/img/cabra.png'
        elif int(anio) == 1944 or int(anio) == 1956 or int(anio) == 1968 or int(anio) == 1980 or int(anio) == 1992 or int(anio) == 2004 or int(anio) == 2016:
            signo = 'Mono'
            img = '../static/bootstrap/img/mono.png'
        elif int(anio) == 1945 or int(anio) == 1957 or int(anio) == 1969 or int(anio) == 1981 or int(anio) == 1993 or int(anio) == 2005 or int(anio) == 2017:
            signo = 'Gallo'
            img = '../static/bootstrap/img/gallo.png'
        elif int(anio) == 1946 or int(anio) == 1958 or int(anio) == 1970 or int(anio) == 1982 or int(anio) == 1994 or int(anio) == 2006 or int(anio) == 2018:
            signo = 'Perro'
            img = '../static/bootstrap/img/perro.png'
        elif int(anio) == 1947 or int(anio) == 1959 or int(anio) == 1971 or int(anio) == 1983 or int(anio) == 1995 or int(anio) == 2007 or int(anio) == 2019:
            signo = 'Cerdo'
            img = '../static/bootstrap/img/cerdo.png'
        else:
            signo = 'Desconocido'


        if btnRes1 == '1':
            r1 = 1
        else:
            r1= 0
        if btnRes2 == '2':
            r2 = 1
        else:
            r2= 0   
        if btnRes3 == '3':
            r3 = 1
        else:
            r3= 0
        if btnRes4 == '2':
            r4 = 1
        else:
            r4 = 0
        if btnRes5 == '3':
            r5 = 1
        else:
            r5= 0
        cali= r1 + r2 + r3 + r4 +r5

        return render_template("resultadosExamen.html", nombre=nombre, signo=signo, edad=edad, cali=cali, img=img)


@app.route("/resultado", methods=["POST"])
def Resultado():
    return render_template("resultadosExamen.html")


if __name__ == "__main__":
    app.run(debug=True, port=3000)
