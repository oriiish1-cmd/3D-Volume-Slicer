import sys
import csv
import numpy as np
import nrrd
import cv2  # OpenCV for video generation

# EPSILON constant for geometry validation
EPS = 0.001


def main():
    # Enforce correct CLI arguments
    if len(sys.argv) != 4:
        print("Usage: python Ex0.py <file.nrrd> <file.csv> <file.mp4>")
        sys.exit(1)

    nrrd_file = sys.argv[1]
    csv_file = sys.argv[2]
    mp4_file = sys.argv[3]

    print(f"Initialization complete.")
    print(f"NRRD: {nrrd_file} | CSV: {csv_file} | Output: {mp4_file}")


if __name__ == "__main__":
    main()