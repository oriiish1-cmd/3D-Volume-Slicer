import sys
import csv
import numpy as np
import nrrd
import cv2  # OpenCV for video generation

# EPSILON constant for geometry validation
EPS = 0.001



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


def validate_plane(points):
    """
    Validates if the points define a valid plane (isosceles triangle/trapezoid).
    Triangle is like a trapezoid where a1 == a2 to prevent code duplication.
    Returns the unified 4 points (a1, a2, b, c) for the algorithm to use.
    """
    if len(points) == 3:
        a1 = a2 = points[0]
        b = points[1]
        c = points[2]
    elif len(points) == 4:
        a1, a2, b, c = points
    else:
        raise ValueError("Invalid number of points- must be 3 or 4")

    # function included in numpy that calculate distance between 3D points.
    dist_a1b = np.linalg.norm(a1 - b)
    dist_a2c = np.linalg.norm(a2 - c)

    # |dist(a1,b) - dist(a2,c)| < EPS
    if abs(dist_a1b - dist_a2c) >= EPS:
        raise ValueError(f"Not an isosceles shape (diff: {abs(dist_a1b - dist_a2c):.4f} >= EPS).")

    # dist(a1,a2) <= dist(b,c) - The top base must be less than or equal to the bottom base. Its suitable triangle too.
    if np.linalg.norm(a1 - a2) > np.linalg.norm(b - c):
        raise ValueError("Trapezoid base a1-a2 is larger than b-c.")

    return a1, a2, b, c


def create_error_frame(width=500, height=500):
    """Creates a black frame(matrix of zeros) to handle invalid points or invalid geometric shape"""
    return np.zeros((height, width), dtype=np.uint8)


def project_plane(volume, points):
    """
    Core algorithm: Projects the 3D volume onto the given plane using NumPy vectorization.
    Achieves high FPS by computing the entire frame grid mathematically in one go.
    """
    # Validate points and get the unified trapezoid vertices
    a1, a2, b, c = validate_plane(points)

    # Calculate optimal frame dimensions based on real physical distances
    height = int(np.ceil(max(np.linalg.norm(a1 - b), np.linalg.norm(a2 - c))))
    width = int(np.ceil(max(np.linalg.norm(a1 - a2), np.linalg.norm(b - c))))

    # S= height * width
    if height == 0 or width == 0:
        return create_error_frame()

    # Vectorization: Create grids for, interpolation parameters
    # v represents vertical progression (0 to 1), u represents horizontal progression (0 to 1)
    v = np.linspace(0, 1, height)[:, np.newaxis, np.newaxis]  # Shape: (height, 1, 1)
    u = np.linspace(0, 1, width)[np.newaxis, :, np.newaxis]  # Shape: (1, width, 1)

    # Reshape points for NumPy broadcasting- (height , width, 3D: x,y,z)
    a1_v = np.array(a1).reshape(1, 1, 3) 
    a2_v = np.array(a2).reshape(1, 1, 3)
    b_v = np.array(b).reshape(1, 1, 3)
    c_v = np.array(c).reshape(1, 1, 3)

    # Interpolate the 3D plane coordinates using bilinear interpolation
    left_edge = a1_v + v * (b_v - a1_v)
    right_edge = a2_v + v * (c_v - a2_v)
    grid_3d = left_edge + u * (right_edge - left_edge)

    # Round the theoretical 3D coordinates to integer indices for array fetching
    coords = np.round(grid_3d).astype(int)
    x, y, z = coords[:, :, 0], coords[:, :, 1], coords[:, :, 2]

    # Hide out of bounds coordinates to strictly prevent crashes
    max_x, max_y, max_z = volume.shape
    valid_mask = (x >= 0) & (x < max_x) & (y >= 0) & (y < max_y) & (z >= 0) & (z < max_z)

    # Initialize a black frame
    frame = np.zeros((height, width), dtype=np.float32)

    # Pull all valid pixels in one operation
    frame[valid_mask] = volume[x[valid_mask], y[valid_mask], z[valid_mask]]

    # Normalize to uint8 (0-255) for OpenCV compatibility
    frame_normalized = cv2.normalize(frame, None, 0, 255, cv2.NORM_MINMAX)
    return frame_normalized.astype(np.uint8)

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

    try:
        # Load Volume
        volume, header = load_nrrd(nrrd_file)

        # Prepare Video Writer parameters
        fps = 30 ##  The velocity that the video plays
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        video_writer = None

        print(f"Reading planes from: {csv_file}")
        # Make sure that the csv file will close automatically (Also there will be an error).
        with open(csv_file, 'r') as f:
            reader = csv.reader(f)

            # Move every row on the csv and give the num of the current row
            for row_idx, row in enumerate(reader):
                if not row:
                    continue  # Skip empty lines

                try:
                    points = parse_csv_line(row)

                    # Calculate the projection
                    frame = project_plane(volume, points)
                    print(f"Frame {row_idx + 1}: Rendered successfully.")

                except Exception as e:
                    # Create a black error frame if points are invalid
                    print(f"Frame {row_idx + 1}: ERROR - {str(e)}. Generating error frame.")
                    frame = create_error_frame()

                # Initialize video writer based on the first processed frame's dimensions
                if video_writer is None:
                    height, width = frame.shape
                    video_writer = cv2.VideoWriter(mp4_file, fourcc, fps, (width, height), isColor=False)

                # Resize if the next frames have different dimensions (for video stability)
                if frame.shape != (height, width):
                    frame = cv2.resize(frame, (width, height), interpolation=cv2.INTER_NEAREST)

                video_writer.write(frame)

        # Release resources
        if video_writer:
            video_writer.release()
        print(f"Processing complete. Video saved to {mp4_file}")

    except Exception as e:
        print(f"Critical System Error: {str(e)}") # Like if the NRRD file does not exist on the computer at all, or if memory has run out
        sys.exit(1)


if __name__ == "__main__":
    main()