# The data we need to retreive.
#1. Total number of votes cast
#2. A complete list of candidates who received votes
#3. Total number of votes each candidate received
#4. Percentage of votes each candidate won
#5. The winner of the election based on popula

# Import the datetime class from the datetime module.
import datetime
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.

print("The time right now is ", now)
import datetime as datetime

now = datetime.datetime.now()
print ("The time right now is", now)

import datetime as dt

now = dt.datetime.now()
print ("The time right now is ", now)
import csv
dir(csv)
dir()
dir(str)
file_to_load = 'Resources/election_results.csv'
# Open the election results and read the file.
election_results = open(file_to_load, 'r')

# To do: perform analysis.

# Close the file.
election_data.close()