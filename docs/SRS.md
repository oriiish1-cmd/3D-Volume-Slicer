## SRS (Software Requirements Specification)

## Introduction

### Purpose
the goal is to takes 3D files cut them to pictures by a plane of  isosceles triangle or  isosceles trapezoid (The plane is determined by 3-4 points) and finally make them into a video.
this system can help doctors to see in one photo all part of the body they need to diagnose.
There used to be a system that looked from above, from the side, and from below. But now it could see regard to wherever they need. not only straight.


### Definitions
- Volume (M): the 3D scan, a matrix M[x][y][z].
- Voxel: one cell of the volume.
- Plane: an isosceles triangle (a, b, c) or an isosceles trapezoid (a1, a2, b, c).
- EPS: the allowed error when comparing lengths, 0.001.
- Error frame: a black 500x500 picture used for a plane that is not valid.

### References
The assignment text and its Q&A, the 3D Slicer project (the sample data), and docs/EDD.md.

## Overall description

### Product perspective
A stand-alone command line program. It is similar to the X/Y/Z views in 3D Slicer, but
the plane can be in any direction.

### Users
- A user who prepares a CSV file and watches the video.
- A developer or checker who runs the demo files.

### Environment
Python 3.10 or newer with numpy, pynrrd and opencv-python, on any operating system.

### Assumptions and constraints
- The size of the volume is at most 1023 in each direction. Voxels are unsigned integers.
- The coordinates in the CSV are voxel positions (x, y, z).
- For a point between voxels, the closest voxel is used.
- The CSV has one plane on each line.

## 3. Specific requirements

### 3.1 Functional requirements
- FR-1: The program reads an NRRD file into a 3D matrix.
- FR-2: The program reads the CSV line by line and skips empty lines. Each line is the number of points (3 or 4) followed by 3 values per point.
- FR-3: If the number of values does not match the number of points, the line is not valid.
- FR-4: With 3 points the order is (a, b, c). With 4 points the order is (a1, a2, b, c). A triangle is handled as a trapezoid where a1 and a2 are the same point.
- FR-5: A plane is valid only if |dist(a1,b) - dist(a2,c)| < EPS and dist(a1,a2) <= dist(b,c).
- FR-6: For a plane that is not valid, the program raises an exception (ValueError).
- FR-7: For each valid plane the program builds a picture as described in docs/EDD.md. Its height is the longer of the two legs, and its width is the longer of the two bases, both rounded up.
- FR-8: Each pixel takes the value of the closest voxel. A point outside the volume gets 0.
- FR-9: The values of each picture are scaled to 0-255 and stored as 8-bit grayscale.
- FR-10: The program writes an MP4 (30 frames per second, grayscale) with one frame per CSV line, in the same order.
- FR-11: For a line that is not valid, the video gets a black 500x500 frame. The other lines are not affected.
- FR-12: The size of the video is the size of the first frame. A frame of a different size is resized to it.
- FR-13: If the NRRD file cannot be read, the program prints "Critical System Error" and the reason, and exits with code 1.
- FR-14: If the number of command line arguments is wrong, the program prints the usage message and exits with code 1.

### External interfaces
- Command line: `python Ex0.py <file.nrrd> <file.csv> <file.mp4>`
- Input files: NRRD and CSV, as described above.
- Output: an MP4 file, and one line on the console for each frame.
- Libraries: pynrrd, numpy, OpenCV.

### Non-functional requirements
- NFR-1: Speed. At least 30 frames per second for a 500x500x500 volume. The assignment's goal is 100. Measured result: <fill in>.
- NFR-2: One bad plane does not stop the program.
- NFR-3: The same input gives the same video.
- NFR-4: The pictures are computed with numpy on whole arrays, not with a Python loop per pixel.

## Appendices

### Use case: make a video from planes
- Actor: the user.
- Before: the NRRD file and the CSV file exist.
- Main flow: the user runs the command. The program loads the volume, then for each CSV line it reads the points, checks them, computes the picture, and finally writes the video.
- Other flow 1: a line is not valid, so a black frame is written and the program goes on.
- Other flow 2: the NRRD file cannot be read, so the program prints an error and stops.

### Data dictionary
- M: the 3D matrix of the scan.
- plane: 3 or 4 points, each one is (x, y, z).
- a1, a2, b, c: the corners of the plane. For a triangle, a1 and a2 are the same point.
- frame: a 2D array of 8-bit values, one picture of the video.
- EPS: 0.001.

### Traceability
- FR-1, FR-13: load_nrrd, main. Checked by running the demo.
- FR-2, FR-3: parse_csv_line. Checked with lecturer_example.csv and edge_cases.csv.
- FR-4, FR-5, FR-6: validate_plane. Checked with edge_cases.csv.
- FR-7, FR-8, FR-9: project_plane. Checked by running the demo.
- FR-10, FR-11, FR-12: main, create_error_frame. Checked with edge_cases.csv.
- NFR-1, NFR-4: project_plane. Checked by the speed measurement in the README.