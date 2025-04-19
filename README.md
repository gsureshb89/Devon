# Run log_analyzer script:
========================
 - python .\log_analyzer.py --logfile app.log
 - python .\log_analyzer.py --logfile app.log --start "2023-03-01 08:15:27" --end "2023-03-01 09:15:20"

# Run test cases:
===============
 - python -m unittest .\log_analyzer.py


# Project Description:
===================
The Log File Analyzer:
○ Write a script (log_analyzer.py) that reads a text file, line by line, from the current
directory (e.g., app.log).
○ Extract the four pieces of information from each line:
■ timestamp
■ service_name
■ log_level
■ message
○ Handle malformed lines gracefully (e.g., lines that don’t fit the expected pattern).
Log them or skip them with a meaningful warning.

2. Data Aggregation &amp; Analysis
○ Tally the number of log entries by log level (e.g., INFO, ERROR, WARN)
○ Tally the number of log entries by service (e.g., ServiceA, ServiceB)
○ Identify the most common ERROR message (by exact string match)
3. Outputs
○ Print or output a short summary that includes:
■ How many lines were INFO, ERROR, WARN, etc.
■ How many lines came from each service
■ The most common ERROR message (and how many times it appeared)
○ Format the summary in a readable way (console, CSV, or JSON—your choice).
4. Error Handling

○ Assume the file might contain unexpected/invalid lines (wrong format, missing
fields).
○ Your script shouldn’t crash; it should log or report an error about those lines and
move on.
5. Code Structure
○ Demonstrate reasonable Python structure (functions and/or classes as needed).
○ Include docstrings or comments to explain what each function does, what inputs
it expects, and what outputs it returns.

6. Bonus (Optional)
○ Add a function that, given a date/time range (e.g., start and end), filters the log
entries and returns only the lines in that range. This can be used to produce a
filtered summary.
○ Provide one or two unit tests (e.g., using unittest or pytest) that confirm your
parsing logic is correct.

Deliverables
1. The Script (log_analyzer.py), runnable from the command line.
2. A Sample Log File (a small app.log with at least a few dozen lines) to test against.
3. Output (printed summary, CSV, or JSON) showing aggregated log stats.
4. Short Documentation or docstrings explaining how to run and what assumptions were
made.