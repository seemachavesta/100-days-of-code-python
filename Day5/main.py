from movie_collection import movie_collection

menu_prompt = "\nEnter 'a' to add, 'l' to view the list, 'f' to find movie by title, 'd' to delete, or 'q' to quit:"

#Helper function user provided title exist in in movie title
def movie_title_matches(movie, title):
  return movie.get('Title', '').lower() == title.lower()
  
# Helper function to display movie info
def display_movie_info(movie):
    print(f"Title: {movie['Title']}, Director: {movie['Director']}, Release year: {movie['Release Year']}")


# Add movies in movie collections
def add_movie(movie_collection):
  title = input('Enter movie title:')
  director = input('Enter movie director: ')
  
  while True:
    try:
      year = int(input('Enter movie release year: '))
      break
    except ValueError:
      print('Invalid value')
    
  movie_collection.append({
    'Title': title,
    'Director': director,
    'Release Year': year
  })
  

# This function display the movie collection  
def display_movie_list(collection):
  if not collection:
    print('No movies in the collection.')
    return
    
  for index, movie in enumerate(collection, start = 1):
    print(f'Movie {index}: ')
   
    display_movie_info(movie)
    print("-" * 20) 
 
    
# The function find the movie by title    
def find_movie(collection):
  
  title = input('Enter the movie title: ').lower()
  found = False
  
  #Looping over the movie collection to find the movie
  for movie in collection:
    #If title exist in movie collection and title match with user provided title
    if movie_title_matches(movie, title):
      display_movie_info(movie)
      found = True
      break
    
  # Displaying movie not found message if movie not found
  if not found:
    print('Movie not found')
    
      
# This function delete the movie from movie collection      
def delete_movie(collection):
  title = input('Enter the movie title: ').strip().lower()
  
  initial_len = len(collection)
  
  collection[:] = [movie for movie in collection if movie['Title'].lower() != title.lower()]
  
  if len(collection) < initial_len:
    print(f'{title} has been delete')
  else:
    print(f'The Movie {title} is not found.')
      

while True:
  option = input(menu_prompt)
  
  if option == 'a':
    add_movie(movie_collection)
    
  elif option == 'l':
    display_movie_list(movie_collection)
    
  elif option == 'f':
    find_movie(movie_collection)
  
  elif option == 'd':
    delete_movie(movie_collection)
  
  elif option == 'q':
    break
  
  else:
    print('Invlid option')
  