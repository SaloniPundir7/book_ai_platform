import React, { useEffect, useState } from "react";
import axios from "axios";

function Dashboard() {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/books/")
      .then(res => {
        console.log(res.data);   // for debugging
        setBooks(res.data);
      })
      .catch(err => console.log(err));
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h2>📚 Book List</h2>

      {books.length === 0 ? (
        <p>No books found</p>
      ) : (
        books.map(book => (
          <div key={book.id} style={{
            border: "1px solid #ccc",
            margin: "10px",
            padding: "10px"
          }}>
            <h3>{book.title}</h3>
            <p><b>Author:</b> {book.author}</p>
            <p><b>Rating:</b> {book.rating}</p>
            <p><b>Summary:</b> {book.summary}</p>
          </div>
        ))
      )}
    </div>
  );
}

export default Dashboard;