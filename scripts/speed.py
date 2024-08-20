from pydub import AudioSegment
from pydub.playback import play

# ------------------------------
# the octave increase is responsible for the pitch and speed increase
OCTAVE_INCREASE = 0.2
INFILENAME = 'audio.wav'
OUTFILENAME = 'output.wav'
# -----------------------------

sound = AudioSegment.from_file(INFILENAME, format="wav")
#speed up and increase pitch
new_sample_rate = int(sound.frame_rate * (2.0 ** OCTAVE_INCREASE))
hipitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})
# fix the sample rate
hipitch_sound = hipitch_sound.set_frame_rate(44100)

hipitch_sound.export(OUTFILENAME, format="wav")

