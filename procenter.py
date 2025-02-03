import os
import time
import subprocess
import psutil
from datetime import datetime

class ProCenter:
    def __init__(self, block_list):
        self.block_list = block_list

    def block_applications(self):
        print("ProCenter is running. Blocking specified applications...")
        while True:
            for process in psutil.process_iter(['pid', 'name']):
                if process.info['name'] in self.block_list:
                    print(f"[{datetime.now()}] Blocking application: {process.info['name']}")
                    os.system(f"taskkill /F /PID {process.info['pid']}")
            time.sleep(5)

    def run(self):
        try:
            print("ProCenter started. Press Ctrl+C to stop.")
            self.block_applications()
        except KeyboardInterrupt:
            print("ProCenter stopped.")

if __name__ == "__main__":
    apps_to_block = ["notepad.exe", "calc.exe"]  # Add applications you want to block
    pro_center = ProCenter(apps_to_block)
    pro_center.run()