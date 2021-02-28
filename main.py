import requests, json, sys

from rich.console import Console
from rich import pretty
from rich.table import Table
from rich import print
from colorama import Fore

console = Console()

CONFIG = {
    "api_key": "YOUR_API_KEY_HERE" # change here
}

class FedSearch():
    @staticmethod
    def search(term:str):
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("IP", style="dim", width=25)
        table.add_column("Email", style="dim", width=50)
        table.add_column("Username", style="dim", width=30)
        table.add_column("Password", style="dim", width=100)
        table.add_column("Token", style="dim", width=50)
        table.add_column("Database", style="dim", width=25)

        DATA = {'search': term, 'key': CONFIG['api_key'], 'submit': ''}
        r = requests.post(url='https://fedsearch.cf/API/search_api.php', data=DATA).text
        
        json_all = json.loads(r)

        for rows in json_all:
            table.add_row(
                rows['ip'],
                rows['email'],
                rows['username'],
                rows['password'],
                rows['token'],
                rows['database'],
            )
        
        return table

    
if __name__ == "__main__":

    while True:
        user_input = input(f"{Fore.CYAN}fedsearch{Fore.MAGENTA}#{Fore.RESET} ")
        args = user_input.split()
        
        if args[0] == "search":
            DBSearch = FedSearch.search(args[1])
            console.print(DBSearch)

        if args[0] == "exit":
            exit()
    
