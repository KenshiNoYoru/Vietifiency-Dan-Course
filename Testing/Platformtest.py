import platform

# Get system information
system = platform.system()
release = platform.release()
version = platform.version()
architecture = platform.machine()
processor = platform.processor()

# Print system information
print(f"System: {system}")
print(f"Release: {release}")
print(f"Version: {version}")
print(f"Architecture: {architecture}")
print(f"Processor: {processor}")
