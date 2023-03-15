SYNONYMS = [
  ('rate', 'ratings'),
  ('approval', 'popularity'),
]

QUERIES = [
  ('obama approval rate', 'obama popularity ratings'),
  ('obama approval rates', 'obama popularity ratings'),
  ('obama approval rate', 'popularity ratings obama')
]

from functools import partial,reduce

def different_word(word_tuple):
      word_1,word_2 = word_tuple

      return word_1 != word_2

def word_is_synonym(word_tuple, synonym):
  return synonym.get(word_tuple[0]) == word_tuple[1] 

def syn_function(s1,s2,syn)->bool:
    # convert to zip
    zipped_sentence = zip(s1,s2)
    
    # different word
    different_words = filter(different_word, zipped_sentence)

    # check that the different words are in the synonym dictionary
    word_syn_func = partial(word_is_synonym, synonym=syn)
    iterator_syn = map(word_syn_func, different_words)

    # reduce using AND
    reduced_syn = reduce(lambda x,y: x & y, iterator_syn)

    return reduced_syn

if __name__ == "__main__":
    syn_dict = dict(SYNONYMS)

    query_1 = QUERIES[0]

    s1,s2 = map(lambda x : x.split(), query_1)

    print(s1,s2)
    iterator_obj = syn_function(s1,s2,syn_dict)
    

