# **PYTHON AS AN ALTERNATIVE TO AUDIT ELECTION RESULTS**

## ***OVERVIEW***

### The purpose of this analysis is to demonstrate that Python is a very good alternative to MS Excel in automating the vote count audit for the congressional dictrict elections in Colorado. By proving the sucess of the analysis, this method can then be used with confidence in more elections to come.

## ***RESULTS***

### **1. Total vote count**

#### The total number of votes can be obtained by using the following code:
```
# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1
````
#### Which will give us a total count of:



### **2. 
