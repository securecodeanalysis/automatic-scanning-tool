#!/usr/bin/python
# modules/recon.py
import os
from rich.console import Console
from rich.progress import Progress

console = Console()

def run(target_ip):
    console.rule("[bold blue]CTF AI Assistant - Recon Stage[/bold blue]")
    console.print(f"[cyan]Target: {target_ip}[/cyan]")

    output_dir = "scans"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    basic_scan_file = f"{output_dir}/{target_ip}_basic.nmap"
    full_scan_file = f"{output_dir}/{target_ip}_full.nmap"
    vuln_scan_file = f"{output_dir}/{target_ip}_vulners.nmap"

    with Progress() as progress:
        task1 = progress.add_task("[green]Running Quick Service Scan...", total=100)
        os.system(f"nmap -sC -sV -oN {basic_scan_file} {target_ip}")
        progress.update(task1, advance=100)

        task2 = progress.add_task("[green]Running Full TCP Port Scan...", total=100)
        os.system(f"nmap -p- --open -T4 -oN {full_scan_file} {target_ip}")
        progress.update(task2, advance=100)

        task3 = progress.add_task("[green]Running Vulners Script Scan (CVEs)...", total=100)
        os.system(f"nmap --script vulners -sV -oN {vuln_scan_file} {target_ip}")
        progress.update(task3, advance=100)

    console.print("\n[bold green]Recon complete![/bold green]")
    console.print(f"[yellow]Check output in: {output_dir}[/yellow]\n")

    console.print(f"[bold magenta]Summary of Commands Used:[/bold magenta]")
    console.print(f"[blue]Quick Scan:[/blue] nmap -sC -sV -oN {basic_scan_file} {target_ip}")
    console.print(f"[blue]Full TCP Scan:[/blue] nmap -p- --open -T4 -oN {full_scan_file} {target_ip}")
    console.print(f"[blue]Vulners CVE Scan:[/blue] nmap --script vulners -sV -oN {vuln_scan_file} {target_ip}")

    console.print("[bold cyan]\nNext step: Analyze services and exploit![/bold cyan]\n")
