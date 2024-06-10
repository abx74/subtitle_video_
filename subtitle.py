import subprocess

input_path = r"C:/Users/aa/OneDrive/Desktop/auto-subtitle-main/abc.mp4"  # Use raw string
output_path = r"C:/Users/aa/OneDrive/Desktop/auto-subtitle-main/output/subtitled_video.mp4"  # Use raw string

subprocess.run(["auto_subtitle", input_path, "-o", output_path])
