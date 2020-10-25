import os
from collections import defaultdict

a = []
b = " "
sentence_structures = {}
sepsen = []
nouns = defaultdict(float)
verbs = defaultdict(float)
adverbs = defaultdict(float)
adjectives = defaultdict(float)
intensifiers = defaultdict(float)
negation = ["but", "neither", "never", "none",  "nor", "not", "nothing", "no_one", "nowhere", "aint", "ain't", "isnt", "isn't"]
exp_positive = False
exp_negative = False
eval_positive = 0
total_positive = 0
eval_negative = 0
total_negative = 0
p_polarity = 0
revfolders = ["gta4/gamespot", "gta4/metacritic", "gta4/steam", "me2/gamespot", "me2/metacritic", "me2/steam", "sims3/gamespot", "sims3/metacritic", "sims3/steam"]


def pcheck(original, words):
    SOs = {}
    intlist = {}
    marked = []
    intsum = 0
    negsum = 0
    negfactor = -4
    wsum = 0
    for word in original:
        if word in nouns:
            SOs[word] = nouns[word]
        elif word in adverbs:
            SOs[word] = adverbs[word]
        elif word in verbs:
            SOs[word] = verbs[word]
        elif word in adjectives:
            SOs[word] = adjectives[word]
        else:
            pass
    for w in SOs:
        wsum += SOs[w]
    so_sentence = ''.join(words)
    for intchk in intensifiers:
        if intchk in so_sentence and (so_sentence[so_sentence.index(intchk) + len(intchk)] in ['_','.', ',', ':', ';', '!', '?']):
            intlist[intchk] = intensifiers[intchk]
        else:
            pass
    intlist = [intlist[i] + 1 for i in intlist]
    for s in intlist:
        intsum += s
    intavg = 1 if intsum == 0 else intsum/len(intlist)
    for neg in negation:
        if neg in so_sentence and (so_sentence[so_sentence.index(neg) + len(neg)] in ['_','.', ',', ':', ';', '!', '?']):
            if neg not in marked:
                negsum += -4
                marked.append(neg)
            else:
                negfactor /= 2
                negsum += negfactor
    score = (intavg * wsum) + negsum
    return score

def add_to_dicts():
    with open("../../SO-CAL/Resources/dictionaries/English/noun_dictionary1.11.txt", mode='r') as noun_data:
        for row in noun_data:
            if '(' in row:
                continue
            nodes = row.split()
            while "" in nodes:
                nodes.remove("")
            nouns[nodes[0]] = float(nodes[1])

    with open("../../SO-CAL/Resources/dictionaries/English/verb_dictionary1.11.txt", mode='r') as verb_data:
        for row in verb_data:
            if '(' in row:
                continue
            nodes = row.split()
            while "" in nodes:
                nodes.remove("")
            verbs[nodes[0]] = float(nodes[1])

    with open("../../SO-CAL/Resources/dictionaries/English/adv_dictionary1.11.txt", mode='r') as adverb_data:
        for row in adverb_data:
            if '(' in row:
                continue
            nodes = row.split()
            while "" in nodes:
                nodes.remove("")
            adverbs[nodes[0]] = float(nodes[1])

    with open("../../SO-CAL/Resources/dictionaries/English/adj_dictionary1.11.txt", mode='r') as adjective_data:
        for row in adjective_data:
            if '(' in row:
                continue
            nodes = row.split()
            while "" in nodes:
                nodes.remove("")
            adjectives[nodes[0]] = float(nodes[1])

    with open("../../SO-CAL/Resources/dictionaries/English/int_dictionary1.11.txt", mode='r') as intense_data:
        for row in intense_data:
            nodes = row.split()
            while "" in nodes:
                nodes.remove("")
            intensifiers[nodes[0]] = float(nodes[1])

add_to_dicts()
for rf in revfolders:
    pathlist = os.path.abspath("../../prepro_data/"+rf)
    for filenm in os.listdir(pathlist):
        if 'yes' in filenm:
            exp_positive = True
            exp_negative = False
            total_positive += 1
        else:
            exp_negative = True
            exp_positive = False
            total_negative += 1
        full_file = pathlist + '/' + filenm
        with open(full_file, mode='r') as gamereview:
            for sentence in gamereview:
                ssp = sentence.split()
                for elem in ssp:
                    elem = elem.split('/')
                    sepsen.extend(elem)
                a = sepsen[::2]
                atmp = []
                for und in range(0, len(a)):
                    if a[und] in ['.', ',', ':', ';', '!', '?']:
                        continue
                    else:
                        atmp.append(a[und])
                        a[und] += '_'
                if not atmp:
                    continue
                b = sepsen[1::2]
                for punc in b:
                    if punc in ['.', ',', ':', ';', "''", '-LRB-', '-RRB-']:
                        b.remove(punc)
                b = " ".join(b)
                sepsen.clear()
                if b in sentence_structures:
                    features = sentence_structures[b]
                    c = []
                    for feature in features:
                        c.append(a[feature])
                    p_polarity = pcheck(atmp, c)
                    c.clear()
                else:
                    sentence_structures[b] = [ft for ft in range(0, len(b.split()))]
                    c = a
                    p_polarity = pcheck(atmp, c)
                    c.clear()
        if exp_positive:
            if p_polarity > 0:
                eval_positive += 1
        elif exp_negative:
            if p_polarity < 0:
                eval_negative += 1
    posacc = (eval_positive/total_positive) * 100
    negacc = (eval_negative/total_negative) * 100
    ovracc = ((eval_positive + eval_negative)/(total_negative + total_positive))*100
    file = open("../CHSCResults/"+rf+"/SA_Acc.txt", "w")
    file.write("% Correct Positive Reviews: "+str(posacc) + "%\n")
    file.write("% Correct Negative Reviews: " + str(negacc) + "%\n")
    file.write("% Correct Overall: " + str(ovracc) + "%")
