from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    val = request.form.get('value')
    try:
        val = float(val)
        result = round(val * 1.5 + 10, 2)
        return f"Predicted value: {result}"
    except:
        return "Invalid input", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)