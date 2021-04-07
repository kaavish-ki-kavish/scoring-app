from scorerapp.models import ImageScore
import random


SCORERS = ['huda', 'faraz', 'mudasir', 'kainat', 'hareem']

url = 'https://raw.githubusercontent.com/kaavish-ki-kavish/aangan-filesystem/main/aagan-urdu-filesystem/'
filepath = 'list_cat.txt'
with open('list_cat.txt', 'r') as f:
    cats = f.read().split('\n')

for cat in cats:
    if cat:
        cat = url + cat + '/' + cat + '-01.png'
        scorer = random.choice(SCORERS)
        image_obj = ImageScore.objects.create(image_path = cat, scorer = scorer)
        scorer = random.choice(SCORERS)
        image_obj = ImageScore.objects.create(image_path = cat, scorer = scorer)
