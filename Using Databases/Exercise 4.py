import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('C:\\Users\\ian.w\\emaildb.sqlite')
cur = conn.cursor()

# Drop the table if it already exists
cur.execute('''
            DROP TABLE IF EXISTS Counts''')

# Create a new table called "Counts" with columns "email" and "count"
cur.execute('''
            CREATE TABLE Counts (email TEXT, count INTEGER)''')

# Prompt the user to enter the file name
fname = input('Enter file name: ')

# Open the file
fh = open(fname)

# Iterate over each line in the file
for line in fh:
    # Check if the line starts with 'From: '
    if not line.startswith('From: '):
        continue
    
    # Split the line into pieces
    pieces = line.split()
    
    # Extract the email address from the line
    email = pieces[1]
    
    # Check if the email address already exists in the table
    cur.execute('SELECT count FROM Counts WHERE email = ?', (email,))
    row = cur.fetchone()
    
    # If the email address doesn't exist, insert a new row with count = 1
    if row is None:
        cur.execute('''
                    INSERT INTO Counts (email, count) VALUES (?, 1)''', (email,))
    # If the email address already exists, increment the count by 1
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))
    
    # Commit the changes to the database
    conn.commit()

# Select the top 10 email addresses with the highest count
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

# Execute the SQL query and print the results
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
    
cur.close()