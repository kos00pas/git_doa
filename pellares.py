import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

filename = 'drones.wav'
y, sr = librosa.load(filename, sr=None)

# Calculate the power spectral density
psd = np.abs(librosa.stft(y))**2
mean_psd = np.mean(psd, axis=1)

# Generate frequency axis
frequencies = librosa.fft_frequencies(sr=sr)

# Plot the power spectrum
plt.figure(figsize=(14, 6))
plt.semilogy(frequencies, mean_psd)  # Use a logarithmic scale for the y-axis
plt.title('Power spectrum of a drone sound')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')
plt.xlim(0, sr/2)  # Limit the x-axis to half the sampling rate (Nyquist frequency)
plt.ylim(bottom=np.min(mean_psd))  # Set the bottom y-limit to the minimum power value
plt.tight_layout()
plt.show()