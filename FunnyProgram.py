import os,  base64, webbrowser, platform

if platform.system() in ["Linux","Darwin"]:
  webbrowser.open(base64.b64decode('aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj1kUXc0dzlXZ1hjUQ==').decode())
else:
  os.system(f"start {base64.b64decode('aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj1kUXc0dzlXZ1hjUQ==').decode()}")
