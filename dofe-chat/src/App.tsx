import { useState } from "react";
import "./App.css";

type Message = { role: "user" | "bot"; text: string };

function App() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");

  function send() {
    const text = input.trim();
    if (!text) return;
    setMessages([
      ...messages,
      { role: "user", text },
      { role: "bot", text: "(fake reply)" },
    ]);
    setInput("");
  }

  return (
    <main className="chat">
      <div className="messages">
        {messages.map((m, i) => (
          <p key={i} className={`message ${m.role}`}>
            {m.text}
          </p>
        ))}
      </div>

      <form
        className="input-bar"
        onSubmit={(e) => {
          e.preventDefault();
          send();
        }}
      >
        <input
          value={input}
          onChange={(e) => setInput(e.currentTarget.value)}
          placeholder="Type a message..."
        />
        <button type="submit">Send</button>
      </form>
    </main>
  );
}

export default App;