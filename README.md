
# Student Prediction Model

This project is an analysis on *[Student Performance Data Set](https://archive.ics.uci.edu/ml/datasets/student+performance)*. It contains two parts:
* A notebook for exploring data, preprocess and training a model.
* A simple Flask API which takes an student's record and returns predicted score for the student based on the traine model in previous stage.

### Requirements
You can install the requirements of this project by:

    pip install -r requirements
### Inference API
By running `server.py` file, an endpoint will be created on `http://127.0.0.1:5000`.
To get inference on an input you should `POST` a request to `http://127.0.0.1/:5000`, format of the request should be like this:

```
{'school':  'GP',  'sex':  'F',  'age':  17,  'address':  'U',
'famsize':  'GT3',  'Pstatus':  'T',  'Medu':  1,  'Fedu':  1,
'Mjob':  'at_home',  'Fjob':  'other',  'reason':  'course', 
'guardian':  'father', 'traveltime':  1,  'studytime':  2, 
'failures':  0,  'schoolsup':  'no', 'famsup':  'yes',  'paid':  'no',
'activities':  'no',  'nursery':  'no', 'higher':  'yes', 
'internet':'yes',  'romantic':  'no',  'famrel':  5,
'freetime':  3,  'goout':  3,  'Dalc':  1, 
'Walc':  1, 'health':  3,  'absences':  4,  'G1':  5,  'G2':  5
}
```
Which each key is a feature of the dataset. The output format is like:
`{"Score": 8}`
Which indicates the predicted score for the student.
