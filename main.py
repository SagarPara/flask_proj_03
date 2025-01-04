from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template('index.html')
    

@app.route("/success/<int:score>")
def success(score):
    res = ""
    if score >= 50:
        res = "PASS"
    else:
        res = "FAIL"

    return render_template('result.html', result=res)


@app.route("/fail/<int:score>")
def fail(score):
    return "The Person has failed and the marks is " + str(score)



@app.route("/results/<int:marks>")
def results(marks):
    result = ""
    if marks >= 50:
        result = "Failed"
    else:
        result = "Passed"
    return redirect(url_for(result, score=marks))

#this will be my result checker html page
@app.route("/submit", methods=["GET", "POST"])
def submit():
    total_score = 0
    if request.method == "POST":
        science = float(request.form["science"])
        maths = float(request.form["maths"])
        c = float(request.form["c"])
        data_science = float(request.form["datascience"])
        total_score = (science + maths + c + data_science)/4

    res = ""
    if total_score >= 50:
        res = "success"
    else:
        res = "fail"
    return redirect(url_for(res, score=total_score))
        



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
    