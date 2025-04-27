# modules/foothold.py
import os
from rich.console import Console
from rich.progress import Progress

console = Console()

def run(target_ip):
    console.rule("[bold blue]CTF AI Assistant - Foothold: Gobuster Scan[/bold blue]")
    console.print(f"[cyan]Target: {target_ip}[/cyan]")

    output_dir = "gobuster_scans"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Default wordlist (you can swap later if needed)
    wordlist = "/usr/share/wordlists/dirb/common.txt"

    # Target URL
    url = f"http://{target_ip}/"

    output_file = f"{output_dir}/{target_ip}_gobuster.txt"

    console.print(f"[yellow]Starting Gobuster with wordlist:[/yellow] {wordlist}")

    gobuster_cmd = f"gobuster dir -u {url} -w {wordlist} -t 50 -o {output_file} --wildcard"

    with Progress() as progress:
        task = progress.add_task("[green]Launching Gobuster...", total=100)
        os.system(gobuster_cmd)
        progress.update(task, advance=100)

    console.print("\n[bold green]Gobuster scan complete![/bold green]")
    console.print(f"[yellow]Results saved to:[/yellow] {output_file}\n")

    # Post-parse output
    try:
        with open(output_file, 'r') as f:
            lines = f.readlines()
            found = [line.strip() for line in lines if "Status: 200" in line or "Status: 403" in line]

        if found:
            console.print("[bold magenta]Interesting Directories/Files Found:[/bold magenta]")
            for entry in found:
                console.print(f"[cyan]{entry}[/cyan]")
        else:
            console.print("[red]No interesting directories found yet.[/red] Try a bigger wordlist!")

    except Exception as e:
        console.print(f"[red]Error reading gobuster output: {e}[/red]")

    console.print("[bold cyan]\nNext step: Manually browse or fuzz discovered directories![/bold cyan]\n")
