import requests
import shutil
import os

data = requests.get("http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152")
print("Urls obtained")
print(len(data.text.split('\n')))
urls = (data.text.split('\n'))

path = 'nothotdog/people'
success = 0; fail = 0
for image_url in urls:
    # Open the url image, set stream to True, this will return the stream content.
    try:
        r = requests.get(image_url, stream = True)
    except:
        fail += 1
        print("Connection Timed Out")
        continue

    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True
        success += 1
        filename = str(success)+'.jpg'
        # Open a local file with wb ( write binary ) permission.
        with open('./'+path+'/'+filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
            
        # print('Image sucessfully Downloaded: ',filename)
    else:
        fail += 1
        # print('Image Couldn\'t be retreived')
    os.system('cls')
    print(success, fail)