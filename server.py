from flask import Flask, request, Response
from inference import Inference

app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():
    student_data = request.json
    inference = Inference(student_data)
    return {"score": f'{inference.get_prediction()}'}

if __name__ == '__main__':
    app.run(host= '127.0.0.1')