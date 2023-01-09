def moldura(l, c):
    if l > 20:
        l = 20
    elif l < 1:
        l = 1
    if c > 20:
        c = 20
    elif c < 1:
        c = 1
    x = 0
    while 1:
        if x == 0:
            linha = ("|") + (c * ("-")) + ("|")
            print(linha)
            x = x + 1
            
        elif x > 0 and x < l:
            linha = ("|") + (c * ("+")) + ("|")
            print(linha)
            x = x + 1
        else:
            linha = ("|") + (c * ("-")) + ("|")
            print(linha)
            break

print(moldura(5, 20))
