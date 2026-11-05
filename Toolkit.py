
text2= """
       Artificial Intelligence is changing the WORLD.

       Machine Learning is part of Artificial Intelligence.

       Python is widely used in AI Engineering.
   """

def clean_text(text2):
 return " ".join(text2.lower().strip().split())

def count_words(text2):
 return len(clean_text(text2).split())

def search_word(text2,word):
     t=clean_text(text2).replace(".","").replace(",","").split()
     if word.lower() in t:
          return True
     else:
        return False
def get_word_frequency(text2):
    frequency = {}
    t = clean_text(text2).replace(".", "").replace(",", "").split()

    for word in t:
        if word not in frequency:
            frequency[word] = 1
        else:
            frequency[word] += 1

    return frequency








print(clean_text(text2))
print(count_words(text2))
print(search_word(text2,"python"))
print(search_word(text2,"no"))
print(search_word("Python is amazing", "py"))
print(search_word(text2, "PYTHON"))
print(get_word_frequency(text2))
