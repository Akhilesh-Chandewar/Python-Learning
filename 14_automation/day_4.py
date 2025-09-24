import psutil
import os
import time


def clear_screen():
    # Works on Windows (cls) and Linux/Mac (clear)
    os.system("cls" if os.name == "nt" else "clear")


def bytes_to_gb(bytes_value):
    return bytes_value / 1e9  # convert to GB


def show_stats():
    # CPU
    cpu = psutil.cpu_percent(interval=1)

    # RAM
    ram = psutil.virtual_memory()
    ram_percent = ram.percent
    ram_total = bytes_to_gb(ram.total)
    ram_used = bytes_to_gb(ram.used)

    # Disk
    disk = psutil.disk_usage("/")
    disk_percent = disk.percent
    disk_total = bytes_to_gb(disk.total)
    disk_used = bytes_to_gb(disk.used)

    print("=" * 50)
    print("      📊 Real-Time System Monitor")
    print("=" * 50)
    print(f"🖥️  CPU Usage  : {cpu}% {'⚠️ HIGH!' if cpu > 80 else ''}")
    print(
        f"💾 RAM Usage  : {ram_percent}% ({ram_used:.2f} GB / {ram_total:.2f} GB) {'⚠️ HIGH!' if ram_percent > 80 else ''}"
    )
    print(f"📂 Disk Usage : {disk_percent}% ({disk_used:.2f} GB / {disk_total:.2f} GB)")
    print("=" * 50)


if __name__ == "__main__":
    try:
        while True:
            clear_screen()
            show_stats()
            time.sleep(2)  # refresh interval
    except KeyboardInterrupt:
        print("\n✅ Monitoring stopped by user.")
