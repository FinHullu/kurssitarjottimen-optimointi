from tqdm import tqdm
listapituus = 15
pakolliset = {1,2,3,4,5,6,8,11,12,13,17,18}
def count(palkit):
    
    amounts = {}
    for x in palkit:
        for i in x:
            if i not in amounts:
                amounts[i] = 0
            amounts[i] += 1
    return amounts
def cleanups(palkit, palkki, numero, pakolliset):
    palkit[palkki] = [x for x in palkit[palkki] if x == numero]
    for i in palkit:
        for j in i:
            if palkit.index(i) != palkki and j == numero:
                i.remove(j)
    pakval = {k: v for k, v in sorted(count(palkit).items(), key=lambda item: item[1]) if k in pakolliset and v == 1}
    if pakval != []:
        for x in list(pakval.keys()):
            for a in palkit:
                if len(a) != 1:
                    for i in a:
                        if i == x:
                            palkit[palkit.index(a)] = [b for b in palkit[palkit.index(a)] if b == x]
    for p in range(3):
        for x in palkit:
            if len(x) == 1:
                for i in palkit:
                    if i != x:
                        palkit[palkit.index(i)] = [a for a in palkit[palkit.index(i)] if [a] != x]
    return palkit
working_palkkis = []
for a in tqdm(range(2**(listapituus))):
    plist = [0]*(listapituus-len([int(x) for x in bin(a)[2:]]))+[int(x) for x in bin(a)[2:]]
    palkit = [[1,2,3],[4,5,3],[6,7],[4,8],[5,4],[9,10,11,12],[13,12],[14,6],[15,16],[14,11,1,12],[6,17],[13,8],[10,1,18],[11,15,2,18],[11,2,17]]
    k=0
    while 1:
        j = 0
        posloc = []
        uval = {k: v for k, v in sorted(count(palkit).items(), key=lambda item: item[1]) if not v == 1 and k in pakolliset}
        if uval == {} or sorted(palkit, key=len)[0] == []:
            break
        guess = list(uval.keys())[0]
        for x in palkit:
            for i in x:
                if guess == i:
                    posloc.append(j)
            j += 1
        cleanups(palkit, posloc[plist[k]], guess, pakolliset)
        k += 1
    working_palkkis.append(palkit)
print("------ TULOKSET ------")
new_k = []
for elem in working_palkkis:
    good = True
    for x in elem:
        k=0
        for i in x:
            if i in pakolliset:
                k += 1
        if k >= 2:
            good = False
    if good == True and elem not in new_k:
        new_k.append(elem)
working_palkkis = sorted(new_k)
for x in working_palkkis:
    n=0
    alist = []
    clean = []
    for y in x:
        for a in y:
            if a in pakolliset:
                n += 1
        clean.append(str(' or '.join(format(c) for c in y)))
        if y[0] not in pakolliset:
            if len(y) != 1:
                alist.append(' or '.join([str(y[0]),str(y[1])]))
            else:
                alist.append(y[0])
    if n != 12:
        continue
    print(alist)
    print(''.join(format(c,'<10') for c in clean))
""" [[3,4,5],[5,7,8],[9,10],[7,11],[7,8],[14,15,16,17],[13,17],[9,18],[16,19,20],[4,16,17,18],[9,21],[11,13],[4,15,22],[3,16,19,22],[3,16,21]]
{3,4,5,7,8,9,11,13,16,17,21,22} """
