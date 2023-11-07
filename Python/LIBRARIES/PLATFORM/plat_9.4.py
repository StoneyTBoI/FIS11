import platform

print("Betriebssystem: ",platform.platform(), end="\n")
print("Zuständiger Prozessor: ",platform.machine(), end="\n")
print("Prozessor: ",platform.processor(), end="\n")
print("Systemname: ",platform.system(), end="\n")
print("Version: ",platform.version(), end="\n")