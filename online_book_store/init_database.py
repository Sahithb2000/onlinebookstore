import sqlite3

with sqlite3.connect('store.db') as conn:
	conn.execute('''
				CREATE TABLE IF NOT EXISTS users
				(username TEXT PRIMARY KEY,
				password TEXT,
				full_name TEXT,
				address TEXT,
				phone_number TEXT)			
				''')

	conn.execute('''
				CREATE TABLE IF NOT EXISTS managers
				(username TEXT PRIMARY KEY,
				password TEXT,
				address TEXT,
				phone_number TEXT)			
				''')


	conn.execute('''
				CREATE TABLE IF NOT EXISTS books
				(isbn TEXT PRIMARY KEY,
				title TEXT,
				author TEXT,
				publisher TEXT,
				pages INTEGER,
				publish_date TEXT,
				quantity INTEGER,
				language TEXT,
				subject TEXT,
				price REAL)			
				''')


	conn.execute('''
				CREATE TABLE IF NOT EXISTS orders
				(
				order_id TEXT NOT NULL,
				isbn TEXT,
				username TEXT,
				quantity INTEGER,
				timestamp TEXT,
				FOREIGN KEY(isbn) REFERENCES books(isbn),
				FOREIGN KEY(username) REFERENCES users(username)
				)			
				''')		
	
	conn.execute('''
				INSERT OR IGNORE INTO managers (username, password, full_name, phone_number) VALUES ('admin', '5f4dcc3b5aa765d61d8327deb882cf99', 'super_user', '9191919191')
				''')
	
	conn.execute('''
				CREATE TABLE IF NOT EXISTS carts
				(
				username TEXT,
				isbn TEXT,
				FOREIGN KEY(isbn) REFERENCES books(isbn),
				FOREIGN KEY(username) REFERENCES users(username)
				)			
				''')

	conn.execute('''
				CREATE TABLE IF NOT EXISTS reviews
				(
				review_id TEXT PRIMARY KEY,
				reviewer TEXT,
				isbn TEXT,
				timestamp TEXT,
				rating INTEGER,
				comment TEXT,
				FOREIGN KEY(isbn) REFERENCES books(isbn),
				FOREIGN KEY(reviewer) REFERENCES users(username)
				)			
				''')
	
	conn.execute('''
				CREATE TABLE IF NOT EXISTS usefulness_scores
				(
				review_id TEXT NOT NULL,
				giver TEXT NOT NULL,
				score INTEGER,
				FOREIGN KEY(giver) REFERENCES users(username),
				FOREIGN KEY(review_id) REFERENCES reviews(review_id),
				PRIMARY KEY (review_id, giver)
				)			
				''')
	
	conn.execute('''
				CREATE TABLE IF NOT EXISTS trusts
				(
				truster TEXT NOT NULL,
				trustee TEXT NOT NULL,
				value INTEGER,
				FOREIGN KEY(truster) REFERENCES users(username),
				FOREIGN KEY(trustee) REFERENCES users(username),
				PRIMARY KEY (truster, trustee)
				)			
				''')
	
	