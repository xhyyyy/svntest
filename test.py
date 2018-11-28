import xlrd

def cengsu(list):
    for i,t in enumerate(list):
        print((i,t))
        num =0
        if t =='':
            num = i
            break
    return num



workxls = xlrd.open_workbook("svn.xlsx")
worksheet = workxls.sheet_by_name("Sheet1")
col = worksheet.ncols
row = worksheet.nrows
svnconf = open("svn.txt","w")
for i in range(row):
    row_list = worksheet.row_values(i)
    print(cengsu(row_list))

