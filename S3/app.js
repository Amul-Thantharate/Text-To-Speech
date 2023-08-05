document
  .getElementById("tts-form")
  .addEventListener("submit", async (event) => {
    event.preventDefault();
    const text = document.getElementById("text").value;
    const voiceId = document.getElementById("voice-id").value;
    const pitch = document.getElementById("pitch").value;
    const response = await fetch(
      "https://your-api-gateway-url/your-api-endpoint", // Replace with your API Gateway URL and API endpoint path (e.g. https://1234567890.execute-api.us-east-1.amazonaws.com/Prod/tts)
      {
        method: "POST",
        mode: "cors",
        credentials: "omit",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text, voiceId, pitch }),
      }
    );
    const responseBody = await response.json();
    const audioBase64 = responseBody.body;
    const audioBlob = new Blob(
      [Uint8Array.from(atob(audioBase64), (c) => c.charCodeAt(0))],
      { type: "audio/mpeg" }
    );
    const audioUrl = URL.createObjectURL(audioBlob);
    const audioPlayer = document.getElementById("audio-player");
    audioPlayer.src = audioUrl;
    audioPlayer.play();
  });
