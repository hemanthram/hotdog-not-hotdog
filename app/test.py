from tensorflow.keras.models import load_model
import tensorflow.compat.v1 as tf
from tensorflow.compat.v1.losses import log_loss
tf.disable_v2_behavior()

print(tf.__version__)

img = cv2.imread("./test/"+fil)   
rimg = cv2.resize(img, (227,227))
rimgd = rimg.reshape((1,227,227,3))


model = load_model("./models/model.h5", custom_objects={'log_loss':log_loss})
