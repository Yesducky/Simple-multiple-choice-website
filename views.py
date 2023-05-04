from flask import Blueprint, render_template, request


views = Blueprint(__name__, 'views')

chartdata = {"A":0, "B":0, "C":0, "D":0}


@views.route('/')
def index():
    title = "Home"
    return render_template('index.html', title = title)

@views.route('/form', methods=["POST","GET"])
def form():
    title = "FORM"
    global chartdata
    mcinput = request.form.get("mcinput")
    if mcinput:
        chartdata[mcinput] += 1
    print(chartdata)
    return render_template('form.html', title = title, mcinput=mcinput)

@views.route('/result', methods=["GET","POST"])
def result():
    title = "RESULT"
    global chartdata
    A = chartdata["A"]
    B = chartdata["B"]
    C = chartdata["C"]
    D = chartdata["D"]
    reset = "False"
    reset = request.form.get("reset")
    if reset == "True":
        chartdata = {"A":0, "B":0, "C":0, "D":0}
        print(chartdata)
        reset = "False"
    return render_template('result.html', title = title, A=A, B=B, C=C, D=D)