class User(object):
    def __init__(self, name, email):
        self.name = name #name is a string
        self.email = email #email is a string
        self.books = {} #books is a dictionary that will map a book object
    def get_email(self):
        return self.email
    def change_email(self, new_email):
        self.email = new_email
        return "Thanks for updating your email! Your new email is: " + self.email
    def __repr__(self):
        return_statement = "Username: " + self.name + ". Email Address: " + self.email + ". Books Read: " + str(len(self.books.values()))
        return return_statement
    def __eq__(self, other_user):
        if (other_user == self.name):
            other_user == self
    def read_book(self, book, rating = None):
        self.books[book] = rating
    def get_average_rating(self):
        average_rating = 0
        ratings_total = 0
        for rating in self.books.values():
            ratings_total += rating
        average_rating = ratings_total / len(self.books)
        return average_rating

class Book:
    def __init__(self, title, isbn):
        self.title = title #title is a string
        self.isbn = isbn #isbn is a number
        self.rating = []
    def get_title(self):
        return self.title
    def get_isbn(self):
        return self.isbn
    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        return "This book's ISBN has been updated. It is now: " + str(new_isbn)
    def add_rating(self, rating):
        if rating and 0 <= rating <= 4:
            self.rating.append(rating)
        else:
            print("Invalid Rating")
    def __eq__(self, book_object):
        if book_object.title == self.title and book_object.isbn == self.isbn:
            book_object = self
    def get_average_rating(self):
        average_rating = 0
        ratings_totals = 0
        for rating in self.ratings:
            ratings_totals += rating
        average_rating = ratings_totals / len(self.rating)
        return average_rating
    def __hash__(self):
        return hash((self.title, self.isbn))
    def __repr__(self):
        return "{title}, ISBN: {isbn}".format(title = self.title, isbn = self.isbn)

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author
    def get_author(self):
        return self.author
    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author = self.author)

class NonFiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject # subject will be a string, like 'Geology'
        self.level = level # level will be a string like "advanced"
    def get_subject(self):
        return self.subject
    def get_level(self):
        return self.level
    def __repr__(self):
        return "{title}, a {level} book on {subject}".format(title = self.title, level = self.level, subject = self.subject)

class TomeRater:
    def __init__(self):
        self.users = {} # dictionary maps email to user object
        self.books = {} # dictionary maps book object to num of users that have read it
    def create_book(self, title, isbn):
        return Book(title, isbn)
    def create_novel(self, title, author, isbn):
        new_fiction = Fiction(title, author, isbn)
        return new_fiction
    def create_non_fiction(self, title, subject, level, isbn):
        nonfiction_object = NonFiction(title, subject, level, isbn)
        return nonfiction_object
    def add_book_to_user(self, book, email, rating = None): # not necessarily understand this part
        if email in self.users.keys():
            user = self.users.get(email, None)
            user.read_book(book, rating)
            book.add_rating(rating)
            if book not in self.books.keys():
                self.books[book] = 1
            else:
                self.books[book] += 1
        else:
            print("No user with email {email}".format(email=email))
    def add_user(self, name, email, user_books = None):
        new_user = User(name,email)
        self.users[email] = new_user
        if user_books is not None:
            for book in user_books:
                self.add_book_to_user(book, email)
    def print_catalog(self):
        for key in self.books.keys():
            print(key)
    def print_users(self):
        for value in self.users.keys():
            print(value)
    def most_read_book(self):
        read_most = None
        read_count = 0
        for book in self.books.keys():
            if self.books[book] > read_count:
                read_count = self.books[book]
            if self.books[book] == read_count:
                read_most = book
        return read_most
    def highest_rated_book(self):
        book_best = None
        highest_rating = 0
        for book in self.books.keys():
            if User.get_average_rating(self) > highest_rating:
                highest_rating = User.get_average_rating(self)
                book_best = book
        return book_best
    def most_positive_user(self):
        highest_rating = 0
        highest_user = None
        for user in self.users.values():
            average = User.get_average_rating(self)
            if User.get_average_rating(self) > highest_rating:
                highest_rating = User.get_average_rating(self)
                highest_user = user
        return highest_user
    def check_for_valid_email(self, email):
        #Get Creative! Tome Rater check for valid email address
        check = ["@"]
        for item in check:
          if item not in email:
            print("Invalid email address. Emails should contain @")
          else: self.check_for_valid_email() # This is practically useless

#Get Creative! Tome Rater: Lets in user input

Input_Class_Obj = TomeRater()
# Get creative! User Input class lets in input
class UserInput(TomeRater):
    def __init__(self):
        super().__init__()
    def input_create_book(self):
        input_title = input("Please enter the book's title: ")
        input_isbn = input("Please enter {title}'s ISBN number: ".format(title = input_title))
        new_book_object = Input_Class_Obj.create_book(input_title, input_isbn)
        #Input_Class_Obj.add_book_to_user(input_title, input_email) How do I add book to user using local variables?
        return "Book added: " + str(new_book_object)
    def input_create_novel(self):
        input_title = input("Please enter the novel's title: ")
        input_author = input("Please enter {title}'s author: ".format(title = input_title))
        input_isbn = input("Please enter {title}'s ISBN number: ".format(title = input_title))
        new_book_object = Input_Class_Obj.create_novel(input_title, input_author, input_isbn)
        return "Book added: " + str(new_book_object) + " ISBN: " + input_isbn
    def input_create_nonfiction(self):
        #nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)
        input_title = input("Please enter the nonfiction title: ")
        input_subject = input("What subject is {title} about? ".format(title = input_title))
        input_level = input("Ahh, so what level is {title} (i.e. beginner, intermediate, advanced)? ".format(title = input_title))
        input_isbn = input("Please enter {title}'s ISBN".format(title = input_title))
        new_book_object = Input_Class_Obj.create_non_fiction(input_title, input_subject, input_level, input_isbn)
        return "Nonfiction book added: {title}. Subject {subject} at {level} level. The book's ISBN is: {isbn}".format(title = input_title, subject = input_subject, level = input_level, isbn = input_isbn)
    def input_add_user(self):
        input_name = input("Please enter your name: ")
        input_email = input("Hello {name}! Please enter your email: ".format(name = input_name))
        #input_books = [str(x) for x in input("Please enter the books you have read: ").split()]
        # Not neccessarily sure how to input a list in Python while not toppling the fragile code above. ;)
        new_book_object = Input_Class_Obj.add_user(input_name, input_email)
        return "User successfully added! Your name is: {name}, your email is: {email}".format(name = input_name, email = input_email)
    #def input_add_rating():
        #Input_Class_Obj = TomeRater()
        #input_bool0 = input("Do you want to add a rating? Yes or No. ")
        #input_bool = input_bool.title()
        #if input_bool == "Yes":
            #input_rating = int(input("Please enter a rating from 1 to 4."))
            #new_book_object = Input_Class_Obj.add_rating(input_rating)
            #return new_book_object
        #else:
            #print("Please type yes or no. If you typed no, then break.")
            #I'm not sure how I can utilize this. How do I add this into the object?

input_object = UserInput()
def new_book():
    input_book = input_object.input_create_book()
    print(input_book)
    #Input_Class_Obj.add_book_to_user(input_book, input_email) How do I add book to user (with local variables...)
def new_novel():
    input_novel = input_object.input_create_novel()
    print(input_novel)
def new_nonfiction():
    input_new_nonfiction = input_object.input_create_nonfiction()
    print(input_new_nonfiction)
def new_user():
    input_new_user = input_object.input_add_user()
    print(input_new_user)
def user_intro():
    new_user()
    while 1:
        choice = input("Do you want to add a 1. A Book (title and isbn), 2. A Novel (title, author, isbn), 3. A Nonfiction Book (title, subject, level, isbn), or 4. Exit? (Choose and type number)")
        if choice == '1':
            new_book()
            #Input_Class_Obj.add_book_to_user(input_book, input_email) Same as above.
        elif choice == '2':
            new_novel()
        elif choice == '3':
            new_nonfiction()
        elif choice == '4':
            break
        else:
            print("Sorry, we don't know what that was! Please try again.")
            user_intro()

# STARTING USER INTERFACE - Should I also make this a function? (similar to User_Intro)
new_user() # RUN TO JUST ADD USER
user_intro() # RUN TO ADD USER WITH BOOKS
Input_Class_Obj.print_users() # PRINT USERS IN CATALOG
# END USER INTERFACE

print(Input_Class_Obj.users) # Dictionary - Not user friendly
#print(Input_Class_Obj.books) Doesn't work without add_book_to_user working

#------------ Populate.py copied in

Tome_Rater = TomeRater()

#Create some books:
book1 = Tome_Rater.create_book("Society of Mind", 12345678)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345)
novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938)
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000)

#Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")

#Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", [book1, novel1, nonfiction1])

#Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)

Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)

#print(Tome_Rater.books) Works here.

#Uncomment these to test your functions:
Tome_Rater.print_catalog()
Tome_Rater.print_users()
print(Tome_Rater.books)
print("Most positive user:")
print(Tome_Rater.most_positive_user())
print("Highest rated book:")
print(Tome_Rater.highest_rated_book())
print("Most read book:")
print(Tome_Rater.most_read_book())
