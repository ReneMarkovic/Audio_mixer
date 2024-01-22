import tkinter as tk
from tkinter import filedialog, Label, Button, Checkbutton, Scale, IntVar
from pydub import AudioSegment
from pydub.playback import play
import audio_effects as ae
import os

class AudioMixerGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.ambient_file = None
        self.letters_file = None
        self.recital_file = None

    def create_widgets(self):
        #Ambient
        self.ambient_label = Label(self, text="Ambient", bg='lightgreen')
        self.ambient_label.grid(row=0, column=0)
        self.load_ambient_button = Button(self, text="load track", bg='lightgreen', command = lambda: self.load_track("ambient"))
        self.load_ambient_button.grid(row=0, column=2)
        
        self.ambient_left_channel = IntVar()
        self.ambient_left_check = Checkbutton(self, text="Left", bg='lightgreen', variable=self.ambient_left_channel)
        self.ambient_left_channel.set(1)
        self.ambient_left_check.grid(row=0, column=3)
        
        self.ambient_right_channel = IntVar()
        self.ambient_right_check = Checkbutton(self, text="Right", bg='lightgreen', variable=self.ambient_right_channel)
        self.ambient_right_channel.set(0)
        self.ambient_right_check.grid(row=0, column=4)
        
        self.ambient_volume = Scale(self, from_=0, to=100, orient='horizontal', bg='lightgreen', label='Vol.')
        self.ambient_volume.set(50)
        self.ambient_volume.grid(row=1, column=0, columnspan=2, sticky="ew")
        
        self.ambient_reverb = Scale(self, from_=0, to=100, orient='horizontal', bg='lightgreen', label='Rev.')
        self.ambient_reverb.set(0)
        self.ambient_reverb.grid(row=1, column=2, columnspan=2, sticky="ew")
        

        #letters
        row = 4
        self.letters_label = Label(self, text="Letters", bg='lightblue')
        self.letters_label.grid(row=row, column=0)
        self.load_letters_button = Button(self, text="load track", bg='lightblue', command= lambda: self.load_track("letters"))
        self.load_letters_button.grid(row=row, column=2)
        
        self.letters_left_channel = IntVar()
        self.letters_left_channel.set(1)
        self.letters_left_check = Checkbutton(self, text="Left", bg='lightblue', variable=self.letters_left_channel)
        self.letters_left_check.grid(row=row, column=3)
        
        self.letters_right_channel = IntVar()
        self.letters_right_channel.set(0)
        self.letters_right_check = Checkbutton(self, text="Right", bg='lightblue', variable=self.letters_right_channel)
        self.letters_right_check.grid(row=row, column=4)
        
        self.letters_volume = Scale(self, from_=0, to=100, orient='horizontal', bg='lightblue', label='Vol.')
        self.letters_volume.set(50)
        
        self.letters_volume.grid(row=row+1, column=0, columnspan=2, sticky="ew")
        self.letters_reverb = Scale(self, from_=0, to=100, orient='horizontal', bg='lightblue', label='Rev.')
        self.letters_reverb.set(0)
        self.letters_reverb.grid(row=row+1, column=2, columnspan=2, sticky="ew")
        
        #recital
        row=row+4
        self.recital_label = Label(self, text="Recital", bg='orange')
        self.recital_label.grid(row=row, column=0)
        self.load_recital_button = Button(self, text="load track", bg='orange', command= lambda: self.load_track("recital"))
        self.load_recital_button.grid(row=row, column=2)
        
        self.recital_left_channel = IntVar()
        self.recital_left_check = Checkbutton(self, text="Left", bg='orange', variable=self.recital_left_channel)
        self.recital_left_channel.set(0)
        self.recital_left_check.grid(row=row, column=3)
        
        self.recital_right_channel = IntVar()
        self.recital_right_check = Checkbutton(self, text="Right", bg='orange', variable=self.recital_right_channel)
        self.recital_right_channel.set(1)
        self.recital_right_check.grid(row=row, column=4)
        
        self.recital_volume = Scale(self, from_=0, to=100, orient='horizontal', bg='orange', label='Vol.')
        self.recital_volume.set(50)
        self.recital_volume.grid(row=row+1, column=0, columnspan=2, sticky="ew")
        
        self.recital_reverb = Scale(self, from_=0, to=100, orient='horizontal', bg='orange', label='Rev.')
        self.recital_reverb.set(0)
        self.recital_reverb.grid(row=row+1, column=2, columnspan=2, sticky="ew")

        self.recital_fade_in = Scale(self, from_=0, to=10, orient='horizontal', bg='orange', label='Fade-in')
        self.recital_fade_in.set(1)
        self.recital_fade_in.grid(row=row+2, column=0, columnspan=2, sticky="ew")

        self.recital_fade_out = Scale(self, from_=0, to=10, orient='horizontal', bg='orange', label='Fade-out')
        self.recital_fade_out.set(1)
        self.recital_fade_out.grid(row=row+2, column=2, columnspan=2, sticky="ew")

        self.generate_button = Button(self, text="Generate", command=self.generate)
        self.generate_button.grid(row=row+3, column=0, columnspan=4)

    def load_track(self,track_type):
        # Open the file dialog to choose a file
        file_path = filedialog.askopenfilename(
            title="Select an Audio File",
            filetypes=(("Audio Files", "*.wav *.mp3 *.ogg *.flac"), ("All Files", "*.*"))
        )

        # Check if a file was selected
        if file_path:
            # Here you can store the file path in an attribute or process the file
            print(f"File selected: {file_path}")
            # For example, if you have a track attribute for storing the path:
            self.track_path = file_path
            if file_path:
                file_name = os.path.basename(file_path)
                if track_type == "ambient":
                    self.ambient_file = file_path
                    self.ambient_label.config(text=file_name)
                elif track_type == "letters":
                    self.letters_file = file_path
                    self.letters_label.config(text=file_name)
                elif track_type == "recital":
                    self.recital_file = file_path
                    self.recital_label.config(text=file_name)
                else:
                    raise ValueError("Unknown track type")
        else:
            print("No file was selected.")

    def add_reverb(self, audio_segment, reverb_intensity=1, decay_factor=0.5):
        """
        Adds a simple reverb effect to the audio segment by overlaying
        delayed versions of the original audio.

        Parameters:
        - audio_segment: instance of AudioSegment to which reverb will be added
        - reverb_intensity: the number of delayed overlays to add. More overlays will simulate a larger space.
        - decay_factor: the decrease in volume for each subsequent overlay. Simulates the decay of the reverb.
        """
        
        # Define a base delay in milliseconds
        base_delay_ms = 50

        # Create a new audio segment to hold the reverberated audio
        reverbed_segment = audio_segment

        for i in range(reverb_intensity):
            # Calculate the delay for this overlay
            delay_ms = base_delay_ms * (i + 1)

            # Create a silent segment for the delay
            silence = AudioSegment.silent(duration=delay_ms)

            # Create the delayed overlay segment with decay
            overlay_segment = silence + (audio_segment - decay_factor * i * 6)

            # Overlay the delayed segment on top of the reverbed_segment
            reverbed_segment = reverbed_segment.overlay(overlay_segment)

        return reverbed_segment

    def volume_adjust(self,audio_segment, slider_value, min_volume=-40, max_volume=20):
        """
        Adjust the volume of an AudioSegment based on a slider value.

        Parameters:
        - audio_segment: the AudioSegment whose volume will be adjusted
        - slider_value: a value from the slider, expected to be between 0 and 100
        - min_volume: the dB change corresponding to the minimum slider value
        - max_volume: the dB change corresponding to the maximum slider value
        """
        
        # Map the slider value to the dB range
        volume_change = (slider_value / 100.0) * (max_volume - min_volume) + min_volume

        # Adjust the volume
        return audio_segment + volume_change

    # Fukcija za dodajanje tišine na konec zvočnega segmenta, da se ujema z želeno dolžino
    def poenotenje_dolzine(self,audio_segment, max_length):
        if len(audio_segment) < max_length:
            silence_duration = max_length - len(audio_segment)
            silence = AudioSegment.silent(duration=silence_duration)
            audio_segment += silence
        return audio_segment

    def adjust_length(self,audio_segment, target_length_ms=20_000):

        current_length_ms = len(audio_segment)
        if len(audio_segment) > target_length_ms:
            # Trim the audio to the target length
            return audio_segment[:target_length_ms]
        
        elif current_length_ms < target_length_ms:
            # Calculate total padding needed
            total_padding_ms = target_length_ms - current_length_ms
            # Padding for beginning and end
            padding_one_side_ms = total_padding_ms // 2
            # Create silent audio for padding
            silence_padding = AudioSegment.silent(duration=padding_one_side_ms)
            # Pad the audio segment at the beginning and end to center it
            return silence_padding + audio_segment + silence_padding
        
        else:
            # If the audio is already the target length, return it as is
            return audio_segment

    def combine_selected_tracks(self, *track_info,pan=0):
        """
        Combines audio tracks that have their corresponding checkbox selected.
        track_info: Tuples of (audio_track, checkbox_state)
        """
        combined_track = None

        for track, checkbox_state in track_info:
            if checkbox_state.get() == 1:  # If the checkbox is checked
                if combined_track is None:
                    combined_track = track
                else:
                    combined_track = combined_track.overlay(track)
        # Pan combined track to the left
        if combined_track is not None:
            combined_track = combined_track.set_channels(1).pan(pan)
            return combined_track
        else:
            combined_track = None
            return combined_track

    # This is where you would integrate your audio processing code
    def process_audio(self, ambient_path, letters_path, recital_path):
        # Implement the audio processing logic here
        # The following is a simplified example:
        
        # Load the tracks
        ambient_track = AudioSegment.from_file(ambient_path)
        #ambient_track = self.add_reverb(ambient_track, reverb_intensity=self.ambient_reverb.get(), decay_factor=0.5)
        ambient_track = self.volume_adjust(ambient_track, slider_value=self.ambient_volume.get())
        ambient_track = self.adjust_length(ambient_track)
        
        letters_track = AudioSegment.from_file(letters_path)
        #letters_track = self.add_reverb(letters_track, reverb_intensity=self.letters_reverb.get(), decay_factor=0.5)
        letters_track = self.volume_adjust(letters_track, slider_value=self.letters_volume.get())
        letters_track = self.adjust_length(letters_track)
        
        recital_track = AudioSegment.from_file(recital_path)
        #recital_track = self.add_reverb(recital_track, reverb_intensity=self.recital_reverb.get(), decay_factor=0.5)
        recital_track = ae.delay(recital_track,
                                 interval=self.recital_reverb.get()/1000.0,
                                    unit=10)
        recital_track = self.volume_adjust(recital_track, slider_value=self.recital_volume.get())
        #apply fade in/out to recital track
        print("Fade-in:",self.recital_fade_in.get())
        print("Fade-out:",self.recital_fade_out.get())
        recital_track = recital_track.fade_in(self.recital_fade_in.get())
        recital_track = recital_track.fade_out(self.recital_fade_out.get())
        
        recital_track = self.adjust_length(recital_track)
        
        # Combine tracks with left channel selected
        levi_kanal_mix = self.combine_selected_tracks(
            (ambient_track, self.ambient_left_channel),
            (letters_track, self.letters_left_channel),
            (recital_track, self.recital_left_channel),
            pan = -1
        )
        
        # Combine tracks with left channel selected
        desni_kanal_mix = self.combine_selected_tracks(
            (ambient_track, self.ambient_right_channel),
            (letters_track, self.letters_right_channel),
            (recital_track, self.recital_right_channel), pan= 1.0
        )
        
        # Apply fade in/out to ambient track
        #ambient_track = ambient_track.fade_in(self.fade_in_duration)
        #ambient_track = ambient_track.fade_out(self.fade_out_duration)
        
        # Apply fade in/out to letters track
        #letters_track = letters_track.fade_in(self.fade_in_duration)
        #letters_track = letters_track.fade_out(self.fade_out_duration)

        levi_kanal = self.adjust_length(levi_kanal_mix).set_channels(1)
        desni_kanal = self.adjust_length(desni_kanal_mix).set_channels(1)
        
        # Ensure both channels have the same length
        max_length = max(len(levi_kanal or AudioSegment.silent(duration=0)),
                        len(desni_kanal or AudioSegment.silent(duration=0)))
        levi_kanal = (levi_kanal or AudioSegment.silent(duration=max_length)).set_channels(1)[:max_length]
        desni_kanal = (desni_kanal or AudioSegment.silent(duration=max_length)).set_channels(1)[:max_length]
        
        print("Desni kanal:")
        print(f"    -len: {len(desni_kanal)} vzorcev")
        print(f"    -trajanje: {desni_kanal.duration_seconds} sekund")
        print(f"    -sample_width: {desni_kanal.sample_width}")
        print(f"    -frame_rate: {desni_kanal.frame_rate}")
        
        print("Levi kanal:")
        print(f"    -len: {len(levi_kanal)} vzorcev")
        print(f"    -trajanje: {levi_kanal.duration_seconds} sekund")
        print(f"    -sample_width: {levi_kanal.sample_width}")
        print(f"    -frame_rate: {levi_kanal.frame_rate}")
        
        # Combine both channels into one stereo audio track
        stereo_mix = AudioSegment.from_mono_audiosegments(levi_kanal, desni_kanal)

        # Export the stereo audio track to a file
        out_file = "mixdown.wav"
        print("Generating audio file....")
        stereo_mix.export(out_file, format="wav")
        
    def generate(self):
        # Implement the logic to process and mix tracks here
        self.process_audio(self.ambient_file, self.letters_file, self.recital_file)