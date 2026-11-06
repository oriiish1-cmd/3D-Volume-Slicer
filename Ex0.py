import sys
import csv
import numpy as np
import nrrd
import cv2  # OpenCV for video generation

# EPSILON constant for geometry validation
EPS = 0.001


def main():
    # Enforce correct CLI(command line interface) arguments
    if len(sys.argv) != 4:
        print("Usage: python Ex0.py <file.nrrd> <file.csv> <file.mp4>")
        sys.exit(1)

    nrrd_file = sys.argv[1]
    csv_file = sys.argv[2]
    mp4_file = sys.argv[3]

    print(f"Initialization complete")
    print(f"NRRD: {nrrd_file} | CSV: {csv_file} | Output: {mp4_file}")


if __name__ == "__main__":
    main()


def load_nrrd(file_path):
    """Loads the NRRD file and returns the 3D matrix and its metadata"""
    print(f"Loading NRRD file: {file_path}")
    data, header = nrrd.read(file_path)
    return data, header

def parse_csv_line(line):
    """
    Parses a CSV line into a list of 3D points- x1, y1, z1, x2, y2 , z2,...
    """
    coords = [float(val) for val in line if val.strip()]
    points = []
    for i in range(0, len(coords), 3):
        points.append(np.array([coords[i], coords[i+1], coords[i+2]]))
    return points