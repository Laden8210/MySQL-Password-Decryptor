import os
import re
import time  # Ensure the time module is imported
import win32crypt  # Requires pywin32 package
from rich.console import Console
from rich.table import Table
from rich.progress import Progress
from rich.panel import Panel
from rich.text import Text

# Initialize console
console = Console()

# Regex pattern for parsing workbench user data
_group = '(?P<{}>{}+)'
WORKBENCH_PATTERN = '{dbm}@{host}:{port}\2{user}\3{password}'.format(
    dbm=_group.format('dbm', r'\w'),
    host=_group.format('host', r'[\w\.-]'),
    port=_group.format('port', r'\d'),
    user=_group.format('user', r'[\w\.-]'),
    password=_group.format('password', '.'),
)

def display_nasa_ph_banner():
    """
    Display NASA PH banner.
    """
    banner_text = Text.from_markup(
        "[bold blue]\n"
         "███╗   ██╗ █████╗ ███████╗ █████╗ \n"
            "████╗  ██║██╔══██╗██╔════╝██╔══██╗\n"
            "██╔██╗ ██║███████║███████╗███████║\n"
            "██║╚██╗██║██╔══██║╚════██║██╔══██║\n"
            "██║ ╚████║██║  ██║███████║██║  ██║\n"
            "╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝\n"
            "██████╗  ██╗  ██╗    ██╗██████╗ \n"
            "██╔══██╗ ██║  ██║    ██║██╔══██╗\n"
            "██████╔╝ ███████║    ██║██████╔╝\n"
            "██╔═══╝  ██╔══██║    ██║██╔═══╝ \n"
            "██║      ██║  ██║    ██║██║     \n"
            "╚═╝      ╚═╝  ╚═╝    ╚═╝╚═╝     \n\n"
        "[cyan]MySQL Workbench Credentials Decryptor[/cyan]"
    )
    console.print(Panel.fit(banner_text, style="blue"))

def decrypt_workbench_data(file_path):
    """
    Decrypt the MySQL Workbench user data.
    """
    try:
        with open(file_path, 'rb') as file:
            encrypted_data = file.read()

        decrypted_data = win32crypt.CryptUnprotectData(encrypted_data, None, None, None, 0)
        return decrypted_data[1].decode('utf-8').split('\n')[:-1]
    except Exception as e:
        console.print(f"[red]Error reading or decrypting file:[/red] {str(e)}")
        return []

def parse_and_display_data(decrypted_lines):
    """
    Parse decrypted data and display it in a styled table.
    """
    table = Table(title="MySQL Workbench Credentials", show_lines=True)
    table.add_column("Database", style="cyan", no_wrap=True)
    table.add_column("Host", style="magenta")
    table.add_column("Port", style="green")
    table.add_column("Username", style="yellow")
    table.add_column("Password", style="red")

    for line in decrypted_lines:
        match = re.match(WORKBENCH_PATTERN, line)
        if match:
            dbm = match.group("dbm")
            host = match.group("host")
            port = match.group("port")
            user = match.group("user")
            password = match.group("password")
            table.add_row(dbm, f"{host}:{port}", port, user, password)
        else:
            console.print(f"[red]Failed to parse line:[/red] {line}")

    console.print(table)

def main():
    """
    Main function to read and display MySQL Workbench user data.
    """
    # Display NASA PH banner
    display_nasa_ph_banner()

    # File path
    file_path = os.path.join(os.getenv('APPDATA'), 'MySQL/Workbench/workbench_user_data.dat')

    console.print("[cyan]Decrypting MySQL Workbench data...[/cyan]")
    with Progress() as progress:
        task = progress.add_task("[green]Decrypting...", total=100)
        decrypted_lines = decrypt_workbench_data(file_path)
        for _ in range(100):
            progress.update(task, advance=1)
            time.sleep(0.01)  # Simulate loading time

    if decrypted_lines:
        console.print("[bold green]Decryption successful![/bold green]")
        parse_and_display_data(decrypted_lines)
    else:
        console.print("[bold red]No data found or decryption failed.[/bold red]")

if __name__ == '__main__':
    main()
