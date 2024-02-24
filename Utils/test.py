from trankit import Pipeline
from Poems import poems_parser as parser
import Utils.utils as utils


p = Pipeline("hebrew")

def analyse_poem(poem):
    result = {}
    all = p(poem['content'])
    result['name'] = poem['poem']
    result['year'] = poem['year']
    result['month'] = poem['month']
    result['Is published'] = poem['published']
    result['number of Paragraphs'] = utils.countParagraphs(all)
    result['number of Sentences'] = utils.countSentences(all)
    result['number of Words'] = utils.countWords(all)
    result['First Upos For evry Sentences'] = utils.countFirstUposForSentences(all)
    result['number of verb in the text'] = utils.countVerbText(all)
    result['histogram oe the words in the text'] = utils.countWordAppirence(all)
    result['number of verb nouns in the text'] = utils.countPartOfSpeechText(all ,'NOUN')
    result['average number of words in sentenc'] = utils.avrWordInSentenc(all)
    result['average number of words in paragrph'] = utils.avrWordInParagraph(all)
    result['number of verb punctuation in the text'] = utils.countPartOfSpeechText(all,'PUNCT')
    return result




def main():
    data = parser.data
    print(data[0])
    ans = analyse_poem(data[0])
    for x in ans.keys():
        print("key: " + x + '\n' + "val : " + str(ans[x]) + '\n')

        


    


    
    





if __name__ == "__main__":
    main()