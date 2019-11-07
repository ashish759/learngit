import xlrd 
  
loc = ("C:/Users/ashishkp/Downloads/Category.xlsx") 
  
wb1 = xlrd.open_workbook(loc) 
sheet1 = wb1.sheet_by_index(0)

sheet1.cell_value(0, 0)

loc2 = ("C:/Users/ashishkp/Downloads/Application.xlsx") 
  
wb2 = xlrd.open_workbook(loc2) 
sheet2 = wb2.sheet_by_index(0)

sheet2.cell_value(0, 0)


val = input("Enter your value: ") 

for j in range(sheet1.ncols):
    for i in range(sheet1.nrows): 
        if(sheet1.cell_value(i, j).lower() == val.lower()):
            print(sheet1.cell_value(i, j+1))
            val2 = (sheet1.cell_value(i, j+1))


for j in range(sheet2.ncols):
    for i in range(sheet2.nrows): 
        if(sheet2.cell_value(i, j) == val2):
            print(sheet2.cell_value(i, j+1))
