# Hangman Game

This project implements a Hangman game using the Tkinter library for the graphical user interface (GUI). The game allows both single and team modes, where players can guess letters to uncover a hidden word or phrase.

## Features

- **Single Player Mode**: Play the game individually.But due to some issues has been facing a error. 
- **Team Mode**: Multiple teams can play, and scores are kept for each team.
- **Graphical User Interface**: The game uses Tkinter to provide a user-friendly interface.
- **Score Keeping**: Scores are displayed after each game.
- **File Logging**: The sentences used in the game are logged to a file.

## How to Use

1. **Install Python**: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. **Install Tkinter**: Tkinter is included with Python, but if you encounter any issues, you can install it using:
    ```sh
    pip install tk
    ```

3. **Run the Game**: Execute the `hangman_collect.py` script to start the game.
    ```sh
    python hangman_collect.py
    ```

4. **Game Interface**: 
    - A window will appear with buttons for "Single" and "Team" modes.
    - Click "Single" to play individually or "Team" to play with multiple teams.
    - Follow the prompts to enter the sentence to be guessed and make guesses.

5. **Score Display**: After the game, the scores will be displayed in the GUI.

## Limitations

- **Input Validation**: The game currently does not handle repeated guesses or invalid inputs robustly.
- **Single and Team Modes**: The current implementation does not differentiate between single and team modes effectively.
- **Game Logic**: The game logic could be enhanced to provide more features like hints, difficulty levels, and better error handling.

## Future Improvements

- **Enhanced Input Validation**: Improve the input validation to handle repeated guesses and invalid inputs more effectively.
- **Separate Modes**: Clearly separate the logic for single and team modes.
- **Hints and Difficulty Levels**: Add features to provide hints and adjust difficulty levels based on player performance.
- **Better File Handling**: Ensure the file is properly closed and handled to avoid any potential issues.

## Conclusion

This Hangman game provides a basic implementation with a graphical interface using Tkinter. While it has some limitations, it serves as a good starting point for further enhancements and improvements.