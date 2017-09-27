# Udacity Full Stack Web Developer Nanodegree Project 3.1 (Movie trailer)
This program answers some analytical questions about a theoretical news website by running SQL queries against the website database.

### Questions answered
- What are the most popular three articles of all time?
- Who are the most popular article authors of all time?
- On which days did more than 1% of requests lead to errors?

### Running the program
1. Logon to your Linux machine which holds the PGSQL database news (populated from *newsdata.sql*) via the CLI
2. Ensure that *Python 2.7* or higher is installed on the machine
3. Ensure that *psycopg2* Python package is installed
4. Copy *news_reports.py* from this project to your machine 
5. Set your CLI working directory to the one containing *news_reports.py*
5. Run command "python news_reports.py". If everything is set up correctly, the program will print out the answer to each question sequentially, in the same order as listed here (see sample-output.txt for a sample of what to expect)