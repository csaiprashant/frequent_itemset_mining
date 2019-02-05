# Mining a Transaction Database For k+ Frequent Itemsets

## Introduction  
Frequent pattern mining is a heavily researched area in the field of data mining with a wide range of applications. Mining frequent patterns from large scale databases has emerged as an important problem in data mining and knowledge discovery community. A number of algorithms have been proposed to determine frequent patterns. The Apriori algorithm is the most popular algorithm proposed in this field.

### Keywords
- Support: Support is the probability of having expected k-item set in a transaction.
- Confidence: Confidence is the conditional probability that a transaction having X also contains Y.
- Frequent Itemset: The sets of items which have atleast minimum support.
- Apriori Algorithm: The subsets of a frequent itemset are also frequent - Downward Closure Property.

## Problem Statement
The transaction database (transactionDB.txt) is a set of reviewers from Amazon.com. Specifically, reviewer ids are the items. A transaction is a set of all reviewer ids which were used to post a review on that product. Each line in the transaction database represents a transaction. For a given transaction, the items (reviewer ids) are separated by a space character. We are required to find frequent patterns in this dataset having minimum support as specified by the user.

## Command to run pattern_mining.py
    python pattern_mining.py <min_sup> <k> <input_file> <output_file>

## Sample input and output
min_sup = 4, k = 3
This would yield all itemsets appearing atleast 4 times and containig atleast 3 elements. Some results of this query would include the following itemsets:
```
A37787I8C184FW AWE8HU0AZKASV A3UIATN5XW74NQ (4) 
A3Y9BX5AS769T AWE8HU0AZKASV A3UIATN5XW74NQ (5) 
AZ7I5GAJZA3JO A28R83ADQPMF2X A2GKW94L6HRND7 A2IE7YPWUYZAXS (4)
```
The first itemset is a frequent 3-itemset having a support count of 4 (i.e., appears 4 times in the data, satisfies the min_sup = 4 and  hence is frequent). The second itemset is a frequent 3-itemset with a support of 5 (i.e., it appears 5 times in the transaction database). The last itemset is a frequent 4-itemset with a support of 4.

## Files in this Repository
- pattern_mining.py - Python 3.6 script which contains my implementation of the Apriori algorithm.
- README.md
- transactionDB - The transaction database of Amazon.com product reviews.
