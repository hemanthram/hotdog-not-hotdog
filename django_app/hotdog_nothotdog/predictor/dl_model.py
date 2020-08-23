import os
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.compat.v1.losses import log_loss

def get_model():
    DIR = os.path.join(os.getcwd(),"dl_model")
    DIR = os.path.join(DIR,"my_model_binClass")
    model = load_model(DIR, custom_objects={'log_loss':log_loss})

    return model