import sys
import os
from pydub import AudioSegment

# Ensure the correct number of arguments is passed
if len(sys.argv) != 2:
    print("Usage: python3 speed.py <OCTAVE_INCREASE>")
    sys.exit(1)

# Get the OCTAVE_INCREASE from the command line argument
OCTAVE_INCREASE = float(sys.argv[1])
INFILENAME = './song_inputs/target_audio_in.wav'
OUTFILENAME = './song_outputs/output.wav'

# Check if the output file exists and find a unique filename
base, ext = os.path.splitext(OUTFILENAME)
counter = 1
while os.path.exists(OUTFILENAME):
    print("CHECKING FOR FILENAME ",OUTFILENAME)
    OUTFILENAME = f"{base}_{counter}{ext}"
    counter += 1

# Load the audio file
sound = AudioSegment.from_file(INFILENAME, format="wav")

# Speed up and increase pitch
new_sample_rate = int(sound.frame_rate * (2.0 ** OCTAVE_INCREASE))
hipitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})

# Set the sample rate to 44100 Hz
hipitch_sound = hipitch_sound.set_frame_rate(44100)

# Export the modified audio
hipitch_sound.export(OUTFILENAME, format="wav")

print(f"Processed audio with OCTAVE_INCREASE={OCTAVE_INCREASE} saved to {OUTFILENAME}")
