#!/usr/bin/python3

import psycopg2

# connect to database
connect_str = 'host=296008-301875 port=5432 dbname=supinfo user=root password=1234'
conn = psycopg2.connect(connect_str)
conn.autocommit = True
cursor = conn.cursor()

# execute sql script
sql_file = open('supinfo.sql', 'r')
sqlFile = sql_file.read()
sql_file.close()
sqlCommands = sqlFile.split(';')
for command in sqlCommands:
    print(command)
    if command.strip() != '':
        cursor.execute(command)

# import data from csv file
with open('supinfo_data.csv', 'r') as f:
    next(f)  # Skip the header row.
    cursor.copy_from(
        f,
        'transactions',
        sep=',',
        columns=('campusId', 'nom', 'prenom', 'email')
    )
    conn.commit()

# confirm by selecting record
command = 'SELECT COUNT(*) FROM public.persone;'
cursor.execute(command)
recs = cursor.fetchall()
print('Row count: %d' % recs[0])
