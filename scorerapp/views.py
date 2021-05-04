from django.http import HttpResponse
from .models import ImageScore
from django.template import loader
import random
from django.contrib.auth.decorators import login_required

SPLITTER = 'char_'
@login_required
def index(request):
    user = request.user.get_username()
    print(user)
    url = request.build_absolute_uri()
    scored = False
    if 'post_pk' in url:
        from urllib.parse import urlparse, parse_qs
        s = url
        post_pk = parse_qs(urlparse(s).query)['post_pk'][0]
        value = parse_qs(urlparse(s).query)['value'][0]
        print(post_pk, value)
        image_score = ImageScore.objects.all().filter(pk = int(post_pk))[0]
        image_score.score = int(value)
        image_score.save()
        scored = True
    if scored: 
        for i in range(3):
            print('SCOREDDDDDDDDDDDDDDDDDDDDDDDDDDDDD')
#     if user == 'huda':
#         print('hudaaaaaaaaaaaa')
#         image_scores_lst = ImageScore.objects.all().filter(id__gt=9000, scorer=user, score = -1)
#         print(image_scores_lst.count())
#         image_score = random.choice(image_scores_lst) if image_scores_lst else None
#     else:
    image_scores_lst = ImageScore.objects.all().filter(scorer=user, score = -1)
    image_score = random.choice(image_scores_lst) if image_scores_lst else None
    img_url = ''

    if image_score:
        img_url = image_score.image_path
        img_url = img_url.split(SPLITTER)[-1]
        if 'alif_mad_aa' in img_url:
            img_url = ' '.join(img_url.split('_')[:3])
        if 'choti_yaa' in img_url or 'bari_yaa' in img_url:
            img_url = ' '.join(img_url.split('_')[:2])
        else:
            img_url = img_url.split('_')[0]
        print(img_url, image_score.image_path)

    template = loader.get_template('scorerapp/index1.html')
    context = {
        'image': image_score,
        'scores_range':  [0, 20, 40, 60, 80, 100],
        'image_name': img_url
    }
    return HttpResponse(template.render(context, request))
