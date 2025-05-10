
import React from 'react';
import SpeechRecognition, { useSpeechRecognition } from 'react-speech-recognition';

function App() {
  const {
    transcript,
    listening,
    resetTranscript,
    browserSupportsSpeechRecognition
  } = useSpeechRecognition();

  if (!browserSupportsSpeechRecognition) {
    return <span>Your browser does not support speech recognition.</span>;
  }

  const handleSend = async () => {
    const response = await fetch("http://localhost:8000/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ message: transcript, history: [] })
    });
    const data = await response.json();
    alert("Bot says: " + data.response);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>🎤 Voice Chat with FastAPI</h2>
      <p>Transcript: {transcript}</p>
      <button onClick={() => SpeechRecognition.startListening({ continuous: true })}>Start</button>
      <button onClick={SpeechRecognition.stopListening}>Stop</button>
      <button onClick={resetTranscript}>Reset</button>
      <button onClick={handleSend}>Send to Chat</button>
      <p>Status: {listening ? "🎙️ Listening..." : "🔇 Stopped"}</p>
    </div>
  );
}

export default App;
