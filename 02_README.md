H*eart Curve Simulation (Python Turtle)*

This project draws a parametric heart curve using Python’s built-in Turtle graphics module. The curve is generated from mathematical equations and rendered smoothly through multiple calculated points.

$*Features:*$

Uses parametric equations to define X and Y coordinates

Produces a smooth heart outline with 720 calculated points

Runs using only standard Python libraries (no external dependencies)

Simple structure suitable for learning and experimentation


*Mathematical Model:*

The program uses the following parametric equations-

                              𝑥=16 sin^3(𝑡)

                    y=13cos(t)−5cos(2t)−2cos(3t)−cos(4t)

Values of 𝑡 range from 0 to 2𝜋, producing a complete heart shape.


*Code Outline:*

The program-

Configures a Turtle drawing window

Converts parametric values into scaled coordinates

Draws the shape by connecting points sequentially

The full script is included in this repository.


*Requirements:*

Python 3.x

Turtle module (included with Python standard library)


*How To Run:*

Use the following command to execute the program-

                        python heart_sim_02.py


*Notes:*

The variable scale controls the size of the heart

Increasing the number of calculation steps will improve curve smoothness

Line color and background color can be adjusted in the script


*Purpose:*

This program demonstrates how mathematical equations can be visualized through Python Turtle. It can be used for practice, education, or graphical experimentation.


*License:*

This project is open for modification and use.
