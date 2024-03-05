import numpy as np
from pydub import AudioSegment
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import welch
import librosa

def split_wav():
        wav_file_path = 'drones.wav'
        audio = AudioSegment.from_file(wav_file_path, format='wav')

        # Define your time segments in milliseconds
        mil = 10**3
        t0_0=1.42*mil
        t0_1=3.9*mil
        t1_0=6*mil
        t1_1=7.85*mil
        t2_0=10*mil
        t2_1=11.64*mil
        t3_0=13.49*mil
        t3_1=15.34*mil
        time_segments = [(t0_0,t0_1),(t1_0,t1_1),(t2_0,t2_1),(t3_0,t3_1)]  # Example segments

        # Loop through each segment and save them as separate files
        for i, (start_ms, end_ms) in enumerate(time_segments, start=1):
            segment = audio[start_ms:end_ms]  # Extract the segment
            segment_file_path = f'segment_{i}.wav'
            segment.export(segment_file_path, format='wav')
            print(f'Segment {i} saved to {segment_file_path}')
def plot_power_spectrum(filename):
    """
    Plots the power spectrum of the given audio file.

    Parameters:
    - filename: str, path to the audio file.
    """
    # Load the audio file
    samplerate, data = wavfile.read(filename)

    # Check if the audio file is stereo or mono
    if data.ndim > 1:
        data = data.mean(axis=1)  # Convert to mono by averaging both channels

    # Use Welch's method to compute the power spectral density
    frequencies, psd = welch(data, samplerate, nperseg=1024)

    # Plot the power spectrum
    plt.semilogy(frequencies, psd, label=filename)
def main_plot_for_drones(num_drones):
    """
    This function plots the power spectrum for multiple drone audio files.

    Parameters:
    - num_drones: int, number of drone files to plot.
    """
    plt.figure(figsize=(14, 6))

    # Iterate over the number of drones and plot each one on the same figure
    for i in range(1, num_drones + 1):
        plot_power_spectrum(f'segment_{i}.wav')

    # Configure the plot
    plt.title('Power Spectrum of Drone Sounds')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Power')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    # Display the plot
    plt.show()
def plot_spect_all( num_of_wav):
    for i in range(0,num_of_wav):
        filename= f'segment_{i+1}.wav'
        # Load the audio file
        y, sr = librosa.load(filename, duration=1)

        # Calculate the Mel spectrogram
        S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=450, fmax=5500)
        # n_mels -> increase number of Mel bands, fmax for sampling
        # Assuming you want to avoid aliasing, set fmax to your desired maximum frequency (e.g., 20 kHz)
        # fmax = 20000

        # Plot the Mel spectrogram
        fig, ax = plt.subplots()
        S_dB = librosa.power_to_db(S, ref=np.max)
        img = librosa.display.specshow(S_dB, x_axis='time',
                                       y_axis='mel', sr=sr,
                                       fmax=8000, ax=ax)
        fig.colorbar(img, ax=ax, format='%+2.0f dB')
        ax.set(title=filename+' Mel-fr spect')
        plt.show()

def fundemental(num_of_wav):
       # for i in range(0,num_of_wav):
       #      filename= f'segment_{i+1}.wav'
            filename= f'segment_{num_of_wav}.wav'
            # Load the audio file
            y, sr = librosa.load(filename, duration=1)
            # print(y)
            y=np.array(y)
            y=y.astype(float)
            f0, voiced_flag, voiced_probs = librosa.pyin(y,sr=sr, fmin=librosa.note_to_hz('C0'), fmax=librosa.note_to_hz('C8'))
            times = librosa.times_like(f0)

            D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
            fig, ax = plt.subplots()
            img = librosa.display.specshow(D, x_axis='time', y_axis='log', ax=ax)
            ax.set(title='pYIN fundamental frequency estimation')
            fig.colorbar(img, ax=ax, format="%+2.f dB")
            ax.plot(times, f0, label='f0', color='cyan', linewidth=3)
            ax.legend(loc='upper right')
            plt.show()
