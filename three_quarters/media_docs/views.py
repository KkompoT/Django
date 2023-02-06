from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import stringformat
from django.views import View
from django.shortcuts import redirect
from .filters import MediaDocsFiler
from .models import Book, Journal, Comics


class BooksView(View):
    queryset = Book.objects.all().select_related("uploaded_by")

    def get(self, request):
        return render(
            request,
            "items_list.html",
            {
                "items": MediaDocsFiler(request.GET, self.queryset).qs,
                "available_years": self.queryset.values("year").distinct(),
                "image": "img/books.png",
                "category": {
                    "name": "Книги",
                    "type": "books",
                    "image": "img/books.png"
                },
            },
        )
    # def post(self, request):
    #     form = BookForm(request.POST)
    #     if form.is_valid():
    #         book = form.save(commit=False)
    #         book.uploaded_by = request.user
    #         book.save()
    #         return redirect("books")
    #     else:
    #         return render(request, "add_book.html", {"form": form})


class DetailBookView(View):
    def get(self, request, book_slug: str):
        return render(
            request,
            "show_item.html",
            {
                "item": get_object_or_404(Book, slug=book_slug),
            },
        )


class JournalView(View):
    queryset = Journal.objects.all().select_related("uploaded_by")

    def get(self, request):
        return render(
            request,
            "items_list.html",
            {
                "items": MediaDocsFiler(request.GET, self.queryset).qs,
                "category": {
                    "name": "Статьи",
                    "type": "journal",
                    "image": "img/journal.png"
                },
            },
        )


class DetailJournalView(View):
    def get(self, request, journal_slug: str):
        return render(
            request,
            "show_item.html",
            {
                "item": get_object_or_404(Journal, slug=journal_slug),
            },
        )


class ComicsView(View):
    queryset = Comics.objects.all().select_related("uploaded_by")

    def get(self, request):
        return render(
            request,
            "items_list.html",
            {
                "items": MediaDocsFiler(request.GET, self.queryset).qs,
                "category": {
                    "name": "Комиксы",
                    "type": "comics",
                    "image": "img/comics.png"
                },
            },
        )


class DetailComicsView(View):
    def get(self, request, comics_slug: str):
        return render(
            request,
            "show_item.html",
            {
                "item": get_object_or_404(Comics, slug=comics_slug),
            },
        )


class Add_book(View):
    def get(self, request):
        return render(request, 'add_book.html')

    def post(self, request):
        title = request.POST.get('title')
        author = request.POST.get('author')
        year = request.POST.get('year')
        file = request.FILES.get('file')
        image = request.FILES.get('image')

        book = Book.objects.create(
            title=title,
            author=author,
            year=year,
            file=file,
            image=image,
        )

        return redirect('books')
