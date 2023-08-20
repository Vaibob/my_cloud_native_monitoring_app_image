import psutil
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    cpu_metric, mem_metric, message = get_metrics()
    return render_template("index.html", cpu_metric=cpu_metric, mem_metric=mem_metric, message=message)

def get_metrics():
    cpu_metric = psutil.cpu_percent()
    mem_metric = psutil.virtual_memory().percent
    message = "High CPU or Memory Detected, scale up!!!" if cpu_metric > 80 or mem_metric > 80 else None
    return cpu_metric, mem_metric, message

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
