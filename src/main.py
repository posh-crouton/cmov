#!/bin/python3
import os, fnmatch, subprocess, math, json, sys, tqdm
from typing import List 

def find_files_matching_pattern(directory: str, *patterns: List[str]):
    ret: List[str] = []
    tree = os.walk(directory)
    if "--progress" in sys.argv or "-p" in sys.argv:
        tree = tqdm.tqdm(tree)

    for root, _, files in tree:
        for file in files: 
            if any(fnmatch.fnmatch(file, pattern) for pattern in patterns):
                ret.append(os.path.join(root, file))

                if "-v" in sys.argv or "--verbose" in sys.argv: 
                    print(f"Found {len(ret)} files", end="\r")
    return ret 

def get_video_duration(file_path):
    try:
        result = subprocess.run(
            [
                'ffprobe',
                '-v', 'error',  
                '-show_entries', 'format=duration',  
                '-of', 'json',  
                file_path
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        metadata = json.loads(result.stdout)
        duration = float(metadata['format']['duration'])
        return math.floor(duration)
    
    except (KeyError, ValueError, FileNotFoundError, json.JSONDecodeError) as e:
        raise RuntimeError(f"Failed to get video duration: {e}")

def seconds_to_hhmmss(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def main():

    if len(sys.argv) == 1:
        print(f"Usage: {sys.argv[0]} <directory>")
        exit(1)

    files = find_files_matching_pattern(sys.argv[1], 
        "*.mp4", "*.mkv", "*.avi", "*.mov", "*.wmv", "*.flv", "*f4v", "*.mpg", "*.mpeg", "*.gif", "*.webm", "*.avi", "*.wmv", "*.yuv", "*.m4v", "*.3gp", "*.3g2")

    if "-v" in sys.argv or "--verbose" in sys.argv: 
        print()

    total: int = 0

    if "--progress" in sys.argv or "-p" in sys.argv:
        files = tqdm.tqdm(files)

    i: int = 0
    for file in files: 
        i += 1
        total += get_video_duration(file)
        if "-v" in sys.argv or "--verbose" in sys.argv: 
            print(f"{i}/{len(files)}: Running total: {seconds_to_hhmmss(total)} ({total}s)", end="\r")


    if "-v" in sys.argv or "--verbose" in sys.argv: 
        print()
    
    if "-s" in sys.argv or "--seconds" in sys.argv:
        print(total)
    else:
        print(seconds_to_hhmmss(total))

if __name__ == "__main__": 
    main()
