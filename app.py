from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template('index.html')
    

@app.route("/success/<int:score>")
def success(score):
    return "<html><body><h1>The Result is passed successfully</h1></body></html>"


@app.route("/failure/<int:score>")
def fail(score):
    return "The Person has failed and the marks is " + str(score)



@app.route("/results/<int:marks>")
def results(marks):
    result = ""
    if marks >= 50:
        result = "Failed"
    else:
        result = "Passed"
    return redirect(url_for(results, score=marks))




#if __name__ == "__main__":
#    app.run(host="0.0.0.0", debug=True)
    