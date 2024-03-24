import subprocess

banner = """
    ██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗  ██╗ ██████╗ ██╗   ██╗███╗   ██╗██████╗  v1.01
    ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██║  ██║██╔═══██╗██║   ██║████╗  ██║██╔══██╗
    ███████║███████║██║     █████╔╝ ███████║██║   ██║██║   ██║██╔██╗ ██║██║  ██║    
    ██╔══██║██╔══██║██║     ██╔═██╗ ██╔══██║██║   ██║██║   ██║██║╚██╗██║██║  ██║
    ██║  ██║██║  ██║╚██████╗██║  ██╗██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║██████╔╝
    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═════╝  by TechSafeguard Solutions
"""
print(banner)


print("Press r to use HackHoundPS for Reconnaissance and Scanning")
print("Press v to use HackHoundVS for Vulnerability Sacnning and Report")
print("Prsss e to use HackHoundEX for Exploitation")
print("Prsee p to use HackHoundPE for PostExploitation")
key = input("Enter a key: ")

if key.lower() == 'r':
        # Execute HackHound_PortScanner.py
        import subprocess
        subprocess.run(["python", "HackHoundPS.py"])

if key.lower() == 'v':
        # Execute HackHound_Vulnerability_Scanner.py
        import subprocess
        subprocess.run(["python", "HackHoundVS.py"])

if key.lower() == 'e':
        # Execute HackHound_Exploitation.py
        import subprocess
        subprocess.run(["python", ""])


