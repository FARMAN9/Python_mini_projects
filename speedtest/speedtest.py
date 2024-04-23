import subprocess


def execute_terminal_command(command):
    # Execute the terminal command
    process = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    # Retrieve the output and errors (if any)
    stdout, stderr = process.communicate()
    
    # Check if the command was successful
    if process.returncode == 0:
        print("Command executed successfully:")
        print(stdout)
    else:
        print("Command failed with error:")
        print(stderr)

# Example usage: call the ''speedtest-cli'' command to list files and directories
execute_terminal_command("speedtest-cli --secure")
