# hotdog-not-hotdog

App which classifies the given image as either a hot dog or not, inspired from Jian Yang in Silicon Valley (TV Series).  
  
<img src="./git-images/jian.jpeg" width="60%">  

## Data Collection :

All the images were taken using [ImageNet](http://image-net.org/download-API)'s API which gives you a collection of URLs of vaiours images, given the desired category (also called a synset). ImageNet is a database organized according to the WordNet hierarchy. To get the URLs for a particular category, we'll have to specify the WordNet ID (wnid) of the synset. Luckily, we have been provided the mapping between WordNet ID and synsets [here](http://image-net.org/archive/words.txt). For the *hotdog* cases, the synsets like 'hotdogs', 'chilidogs' and 'franfurters' were considered. For the *not-hotdog* cases, common categories like 'people', 'food', 'animals', 'faces' and some specific food categoris like 'pizza', 'burger' and 'rice' were considerd. Since some images obtained were unavailable, we had to find those and remove them as done in *cleanData.py*. We finally have around 1600 images of *hotdog* and 1800 images of *nothotdog*.  
  
PS : Jian Yang was absoltely right about data scrapping .... "That's (a) very boring work. That's scrapping the internet for thousands of food pictures." :smile:

## Data Preprocessing :
Some images which contained people in them eating hotdogs were randomly removed manually. All the images are resized to *128x128* and the pixel values are normalized by division with *255*, to make sure that their values are between 0 and 1.
