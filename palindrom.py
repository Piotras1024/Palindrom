def palindrom_check(napis):
    napis_lower = napis.lower()
    index_start = 0
    index_end = int(len(napis_lower)/2 )
    for index in range(index_start, index_end):
        if napis_lower[index] != napis_lower[len(napis) -1 -index]:
            return False
    return True


for napis in ('aabbaa', 'kAjaK', 'abba abba abba', 'niedziala'):
    print(f" {napis} : {palindrom_check(napis)}")
