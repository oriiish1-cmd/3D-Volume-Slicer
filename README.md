# 3D-Volume-Slicer

extracts 2D planar cross sections from 3D volumetric raster data (in NRRD format) and saves the ordered sequence of projections as an MP4 video.

repository: https://github.com/oriiish1-cmd/3D-Volume-Slicer.git
### Installation
Ensure Python 3.10+ is installed ,if not install it.

then install required dependencies:
```bash
pip install numpy pynrrd opencv-python
```
### Usage
Execute the projection pipeline from the command line
```bash
python Ex0.py <file.nrrd> <file.csv> <file.mp4>
```
<file.nrrd>: input 3D volume file.
<file.csv>: CSV containing 3 point or 4 point slice plane coordinates each row. it's need to be isosceles.
<file.mp4>: Output video.
* The input files are placed in the data folder

## Configuration
EPS = 0.001

## Tests
There are 2 csv test files 
```bash
python Ex0.py data/<file.nrrd> data/csv/edge_cases.csv edge_test_output.mp4
python Ex0.py data/<file.nrrd> data/csv/lecturer_example.csv LE_test_output.mp4
```

## Project Structure
 Ex0.py             main script (demo + algorithm)
 data/              all the data, includes NRRD files
 data/csv/          data of csv files (demo and test files)
 data/images/       images
 docs/SRS.md        requirements
 docs/EDD.md        algorithm
 output2            outputfile from thee execution- It is an example
 tests/test_Ex0.py  test file

## LICENSE
this is a open source, you can use it gladdly.
For contact: ORI. mail: oriiish1@gmail.com

