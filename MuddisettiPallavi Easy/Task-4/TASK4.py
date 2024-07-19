import pyaudio
import wave                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      

chunk = 1024
format = pyaudio.paInt16
CHANNELS = 2
rate = 44100
time = 5
audio = pyaudio.PyAudio()


stream = audio.open(format = format, channels = CHANNELS,
                     rate = rate,
                     input = True,frames_per_buffer=chunk )
print("start recording...")
frames = []
# record audio in chunks
for i in range(0, int(rate / chunk*time )):
    data = stream.read(chunk)
    # store in frames
    frames.append(data)
print("recording stops")   
# stoping stream
stream.stop_stream()
stream.close()
audio.terminate()

# for saving the audio
filename = "record_output.wav"
wf = wave.open(filename , 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(audio.get_sample_size(format))
wf.setframerate(rate)
wf.writeframes(b''.join(frames))
wf.close()
# saving audio with file name 
print(f"audio saved as {filename}")



