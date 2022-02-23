alfabeto = str('a,b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z')

r = 3
senha = input("Digite uma senha de 4 dígitos: ")

d0 = ( alfabeto.index(senha[0]) + r) % len(alfabeto)
d1 = ( alfabeto.index(senha[1]) + r) % len(alfabeto)
d2 = ( alfabeto.index(senha[2]) + r) % len(alfabeto)
d3 = ( alfabeto.index(senha[3]) + r) % len(alfabeto)
senha_c = alfabeto[d0]+alfabeto[d1]+alfabeto[d2]+alfabeto[d3]

d0 = ( alfabeto.index(senha_c[0]) - r) % len(alfabeto)
d1 = ( alfabeto.index(senha_c[1]) - r) % len(alfabeto)
d2 = ( alfabeto.index(senha_c[2]) - r) % len(alfabeto)
d3 = ( alfabeto.index(senha_c[3]) - r) % len(alfabeto)
senha_d = alfabeto[d0]+alfabeto[d1]+alfabeto[d2]+alfabeto[d3]

print(senha,senha_c,senha_d)
