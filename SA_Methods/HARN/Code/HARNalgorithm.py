import os
import HARN.Code.sentiment as sa

a = []
b = " "
sentence_structures = {}
sepsen = []
nv_dict = {}
exp_positive = False
exp_negative = False
eval_positive = 0
total_positive = 0
eval_negative = 0
total_negative = 0
p_polarity = 0
shift = 1
revfolders = ["gta4/gamespot", "gta4/metacritic", "gta4/steam", "me2/gamespot", "me2/metacritic", "me2/steam", "sims3/gamespot", "sims3/metacritic", "sims3/steam"]
s = sa.SentimentAnalysis(filename='SentiWordNet.txt', weighting='average')


def pcheck(words, tags):
    p_words = 0
    nouns = []
    vb_jj_rb = []
    if 'NN' in tags:
        for x in range(0, len(tags)):
            if "NN" in tags[x]:
                nouns.append(words[x])
            else:
                vb_jj_rb.append(words[x])
        for n in nouns:
            for vjr in vb_jj_rb:
                if (n, vjr) in nv_dict:
                    p_words += nv_dict[n, vjr]
                else:
                    mash = vjr + " " + n
                    sval = s.score(mash)
                    nv_dict[n, vjr] = sval
                    p_words += nv_dict[n, vjr]
        for y in range(0, tags):
            if "VB" in tags[y]:
                if "JJ" in tags[y+1]:
                    if p_words < 0:
                        p_words += -1
                    else:
                        p_words += 1
                else:
                    continue
    else:
        p_words = s.score(sentence)
        return p_words
    return p_words/len(words)


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
                if len(a) == 1:
                    p_polarity += s.score(a)
                    continue
                b = sepsen[1::2]
                btemp = b.copy()
                for punc in b:
                    if punc in ['.', ',', ':', "''", '-LRB-', '-RRB-']:
                        b.remove(punc)
                b = " ".join(b)
                sepsen.clear()
                if b in sentence_structures:
                    features = sentence_structures[b]
                    features = list(map(int, features.split(',')))
                    c = []
                    d = []
                    for feature in features:
                        c.append(a[feature])
                        d.append(b[feature])
                    if 'not' in a or 'no' in a:
                        shift = -1
                        p_polarity += (pcheck(c, d) * shift)
                    elif 'but' in a:
                        p_polarity = 0
                    else:
                        p_polarity += (pcheck(c, d) * shift)
                else:
                    atemp = a.copy()
                    for index_guide in range(0, len(atemp)):
                        atemp[index_guide] = str(index_guide)+': ' + atemp[index_guide]
                    feature_select = input(str(atemp) + '\n' + 'Select index # of desired features of sentence (comma separated):\n')
                    sentence_structures[b] = feature_select
                    feature_select = list(map(int, feature_select.split(',')))
                    c = []
                    d = []
                    for feature in feature_select:
                        c.append(a[feature])
                        d.append(btemp[feature])
                    if 'not' in a or 'no' in a:
                        shift = -1
                        p_polarity += (pcheck(c, d) * shift)
                    elif 'but' in a:
                        p_polarity = 0
                    else:
                        p_polarity += (pcheck(c, d) * shift)
        if exp_positive:
            if p_polarity > 0:
                eval_positive += 1
        elif exp_negative:
            if p_polarity < 0:
                eval_negative += 1
    posacc = (eval_positive/total_positive) * 100
    negacc = (eval_negative/total_negative) * 100
    ovracc = ((eval_positive + eval_negative)/(total_negative + total_positive))*100
    file = open("../HResults/"+rf+"/SA_Acc.txt", "w")
    file.write("% Correct Positive Reviews: "+str(posacc) + "%\n")
    file.write("% Correct Negative Reviews: " + str(negacc) + "%\n")
    file.write("% Correct Overall: " + str(ovracc) + "%")
