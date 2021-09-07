# bangla
It's a dependency project of [Bus-Mama](https://github.com/rjarman/Bus-Mama). It basically an implementation of a lemmatization algorithm using the Trie data structure. Algorithm flows:

- It takes Bengali words from stored data, then feeds them to the trie and loads the whole trie to the main memory.
- It makes a new node for every new character which contains a character dictionary of the character itself and a boolean flag that indicates whether the character end of a word or not if it traverses to the last word it sets the flag as true. If a character node exists on trie, then it traverses until found the match on character dictionary, if the word contains a new character then it adds the character to its parent character dictionary as a new node. When a new word is inserted into the trie, then it traverses the trie characterwise until it matches the dictionary key, if there are no matches for the next character it returns the matched word as a lemma word.
- It also contains Data Providers of the Bengali language as follows:
  - STOP_WORDS-->385
  - PUNCTUATIONS-->33
  - LETTERS-->50
  - NUMBERS-->20
  - get_words()-->63205(total collected Bengali words)
