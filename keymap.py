#!/usr/bin/python
#encoding=utf-8

# other coordinates
login = '1063-82'
logout = '1095-82'
sure = '743-455'
down = '1271-750'
clickNum = 2
up = '1271-70'
view = '386-734'
blank = '60-400'

# initial values
pos_1 = [127, 63]
pos_0 = [487, 63]
pos_rctrl = [457, 155]

# heigh and width of each 1-key
width = (pos_0[0] - pos_1[0]) / 9
height = (pos_rctrl[1] - pos_0[1]) / 4

# other keys (number)
pos_2 = [pos_1[0] + width, pos_1[1]]
pos_3 = [pos_1[0] + 2 * width, pos_2[1]]
pos_4 = [pos_1[0] + 3 * width, pos_2[1]]
pos_5 = [pos_1[0] + 4 * width, pos_2[1]]
pos_6 = [pos_1[0] + 5 * width, pos_2[1]]
pos_7 = [pos_1[0] + 6 * width, pos_2[1]]
pos_8 = [pos_1[0] + 7 * width, pos_2[1]]
pos_9 = [pos_1[0] + 8 * width, pos_2[1]]

# other keys (characters)
# row 1
pos_q = [pos_1[0] - int(0.5 * width), pos_1[1] + height] 
pos_w = [pos_2[0] - int(0.5 * width), pos_2[1] + height] 
pos_e = [pos_3[0] - int(0.5 * width), pos_3[1] + height] 
pos_r = [pos_4[0] - int(0.5 * width), pos_4[1] + height] 
pos_t = [pos_5[0] - int(0.5 * width), pos_5[1] + height] 
pos_y = [pos_6[0] - int(0.5 * width), pos_6[1] + height] 
pos_u = [pos_7[0] - int(0.5 * width), pos_7[1] + height] 
pos_i = [pos_8[0] - int(0.5 * width), pos_8[1] + height] 
pos_o = [pos_9[0] - int(0.5 * width), pos_9[1] + height] 
pos_p = [pos_0[0] - int(0.5 * width), pos_0[1] + height] 
# row 2
pos_a = [pos_1[0], pos_1[1] + 2 * height]
pos_s = [pos_2[0], pos_2[1] + 2 * height]
pos_d = [pos_3[0], pos_3[1] + 2 * height]
pos_f = [pos_4[0], pos_4[1] + 2 * height]
pos_g = [pos_5[0], pos_5[1] + 2 * height]
pos_h = [pos_6[0], pos_6[1] + 2 * height]
pos_j = [pos_7[0], pos_7[1] + 2 * height]
pos_k = [pos_8[0], pos_8[1] + 2 * height]
pos_l = [pos_9[0], pos_9[1] + 2 * height]
pos_z = [pos_w[0], pos_w[1] + 2 * height]
# row 3
pos_z = [pos_w[0], pos_w[1] + 2 * height]
pos_x = [pos_e[0], pos_e[1] + 2 * height]
pos_c = [pos_r[0], pos_r[1] + 2 * height]
pos_v = [pos_t[0], pos_t[1] + 2 * height]
pos_b = [pos_y[0], pos_y[1] + 2 * height]
pos_n = [pos_u[0], pos_u[1] + 2 * height]
pos_m = [pos_i[0], pos_i[1] + 2 * height]
# special ones
pos_dot = [pos_m[0] + 2 * width, pos_m[1]]
pos_tab = [pos_q[0] - int(1.5 * width), pos_q[1]]
pos_caps = [pos_a[0] - int(1.75 * width), pos_a[1]]
pos_lshift = [pos_z[0] - int(2 * width), pos_z[1]]
pos_enter = [pos_l[0] + int(3.75 * width), pos_l[1]]

def keyCoord(pos_key) :
	return str(pos_key[0]) + '-' + str(pos_key[1])

# keys dict
key = {}
key['1'] = keyCoord(pos_1)
key['2'] = keyCoord(pos_2)
key['3'] = keyCoord(pos_3)
key['4'] = keyCoord(pos_4)
key['5'] = keyCoord(pos_5)
key['6'] = keyCoord(pos_6)
key['7'] = keyCoord(pos_7)
key['8'] = keyCoord(pos_8)
key['9'] = keyCoord(pos_9)
key['0'] = keyCoord(pos_0)
key['q'] = keyCoord(pos_q)
key['w'] = keyCoord(pos_w)
key['e'] = keyCoord(pos_e)
key['r'] = keyCoord(pos_r)
key['t'] = keyCoord(pos_t)
key['y'] = keyCoord(pos_y)
key['u'] = keyCoord(pos_u)
key['i'] = keyCoord(pos_i)
key['o'] = keyCoord(pos_o)
key['p'] = keyCoord(pos_p)
key['a'] = keyCoord(pos_a)
key['s'] = keyCoord(pos_s)
key['d'] = keyCoord(pos_d)
key['f'] = keyCoord(pos_f)
key['g'] = keyCoord(pos_g)
key['h'] = keyCoord(pos_h)
key['j'] = keyCoord(pos_j)
key['k'] = keyCoord(pos_k)
key['l'] = keyCoord(pos_l)
key['z'] = keyCoord(pos_z)
key['x'] = keyCoord(pos_x)
key['c'] = keyCoord(pos_c)
key['v'] = keyCoord(pos_v)
key['b'] = keyCoord(pos_b)
key['n'] = keyCoord(pos_n)
key['m'] = keyCoord(pos_m)
key['.'] = keyCoord(pos_dot)
cap = keyCoord(pos_caps)
ctl = keyCoord(pos_rctrl)
sht = keyCoord(pos_lshift)
tab = keyCoord(pos_tab)
ent = keyCoord(pos_enter)
