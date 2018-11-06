# Table of Contents
1. [Problem](README.md#problem)
2. [Approach](README.md#approach)
3. [Run Instructions](README.md#run-instructions)
4. [More tests](README.md#more-tests)
5. [Notes on style](README.md#notes-on-style)

# Problem

A client was requesting a re-runnable report on H1B visas. Questions arose around which states and which occupations were the most popular, and which resulted in the most CERTIFIED application outcomes. 

Client was seeking an approach that would tally and sort Top 10 approach, for top 10 occupations and top 10 states, respectively. 

Source data was available from Department of Labor.

# Approach

Semicolon separated value format files were available from an intermediary data provider. This was used as the input for the reports. 

Approach in the code was basically to split the problem up into different components responsible for different layers of an ETL-style pipeline. 
Raw data (SlimRow) was pulled from the broad raw records in the file. 
Records were filtered on criteria (certification status).  
Counts were tallied in a dictionary.  
Aggregate tabulations were then performed.  
Broadly, separation of concerns was observed by separating the code into two main parts: 1) reading the raw file and getting the counts 2) output formatting and writing to destination file(s). 

# Run instructions

usage: reportrunner.py <inputfile> <occupationsoutputfile> <statessoutputfile>

From the src folder:
python ./src/insightH1bReport/insightH1bReport/ReportRunner.py ./input/h1b_input.csv ./output/top_10_occupations.txt ./output/top_10_states.txt

# More tests 

Unit tests were added using pytest. 

As such, those unit tests can be performed with the following type of commands:  

python -m pytest Tests/DataContractTests.py  
python -m pytest Tests/ReportReaderTests.py  
python -m pytest Tests/ReportWriterTests.py  

# Notes on style

I do c# during the day. So, the casing and conventions here follow more closely to typical c# style.   
If I were to redo this project, I would take the opportunity to follow a more pythonic naming scheme and use a_lot_more_underscores so it is easier for a python community member to use and modify.
