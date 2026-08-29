import mido
import sys

if len(sys.argv) != 3:
    print("Usage: python midi_to_type0.py input.mid output.mid")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

mid = mido.MidiFile(input_file)
if mid.type == 0:
    print("Already Type 0, copying as-is.")
    mid.save(output_file)
else:
    # Merge all tracks into one (preserves timing)
    merged_track = mido.merge_tracks(mid.tracks)
    new_mid = mido.MidiFile(type=0, ticks_per_beat=mid.ticks_per_beat)
    new_mid.tracks = [merged_track]
    new_mid.save(output_file)
    print(f"Converted to Type 0: {output_file}")
