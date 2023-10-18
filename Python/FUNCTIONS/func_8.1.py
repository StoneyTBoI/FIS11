def ist_schaltjahr(jahr):
    if jahr % 4 == 0:
        if jahr % 100 == 0:
            if jahr % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

for year in range(1900, 2900):
    if ist_schaltjahr(year):
        print(year, end=" ")