import sys
import itertools

import time
start = time.time()


min_sup = int(sys.argv[1])
k = int(sys.argv[2])

wordcount = dict()  # key - string reviewer ID; value - number of times the word occurs in transactionDB.txt
wordID = dict()  # key - string reviewer ID; value - unique integer assigned to the reviewer ID

# populate wordcount dictionary
f1 = open(sys.argv[3])
for reviewerID in f1.read().split():
    count = wordcount.get(reviewerID, 0)
    wordcount[reviewerID] = count + 1
f1.close()
wordcount_keys = wordcount.keys()

# populate wordID dictionary
ID = 1
for i in sorted(wordcount_keys):
    wordID[i] = ID
    ID += 1

inv_wordID = {v: k for k, v in wordID.items()}

wordID_keys = wordID.keys()


# c1 - Arguments: None. Returns: A list of all individual items with frequency greater than minimum support
def c1():
    output_list = []
    for i in wordcount_keys :
        if wordcount[i] >= min_sup:
            output_list.append(i)
    return output_list


# candidate_gen_and_prune - Arguments - Cn-1 list. Returns: Fn list
def candidate_gen_and_prune(argument_list):
        
    n = len(argument_list[0])
    ck = []
    argument_list = sorted([tuple(sorted(x)) for x in argument_list])

    # Candidate generation step
    for i in argument_list:
        for j in argument_list[argument_list.index(i) + 1:]:
            compatible = True
            for x in range(0,len(i) - 1):
                if i[x] != j[x]:
                    compatible = False
                    break
            if compatible:
                ck.append(tuple(set(i + j)))

    ck = [sorted(x) for x in ck]
    argument_list = [sorted(x) for x in argument_list]

    # Pruning
    for element in ck:
        subsets = list(itertools.combinations(element, n))
        subsets = [sorted(x) for x in subsets]
        a = 0
        for x in subsets:
            if x in argument_list:
                a += 1
        if a != len(subsets):
            ck.remove(element)

    return ck


linetransactions = dict()
# key - unique integer ID mapped to the string reviewer ID; value - line numbers(or transaction IDs)
# in which the string occurs

# populating linetransactions
for x in inv_wordID.keys():
    linetransactions[x] = []

with open(sys.argv[3], 'r') as argfile:
    contents = argfile.read()
inputstring = contents.splitlines()
line_count = 1
for line in inputstring:
    words = line.split()
    listwords = [wordID.get(item,item) for item in words]
    for y in listwords:
        linetransactions[y].append(line_count)
    line_count += 1
argfile.close()

# the core apriori implementation
if k == 1:
    output = [[[x], wordcount[x]] for x in c1()]
else :
    output = []    

c1_list = [wordID[x] for x in c1()]
c2_list = list(itertools.combinations(c1_list,2))


def apriori(argument_list):    
    
    frequent_itemsets = []
    
    for itemset in argument_list:
        linetransactionslist = [set(linetransactions[item]) for item in itemset]
        intersectionset = set.intersection(*linetransactionslist)
        if len(list(intersectionset)) >= int(sys.argv[1]):
            frequent_itemsets.append((itemset, len(list(intersectionset))))
    
    if len(frequent_itemsets) != 0:
        output.extend(frequent_itemsets)
    
    if len(frequent_itemsets) > 1:
        next_list = [x for (x, y) in frequent_itemsets]
        apriori(candidate_gen_and_prune(next_list))


apriori(c2_list)

# writing output in file
outputfile = sys.argv[4]
outf = open(outputfile, 'w')
for x in output:
    if not len(x[0]) < k:
        if len(x[0]) == 1:
            outf.write(" ".join((x[0])) + " ({})".format(x[1]) + "\n")
        else:
            y = [a for a in x[0]]
            y = [inv_wordID[item] for item in y]
            outf.write(" ".join(y) + " ({})".format(x[1]) + "\n")
outf.close()

end = time.time()
print(end - start)
