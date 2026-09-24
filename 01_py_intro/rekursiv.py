"""
# UE 1 - 24.09.26 F
"""

__author__ = "Clemens Zimmer"
__example__ = "SEW4/01/F"
__date__ = "24.09.2026"
__license__ = "GNU GPLv3"

from time import time


# -----------------------------------------------------------------------------------------------------------------------

def M(n: int) -> int:
    """
    Erwartet ist das alle Ergebnisse letztendlich auf 91 enden
    >>> M(5)
    91
    >>> M(100)
    91
    """
    if n > 100:
        return n - 10
    else:
        return M(M(n + 11))


# Bonus - M + Tiefe

def M_tiefe(n: int, t=1) -> tuple[int, int]:
    """
    Erwartet ist das alle Ergebnisse letztendlich auf 91 enden
    >>> M_tiefe(100)
    (91, 2)
    >>> M_tiefe(0)
    (91, 102)
    """
    if n > 100:
        return n - 10, t
    else:
        out, d1 = M_tiefe(n + 11, t)
        out, d2 = M_tiefe(out, d1 + 1)
        return out, (max(d1, d2))


# -----------------------------------------------------------------------------------------------------------------------
def main():
    t0 = time()
    m_list = [M(x) for x in range(200)]
    print(f"{m_list = }")
    print("#" * 100)
    m_dict = {x: M(x) for x in range(200)}
    print(f"{m_dict = }")
    print("#" * 100)
    print(f"time = {time() - t0}", end="sek\n")
    print("#" * 100)
    m_dict_t = {x: M_tiefe(x)[1] for x in range(200)}
    print(f"tiefe für jeden index 0 - 199 = {m_dict_t}")
    print("#" * 100)


if __name__ == "__main__":
    main()
