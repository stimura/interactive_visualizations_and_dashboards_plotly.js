from data_wrangling import *


from flask import Flask, jsonify, render_template
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/names")
def names():

    # Store results into a dictionary
    forecast = get_samples()
    
    return jsonify(forecast)
    # Redirect back to home page
    # return redirect("http://localhost:5000/", code=302)


@app.route("/pie")
def make_pie_chart():

    data = [{
        "labels": get_otu_pie_labels(),
        "values": get_otu_pie_values(),
        "type": "pie"}]

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
