import logging
from models import database
from flask import session, request, render_template, url_for, redirect #type:ignore
import datetime
import uuid

review_column_dict = {
        'review_id' : 0,
        'reviewer': 1,
        'isbn': 2,
        'timestamp': 3,
        'rating': 4,
        'comment' : 5
    }
vote_type_dict = {
        "useless": -2,
        "useful": 1,
        "very_useful": 2
    }

class Review(object):
    
    def __init__(self, review_id):
        self.review_id = review_id  
        self.review_details = database.query_db('SELECT * FROM reviews WHERE review_id = ?',
                    [review_id], one=True)
        self.rating = self.review_details['rating']
        self.comment = self.review_details['comment']
        self.reviewer = self.review_details['reviewer']
        self.isbn = self.review_details['isbn']
        self.votes_stats = self.getVotesStat()
        self.display_time = self.getDisplayTime()
        self.product_title = self.getProductTitle()

    def getVotesStat(self):
        votes_stats_dict = {}
        for vote_type, score in vote_type_dict.items():
            score_results = database.query_db('SELECT COUNT(giver) FROM usefulness_scores WHERE review_id = ? AND score = ?',
                    [self.review_id, score])
            freq = 0
            if score_results is not None:
                freq = score_results[0][0]
            votes_stats_dict[vote_type] = freq
        return votes_stats_dict

    def getDisplayTime(self):
        timestamp_str = self.review_details['timestamp']
        timestamp = datetime.datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S.%f')
        return str(timestamp.strftime('%d-%m-%Y') + " " + str(timestamp.strftime('%H:%M:%S')))
        
    def isCurrentUser(self, current_user):
        return (current_user == self.reviewer)
    
    def getProductTitle(self):
        book_details = database.query_db('SELECT title FROM books where isbn = ?', [self.isbn], one=True)
        return book_details['title']

class User(object):
    def __init__(self, username):
        self.username = username  
        self.review_details = database.query_db('SELECT * FROM users WHERE username = ?',
                    [username], one=True)
        
        self.reviews = self.getReviews()
        self.usefulness_score = self.getUsefulnessScore()
        self.trusts = self.getTrusts(1)
        self.non_trusts = self.getTrusts(-1)
    
    def getUsefulnessScore(self):
        score = database.query_db('SELECT sum(score) FROM usefulness_scores NATURAL JOIN reviews WHERE reviewer = ?',
                    [self.username])
        if score[0][0] is None:
            return 0
        else :
            return score[0][0]

    def getTrusts(self, trust_val):
        trusts = database.query_db('SELECT count(*) FROM trusts WHERE trustee = ? AND value = ?',
                    [self.username, trust_val])
        if trusts[0][0] is None:
            return 0
        else :
            return trusts[0][0]
    
    def getReviews(self):
        reviews_list = []
        reviews_details = database.query_db('SELECT * FROM reviews WHERE reviewer = ? ORDER BY timestamp DESC', [self.username])
        if reviews_details is None or reviews_details[0] is None:
            return reviews_list
        for review in reviews_details:
            cur_review = {}
            for col, i in review_column_dict.items():
                cur_review[col] = review[i]            
            reviews_list.append( Review(cur_review['review_id']) )
        return reviews_list
    
def hasReviewed(username, isbn):
    review_details = database.query_db('SELECT * FROM reviews WHERE reviewer = ? AND isbn = ?',
                    [username, isbn], one=True)
    return review_details != None

def getReviewsList(isbn, field, n):
    reviews_list = []
    reviews_details = None
    if field == 'timestamp':
        reviews_details = database.query_db('SELECT *  FROM reviews NATURAL JOIN usefulness_scores WHERE isbn = ? GROUP BY reviewer ORDER BY timestamp DESC LIMIT ?',[isbn, int(n)])
    else:
        reviews_details = database.query_db('SELECT *  FROM reviews NATURAL JOIN usefulness_scores WHERE isbn = ? GROUP BY reviewer ORDER BY sum(score) DESC LIMIT ?',[isbn, int(n)])
    if reviews_details is None:
        return reviews_list 
    for review in reviews_details:
        cur_review = {}
        for col, i in review_column_dict.items():
            cur_review[col] = review[i]            
        reviews_list.append(Review(cur_review['review_id']))
    return reviews_list

def getRating(isbn):
    rating = database.query_db('SELECT AVG(rating) FROM reviews where isbn = ?', [isbn])
    return rating[0][0]

def editReview(isbn, review_id):
    if request.method == 'POST':
        rating = request.form.get('rating')
        comment = request.form.get('comment')
        database.update_db('UPDATE reviews SET rating = ?, comment = ? WHERE review_id = ?',
                        (rating, comment, review_id))
        return redirect(url_for('viewProduct', isbn = isbn)) 
    else:
        return render_template("editReview.html", isbn = isbn, review = Review(review_id))

def addReview(isbn):
    username = session['username']
    if request.method == 'POST':
        rating = request.form.get('rating')
        comment = request.form.get('comment')
        review_id = str(uuid.uuid4().fields[-1])[:6]
        timestamp = datetime.datetime.now()
        database.update_db('INSERT OR REPLACE INTO reviews VALUES (?, ?, ?, ?, ?, ?)', [review_id, username, isbn, timestamp, rating, comment])
        return redirect(url_for('viewProduct', isbn = isbn)) 
    else:
        return render_template("editReview.html", isbn = isbn)

def voteReview(review_id, vote_type):
    giver = session['username']
    database.update_db('INSERT OR REPLACE INTO usefulness_scores VALUES (?, ?, ?)', [review_id, giver, vote_type_dict[vote_type]])
    book_details = database.query_db("select isbn from reviews where review_id = ?",[review_id], one=True)
    return redirect(url_for('viewProduct', isbn = book_details['isbn']))

def trustVoteUser(trustee, trust_val):
    truster = session['username']
    database.update_db('INSERT OR REPLACE INTO trusts VALUES (?, ?, ?)', [truster, trustee, trust_val])
    
    return redirect(url_for('viewUser', username = trustee))

def viewUser(username):
    return render_template("user.html", user = User(username), logged_in = session.get('username')) 