class Solution:
	def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
		result = 0
		queue = deque([])
		for index in range(len(tickets)):
			queue.append([tickets[index] , index])
		while len(queue) > 0:
			first_person , index = queue.popleft()
			result = result + 1
			first_person = first_person - 1
			if index == k and first_person == 0:
				return result
			elif first_person != 0:
				queue.append([first_person , index])

import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
from pydub import AudioSegment

def draw(x_axis, y_axis, label, color, x_label, y_label, title, lw):
    plt.figure(figsize=(15, 5))
    plt.grid(alpha=0.3)
    plt.style.use('dark_background')
    plt.plot(x_axis, y_axis, label=label, color=color, linewidth=lw)
    plt.xlabel(x_label, fontsize=20)
    plt.ylabel(y_label, fontsize=20)
    plt.title(title, fontsize=30)
    plt.legend(loc='upper right')
    plt.show()
    return

sample_rate, audio = wavfile.read('noise2.wav')

normalized_audio = audio.astype(np.float32) / np.max(np.abs(audio))

# Time axis
t = np.arange(0, len(normalized_audio)) / sample_rate

# Plot the original audio
draw(x_axis=t, y_axis=audio, label="Original Audio", color="y", x_label="Time(s)", title="Original Audio",
     y_label="Amplitude", lw=4)

# Perform noise reduction using FFT-based spectral subtraction
window_size = 128
hop_size = 128
alpha = 0.01  # Scaling factor for noise reduction (adjust as needed)

denoised_audio = np.zeros_like(audio, dtype=np.float64)

for i in range(0, len(audio) - window_size, hop_size):
    frame = audio[i:i + window_size]
    
    # Compute the magnitude spectrum using FFT
    magnitude_spectrum = np.abs(np.fft.fft(frame))