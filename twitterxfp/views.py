from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import git
import os

@csrf_exempt
def update(request):
    if request.method == "POST":
        # Pass the path of the directory where your project will be stored on PythonAnywhere
        repo = git.Repo('/home/temistoclisxp58/TwitterXFp')
        origin = repo.remotes.origin
        origin.pull()
        return HttpResponse("Updated code on PythonAnywhere")
    else:
        return HttpResponse("Couldn't update the code on PythonAnywhere")


def hello_world(request):
    template = loader.get_template('hello_world.html')
    return HttpResponse(template.render())
