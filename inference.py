import tensorflow as tf
import numpy as np

def rmse_loss(y_true, y_pred):
        return tf.sqrt(tf.reduce_mean(tf.math.squared_difference(tf.cast(y_true, tf.float32), y_pred)))


class Inference():
    def create_model(self, model_path='best_model'):
        return tf.keras.models.load_model(model_path, custom_objects={'rmse_loss': rmse_loss})


    def lookup_table(self, key, value):
        table = {
        'school' : {'GP':0, 'MS':1},
        'sex' : {'F':0, 'M':1},
        'address' : {'U':0, 'R':1},
        'famsize' : {'GT3':0, 'LE3':1},
        'Pstatus': {'A':0, 'T':1},
        'Mjob' : {'at_home':0, 'health':1, 'other':2, 'services':3, 'teacher':4},
        'Fjob' : {'teacher':0, 'other':1, 'services':2, 'health':3, 'at_home':4},
        'reason' : {'course':0, 'other':1, 'home':2, 'reputation':3},
        'guardian' : {'mother':0, 'father':1, 'other':2},
        'schoolsup' : {'yes':0, 'no':1},
        'famsup' : {'no':0, 'yes':1},
        'paid' : {'no':0, 'yes':1},
        'activities' : {'no':0, 'yes':1},
        'nursery'	 : {'yes':0, 'no':1},
        'higher' : {'yes':0, 'no':1},
        'internet' : {'no':0, 'yes':1},
        'romantic' : {'no':0, 'yes':1},
        }
        return table[key][value]


    def convert_categorical(self, data):
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = self.lookup_table(key, value)
        return data


    def __init__(self, student_data):
        self.model = self.create_model()
        self.student_data = self.convert_categorical(student_data)
        self.student_data = np.array(list(self.student_data.values()))


    def get_prediction(self):
        return self.model.predict(self.student_data.reshape(-1,32))[0][0]