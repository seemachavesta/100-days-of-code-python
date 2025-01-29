from utils import ArticleManager, Article

manager = ArticleManager()
manager.create_table()

user_menu = """
Enter:
 - 1 To add an article
 - 2 To display all articles
 - 3 To filter articles by criteria
 - 4 To change the read status of an article
 - 5 To delete an article
 - 6 To exit
Your Choice: """

# Prompt the user to add the article 
def prompt_add_article():
    title = input("Enter the title of the article: ")
    url = input('Enter the url: ')
    category = input('Enter the category: ')
    date = input('Enter the date: ')
    article = Article(title, url, category, date)
    
    manager.add_article(article)

def display_aricles():
    articles = manager.display_articles()
    if not articles:
        print('No articles found.')
        return 
    
    print("\n{:<30} {:<40} {:<15} {:<15} {:<10}".format(
        "Title", "URL", "Category", "Date", "Read"
    ))

    print("=" * 115)

    for article in articles:
        title, url, category, date, read = article
        read_status = "Yes" if read == 1 else "No"
        print("{:<30} {:<40} {:<15} {:<15} {:<10}".format(
            title[:30], url[:40], category[:15], date, read_status
        ))
    print("=" * 115)


def prompt_filter_article():
    filter_key = input("Filter by (title, category, read): ").strip().lower()
    filter_value = input("Enter the value to filter by: ").strip()
    manager.filter_article(manager.filter_summary, filter_key, filter_value)


def prompt_change_read_status():
    title = input('Enter the title: ')
    status = int(input('Enter 1 for read, 0 for not read: '))
    manager.change_read_status(title, status)
        
      
def prompt_delete_article():
    title = input('Enter the title: ')
    manager.delete_article(title)

       
def main():
    while True:
        try:
            choice = int(input(user_menu))
            if choice == 1:
                prompt_add_article()
            elif choice == 2:
                display_aricles()
            elif choice == 3:
                prompt_filter_article()
            elif choice == 4:
                prompt_change_read_status()
            elif choice == 5:
                prompt_delete_article()
            elif choice == 6:
                print('Exiting the program. Goodbye!"')
                break
            else: 
                print('Invalid input try again.')
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")
            


if __name__ == "__main__":
    main()

        


        


        

        
      


