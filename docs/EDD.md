# EDD - The projection algorithm

## What it does
The algorithm gets a 3D volume M and a valid plane with the corners a1, a2, b, c, and returns
a 2D picture of the cut. A triangle is treated as a trapezoid where a1 and a2 are the same point.

Think of the plane as a sheet of paper. Two lines (rails) go from the top corners down to the
bottom corners. For every row of the picture we stretch a line between the two rails, and we
read the voxel at every step along it.

## Input and output
- Input: the volume M (M[x][y][z]) and the corners a1, a2, b, c.
- Output: a 2D array of 8-bit values.

## Steps
1. Calculate the size of the picture:
   - height = ceil(max(dist(a1,b), dist(a2,c)))
   - width = ceil(max(dist(a1,a2), dist(b,c)))
   - If one of them is 0, return an error frame.
2. Make two lists of numbers from 0 to 1: v with `height` values (how far down we are), and u with `width` values (how far along the row we are).
3. Compute the two rails:
   - left(v) = a1 + v * (b - a1)
   - right(v) = a2 + v * (c - a2)
4. Compute the 3D point of every pixel: point(v, u) = left(v) + u * (right(v) - left(v)). This is done for all pixels at the same time with numpy.
5. Round every point to the closest whole voxel position (x, y, z).
6. If the position is inside M, the pixel gets M[x][y][z]. If it is outside, the pixel stays 0 (black).
7. Scale the picture to 0-255 using its own minimum and maximum, and convert it to 8 bits.
8. Return the picture.

## Pseudo-code
    height = ceil(max(dist(a1,b), dist(a2,c)))
    width  = ceil(max(dist(a1,a2), dist(b,c)))
    for each row, v goes from 0 to 1:
        left  = a1 + v * (b - a1)
        right = a2 + v * (c - a2)
        for each column, u goes from 0 to 1:
            point = left + u * (right - left)
            (x, y, z) = round(point)
            pixel = M[x][y][z] if (x, y, z) is inside M, else 0
    scale all pixels to 0-255
    return the picture

The code does not use these two loops. It calculates all rows and columns in one step with numpy.