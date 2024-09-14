# DDOS URL Pinger - Documentation

This program pings a specified URL multiple times using the `requests` library in Python. It uses multi-threading to send requests concurrently and checks the response status to determine if the URL is reachable.

## Requirements

- Python 3.x
- `requests` library version 2.32.3

## Installation

1. **Install Python**: Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. **Install Dependencies**: Use `pip` to install the required dependencies. Open a terminal and run:

   ```bash
   pip install requests==2.32.3
   ```

## Usage

### Running with `ddosOn.bat`

1. **Run the Batch File**: Simply double-click the `ddosOn.bat` file. This batch file is designed to execute the Python program automatically without requiring you to use the command line.
   
   - The batch file will automatically change to the directory where the Python script is located and execute `main.py`.
   - Ensure Python is correctly installed and accessible through the system's PATH environment variable.

2. **User Input**: After running the batch file, you will be prompted to:
   - Enter the URL you wish to ping.
   - Enter the number of threads to use (default is 4 if no number is given).

### Explanation (Optional)
While using `ddosOn.bat` does not require command-line interaction, you can manually navigate to the directory containing `main.py` and run the following command if preferred:

```bash
python main.py
```

## Notes

- The program continuously pings the URL as long as it remains reachable (HTTP status code 200). If the URL becomes unreachable, the program will stop sending requests.
- If the URL is invalid or does not exist, the program will notify you immediately.
  
