from django.urls import path
from blog import views

urlpatterns = [
    path("home", views.homepage, name = "home"),
    path("about", views.aboutus, name = "about"),
    path("contact", views.contact, name = "contact"),
    path("services", views.servicesus, name = "services"),
    path("save-my-data", views.savethisdaa),

    path("delete-record/<int:myid>",views.deletethisdata),

    path("updatethis/<int:xyz>", views.updatethisdata),

    path("updatethisdata/<int:hey>" , views.updatedata),
    path("search-my-data", views.searchhing),
    path("signup", views.signup , name="signup"),

    path("login", views.loginhere,name="login"),
    path("logout",views.logouthere,name="logout"),
]