from django.shortcuts import render
from .models import Books
from django.shortcuts import redirect
from .forms import BooksForm

# Create your views here.
def homepage(request):
    books=Books.objects.all()
    books_with_index = [(index + 1, book) for index, book in enumerate(books)]
    return render(request,"index.html",{'books_with_index':books_with_index})
    

def bookdetails(request,slug):
    book=Books.objects.filter(id=slug).first()
    return render(request,"books.html",{'book':book})

def additem(request):
    if request.method=="POST":
        name=request.POST.get("book_name",None)
        desc=request.POST.get("desc",None)
        image=request.FILES['img']
        price=request.POST.get("price",None)
        book=Books(name=name,des=desc,image=image,price=price)
        book.save()
    return render(request,"add_item.html",{})

def deleteitem(request,slug):
    Books.objects.filter(id=slug).delete()
    return redirect("/")

def updateitem(request, item_id):
    item = Books.objects.filter(id=item_id).first()

    if request.method == 'POST':
        form = BooksForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = BooksForm(instance=item)

    return render(request, 'edit_item.html', {'form': form})
