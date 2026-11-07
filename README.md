# 3D-Volume-Slicer

extracts 2D planar cross sections from 3D volumetric raster data (in NRRD format) and saves the ordered sequence of projections as an MP4 video.

the goal is to takes 3D files cut them to pictures by a plane of  isosceles triangle or  isosceles trapezoid (The plane is determined by 3-4 points) and finally make them into a video.
this system can help doctors to see in one photo all part of the body they need to diagnose.
There used to be a system that looked from above, from the side, and from below. But now it could see regard to wherever they need.



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

## Project Structure

## LICENSE
p

תיאור קצר (What it is): תיאור המוצר והמטרה שלו במשפט אחד

התחלה מהירה (Quick start): הוראות פשוטות להתקנה והרצה ראשונית

דוגמת שימוש (Usage example): דוגמת קוד או פקודה להפעלת המערכת

הגדרות וסביבה (Configuration & Environment): פירוט משתני סביבה ודרישות קונפיגורציה

הרצת בדיקות (How to run tests): ההנחיות והפקודות להרצת הבדיקות

מבנה הפרויקט (Project structure): הסבר על חלוקת התיקיות והקבצים במאגר

תרומה לפרויקט (How to contribute): הנחיות למפתחים המעוניינים לתרום לקוד

רישיון ויצירת קשר (License & Contact): סוג הרישיון (כגון MIT) ופרטי ליצירת קשר
.