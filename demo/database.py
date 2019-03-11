import sqlite3

conn = sqlite3.connect('SAT_score.db')

print ("Opened database successfully")

c = conn.cursor()
c.execute(''' CREATE TABLE scores
			  (category text, people text, time int, score int) ''')
score_list = [('reading', 'White', 2010, 528),
			  ('reading', 'White', 2011, 527),
			  ('reading', 'White', 2012, 527),
			  ('reading', 'White', 2013, 529),
			  ('reading', 'White', 2014, 529),
			  ('reading', 'Black', 2010, 428),
			  ('reading', 'Black', 2011, 428),
			  ('reading', 'Black', 2012, 431),
			  ('reading', 'Black', 2013, 431),
			  ('reading', 'Black', 2014, 431),
			  ('reading', 'Mexican American', 2010, 451),
			  ('reading', 'Mexican American', 2011, 448),
			  ('reading', 'Mexican American', 2012, 449),
			  ('reading', 'Mexican American', 2013, 450),
			  ('reading', 'Mexican American', 2014, 448),
			  ('reading', 'Puerto Rican', 2010, 452),
			  ('reading', 'Puerto Rican', 2011, 452),
			  ('reading', 'Puerto Rican', 2012, 456),
			  ('reading', 'Puerto Rican', 2013, 456),
			  ('reading', 'Puerto Rican', 2014, 456),
			  ('reading', 'Asian', 2010, 517),
			  ('reading', 'Asian', 2011, 518),
			  ('reading', 'Asian', 2012, 521),
			  ('reading', 'Asian', 2013, 523),
			  ('reading', 'Asian', 2014, 525),
			  ('reading', 'American Indian', 2010, 484),
			  ('reading', 'American Indian', 2011, 482),
			  ('reading', 'American Indian', 2012, 480),
			  ('reading', 'American Indian', 2013, 483),
			  ('reading', 'American Indian', 2014, 481),
			  ('mathematics', 'White', 2010, 535),
			  ('mathematics', 'White', 2011, 536),
			  ('mathematics', 'White', 2012, 534),
			  ('mathematics', 'White', 2013, 534),
			  ('mathematics', 'White', 2014, 534),
			  ('mathematics', 'Black', 2010, 427),
			  ('mathematics', 'Black', 2011, 428),
			  ('mathematics', 'Black', 2012, 429),
			  ('mathematics', 'Black', 2013, 429),
			  ('mathematics', 'Black', 2014, 428),
			  ('mathematics', 'Mexican American', 2010, 466),
			  ('mathematics', 'Mexican American', 2011, 465),
			  ('mathematics', 'Mexican American', 2012, 464),
			  ('mathematics', 'Mexican American', 2013, 461),
			  ('mathematics', 'Mexican American', 2014, 457),
			  ('mathematics', 'Puerto Rican', 2010, 452),
			  ('mathematics', 'Puerto Rican', 2011, 452),
			  ('mathematics', 'Puerto Rican', 2012, 453),
			  ('mathematics', 'Puerto Rican', 2013, 450),
			  ('mathematics', 'Puerto Rican', 2014, 449),
			  ('mathematics', 'Asian', 2010, 595),
			  ('mathematics', 'Asian', 2011, 595),
			  ('mathematics', 'Asian', 2012, 597),
			  ('mathematics', 'Asian', 2013, 598),
			  ('mathematics', 'Asian', 2014, 598),
			  ('mathematics', 'American Indian', 2010, 488),
			  ('mathematics', 'American Indian', 2011, 489),
			  ('mathematics', 'American Indian', 2012, 486),
			  ('mathematics', 'American Indian', 2013, 484),
			  ('mathematics', 'American Indian', 2014, 482),
			  ('writing', 'White', 2010, 516),
			  ('writing', 'White', 2011, 515),
			  ('writing', 'White', 2012, 515),
			  ('writing', 'White', 2013, 513),
			  ('writing', 'White', 2014, 513),
			  ('writing', 'Black', 2010, 417),
			  ('writing', 'Black', 2011, 417),
			  ('writing', 'Black', 2012, 418),
			  ('writing', 'Black', 2013, 418),
			  ('writing', 'Black', 2014, 418),
			  ('writing', 'Mexican American', 2010, 445),
			  ('writing', 'Mexican American', 2011, 443),
			  ('writing', 'Mexican American', 2012, 442),
			  ('writing', 'Mexican American', 2013, 443),
			  ('writing', 'Mexican American', 2014, 438),
			  ('writing', 'Puerto Rican', 2010, 442),
			  ('writing', 'Puerto Rican', 2011, 442),
			  ('writing', 'Puerto Rican', 2012, 445),
			  ('writing', 'Puerto Rican', 2013, 443),
			  ('writing', 'Puerto Rican', 2014, 442),
			  ('writing', 'Asian', 2010, 528),
			  ('writing', 'Asian', 2011, 528),
			  ('writing', 'Asian', 2012, 527),
			  ('writing', 'Asian', 2013, 530),
			  ('writing', 'Asian', 2014, 531),
			  ('writing', 'American Indian', 2010, 465),
			  ('writing', 'American Indian', 2011, 462),
			  ('writing', 'American Indian', 2012, 461),
			  ('writing', 'American Indian', 2013, 461),
			  ('writing', 'American Indian', 2014, 460),
			  ]
c.executemany('INSERT INTO scores VALUES (?, ?, ?, ?)', score_list)
conn.commit()

t = ('Asian', 'mathematics')
for row in c.execute("SELECT * FROM scores WHERE people=? AND category=?",t):
	print (row[3])

conn.close()
print("Database closed")
