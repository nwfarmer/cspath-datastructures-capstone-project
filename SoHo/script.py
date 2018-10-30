from trie import Trie
from data import *
from welcome import *
from hashmap import HashMap
from linkedlist import LinkedList

#Printing the Welcome Message

print_welcome()

#Write code to insert food types into a data structure here. The data is in data.py

#I went for it. Did a trie. Woo.

food_trie = Trie()

for food in types:
  food_trie.insert(food)

#Write code to insert restaurant data into a data structure here. The data is in data.py


#Create the overall HashMap
resto_styles = HashMap(len(types))

#Create the Linked Lists for the HashMap
for food in types:
  resto_styles.assign(food, LinkedList())

#Create the HashMaps for each restaurant and plug them into the appropriate Linked List
def build_data(dat):
  for restaurant in dat:
    resto = resto_styles.retrieve(restaurant[0])
    resto.insert_beginning(HashMap(4))
    node = resto.get_head_node().get_value()
    node.assign('Name', restaurant[1])
    node.assign('Price', restaurant[2])
    node.assign('Rating', restaurant[3])
    node.assign('Address', restaurant[4])
  return resto_styles
  
build_data(restaurant_data)

#Write code for user interaction here

while True:
  try:
    user_input = str(input("\nWhat type of food would you like to eat?\nType the beginning of that food type and press enter to see if it's here.\n")).lower()
    length = len(list(food_trie.beginning_with(user_input)))
    choices = (list(food_trie.beginning_with(user_input)))
    choice = list(food_trie.beginning_with(user_input))[0]
  
  #Search for user_input in food types data structure here
    if length > 1:
      input1 = str(input('The following options are available: {0}! Please write out a little more to pick one.\n'.format(choices)))
    elif length == 1:
      input2 = str(input('The only option beginning with {0} is {1}. Do you want to look at {1} restaurants? Enter \'y\' for yes and \'n\' for no.\n'.format(user_input, choice))) 
      if input2 == 'n':
        print('Ok! Let\'s try again.')
        continue
    #After finding food type write code for retrieving restaurant data here
      if input2 == 'y':
        print('Here are all the {0} restaurants in SoHo!'.format(choice))
        resto = resto_styles.retrieve(choice).get_head_node()
        while resto.get_next_node() != None:
          print('\nName: {0}\nPrice: {1}\nRating: {2}\nAddress: {3}\n'.format(resto.get_value().retrieve('Name'), resto.get_value().retrieve('Price'), resto.get_value().retrieve('Rating'), resto.get_value().retrieve('Address')))
          resto = resto.get_next_node()
        input3 = (str(input('Do you want to look at other restaurants? Enter \'y\' for yes and \'n\' for no.\n')))
        if input3 == 'y':
          continue
        elif input3 == 'n':
          print('Thank you for using SoHo Restaurants!')
          break
  except (IndexError, NameError):
    print("Sorry, something went wrong. Please try again")
