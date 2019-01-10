# Can't solve now.

#s = [[4, 9, 2], [3, 5, 7], [8, 1, 5]]
s = [[4, 8, 2],[4 ,5 ,7],[6 ,1 ,6]]


values = []
row1 = s[0][0] + s[0][1] + s[0][2]
row2 = s[1][0] + s[1][1] + s[1][2]
row3 = s[2][0] + s[2][1] + s[2][2]

column1 = s[0][0] + s[1][0] + s[2][0]
column2 = s[0][1] + s[1][1] + s[2][1]
column3 = s[0][2] + s[1][2] + s[2][2]

diagonal1 = s[0][0] + s[1][1] + s[2][2]
diagonal2 = s[0][2] + s[1][1] + s[2][0]

magic_contant = 3 * ((3**2 + 1) / 2)

min_magic = 999


if diagonal1 == magic_contant and diagonal2 == magic_contant:
    if row1 != magic_contant:
        deta_row1 = abs(row1 - magic_contant)
        if deta_row1 < min_magic:
            min_magic = deta_row1
    if row2 != magic_contant:
        delta_row2 = abs(row2 - magic_contant)
        if delta_row2 < min_magic:
            min_magic = delta_row2
    if row3 != magic_contant:
        delta_row3  = abs(row3 - magic_contant)
        if delta_row3 < min_magic:
            min_magic = delta_row3
    if column1 != magic_contant:
        deta_column1  = abs(column1 - magic_contant)
        if deta_column1 < min_magic:
            min_magic = deta_column1
    if column2 != magic_contant:
        delta_column2 = abs(column2 - magic_contant)
        if delta_column2 < min_magic:
            min_magic = delta_column2
    if column3 != magic_contant:
        delta_column3 = abs(column3 - magic_contant)
        if delta_column3 < min_magic:
            min_magic = delta_column3
else:
    if diagonal1 != magic_contant :
        delta_diagonal = abs(diagonal1 - magic_contant)
        if delta_diagonal < min_magic :
            min_magic = delta_diagonal
    if diagonal2 != magic_contant:
        delta_diagonal2 = abs(diagonal2 - magic_contant)
        if delta_diagonal2 < min_magic:
            min_magic = delta_diagonal2
print ((int)(min_magic))

