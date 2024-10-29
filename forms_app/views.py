from django.shortcuts import render
from .forms import FormName
from .models import Feedback

# Create your views here.
# forms_app / views.py

def form_name_view(request):
    form = FormName()
    profile_pic_url = None  # Initialize profile picture url

    if request.method == 'POST':
        form = FormName(request.POST, request.FILES)  # Handle file uploads
        form = FormName(request.POST)
        if form.is_valid():
            # Extract the cleaned data from the form
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            feedback = form.cleaned_data['feedback']
            profile_pic = form.cleaned_data.get('profile_pic')

            # save data to the database
            # Feedback.objects.create(name=name,email=email,feedback=feedback)
            feedback_instance = Feedback.objects.create(
                name=name,
                email=email,
                feedback=feedback,
                profile_pic=profile_pic
            )

            # Get the URL of the uploaded profile picture
            if profile_pic:
                profile_pic_url = feedback_instance.profile_pic.url


            # Print formated output in the terminal

            print("\n" + "=" * 50)
            print("User Form Submission".center(50))
            print("=" * 50)
            print(f"Name:{name}")
            print(f"Email:{email}")
            print(f"Feedback:{feedback}")
            if profile_pic:
                print(f"Profile Picture:{profile_pic_url}")
            print("=" * 50 + "\n")

    return render(request, 'forms_app/form_page.html', {
        'form': form,
        'profile_pic_url': profile_pic_url
    })





