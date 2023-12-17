# Progression Outcome Calculator

This Python program calculates progression outcomes based on user input of PASS, DEFER, and FAIL credits. The outcomes include "Progress," "Progress(module trailer)," "Module Retriever," and "Exclude." The program also provides a histogram of the distribution of outcomes.

## Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [How to Use](#how-to-use)
- [Custom Exceptions](#custom-exceptions)
- [File Handling](#file-handling)
- [Graphical Histogram](#graphical-histogram)

## Introduction

This program takes user input for PASS, DEFER, and FAIL credits and determines the progression outcome based on certain criteria. The outcomes are then stored in a file, and a graphical histogram is displayed.

## Requirements

- Python 3.x
- `graphics` module (make sure to install it using `pip install graphics`)

## How to Use

1. Run the script in a Python environment.
2. Enter the total PASS, DEFER, and FAIL credits when prompted.
3. The program will determine the progression outcome and display it.
4. You can enter multiple sets of data or quit to view the overall results.

## Custom Exceptions

The program defines a custom exception, `OutOfRangeError`, which is raised when credits entered are out of the allowed range.

## File Handling

The program reads and writes data to a file (`data.txt`). It stores each set of credits and outcomes for future reference.

## Graphical Histogram

The program provides a graphical histogram of the distribution of progression outcomes. The bars represent the counts of different outcomes, and the total is displayed for reference.

**Note:** The graphical part of the program requires the `graphics` module, and a window will pop up to display the histogram.Graphics Reference (graphics.py v5) - https://mcsp.wartburg.edu/zelle/python/graphics/graphics.pdf 

Feel free to contribute, report issues, or suggest improvements!

