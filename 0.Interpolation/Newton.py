from Lb1._init_ import nodes

inter_point = 1.4301

nodes_len = len(nodes)
tabel_div_dif = [[i.f for i in nodes]]
div_dif = []
sum = 0
offset = 1

for i in range(nodes_len-1):
    for j in range(len(tabel_div_dif[i])-1):
        fract_part = 1/(nodes[j+offset].x - nodes[j].x)
        div_dif.append((tabel_div_dif[i][j+1] - tabel_div_dif[i][j])*fract)
    tabel_div_dif.append(div_dif)
    div_dif = []
    offset += 1

div_dif = [tabel_div_dif[i][0] for i in range(nodes_len)]

sum = div_dif[0]
mult = 1

for i in range(1, nodes_len):
    for j in range(0, i):
        mult *= (inter_point - nodes[j].x)
    sum += div_dif[i]*mult
    mult = 1

print(sum)
