from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.get_books),
    path('books/<int:id>/', views.get_book_detail),
    path('books/add/', views.add_book),
    path('ask/', views.ask_book_question),
]