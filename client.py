import requests

ENDPOINT = 'http://127.0.0.1:5000/'

def post_request(json):
    result = requests.post(ENDPOINT, json=json)
    if result.status_code == 200:
        print(result.json())

if __name__ == '__main__':
    example = {'school': 'GP', 'sex': 'F', 'age': 17, 'address': 'U',
    'famsize': 'GT3', 'Pstatus': 'T', 'Medu': 1, 'Fedu': 1,
    'Mjob': 'at_home', 'Fjob': 'other', 'reason': 'course', 'guardian': 'father',
    'traveltime': 1, 'studytime': 2, 'failures': 0, 'schoolsup': 'no',
    'famsup': 'yes', 'paid': 'no', 'activities': 'no', 'nursery': 'no',
    'higher': 'yes', 'internet': 'yes', 'romantic': 'no', 'famrel': 5,
    'freetime': 3, 'goout': 3, 'Dalc': 1, 'Walc': 1,
    'health': 3, 'absences': 4, 'G1': 5, 'G2': 5
    }
    # G3 is 6.
    post_request(example)