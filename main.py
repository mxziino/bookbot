def main():
  #set the path
  book_path = "books/frankestein.txt"
  #get the text to a variable
  text = get_book_text(book_path)
  count = count_words(text)
  letters_dict = count_letters(text)
  sorted_letters = chars_dict_to_sorted(letters_dict)

  print(f"******** Begin report of book in path: {book_path} ********")
  print(f"the book has {count} words")
  print()

  for item in sorted_letters:
    print(f"the {item['char']} character was found {item["num"]} times")

  print(f"******** End report ********")



#define the function to count words
def count_words(book_text):
  #conver split the text into a words list
  words = book_text.split()
  #return the length of the words
  return len(words)

# define the function to count letters
def count_letters(book_text):
  #create empty dict
  letters_dict = {}
  #for each character in the text
  for c in book_text:
    # convert it to lowercase
    lowered = c.lower()
    # if the char is in the dict add +1
    if lowered in letters_dict:
      letters_dict[lowered] += 1
    else:
      letters_dict[lowered] = 1
  return letters_dict

# define the function that sort() will take into consideration
def sort_on(d):
  return d["char"]

# function to remove not letters char and sort the dict
def chars_dict_to_sorted(letters_dict):
  # create a empty list
  sorted_list = []
  #for each character in the dict
  for ch in letters_dict:
    # if the char is a letter
    if ch.isalpha():
      # append it to the list with the keys char and num
      sorted_list.append({"char": ch, "num": letters_dict[ch]})
  #sort the list
  sorted_list.sort(reverse=False, key=sort_on)
  return sorted_list

# create the function to get the text in the book
def get_book_text(path):
  with open(path) as f:
    return f.read()





main()