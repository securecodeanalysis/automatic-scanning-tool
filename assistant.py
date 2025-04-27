#!/usr/bin/python
# assistant.py
from rich.console import Console
from rich.progress import track
import time
import argparse
from modules import recon#, foothold, shell, postex, privesc, loot, report

console = Console()

def banner():
    console.print("""
[bold magenta]
   ______   _______   ______    _______     ___   .___________. _______ 
  /  __  \ |   ____| /  __  \  |   ____|   /   \  |           ||   ____|
 |  |  |  ||  |__   |  |  |  | |  |__     /  ^  \ `---|  |----`|  |__   
 |  |  |  ||   __|  |  |  |  | |   __|   /  /_\  \    |  |     |   __|  
 |  `--'  ||  |____ |  `--'  | |  |____ /  _____  \   |  |     |  |____ 
  \______/ |_______| \______/  |_______/__/     \__\  |__|     |_______|
                                                                        
[/bold magenta]
    """)
    console.print("[bold blue]Welcome to CTF AI Assistant![/bold blue]")
    console.print("[bold yellow]Bootstrapping your CTF conquest...[/bold yellow]\n")
    time.sleep(2)

def loading_effect(task_name):
    for _ in track(range(10), description=f"[cyan]{task_name}...[/cyan]"):
        time.sleep(0.1)

def main():
    banner()

    parser = argparse.ArgumentParser(description="CTF AI Assistant for Linux Boot-to-Root challenges.")
    parser.add_argument("--target", required=True, help="Target IP address")
    parser.add_argument("--recon", action="store_true", help="Run smart recon")
    parser.add_argument("--foothold", action="store_true", help="Try foothold attacks")
    parser.add_argument("--shell", action="store_true", help="Generate reverse shells")
    parser.add_argument("--postex", action="store_true", help="Smart enumeration after foothold")
    parser.add_argument("--privesc", action="store_true", help="Analyze for privilege escalation")
    parser.add_argument("--loot", action="store_true", help="Find user/root flags")
    parser.add_argument("--full", action="store_true", help="Run full chain (best for CTFs)")

    args = parser.parse_args()

    if args.full:
        loading_effect("Reconnaissance")
        recon.run(args.target)
        
        loading_effect("Gaining Foothold")
        foothold.run(args.target)

        console.print("[yellow][*] Waiting for user to gain shell manually if needed...[/yellow]")
        input("[bold cyan]Press Enter once shell obtained...[/bold cyan]")

        loading_effect("Post Exploitation Enumeration")
        postex.run()

        loading_effect("Privilege Escalation Analysis")
        privesc.run()

        loading_effect("Flag Hunting")
        loot.run()

        loading_effect("Generating Report")
        report.run()

    else:
        if args.recon:
            loading_effect("Reconnaissance")
            recon.run(args.target)
        if args.foothold:
            loading_effect("Gaining Foothold")
            foothold.run(args.target)
        if args.shell:
            loading_effect("Reverse Shell Payloads")
            shell.run(args.target)
        if args.postex:
            loading_effect("Post Exploitation Enumeration")
            postex.run()
        if args.privesc:
            loading_effect("Privilege Escalation Analysis")
            privesc.run()
        if args.loot:
            loading_effect("Flag Hunting")
            loot.run()
            loading_effect("Generating Report")
            report.run()

if __name__ == "__main__":
    main()
