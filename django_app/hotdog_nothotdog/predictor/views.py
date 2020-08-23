from django.shortcuts import render
from predictor.forms import UploadFileForm
from predictor.dl_model import get_model
import cv2
import numpy as np
# Create your views here.

model = get_model()

def index(request):

    is_uploaded = False
    is_hotdog = False
    if(request.method=="POST"):
        form = UploadFileForm(request.POST, request.FILES)
        if(form.is_valid()):
            test_img = cv2.imdecode(np.fromstring(request.FILES['Image'].read(), np.uint8), cv2.IMREAD_UNCHANGED)
            test_img = np.reshape(cv2.resize(test_img, (227,227)), (1,227,227,3))
            test_img = test_img/255
            preds = model.predict(test_img)
            is_uploaded = True
            if(preds[0][0]>0.52):
                is_hotdog = True
            else:
                is_hotdog = False
    
    else:
        form = UploadFileForm()
    
    return render(request,'predictor/index.html',{'form':form,
                                                'is_uploaded':is_uploaded,
                                                'is_hotdog':is_hotdog})
