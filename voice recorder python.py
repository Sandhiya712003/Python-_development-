import sounddevice as sd
import wavio

def record_audio(filename, duration, samplerate=44100):
    print("Recording...")
    audio_data = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=2, dtype='int16')
    sd.wait()  # Wait for recording to finish
    print("Recording finished successfully.")

    print("Saving audio successfully...")
    wavio.write(filename, audio_data, samplerate, sampwidth=3)
    print(f"Audio saved as {filename}")


if __name__ == "__main__":
    filename = "recorded_audio.wav"  # Name of the output audio file
    duration = 5  # Duration of recording in seconds

    record_audio(filename, duration)
