# Audio_mixer

Audio Mixer is a simple GUI application built with Tkinter in Python that allows users to load, mix, and adjust audio tracks with various controls like volume, balance, reverb, and fade-in/fade-out effects.

## Installation

To run Audio Mixer, you will need Python installed on your system. Clone the repository to your local machine, and follow the platform-specific instructions below.

### Windows

1. Open Command Prompt as Administrator.
2. Navigate to the cloned repository's directory.
3. Run the batch file to install dependencies and start the application:

```
install_and_run.bat
```


### Unix/Linux

1. Open a terminal window.
2. Navigate to the cloned repository's directory.
3. Make the script executable and run it:

```
chmod +x install_and_run.sh

./install_and_run.sh
```

### macOS

1. Open a terminal window.
2. Navigate to the cloned repository's directory.
3. Make the script executable and run it:

```
chmod +x install_and_run.command
./install_and_run.command
```


## Usage

After starting the application, you will see a GUI with the following options:

- **Load Track**: Load your ambient, letters, and recital tracks.
- **Channel Selection**: Select which audio channel (left or right) the track should play.
- **Volume Control**: Adjust the volume of each track.
- **Reverb Control**: Adjust the reverb effect on the recital and letter tracks.
- **Fade Controls**: Set the fade-in and fade-out durations for the recital track.
- **Generate**: Mixes the tracks and outputs the final audio file.

## Contributing

Contributions to Audio Mixer are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
