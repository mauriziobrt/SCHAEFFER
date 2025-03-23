import os
import numpy as np
import soundfile as sf
from scipy.signal import find_peaks

def remove_trailing_silence(input_file, output_file, threshold=0.01):
    # Load audio file
    audio, samplerate = sf.read(input_file)
    
    # Compute absolute amplitude
    amplitude = np.abs(audio)
    
    # Find last non-silent sample
    non_silent_indices = np.where(amplitude > threshold)[0]
    
    if len(non_silent_indices) == 0:
        print(f"No non-silent parts detected in {input_file}. Outputting empty file.")
        sf.write(output_file, np.array([], dtype=audio.dtype), samplerate)
        return
    
    last_non_silent = non_silent_indices[-1]
    trimmed_audio = audio[:last_non_silent + 44100]
    
    # Export the trimmed audio
    sf.write(output_file, trimmed_audio, samplerate)
    print(f"Processed: {input_file} -> {output_file}")

def process_folder(input_folder, output_folder, threshold=0.01):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".wav"):
            input_file = os.path.join(input_folder, file_name)
            output_file = os.path.join(output_folder, file_name)
            remove_trailing_silence(input_file, output_file, threshold)

if __name__ == "__main__":
    
    input_folder = "*"  # Change this to your input folder
    for root, _, files in os.walk(input_folder):
        out_path = root
        process_folder(out_path, out_path)

    # output_folder = "*"  # Change this to your desired output folder
   