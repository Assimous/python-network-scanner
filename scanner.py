import socket
import concurrent.futures
from rich.console import Console
from rich.table import Table
import time

console = Console()

def get_banner(ip, port):
    """Attempt to grab the banner to identify the service version."""
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        s.send(b'WhoAreYou\r\n')
        banner = s.recv(1024).decode('utf-8', errors='ignore').strip()
        s.close()
        return banner[:50] if banner else "Service Unknown"
    except:
        return "No Banner/Hidden"

def scan_port(ip, port):
    """Scan a single port and return its status."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            banner = get_banner(ip, port)
            sock.close()
            return port, "OPEN", banner
        sock.close()
    except Exception:
        pass
    return None

def main(target_ip, start_port, end_port):
    console.print(f"\n[bold blue][*] Starting Advanced Scan on {target_ip}[/bold blue]")
    console.print(f"[*] Scanning ports {start_port} to {end_port}...\n")
    
    start_time = time.time()
    open_ports = []

    # Using ThreadPoolExecutor for fast concurrent scanning
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = {executor.submit(scan_port, target_ip, port): port for port in range(start_port, end_port + 1)}
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                open_ports.append(result)

    end_time = time.time()

    # Displaying results in a professional table
    table = Table(title=f"Scan Results for {target_ip}")
    table.add_column("PORT", justify="right", style="cyan", no_wrap=True)
    table.add_column("STATUS", style="green")
    table.add_column("SERVICE / BANNER", style="magenta")

    if open_ports:
        for port, status, banner in sorted(open_ports):
            table.add_row(str(port), status, banner)
        console.print(table)
    else:
        console.print("[bold red][-] No open ports found in the specified range.[/bold red]")

    console.print(f"\n[bold green][+] Scan completed in {round(end_time - start_time, 2)} seconds.[/bold green]")

if __name__ == "__main__":
    # Defaulting to localhost for safety, but can be modified via CLI args in future updates
    target = "127.0.0.1" 
    main(target, 1, 1024)
