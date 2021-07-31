from nltk.stem import PorterStemmer, SnowballStemmer, LancasterStemmer, RegexpStemmer

porter = PorterStemmer()
lancaster = LancasterStemmer()
snowball = SnowballStemmer(language='english')
regexp = RegexpStemmer('ing$|s$|e$|able$', min=4)

word_list = ["friend", "friendship", "friends", "friendships"]
print("{0:20}{1:20}{2:20}{3:30}{4:40}".format("Word", "Porter Stemmer",
      "Snowball Stemmer", "Lancaster Stemmer", 'Regexp Stemmer'))
for word in word_list:
    print("{0:20}{1:20}{2:20}{3:30}{4:40}".format(word, porter.stem(
        word), snowball.stem(word), lancaster.stem(word), regexp.stem(word)))
