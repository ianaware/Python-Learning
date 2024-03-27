import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('C:/Users/ian.w/counts.sqlite')
cur = conn.cursor()

# Drop the table if it already exists
cur.execute('DROP TABLE IF EXISTS Counts')

# Create a new table called "Counts"
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

# Prompt the user to enter the file name
fname = input('Enter file name: ')

# Open the file
fh = open(fname)

# Iterate over each line in the file
for line in fh:
    if line.startswith('From '):  # Checks if the line starts with 'From '
        pieces = line.split()
        if len(pieces) > 1:
            email = pieces[1]  # Assumes the email is the second item

            try:
                # Split the email by '@' and extract the domain
                domain = email.split('@')[1]
                
                # Check if the organization already exists in the table
                cur.execute('SELECT count FROM Counts WHERE org = ?', (domain,))
                row = cur.fetchone()

                # If the organization doesn't exist, insert new row with count = 1
                if row is None:
                    cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (domain,))
                else:
                    # If the organization exists, increment the count by 1
                    cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (domain,))
                
                # Commit the changes to the database
                conn.commit()
            except IndexError:
                # If there's an index error, skip this iteration
                continue

# Close the file
fh.close()

# Select the organization and count the number of emails per org
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

# Execute the SQL query and print the results
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

# Close the cursor and connection
cur.close()
conn.close()