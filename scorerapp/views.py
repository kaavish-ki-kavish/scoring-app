from django.http import HttpResponse
from .models import ImageScore
from django.template import loader
import random
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    user = request.user.get_username()
    print(user)
    url = request.build_absolute_uri()
    if 'post_pk' in url:
        from urllib.parse import urlparse, parse_qs
        s = url
        post_pk = parse_qs(urlparse(s).query)['post_pk'][0]
        value = parse_qs(urlparse(s).query)['value'][0]
        print(post_pk, value)
        image_score = ImageScore.objects.all().filter(pk = int(post_pk))[0]
        image_score.score = int(value)
        image_score.save()

    image_scores_lst = ImageScore.objects.all().filter(scorer=user, score = -1)
    image_score = random.choice(image_scores_lst) if image_scores_lst else None
    template = loader.get_template('scorerapp/index1.html')
    context = {
        'image': image_score,
        'scores_range':  [0, 20, 40, 60, 80, 100],
    }
    return HttpResponse(template.render(context, request))
