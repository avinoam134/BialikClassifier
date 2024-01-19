

def countParagraphs(all):
  substring = "\n\n\n"
  return all['text'].count(substring)

def countSentences(all):
  return len(all['sentences'])

def countWords(all):
  count = 0
  sentences = all['sentences']
  for sentenc in sentences :
    for word in sentenc['tokens']:
      if not(word['text'] in ['.', ',', ';', '"' , '-', "?" ,'!',':']):
        count = count+1
  return count

def avrWordInSentenc(all):
  numSentences = countSentences(all)
  numWords = countWords(all)
  return numWords / numSentences

def avrWordInParagraph(all):
  numWords = countWords(all)
  numParagraphs = countParagraphs(all)
  return numWords/numParagraphs

# def countVerbWord(word):

# def countVerbText(all):
#   count = 0
#   sentences = all['sentences']
#   for sentenc in sentences :
#     for word in sentenc['tokens']:
