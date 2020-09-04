from django.shortcuts import render, redirect
from .models import feedback
from django.contrib import messages

# Create your views here.
def showbase(request):
    comments = feedback.objects.all().order_by("-timeStamp")
    comments_no = feedback.objects.all().count

    print(comments)
    context = {
        "comments": comments,
        "comments_no": comments_no,
    }
    if request.method == "POST":
        _mail = request.POST.get("email")
        _message = request.POST.get("msg")
        _name = request.POST.get("fname")
        print("mail")
        print(_mail)
        print(_message)
        print(_name)

        if _mail and _message:
            if len(_message) > 250:
                messages.info(request, "Feedback Can't be greater than 250 chars")
                return redirect("/")
            feedback_instance = feedback(name=_name, mail=_mail, message=_message)
            feedback_instance.save()
            print("Saved!")
        return redirect("/")
    return render(request, "feedbackapp/form1.html", context)
