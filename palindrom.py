def palindrom_check(napis):
    indexstart = 0
    indexend = int(len(napis)/2 )
    for index in range(indexstart, indexend):
        if napis[index] != napis[len(napis) -1 -index]:
            return False
    return True



for napis in ('aabbaa', 'kajak', 'abba abba abba', 'niedziala'):
    print(f" {napis} : {palindrom_check(napis)}")