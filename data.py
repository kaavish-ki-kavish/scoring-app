from scorerapp.models import ImageScore
import random
import pandas as pd

SCORERS = ['huda', 'faraz', 'mudasir', 'kainat', 'hareem']

url = 'https://raw.githubusercontent.com/kaavish-ki-kavish/dataset_urdu_chars/main/image_paths.csv'

filepath = 'https://raw.githubusercontent.com/kaavish-ki-kavish/dataset_urdu_chars/main/images/'

df = pd.read_csv(url)
print(len(df))
print(ImageScore.objects.all().count())
for (i, row) in df.iterrows():
    img_path = filepath + row['img_paths']
    num_results = ImageScore.objects.filter(image_path = img_path).count()
    if num_results == 0:
        scorer1 = random.choice(SCORERS)
        image_obj = ImageScore.objects.create(image_path = img_path, scorer = scorer1)
        scorer2 = random.choice(list(set(SCORERS) - set([scorer1])))
        image_obj = ImageScore.objects.create(image_path = img_path, scorer = scorer2)
