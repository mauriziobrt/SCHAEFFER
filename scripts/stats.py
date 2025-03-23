import os
import numpy as np
import soundfile as sf

def get_wav_durations(directory):
    durations = []
    file_paths = []
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(".wav"):
                file_path = os.path.join(root, file)
                try:
                    with sf.SoundFile(file_path) as audio_file:
                        duration = len(audio_file) / audio_file.samplerate
                        durations.append(duration)
                        file_paths.append(file_path)
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
    
    return durations, file_paths

def compute_statistics(durations, file_paths):
    if not durations:
        print("No WAV files found.")
        return
    
    mean_duration = np.mean(durations)
    std_dev = np.std(durations)
    min_duration = np.min(durations)
    max_duration = np.max(durations)
    median_duration = np.median(durations)
    
    lower_bound = mean_duration - 2 * std_dev
    upper_bound = mean_duration + 2 * std_dev
    
    outliers = [(file_paths[i], durations[i]) for i in range(len(durations)) if durations[i] < lower_bound or durations[i] > upper_bound]
    
    print(f"Total WAV files processed: {len(durations)}")
    print(f"Mean duration: {mean_duration:.2f} seconds")
    print(f"Standard deviation: {std_dev:.2f} seconds")
    print(f"Minimum duration: {min_duration:.2f} seconds")
    print(f"Maximum duration: {max_duration:.2f} seconds")
    print(f"Median duration: {median_duration:.2f} seconds")
    
    if outliers:
        print("Outliers:")
        for path, duration in outliers:
            print(f"{path} - {duration:.2f} seconds")
    else:
        print("No outliers detected.")

if __name__ == "__main__":
    directory = input("Enter the path to the folder: ").strip()
    durations, file_paths = get_wav_durations(directory)
    compute_statistics(durations, file_paths)