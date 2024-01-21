mjau = "hei"
print(mjau)
print("Hei")


import sqlite3

conn = sqlite3.connect('test.db')

print("Opened database successfully")



#conn.execute('''CREATE TABLE Film
 #        (FNr INT PRIMARY KEY     NOT NULL,
 #        Tittel          TEXT    NOT NULL,
  #       År            INT     NOT NULL,
   #      Land        TEXT,
    #     Sjanger         TEXT,
     #       Alder INT,
      #       Tid INT,
       #      Pris INT );''')
#print("Table created successfully")

cur = conn.cursor()


#cur.execute("INSERT INTO Film (FNr,Tittel,År,Land,Sjanger, Alder, Tid, Pris) VALUES (1, 'Casablanca', 1942, 'USA', 'Drama', 15, 102, 149 )");
#cur.execute("INSERT INTO Film (FNr,Tittel,År,Land,Sjanger, Alder, Tid) VALUES (2, 'Fort Apache', 1948, 'USA', 'Western', 15, 127 )")
#cur.execute("INSERT INTO Film (FNr,Tittel,År,Land,Sjanger, Alder, Tid, Pris) VALUES (3, 'Apocalypse Now', 1979, 'USA', 'Action', 18, 155, 123 )")
#cur.execute("INSERT INTO Film (FNr,Tittel,År,Land,Sjanger, Alder, Tid) VALUES (4, 'Streets of Fire', 1984, 'USA', 'Action', 15, 93 )")
#cur.execute("INSERT INTO Film (FNr,Tittel,År,Land,Sjanger, Alder, Tid, Pris) VALUES (5, 'High Noon', 1952, 'USA', 'Western', 15, 85, 123 )")
#cur.execute("INSERT INTO Film (FNr,Tittel,År,Land,Sjanger, Alder, Tid) VALUES (6, 'Cinema Paradiso', 1988, 'Italia', 'Komedie', 11, 123 )")
#cur.execute("INSERT INTO Film (FNr,Tittel,År,Land,Sjanger, Alder, Tid, Pris) VALUES (7, 'Asterix hos britene', 1988, 'Frankrike', 'Tegnefilm', 7, 78, 149 )")
#cur.execute("INSERT INTO Film (FNr,Tittel,År,Land,Sjanger, Alder, Tid, Pris) VALUES (8, 'Veiviseren', 1987, 'Norge', 'Action', 15, 96, 87 )")
#cur.execute("INSERT INTO Film (FNr,Tittel,År,Land,Sjanger, Alder, Tid, Pris) VALUES (9, 'Salmer fra kjøkkenet', 2002, 'Norge', 'Komedie', 7, 80, 149 )")
#cur.execute("INSERT INTO Film (FNr,Tittel,År,Land,Sjanger, Alder, Tid, Pris) VALUES (10, 'Anastasia', 1997, 'USA', 'Tegnefilm', 7, 94, 123 )")
#cur.execute("INSERT INTO Film (FNr,Tittel,År,Land,Sjanger, Alder, Tid, Pris) VALUES (11, 'La Grande bouffe', 1973, 'Frankrike', 'Drama', 15, 129, 87 )")
#cur.execute("INSERT INTO Film (FNr,Tittel,År,Land,Sjanger, Alder, Tid, Pris) VALUES (12, 'The Blues Brothers', 1980, 'USA', 'Komedie', 11, 133, 135 )");
#cur.execute("INSERT INTO Film (FNr,Tittel,År,Land,Sjanger, Alder, Tid) VALUES (13, 'Beatles Help', 1965, 'Storbritannia', 'Musikk', 11, 144 )");



conn.commit()


res = cur.execute("SELECT * FROM Film;")



res = cur.execute("SELECT Tittel, År, 2024-År FROM Film WHERE 2024 - År > 50; ")


for row in res:
    print(row)
    



conn.close()

