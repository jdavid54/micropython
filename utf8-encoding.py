# https://fr.wikipedia.org/wiki/UTF-8
for n in range(100):  #8192
    b = str(chr(128+n))
    #print(b, end='')
    #print(b.encode(encoding='utf-8'),b,hex(128+n))
    
legende="""
# ascii : 0 - 127(0x7f)
# unicode : 128(0x80) - 2047(0x7ff) (2 octets)
# unicode : 2048(0x800) - 55295(0xd7ff) (3 octets)
# codage interdit (demi-codets) : 55296(d800) - 57343(dfff) 
# unicode : 57344(e000) - 65535(ffff) (3 octets)
# unicode : 65536(10000) - 1114111(10ffff) (4 octets)
"""
print(legende)

for n in range(200):  #8192
    b = str(chr(160+n))
    #print(b, end='')
    #print(b.encode(encoding='utf-8'),b,hex(8192+n), 8192+n)
    
for n in range(10000):  #8192
    b = str(chr(128+n))
    #print(b, end='')
    print(b,end='')
    if n%1000 == 0 and n!=0: print('\n',n)

# unicode d'un string
#print('Ạ Đ đ'.encode('utf-8'))
#b'\xe1\xba\xa0 \xc4\x90 \xc4\x91'

viet_char = 'áàãăêèéíìôơóòùúũưÂĐđ ẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ'

for v in viet_char:
    print(v,v.encode('utf-8'))
    
viet = 'Việt Nam, tên chính thức là Cộng hòa Xã hội chủ nghĩa Việt Nam, là quốc gia nằm ở cực phía Đông của bán đảo Đông Dương thuộc khu vực Đông Nam Á, giáp với Lào, Trung Quốc, Campuchia, Biển Đông và vịnh Thái Lan.'     
viet2 = 'Các khai quật khảo cổ học cho thấy Việt Nam đã có người sinh sống sớm nhất từ thời đại đồ đá cũ. Sau thời kỳ Văn Lang, nước Âu Lạc cổ đại, lấy trung tâm là trung du và đồng bằng sông Hồng cùng vùng ven biển gần đó, bị nhà Triệu từ phương bắc thôn tính vào đầu thế kỷ thứ 2 TCN, sau đó Việt Nam trở thành một bộ phận của các triều đại Trung Quốc trong hơn một thiên niên kỷ.'

for v in viet2:
    l = 3-len(v.encode('utf-8'))
    #print(v.encode('utf-8'),'\t'*l,v)