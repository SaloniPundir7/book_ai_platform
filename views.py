from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from .ai_utils import generate_summary, ask_question
from books.models import Book
from books.rag_utils import store_books

store_books(Book.objects.all())


# 🔹 GET: List all books
@api_view(['GET'])
def get_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


# 🔹 GET: Single book detail
@api_view(['GET'])
def get_book_detail(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return Response({'error': 'Book not found'}, status=404)

    serializer = BookSerializer(book)
    return Response(serializer.data)


# 🔹 POST: Add new book
@api_view(['POST'])
def add_book(request):
    serializer = BookSerializer(data=request.data)

    if serializer.is_valid():
        book = serializer.save()

        # 🔥 Generate summary (AI / mock)
        summary = generate_summary(book.description)
        book.summary = summary
        book.save()

        return Response(BookSerializer(book).data)

    return Response(serializer.errors, status=400)


# 🔹 POST: Ask question (Q&A)

from .rag_utils import query_books

@api_view(['POST'])
def ask_book_question(request):
    question = request.data.get("question")

    if not question:
        return Response({"error": "Question is required"}, status=400)

    # 🔥 Get relevant documents (RAG)
    relevant_docs = query_books(question)

    context = " ".join(relevant_docs)

    # Send to AI (or mock)
    answer = ask_question(context, question)

    return Response({"answer": answer})

