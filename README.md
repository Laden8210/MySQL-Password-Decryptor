
# MySQL Workbench Credentials Decryptor

## Description
A Python script to decrypt and display MySQL Workbench credentials from the `workbench_user_data.dat` file. Features include a NASA PH-themed banner, real-time decryption progress, and a styled table output for credentials. Requires `pywin32` and `rich` for functionality and UI enhancements.

## Features
- NASA PH ASCII Banner for a visually appealing UI.
- Real-time progress bar during decryption.
- Styled table output of database credentials.
- Robust error handling for decryption and file parsing.

## Requirements
- **Python 3.x**
- Required Python Libraries:
  - `pywin32`
  - `rich`

Install dependencies using:
```bash
pip install pywin32 rich
```

## Setup
1. Save the script as `workbench.py` in your desired directory.
2. Ensure MySQL Workbench is installed and credentials are saved in the file located at:
   ```
   C:\Users\<YourUsername>\AppData\Roaming\MySQL\Workbench\workbench_user_data.dat
   ```

## Usage
1. Open your terminal or command prompt.
2. Navigate to the script's directory:
   ```bash
   cd path\to\script\directory
   ```
3. Run the script:
   ```bash
   python workbench.py
   ```

## Example Output

### Banner:
```
███╗   ██╗ █████╗ ███████╗ █████╗     ██████╗ ██╗  ██╗
████╗  ██║██╔══██╗██╔════╝██╔══██╗    ██╔══██╗██║ ██╔╝
██╔██╗ ██║███████║███████╗███████║    ██████╔╝█████╔╝ 
██║╚██╗██║██╔══██║╚════██║██╔══██║    ██╔═══╝ ██╔═██╗ 
██║ ╚████║██║  ██║███████║██║  ██║    ██║     ██║  ██╗
╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚═╝     ╚═╝  ╚═╝
MySQL Workbench Credentials Decryptor
```

### Decryption Progress:
```
Decrypting MySQL Workbench data...
[███████████████████████████████████████████████████████] 100%
```

### Table:
```
+----------+----------------+------+----------+----------+
| Database | Host           | Port | Username | Password |
+----------+----------------+------+----------+----------+
| mydb     | localhost:3306 | 3306 | admin    | secret   |
| testdb   | 192.168.1.10   | 3306 | user     | pass123  |
+----------+----------------+------+----------+----------+
```

## License
This script is for educational purposes only. Use responsibly and ensure compliance with all applicable laws and regulations when handling sensitive data.
