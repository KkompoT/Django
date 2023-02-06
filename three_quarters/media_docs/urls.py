from django.urls import path
from django.views.generic import TemplateView
from . import views
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings



urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html")),
    # path("books/<slug:book_slug>", views.DetailBookView.as_view(), name="show-book"),
    path("books/", views.BooksView.as_view(), name="books"),
    path("books/add", views.Add_book.as_view(), name="add_book"),

    path("journal/<slug:journal_slug>", views.DetailJournalView.as_view(), name="show-journal"),
    path("journal/", views.JournalView.as_view(), name="journal"),

    path("comics/<slug:comics_slug>", views.DetailComicsView.as_view(), name="show-comics"),
    path("comics/", views.ComicsView.as_view(), name="comics"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

