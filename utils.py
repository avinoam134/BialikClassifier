

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
      if not(word['text'] in ['.', ',', ';', '"' , '-', "?" ,'!',':','\n']):
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

def countVerbWord(word):
  count = 0
  if 'expanded' in word:
    for partWord in word['expanded']:
      count = count + countVerbWord(partWord)
  elif 'upos' in word:
    if word['upos'] == 'VERB':
      count = count +1
  return count


def countVerbText(all):
  count = 0
  sentences = all['sentences']
  for sentenc in sentences :
    for word in sentenc['tokens']:
      count = count + countVerbWord(word)
  return count

# check for sentences in what part of speech it strat and return a dic thar summarize the result 
def countFirstUposForSentences(all):
  result = {}
  sentences = all['sentences']
  for sentenc in sentences :
    firstWord = sentenc['tokens'][0]
    if 'upos' in firstWord:
      type = firstWord['upos']
      if type in result:
        result[type] = result[type] + 1
      else:
         result[type] = 1
    else:
      if 'expanded' in firstWord:
        if 'upos' in firstWord['expanded'][0]:
          type = firstWord['expanded'][0]['upos']
          if type in result:
            result[type] = result[type] + 1
          else:
            result[type] = 1
  return result

def countPartOfSpeechWord(word ,PartOfSpeech):
  count = 0
  if 'expanded' in word:
    for partWord in word['expanded']:
      count = count + countVerbWord(partWord)
  elif 'upos' in word:
    if word['upos'] == PartOfSpeech:
      count = count +1
  return count


def countPartOfSpeechText(all , PartOfSpeech):
  count = 0
  sentences = all['sentences']
  for sentenc in sentences :
    for word in sentenc['tokens']:
      count = count + countPartOfSpeechWord(word , PartOfSpeech)
  return count

def countWordAppirence(all):
  result = {}
  sentences = all['sentences']
  for sentenc in sentences :
    for word in sentenc['tokens']:
      text = word['text']
      if text in result:
        result[text] = result[text] + 1
      else:
        result[text] = 1
  return result
