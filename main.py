import psutil

def list_processes():
    print(f"{'PID':<10} {'Name':<25} {'Status':<15} {'Memory (MB)':<15}")
    print("=" * 70)
    for proc in psutil.process_iter(['pid', 'name', 'status', 'memory_info']):
        try:
            # Getting process details
            pid = proc.info['pid']
            name = proc.info['name']
            status = proc.info['status']
            memory_mb = proc.info['memory_info'].rss / (1024 * 1024)  # Convert bytes to MB
            
            # Displaying process details
            print(f"{pid:<10} {name:<25} {status:<15} {memory_mb:<15.2f}")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass  # Skip processes that are no longer running or inaccessible

if __name__ == "__main__":
    list_processes()
