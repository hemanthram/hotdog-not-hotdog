from tensorflow.keras.models import load_model
import tensorflow.compat.v1 as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import ResNet50
from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from pathlib import Path
import uvicorn, aiohttp, asyncio
import cv2
import sys, numpy as np
from tensorflow.compat.v1.losses import log_loss
import time
tf.compat.v1.disable_v2_behavior()

path = Path(__file__).parent
model_file_name = 'model'
classes = ['hotdog, nothotdog']

app = Starlette()
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_headers=['X-Requested-With', 'Content-Type'])
app.mount('/static', StaticFiles(directory='./static'))

MODEL_PATH = path/'models'/f'{model_file_name}.h5'

async def download_file(url, dest):
    if dest.exists(): return
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.read()
            with open(dest, 'wb') as f: f.write(data)

async def setup_model():
    #UNCOMMENT HERE FOR CUSTOM TRAINED MODEL
    # await download_file(model_file_url, MODEL_PATH)
    model = load_model(MODEL_PATH, custom_objects={'log_loss':log_loss}) # Load your Custom trained model
    model._make_predict_function()
    # model = ResNet50(weights='imagenet') # COMMENT, IF you have Custom trained model
    return model

# Asynchronous Steps
loop = asyncio.get_event_loop()
tasks = [asyncio.ensure_future(setup_model())]
model = loop.run_until_complete(asyncio.gather(*tasks))[0]
loop.close()

@app.route("/upload", methods=["POST"])
async def upload(request):
    data = await request.form()
    filename = 'img_'+time.strftime("%Y%m%d-%H%M%S")+'.jpg'
    img_bytes = await (data["file"].read())
    IMG_FILE_SRC = './tmp/'+filename
    with open(IMG_FILE_SRC, 'wb') as f: f.write(img_bytes)
    return model_predict(IMG_FILE_SRC, model)

def model_predict(img_path, model):
    result = []; 
    img = cv2.imread(img_path)
    img = cv2.resize(img, (227,227))
    img = np.reshape(img, (1,227,227,3))
    img = img/255
    # result = model.predict(img)
    answer = "Hotdog" if model.predict(img)[0][0]>0.52 else "Not Hotdog"
    result_html1 = path/'static'/'result1.html'
    result_html2 = path/'static'/'result2.html'
    if(answer == "Hotdog"):
        result = "<p class=\"result-text\">"+answer+"</p><img src=\"static/images/right.jpg\" width=\"40px\" height=\"40px\" >"
    else:
        result = "<p class=\"result-text\">"+answer+"</p><img src=\"static/images/wrong.jpg\" width=\"40px\" height=\"40px\" >"
    result_html = str(result_html1.open().read() +str(result) + result_html2.open().read())
    return HTMLResponse(result_html)

@app.route("/")
def form(request):
    index_html = path/'static'/'index.html'
    return HTMLResponse(index_html.open().read())

if __name__ == "__main__":
    if "serve" in sys.argv: uvicorn.run(app, host="0.0.0.0", port=8080)
