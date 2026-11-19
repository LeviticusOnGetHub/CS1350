# problem 1

#write a class libary in a dic mapping isbn strings to a dic of title str author str and copies int 

# add_book(isbn,title,author,copies) add a book if the isbn already exists add copies to the existing count title and author stay unchanged
# check_out(isbn) reduces the copies of the book by 1 snd returns true or false if number is unknown or checked out copies are 0
# by_author(author) returns a list of all books by the author case insensitive
# inventory_value(prices) takes price and copies times price for all books and returns the total value
# low_stock(threshold) returns a list of all books with copies less than the threshold

class Library:
    def __init__(self):
        #make empty library dictionary
        self.library = {}
        # book peramaters
    def add_book (self,isbn,title,author,copies):
        # check if the book already exists in the library
        if isbn in self.library:
            self.library[isbn]['copies'] += copies
            # if the book is real only update copies, title and author remain unchanged
        else:
            self.library[isbn] = {'title': title, 'author': author, 'copies': copies}
    # checkout function
    def checkout(self,isbn):
        # check if the book exists and has copies available
        if isbn not in self.library:
            return False
        # if the book exists but has no copies false
        if self.library[isbn]['copies'] == 0:
            return False
        # reduce the number of copies by 1 if checked out
        self.library[isbn]["copies"] -=1
        return True
    
    def by_author(self, author):
        # find all books by the given author, case insensitive
        outcome = []
        # look through all books
        for book in self.library.values():
            # if author matches, add
            if book["author"].lower() == author.lower():
                outcome.append(book)
        return outcome
    
    def inventory_value(self,prices):
        total = 0 
        # look through all book and find price
        for isbn, book in self.library.items():
            # check if the isbn has a price
            if isbn in prices:
                total += book['copies'] * prices[isbn]
        return total
    
    def low_stock(self,threshold):
        outcome = []
        # look through all books and find those with copies below the threshold
        for book in self.library.values():
            if book["copies"] < threshold:
                outcome.append(book)
        return outcome

lib = Library()
lib.add_book("111", "One", "batman", 2)
lib.add_book("222", "Two", "antman", 1)
lib.add_book("333", "Three", "batman", 3)
lib.add_book("444", "Four", "batman", 1)

print(lib.checkout("222"))
print(lib.checkout("222"))
print(lib.checkout("999"))
print(lib.by_author("batman"))
print(lib.inventory_value({"111": 20.0, "333": 30.0, "999": 5.0})) 
print(lib.low_stock(3))

                        


# part 2 confrence sessions with sets

# class session with 
    #constructor takes title and makes empty set for attendees
    #reg(name) adds an attendee
    #unreg(name) removes if present no error if gone
    #attandee_count() returns the number of attendees

# standalones
    #all(sessions) returns a set of attendees who attended all
    #just_one(sessions)
    #no_shows(registered, sessions) no shows
    #summuary(sessions) all titles and headcounts than distinct attendees

# classes and methods    
class Session:
    def __init__(self, title):
        self.title = title
        self.attendees = set()
    # register an attendee
    def reg(self,name):
        self.attendees.add(name)
    # unregister an attendee
    def unreg(self,name):
        self.attendees.discard(name)
    # return the number of attendees
    def attendee_count(self):
        return len(self.attendees)

# defining all sessions function to figure out whos in all sessions
def all(sessions):
    # if there in no sessions return an empty set
    if not sessions:
        return set()
    # start with attendees from the first session
    attendees = sessions[0].attendees.copy()
    # intersect with attendees from the remaining sessions so on and so forth to find common attendees
    for session in sessions[1:]:
        # update the attendees set to only include those also in the current session
        attendees &= session.attendees
    return attendees

# just_one returns attendees who attended exactly one session
def just_one(sessions):
    if not sessions:
        return set()
    all_attendees = set()
    for session in sessions:
        all_attendees |= session.attendees
        # for a person in the current session 
    return {attendee for attendee in all_attendees if sum(attendee in s.attendees for s in sessions) == 1}

# no shows calls out attendees who registered but did not attend any session
def no_shows(registered, sessions):
    attended = set()
    for session in sessions:
        attended |= session.attendees
        # return the registered attendees without attendances 
    return registered - attended

# sum_sessions returns total headcount and set of all attendees across sessions
def sum_sessions(sessions):
    total_headcount = 0
    all_attendees = set()
    for session in sessions:
        total_headcount += session.attendee_count()
        # add all attendees from the current session | makes the set add up the unique attendees without duplicates
        all_attendees |= session.attendees
    return total_headcount, all_attendees

# summary returns tuple with list of title and headcounts and set of all people
def summary(sessions):
    titles_and_headcounts = [(session.title, session.attendee_count()) for session in sessions]
    all_attendees = set()
    for session in sessions:
        # add all attendees from the current session | makes the set add up the unique attendees without duplicates
        all_attendees |= session.attendees
    return titles_and_headcounts, all_attendees


#testers 
keynote = Session("Keynote")
for p in ["Ana", "Ben", "Cruz","Dee"]:
    keynote.reg(p)

workshop = Session("Workshop")
for p in ["Ana", "Cruz", "Eli"]:
    workshop.reg(p)
    
panel = Session("Panel")
for p in ["Ana", "Dee", "Eli","Fay"]:
    panel.reg(p)

workshop.unreg("Eli")
workshop.unreg("Zed")
print(workshop.attendee_count())

sessions = [keynote, workshop, panel]
print(all(sessions))
print(just_one(sessions))
print(no_shows({"Ana", "Ben","Fay","gus"}, sessions))
print(summary(sessions))