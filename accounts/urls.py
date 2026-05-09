from django.urls import path
from .views import SignUpView                                # Note: Leave this empty at first, and return to place contents later.

urlpatterns = [
                                                              # Note: When the user inputs the signup/ endpoint in the URL window of the browser, it will trigguer the SignUpView function, so that the appropriate page will render in the browser.
    path("signup/", SignUpView.as_view(), name="signup"),     # Note: You can leave the list empty at first, and return to fill it later, after we have developed the views.py file in the accounts folder/app. The name of the function "signup" is what we place in the navbar anchor tag.
]