# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 15:02:18 2024

@author: wayne
"""

import subprocess

def run_all_scripts(scripts):
    for script in scripts:
        print(f"Running {script}...")  # start Script msg
        try:
            # Run each script as a separate process
            subprocess.run(['python', script], check=True)
            print(f"Completed {script}.")  # end script msr
        except subprocess.CalledProcessError as e:
            print(f"Error running '{script}': {e}")

    print("run_all done.")  # done msg

# List of scripts to run in the desired order
scripts_to_run = ['main.py', 'analyze_json.py', 'visualize_lr_vs_arprc.py']

# Run the scripts from 'run_all.py'
if __name__ == "__main__":
    run_all_scripts(scripts_to_run)  # Initiate the script running process
