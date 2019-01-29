import re;
import sys;
import pandas as pd;

#Methods
def countPair(w1, w2):
    count = 0
    for i, x in enumerate(s):
        if x == w1 and s[i+1] == w2:
            count+=1
    return count

def removeDupes(seq):
   arr = []
   [arr.append(i) for i in seq if not arr.count(i)]
   return arr

def getStartProb(sentence):
    occ = 0
    senSplit = sentence.lower().split()
    sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text.lower())
    for sentence in sentences:
        if(senSplit[0] == sentence.partition(' ')[0]):
            occ += 1
    return (occ/len(sentences))

def calculateProbability(sentence, arrs, probTable):
    probability = getStartProb(sentence)
    senSplit = sentence.lower().split()
    for i in range(len(senSplit)-1):
        probability = probability * probTable[arrs.index(senSplit[i])][arrs.index(senSplit[i+1])]
    return probability

def calcTableCase1(sentence, arrs):
    table = []
    countTable = []
    for w1 in arrs:
        countRow = []
        for w2 in arrs:
            countRow.append(countPair(w1, w2))
        table.append(countRow)
        
    for w1 in arrs:
        totalCount = 0
        for i, x in enumerate(s):
            if x == w1:
                totalCount += 1
        countTable.append(totalCount)
    countDf = getDataFrame(1, table, arrs)

    for i in range(len(table)):
        for j in range(len(table[i])):
            table[i][j] = table[i][j]/countTable[i]
    probDf = getDataFrame(2, table, arrs)
    
    probability = calculateProbability(sentence.lower(), arrs, table)
    return countDf, probDf, probability

def calcTableCase2(sentence, arrs):
    table = []
    countTable = []
    for w1 in arrs:
        countRow = []
        for w2 in arrs:
            countRow.append((countPair(w1, w2)+1))
        table.append(countRow)
        
    for w1 in arrs:
        totalCount = 0
        for i, x in enumerate(s):
            if x == w1:
                totalCount += 1
        countTable.append(totalCount)
    countDf = getDataFrame(1, table, arrs)


    for i in range(len(table)):
        for j in range(len(table[i])):
            table[i][j] = table[i][j]/(countTable[i]+nums)
    probDf = getDataFrame(2, table, arrs)

    probability = calculateProbability(sentence.lower(), arrs, table)
    return countDf, probDf, probability
    

def getDataFrame(tabletype, table, arrs):
    dataframe = pd.DataFrame(table, index=pd.Index(arrs), columns=pd.Index(arrs))
    pd.set_option('expand_frame_repr', False)
    return dataframe

#Variable initialization
global s, nums
s = []
arrs1 = []
arrs2 = []
#s1 = "Facebook announced plans to built a new datacenter in 2018"
s1 = sys.argv[2]


#Reading and preprocessing file and sentences
'''f = open('./corpus.txt', 'r')'''
f = open(sys.argv[1])
text = f.read()
f.close()
s = re.sub("[^\w]", " ", text.lower()).split()
arrs1 = removeDupes(re.sub("[^\w]", " ", s1.lower()).split())
nums = len(set(s))


#Sentence 1 count table, probability table and total probability 
ct_s1_Case1, pt_s1_Case1, p_s1_Case1 = calcTableCase1(s1, arrs1)
ct_s1_Case2, pt_s1_Case2, p_s1_Case2 = calcTableCase2(s1, arrs1)

#Print output
opTxt = ""

opTxt = opTxt + "\n===== Sentence: "+ s1 + " =====\n"

opTxt = opTxt + "\nCase 1: Without smoothing:\n"
opTxt = opTxt + "\nCount Table:\n"
opTxt = opTxt + ct_s1_Case1.to_string()
opTxt = opTxt + "\n\nProbability Table:\n"
opTxt = opTxt + pt_s1_Case1.to_string()
opTxt = opTxt + "\n\nTotal Probability: " + str(p_s1_Case1)

opTxt = opTxt + "\n\nCase 2: With add-one smoothing:\n"
opTxt = opTxt + "\nCount Table:\n"
opTxt = opTxt + ct_s1_Case2.to_string()
opTxt = opTxt + "\n\nProbability Table:\n"
opTxt = opTxt + pt_s1_Case2.to_string()
opTxt = opTxt + "\n\nTotal Probability: " + str(p_s1_Case2)



opTxt = opTxt + '\n\n===== RESULT SUMMARY =====\n'
opTxt = opTxt + '\nTotal probability of sentence 1 without smoothing: ' + str(p_s1_Case1)
opTxt = opTxt + '\nTotal probability of sentence 1 with add-one smoothing: ' + str(p_s1_Case2)
opTxt = opTxt + '\n'

print(opTxt)

myfile = open('output.txt', 'w+')
myfile.write(opTxt)
myfile.close()


#python3 Bigram_Model.py corpus.txt "Facebook announced plans to built a new datacenter in 2018" 

