from tkinter import Tk
from audiomixer import AudioMixerGUI

def main():
    root = Tk()
    audio_mixer = AudioMixerGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()