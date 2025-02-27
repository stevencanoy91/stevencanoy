from flask import Flask, request
import whisper

app = Flask(__name__)
model = whisper.load_model("base")

@app.route("/transcribe", methods=["POST"])
def transcribe_audio():
    audio_file = request.files["audio"]
    result = model.transcribe(audio_file)
    return {"transcription": result["text"]}

if __name__ == "__main__":
    app.run(debug=True)