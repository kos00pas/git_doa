
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pyaudio
import datetime
from funcss import my_funcs as mf
from classesss import Tun_Param as pt
from WAV import WAV  # Importing WAV class from WAV.py

def run_gui(r,param):
    root = tk.Tk()
    app = AudioRecorderGUI(root,r,param)
    root.mainloop()

class AudioRecorderGUI:
    def __init__(self, root, r, param):
        self.root = root
        self.param = param
        self.r = r
        self.wav_recorder = WAV(param)  # WAV object for recording
        # Rest of the __init__ code

    def start_recording(self):
        # Assuming rec_sec is a predefined recording duration or can be set by the user
        rec_sec = 10  # Set this to the desired recording duration
        self.wav_recorder.record_all(rec_sec)
        # You may need to handle threading or asynchronous execution depending on your requirements
        # Rest of the start_recording code

    def stop_recording(self):
        # Add logic here to stop the recording if required
        # Rest of the stop_recording code

    # Rest of the AudioRecorderGUI class code
