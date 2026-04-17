# 📚 Book AI Platform (Full-Stack + AI/RAG)

## 🚀 Overview

This is a full-stack web application that collects book data using automation, stores it in a backend, and enables intelligent querying using AI.

The system supports:

* Book data scraping
* Backend API management
* AI-based insights (summary & Q&A)
* Simple frontend interface for users

---

## ✨ Features

* 📖 **Book Scraping** using Selenium
* 🗄️ **Backend APIs** using Django REST Framework
* 🤖 **AI Integration** (Summary + Q&A system)
* 🔍 **Question Answering** over book data
* 🌐 **Frontend UI** built with React
* ⚡ **(Optional)** RAG-based querying with vector search

---

## 🛠️ Tech Stack

### Backend:

* Python
* Django REST Framework

### Frontend:

* ReactJS
* Axios

### Database:

* SQLite / MySQL

### AI:

* OpenAI API (or Mock AI if quota exceeded)

### Automation:

* Selenium

---

## ⚙️ Setup Instructions

### 🔹 Backend Setup

```bash
cd book_ai_platform
pip install -r requirements.txt
python manage.py runserver
```

---

### 🔹 Frontend Setup

```bash
cd frontend
npm install
npm start
```

---

## 🔗 API Endpoints

| Method | Endpoint           | Description              |
| ------ | ------------------ | ------------------------ |
| GET    | `/api/books/`      | List all books           |
| GET    | `/api/books/<id>/` | Get book details         |
| POST   | `/api/books/add/`  | Add new book             |
| POST   | `/api/ask/`        | Ask question about books |

---

## 💡 Sample Usage

### ➤ Add Book

```json
{
  "title": "Test Book",
  "author": "Author Name",
  "description": "This is an adventure story",
  "rating": 4.5,
  "url": "https://example.com"
}
```

---

### ➤ Ask Question

```json
{
  "question": "Which books are about adventure?"
}




## 📸 Screenshots

(Add screenshots here)

* 📊 Dashboard (Book List)
* 📘 Book Details Page
* ❓ Q&A Interface
* 🛠️ Django Admin Panel



## 🎯 Project Highlights

* End-to-end full-stack implementation
* Integration of AI with backend APIs
* Automated data collection pipeline
* Clean and modular code structure



## 🚀 Future Improvements

* 🔥 Full RAG implementation using ChromaDB
* 📚 Better recommendation system
* 🎨 Improved UI/UX
* 🧠 Advanced AI insights


## 👩‍💻 Author

* Developed as part of internship assignment
* Focused on practical implementation of AI + Full Stack


