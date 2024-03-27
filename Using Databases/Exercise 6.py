import sqlite3

# Connect to the database
conn = sqlite3.connect('C:/Users/ian.w/OneDrive - AWARE CORPORATION LIMITED/GitHub/Python/Python-Learning/Using Databases/trackdb2.sqlite')
cur = conn.cursor()

# Drop existing tables if they exist and create new tables
cur.executescript('''
    DROP TABLE IF EXISTS Artist;
    DROP TABLE IF EXISTS Album;
    DROP TABLE IF EXISTS Genre;
    DROP TABLE IF EXISTS Track;

    CREATE TABLE Artist (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name    TEXT UNIQUE
    );

    CREATE TABLE Genre (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name    TEXT UNIQUE
    );

    CREATE TABLE Album (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        artist_id  INTEGER,
        title   TEXT UNIQUE
    );

    CREATE TABLE Track (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT  UNIQUE,
        album_id  INTEGER,
        genre_id  INTEGER,
        len INTEGER, rating INTEGER, count INTEGER
    );
''')

# Open the CSV file containing track information
handle = open('C:/Users/ian.w/OneDrive - AWARE CORPORATION LIMITED/GitHub/Python/Python-Learning/Using Databases/tracks.csv')

# Iterate over each line in the file
for line in handle:
    line = line.strip()
    pieces = line.split(',')

    # Skip lines with less than the expected pieces of data
    if len(pieces) < 6:  # Adjust based on the number of columns in your CSV
        continue

    # Extract the relevant information from the line
    name, artist, album, count, ratings, length, genre = pieces  # Add more variables if your CSV has more columns

    # Insert or ignore the artist into the Artist table
    cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (artist,))
    cur.execute('SELECT id FROM Artist WHERE name = ?', (artist,))
    artist_id = cur.fetchone()[0]

    # Insert or ignore the album into the Album table
    cur.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?, ?)', (album, artist_id))
    cur.execute('SELECT id FROM Album WHERE title = ?', (album,))
    album_id = cur.fetchone()[0]

    # Insert or ignore the genre into the Genre table
    cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)', (genre,))
    cur.execute('SELECT id FROM Genre WHERE name = ?', (genre,))
    genre_id = cur.fetchone()[0]

    # Insert or replace the track into the Track table
    cur.execute('INSERT OR REPLACE INTO Track (title, album_id, genre_id, len, rating, count) VALUES (?, ?, ?, ?, ?, ?)', 
                (name, album_id, genre_id, length, ratings, count))

    # Commit the changes made to the database
    conn.commit()

# Close the connection to the database
conn.close()