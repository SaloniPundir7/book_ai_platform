import React, { useState } from "react";
import axios from "axios";

function QA() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const askQuestion = () => {
    axios.post("http://127.0.0.1:8000/api/ask/", {
      question: question
    })
    .then(res => setAnswer(res.data.answer))
    .catch(err => console.log(err));
  };

  return (
    <div>
      <h2>Ask Question</h2>
      <input 
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />
      <button onClick={askQuestion}>Ask</button>

      <p>{answer}</p>
    </div>
  );
}

export default QA;