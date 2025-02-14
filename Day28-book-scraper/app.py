import requests

from pages.book_pages import BookPage

# Fetch book data
url = "https://books.toscrape.com/"
book_content = requests.get(url).content

book = BookPage(book_content)

# Helper function for displaying book details
def books_information(b):
    print(f"📖 Title: {b.name}")
    print(f"💰 Price: £{b.price}")
    print(f"⭐ Rating: {b.rating} Star")
    print(f"🔗 Link: {b.link}")
    print("-" * 40)

# Display all books
def display_books(book= book):   
     for b in book.books:
        books_information(b)

# Filter books below a certain price
def filter_books_below_price(price, book=book):
    filtered_books = [b for b in book.books if b.price <= price]

    if filtered_books:
        for b in filtered_books:
            books_information(b)
    else:
        print('❌ No books found in that price range')


# Filter books above a certain price
def filter_books_above_price(price, book=book):
    filtered_books = [b for b in book.books if b.price >= price]

    if filtered_books:
        for b in filtered_books:
            books_information(b)
    else:
        print('❌ No books found in that price range')

# Filter books by rating
def filter_books_by_rating(rating, book=book):
    filtered_books  = [b for b in book.books if b.rating == rating]
    if filtered_books:
        for b in filtered_books:
            books_information(b)
    else:
        print('❌ No books found for that rating')


# User menu
user_menu = """Enter:
 - 1: To display all books with price and rating
 - 2: To display books above a certain price
 - 3: To display books below a certain price
 - 4: To display books with a specific rating
 - 5: To exit
Your choice: """


while True:
    try:
        choice = int(input(user_menu))
    except ValueError:
        print("❌ Invalid input! Please enter a number.")
        continue

    if choice == 1:
        display_books()  
    elif choice == 2:
        price = float(input('What is the minimum price you want to see? '))
        filter_books_above_price(price)
 
    elif choice == 3:
        price = float(input('What is the maximum price of books you want to see? '))
        filter_books_below_price(price)
    
    elif choice == 4:
        rating = int(input('What rating books you want to see? '))
        filter_books_by_rating(rating)
       
    elif choice == 5:
        print("👋 Exiting program. Goodbye!")
        break
    else:
        print("❌ Invalid choice! Please select a valid option.")