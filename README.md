# MODI-SIC ASSEMBLER

The Modi-SIC assembler retains all the instructions and memory variable reserve concepts found in the standard SIC assembler, specifically supporting Format 3 instructions. In addition to these, it also includes support for Format 1 instructions and Immediate Instructions (Format 3), which handle immediate values provided as integers.


## Overview
It reads an assembly program written in Modi-Sic as input in the form of a text file (in.txt). 


It generates five files, and set them in the folder "generated files".
    
    pass_one.txt
    symboltable.txt
    intermediate.txt 
    out_pass2.txt
    HTE_Record.txt


## Project Criteria
+   Ensure that you use a tab separator to divide each column in your input file.


## Installation
1.  Install pandas by running this command
    ```bash
    pip install pandas
    ```
2.  put your input in input.txt
3.  run the project by running this command 

    ```bash
    python main.py
    ```



