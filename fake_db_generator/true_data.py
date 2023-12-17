import sqlite3

# Step 1: Connect to the database (creates the database if it doesn't exist)
conn = sqlite3.connect('data.db')

# Step 2: Create a cursor to execute SQL commands
cursor = conn.cursor()

# Step 3: Create the "Users" table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        address TEXT,
        code TEXT,
        iban TEXT
    )
''')

# Step 4: Insert the provided data into the table
data = [
    (1, 'Giulia Rossi', 'giuliarossi@example.com', 'Via Roma, 123 20121, Milano (MI)', 'AB123CD', 'IT12A3456789012345678901234'),
    (2, 'Luca Ferrari', 'lucacavalli@example.org', 'Piazza del Popolo, 7 00187, Roma (RM)', 'XY456ZA', 'IT56B7890123456789012345678'),
    (3, 'Alessia Moretti', 'alessiamoretti@example.net', 'Corso Vittorio Emanuele, 15 10123, Torino (TO)', 'CD789EF', 'IT34C9012345678901234567890'),
    (4, 'Marco Bianchi', 'marcobianchi@example.com', 'Viale dei Giardini, 32 40123, Bologna (BO)', 'FG012HI', 'IT78D2345678901234567890123'),
    (5, 'Anna Ricci', 'annaricci@example.org', 'Via Garibaldi, 99 16126, Genova (GE)', 'JK345LM', 'IT90E5678901234567890123456'),
    (6, 'Giuseppe Russo', 'giusepperusso@example.net', 'Largo di Trastevere, 18 00153, Roma (RM)', 'NO678PQ', 'IT12F6789012345678901234567'),
    (7, 'Isabella Conti', 'isabellaconti@example.com', 'Piazzale Michelangelo, 5 50125, Firenze (FI)', 'RS901TU', 'IT56G7890123456789012345678'),
    (8, 'Antonio De Luca', 'antoniodeluca@example.org', 'Corso Umberto I, 45 70121, Bari (BA)', 'VW234XY', 'IT34H9012345678901234567890'),
    (9, 'Francesca Ferrari', 'francescaferrari@example.net', 'Via della Moscova, 27 20121, Milano (MI)', 'YZ345AB', 'IT78I2345678901234567890123'),
    (10, 'Luigi Bianco', 'luigibianco@example.com', 'Viale XX Settembre, 10 16121, Genova (GE)', 'CD678DE', 'IT90J5678901234567890123456'),
    
]

cursor.executemany('INSERT INTO Users VALUES (?, ?, ?, ?, ?, ?)', data)

# Step 5: Execute a SELECT query to retrieve the results
cursor.execute('SELECT * FROM Users')
result = cursor.fetchall()


# Save changes and close the connection
conn.commit()
conn.close()