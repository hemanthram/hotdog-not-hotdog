# hotdog-not-hotdog

App which classifies the given image as either a hot dog or not, inspired from Jian Yang in Silicon Valley (TV Series).

## Data Collection :

All the images were taken using [ImageNet](http://image-net.org/download-API)'s API which gives you a collection of URLs of vaiours images, given the desired category (also called a synset). ImageNet is a database organized according to the WordNet hierarchy. To get the URLs for a particular category, we'll have to specify the WordNet ID (wnid) of the synset. Luckily, we have been provided the mapping between WordNet ID and synsets [here](http://image-net.org/archive/words.txt). For the *hotdog* cases, the synsets like 'hotdogs', 'chilidogs' and 'franfurters' were considered. For the *not-hotdog* cases, common categories like 'people', 'food', 'animals', 'faces' and some specific food categoris like 'pizza', 'burger' and 'rice' were considerd. Since some images obtained were unavailable, we had to find those and remove them as done in *cleanData.py*. As Jian Yang said .... "That's (a) very boring work. That's scrapping the internet for thousands of food pictures." :smile:
