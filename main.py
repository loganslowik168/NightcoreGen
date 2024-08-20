import sys
import subprocess
import os
import shutil

def find_and_move_wav(src_directory, dest_directory):
    # Ensure the destination directory exists
    if not os.path.exists(dest_directory):
        os.makedirs(dest_directory)

    # List all files in the source directory
    for filename in os.listdir(src_directory):
        # Check if the file is a .wav file
        if filename.endswith('.wav'):
            src_file = os.path.join(src_directory, filename)
            dest_file = os.path.join(dest_directory, "target_audio_in.wav")

            # Move the file to the destination directory
            shutil.move(src_file, dest_file)
            print(f"Moved {filename} to {dest_directory}")
            return

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 main.py <youtube_link> <octaval_increase>")
        sys.exit(1)

    youtube_arg = sys.argv[1]
    speed_arg = sys.argv[2]

    try:
        # Run youtube.py with the first argument
        subprocess.run(['python3', './scripts/youtube.py', youtube_arg], check=True)
        find_and_move_wav('./', './song_inputs/')
        # Run speed.py with the second argument
        subprocess.run(['python3', './scripts/speed.py', speed_arg], check=True)

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the scripts: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
