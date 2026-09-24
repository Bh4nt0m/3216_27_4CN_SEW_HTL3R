"""
# UE 1 - 24.09.26 F
"""

__author__ = "Clemens Zimmer"
__example__ = "SEW4/01/F"
__date__ = "24.09.2026"
__license__ = "GNU GPLv3"


# -----------------------------------------------------------------------------------------------------------------------
def collatz_sequence(number: int) -> list[int]:
    """
    :param number: Startzahl
    :return: Collatz Zahlenfolge, resultierend aus n
    >>> collatz_sequence(19)
    [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    >>> collatz_sequence(1)
    [1]
    >>> collatz_sequence(4)
    [4, 2, 1]
    >>> collatz_sequence(6)
    [6, 3, 10, 5, 16, 8, 4, 2, 1]
    >>> collatz_sequence(19)
    [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    >>> collatz_sequence(27)[:10]
    [27, 82, 41, 124, 62, 31, 94, 47, 142, 71]
    """

    list_c = [number]
    n = number
    while not (list_c[-1] == 1):
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        list_c.append(n)
    return list_c

def longest_collatz_sequence(n: int) -> tuple[int, int]:
    """
    :param number: Startzahl
    :return: Startwert und Länge der längsten Collatz Zahlenfolge deren Startwert <=n ist
    >>> longest_collatz_sequence(100)
    (97, 119)
    >>> longest_collatz_sequence(10)
    (9, 20)
    >>> longest_collatz_sequence(20)
    (18, 21)
    >>> longest_collatz_sequence(50)
    (27, 112)
    >>> longest_collatz_sequence(100)
    (97, 119)
    >>> longest_collatz_sequence(1000)
    (871, 179)
    """
    start = -1
    length = -1
    for i in range(1, n +1 ):
        cur = collatz_sequence(i)
        if len(cur) > length:
            start = i
            length = len(cur)

    return start, length

#Bonus -> Frage: ...d man am Computer empirisch nicht beweisen können – warum eigentlich nicht:
#Antwort: Sollte die Operation unendlich lange ansteigen wird der Prozess irgendwann kein Memory mehr haben um die liste
# mit den immer mehr werdenden Zahlen zu speichern.
# Bei zu großen p wird n immer weiter anwachsen

def collatz_sequence_b(number: int, p: int) -> list[int]:
    """
    :param number: Startzahl
    :param p: Multiplikator wenn -> n % 2 != 0
    :return: Collatz Zahlenfolge, resultierend aus n
    >>> collatz_sequence_b(7, 3)
    [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    >>> collatz_sequence_b(2, 3)
    [2, 1]
    >>> collatz_sequence_b(3, 1)
    [3, 4, 2, 1]
    ___ >>> collatz_sequence(7, 5) -> Alles was über 3 hat führt leider zu einer Endlosschleife:
    -> Macht auch sein da die Zahl ab 5 mehr steigt als sinkt -> Endlosschleife
    -> Bei allen p werten die gerade sind wird das ergebniss immer ungerade sein also wird nie geteil -> Endlosschleife
    [7, 36, 18, 9, 46, 23, 116, 58, 29, 146, 73, 366, 183, 916, 458, 229, 1146, 573, 2866, 1433, 7166, 3583, 17916, 8958, 4479, 22396, 11198, 5599, 27996, 13998, 6999, 34996, 17498, 8749, 43746, 21873, 109366, 54683, 273416, 136708, 68354, 34177, 170886, 85443, 427216, 213608, 106804, 53402, 26701, 133506, 66753, 333766, 166883, 834416, 417208, 208604, 104302, 52151, 260756, 130378, 65189, 325946, 162973, 814866, 407433, 2037166, 1018583, 5092916, 2546458, 1273229, 6366146, 3183073, 15915366, 7957683, 39788416, 19894208, 9947104, 4973552, 2486776, 1243388, 621694, 310847, 1554236, 777118, 388559, 1942796, 971398, 485699, 2428496, 1214248, 607124, 303562, 151781, 758906, 379453, 1897266, 948633, 4743166, 2371583, 11857916, 5928958, 2964479, 14822396, 7411198, 3705599, 18527996, 9263998, 4631999, 23159996, 11579998, 5789999, 28949996, 14474998, 7237499, 36187496, 18093748, 9046874, 4523437, 22617186, 11308593, 56542966, 28271483, 141357416, 70678708, 35339354, 17669677, 88348386, 44174193, 220870966, 110435483, 552177416, 276088708, 138044354, 69022177, 345110886, 172555443, 862777216, 431388608, 215694304, 107847152, 53923576, 26961788, 13480894, 6740447, 33702236, 16851118, 8425559, 42127796, 21063898, 10531949, 52659746, 26329873, 131649366, 65824683, 329123416, 164561708, 82280854, 41140427, 205702136, 102851068, 51425534, ...
    """
    list_c = [number]
    n = number
    while not (list_c[-1] == 1):
        if n % 2 == 0:
            n //= 2
        else:
            n = p * n + 1
        list_c.append(n)
    return list_c


    
# -----------------------------------------------------------------------------------------------------------------------
def main():
    pass


if __name__ == "__main__":
    main()
