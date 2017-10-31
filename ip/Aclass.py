

ainfo = []
for i in range(2, 23):
	subnum = (2 ** i)  - 2
	pcs = 2 ** (32 - (i + 8)) - 2
	b = '1' * 8 + '1' * i + '0' * (32-(i+8))
	x = tuple(map(lambda x: int(x, 2), (b[0:8], b[8:16],b[16:24],b[24:32])))
	mask = "%s.%s.%s.%s" % x
	ainfo.append((i,subnum,mask,pcs))	

for row in ainfo:
	print("<tr>")
	for item in row:
		print("<th>%s</th>" % item)
	print("</tr>")
