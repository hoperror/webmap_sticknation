from django.shortcuts import render, get_object_or_404, redirect
from .models import Stick, Comment, MapLayer
from .forms import CommentForm
from django.http import JsonResponse
from django.db.models import Min, Max
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

def post_list(request):
    posts = Stick.objects.filter(status='Published').order_by('-publish')
    return render(request, 'MyBlog/post_list.html', {'posts': posts})

def post_detail(request, id, slug):
    post = get_object_or_404(Stick, id=id, slug=slug, status='Published')
    comments = post.comments.filter(active=True)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect(post.get_absolute_url())
    else:
        comment_form = CommentForm()
    return render(request, 'MyBlog/post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})

def explorer(request):
    ranges = Stick.objects.filter(status='Published').aggregate(min_year=Min('publish__year'), max_year=Max('publish__year'))
    layers = MapLayer.objects.all()
    return render(request, 'MyBlog/explorer.html', {'min_year': ranges['min_year'] or 2020, 'max_year': ranges['max_year'] or 2026, 'layers': layers})

def user_profile(request, username):
    user_expert = get_object_or_404(User, username=username)
    # On récupère tous les sticks de cet utilisateur
    user_sticks = Stick.objects.filter(author=user_expert, status='Published').order_by('-publish')
    
    return render(request, 'MyBlog/profile.html', {
        'user_expert': user_expert,
        'sticks': user_sticks
    })

def stick_api(request):
    sticks = Stick.objects.filter(status='Published')
    year = request.GET.get('year')
    if year:
        if request.GET.get('cumulative') == 'true':
            sticks = sticks.filter(publish__year__lte=year)
        else:
            sticks = sticks.filter(publish__year=year)
    data = [{'id': s.id, 'title': s.title, 'lat': s.latitude, 'lon': s.longitude, 'year': s.publish.year, 'likes': s.likes, 'image_url': s.image.url if s.image else None, 'url': s.get_absolute_url()} for s in sticks]
    return JsonResponse({'sticks': data})

def get_geojson(request, id):
    layer = get_object_or_404(MapLayer, id=id)
    return JsonResponse({'url': layer.geojson_file.url})

@csrf_exempt
def like_stick(request, id):
    if request.method == 'POST':
        stick = get_object_or_404(Stick, id=id)
        stick.likes += 1
        stick.save()
        return JsonResponse({'new_count': stick.likes})
    return JsonResponse(status=400)