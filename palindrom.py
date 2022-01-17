import string

def palindrom_check(napis):
    napis_lower = napis.lower()
    words = napis_lower.split()
    table = str.maketrans("", "", string.punctuation)
    stripped = [w.translate(table) for w in words]
    assembled = " ".join(stripped)
    index_start = 0
    index_end = int(len(assembled)/2 )
    for index in range(index_start, index_end):
        if assembled[index] != assembled[len(assembled) -1 -index]:
            return False
    return True


for napis in ('a,,abba!!!!a', 'kAjaK', 'abba!!!,.,., abba abba', 'niedziala', "aa   !!!,,...!!??$$  aa"):
    print(f" {napis} : {palindrom_check(napis)}")
