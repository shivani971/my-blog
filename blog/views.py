from django.shortcuts import render
from blog.forms import PostForm
from django.utils import timezone
from homepage import views
# Create your views here.
def index(request):
	return render(request,'home.html')
def post_new(request):
	form = PostForm(request.POST)
	if form.is_valid():
		post = form.save(commit=False)
		post.date=timezone.now()
		post.save()
		print 'saved'
		form=PostForm()
	else :
		form = PostForm()
	return render(request,'post_edit.html',{'form':form})