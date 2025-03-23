import os
import soundfile as sf

def get_wav_files(directory):
    wav_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(".wav"):
                wav_files.append(os.path.join(root, file))
    return wav_files

def get_durations(wav_files):
    durations = {"<1s": 0, "1-2s":0,"2-3s":0, "3-4s":0, "4-5s":0, "5-6s": 0,"6-7s": 0,"7-8s": 0,"8-9s": 0,"9-10s": 0, "10-11s": 0, "11-12s": 0,"12-13s": 0,"13-14s": 0, "14-15s": 0,  ">15s": 0}
    crop_bias = []
    for file_path in wav_files:
        try:
            data, samplerate = sf.read(file_path)
            duration = len(data) / samplerate
            
            if duration < 1:
                durations["<1s"] += 1
            elif 1 <= duration <= 2:
                durations["2-3s"] += 1
            elif 2 <= duration <= 3:
                durations["2-3s"] += 1
            elif 3 <= duration <= 4:
                durations["3-4s"] += 1
            elif 4 <= duration <= 5:
                durations["4-5s"] += 1
            elif 5 <= duration <= 6:
                durations["5-6s"] += 1
            elif 6 <= duration <= 7:
                durations["6-7s"] += 1
            elif 7 <= duration <= 8:
                durations["7-8s"] += 1
            elif 8 <= duration <= 9:
                durations["8-9s"] += 1
            elif 9 <= duration <= 10:
                durations["9-10s"] += 1
                crop_bias.append(file_path)
            elif 10 <= duration <= 11:
                durations["10-11s"] += 1
            elif 11 <= duration <= 12:
                durations["11-12s"] += 1
            elif 12 <= duration <= 13:
                durations["12-13s"] += 1
            elif 13 <= duration <= 14:
                durations["13-14s"] += 1
            elif 14 <= duration <= 15:
                durations["14-15s"] += 1
            else:
                durations[">15s"] += 1
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    return durations, crop_bias

def save_results(durations, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        for file in bias:
            f.write(file)
        for category, count in durations.items():
            f.write(f"{category}: {count}\n")

if __name__ == "__main__":
    # directory = input("Enter the path to the folder: ").strip()
    directory = "*"
    output_file = "wav_duration_counts.txt"
    wav_files = get_wav_files(directory)
    # print(wav_files)
    durations, bias = get_durations(wav_files)
    save_results(durations, output_file)
    print(f"Results saved to {output_file}")
