
def remove_ignored(napis):
    new_chars = []
    for char in napis:
        ascii_nr = ord(char)
        # print(f"char: {char} ascii: {ascii_nr}")
        
        if 97 <= ascii_nr <= 122 or 48 <= ascii_nr <= 57:
            new_chars.append(char)
    return "".join(new_chars)

def palindrom_check(napis):
    napis_lower = napis.lower()
    nowy_napis = remove_ignored(napis_lower)
    print(f'nowy_napis: {nowy_napis}')
    index_start = 0
    index_end = int(len(nowy_napis)/2 )
    for index in range(index_start, index_end):
        if nowy_napis[index] != nowy_napis[len(nowy_napis) -1 -index]:




for napis in ('a,,abba!!!!a', 'kAjaK', 'abba!!!,.,., abba abba', 'niedziala', "aa   !!!,,...!!??$$  aa"):
