# ProCenter

ProCenter is a simple Python program designed to enhance privacy by blocking access to user-specified applications on Windows. It continuously monitors running processes and terminates any that match the specified block list.

## Features

- Blocks access to specified applications.
- Runs continuously and monitors active processes.
- Simple and easy to configure.

## Requirements

- Python 3.x
- [psutil](https://pypi.org/project/psutil/) library

## Installation

1. Clone this repository or download the `procenter.py` file.

2. Install the required Python library:

   ```bash
   pip install psutil
   ```

## Usage

1. Edit the `procenter.py` file to specify the applications you want to block. Modify the `apps_to_block` list with the executable names.

   ```python
   apps_to_block = ["notepad.exe", "calc.exe"]  # Add applications you want to block
   ```

2. Run the program:

   ```bash
   python procenter.py
   ```

3. ProCenter will start running and block the specified applications. Use `Ctrl + C` to stop the program.

## Disclaimer

Please note that ProCenter is intended for personal privacy enhancement and should be used responsibly. Blocking critical system applications may cause instability in your operating system.

## License

This project is licensed under the MIT License.