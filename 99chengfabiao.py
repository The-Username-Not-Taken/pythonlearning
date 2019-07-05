import xlwt
book=xlwt.Workbook(encoding='utf-8')
sheet1=book.add_sheet('九九乘法表')

for hang in range(0,9):
    for lie in range(0,hang+1):

        shoubing=open(r'shuzi.txt',encoding='UTF-8')

        chengji=(hang+1)*(lie+1)

        shuzi=shoubing.readlines()
        h=shuzi[hang]
        l=shuzi[lie]
        cj=shuzi[chengji-1]

        shoubing.close()

        if len(str(chengji))==1:
            sheet1.write(hang,lie,'%s%s得%s'%(l,h,cj))
        else:
            sheet1.write(hang,lie,'%s%s%s'%(l,h,cj))

book.save('乘法表.xls')
print('OK了!')