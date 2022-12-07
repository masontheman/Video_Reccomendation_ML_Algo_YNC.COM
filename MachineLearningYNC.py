import pandas as pd # Dataframe to read data
import numpy as np # it's numpy 
import difflib # compares every item in a data container to every other item in that container
from sklearn.feature_extraction.text import TfidfVectorizer #used to get words that are repeated frequesntly
from sklearn.metrics.pairwise import cosine_similarity # is a way to measure looks like cosine similarity not to sure much about it
#####
# From
# Part 1 of this project
#####
#ync_data = pd.read_csv('/content/onehundredpages2.csv') 
#####


#####
ync_data.isnull().drop(columns='user name',inplace=True)
ync_data = ync_data.dropna(how='any')
combine_features = ync_data['title'] +ync_data['user name']+str(ync_data['date'])+str(ync_data['comments'])+str(ync_data['views'])+str(ync_data['up votes'])
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combine_features)
similarity = cosine_similarity(feature_vectors) 
video_name = input(' Enter your favorite movie name: ')
list_of_all_titles = ync_data['title'].tolist()
find_close_match = difflib.get_close_matches(video_name,list_of_all_titles) # uses that library and extracted function getclosemataches, which 
# takes paramters the movie name that was given by user inout and the list of movie titles directly from the pandas dataframe
print(find_close_match) # prints the varible that has a list of similar names 
close_match = find_close_match[0]
not_index_of_the_title_name = ync_data[ync_data.title == close_match]['title'].values[0] #so it goes into the pandas dataframe at location 
# in feature name title that is equal to close match , then goes to the index feature columns and pulls that exact value which returns its position in the column 
user_name_index = ync_data[ync_data.title == close_match]['user name'].values[0]
print(user_name_index)
print(not_index_of_the_title_name) # prints the index of that 
row_numbers = ync_data[(ync_data['title'] == not_index_of_the_title_name) & (ync_data['user name'] == user_name_index)].index
# row_numbers = df[(df['Gender'] == 'Female') & (df['City'] == 'Toronto')].index
print(row_numbers)
similarity_score = list(enumerate(similarity[row_numbers[0]])) # it creates a list of enumerations or iterations through the similar movies list
#so the similarity list is a list of movies in the order that they are similar to each other
#so what this does is return the position in the list as the first value and as the second value in the list of tuples is the acutaly similarity which is also the move they are equivalent
#so it takes that index and every movie after it is similar to the movie at that postion until twn postition later then movie might not be so similar but the the 11th movie is similar to the 10th and so on
# then it prints the list of tuples agin with 2 values the position then the movie similarity 
print(similarity_score)
len(similarity_score)
sorted_similar_titles = sorted(similarity_score, key = lambda x:x[1], reverse= True) # so it sets a new list of tuples based on the list of tuples that it takes as the first parameter
# it takes the next parameter key  which just says take the next element 
# the last parameter is reverse true which sorts the list in order of how similar it is to the movie at the first position of similarity score
# so this new list return a list that is increasingly not similar to the most similar movie 
print(sorted_similar_titles)
# print the name of similar movies based on the index
print('Videos Recommended for you: \n') # print statement with a new line at the end 
i = 1 # initialize i as 1 
for titlle in sorted_similar_titles: # looping through that movie list that starts as the most similar 
  index = titlle[0] # intializes variable index which is the index of the first movie that is most similar to the movie that was inputted and stores it as the name index 
  title_from_index = ync_data.iloc[index -1]['title'] # at the position  where this new index value is equal to the index value in the dataframe in the movie data dataframe 
  # its saying to go to the title feature column at this index and take the value at that index which would be the movie title 
  # then store it in the title_from_index variable 
  if (i<6): # i will always start out as less than six so it goes until it has gone through 6 times
    print(i,'-',title_from_index) # prints the title and then a number associted with i which isnt related to any index in any data 
    i+=1 # i increases to stop the values from printing, however the for loop goes through all the values in the list it just doesn't print them 