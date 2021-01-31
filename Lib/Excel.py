from openpyxl import Workbook, load_workbook, worksheet, workbook
from contextlib import closing
from fileinput import filename
import os.path
from openpyxl.xml.constants import MAX_ROW

def create_excel_file(sheet_name, file_name):
    with closing(Workbook()) as wb:
        ws = wb.active
        ws.title = sheet_name
        ws.column_dimensions['A'].width = 80
        ws.column_dimensions['B'].width = 80
        wb.save(file_name)
        
def add_new_sheet(sheet_name, file_name):
    with closing(load_workbook(filename=file_name)) as wb:
        wb.create_sheet(sheet_name)
        ws = wb[sheet_name]
        ws.column_dimensions['A'].width = 80
        ws.column_dimensions['B'].width = 80
        ws.column_dimensions['C'].width = 80
        wb.save(file_name)

def add_value(sheet_name, file_name, cell_cords, value):
    with closing(load_workbook(filename=file_name)) as wb:
        ws = wb[sheet_name]
        ws[cell_cords] = value
        wb.save(file_name)

        
def get_row_count(sheet_name, file_name):
    with closing(load_workbook(filename=file_name)) as wb:
        ws = wb[sheet_name]
        return ws.max_row
        
def append_value(sheet_name, file_name, c1_value):
    with closing(load_workbook(filename=file_name)) as wb:
        ws = wb[sheet_name]
        ws.append([c1_value])
        wb.save(file_name)
#name changed from append_value to append_value1 to remove duplicacy.change it back if required  		
def append_values_old(sheet_name, file_name, c1_value, c2_value):
    with closing(load_workbook(filename=file_name)) as wb:
        ws = wb[sheet_name]
        ws.append([c1_value, c2_value])
        wb.save(file_name)

def append_values(sheet_name, file_name, c1_value, c2_value, c3_value, c4_value, c5_value):
    Value = get_value_from_excel(sheet_name,file_name,c1_value)
    #print(Value)
    if  Value == 'Key Not Found':
        with closing(load_workbook(filename=file_name)) as wb:
            ws = wb[sheet_name]
            ws.append([c1_value, c2_value, c3_value, c4_value, c5_value])
            wb.save(file_name)
    
		
def check_file(path):
    if os.path.isfile(path):
        return True
    else:
        return False
        
def find_model(sheet_name, file_name, value):
    with closing(load_workbook(filename=file_name)) as wb:
        ws = wb[sheet_name]
        for row in ws.iter_rows(max_row=ws.max_row, min_col=2):
            for cell in row:
                if (value == cell.value):
                    cr = 'A'+str(cell.row)
                    return ws[cr].value
                
        else:
            return 0
                
                
def find_value(sheet_name, file_name, value):
    with closing(load_workbook(filename=file_name)) as wb:
        ws = wb[sheet_name]
        for row in ws.iter_rows(max_row=ws.max_row, min_col=1):
            for cell in row:
                if (value == cell.value):
                    
                    return cell.row
                
        else:
            return 0            

def find_row(sheet_name, file_name, value):
    with closing(load_workbook(filename=file_name)) as wb:
        ws = wb[sheet_name]
        for row in ws.iter_rows(max_row=ws.max_row, min_col=1):
            for cell in row:
                if (value == cell.value):
                    print(cell.value)
                    return cell.row
                
        else:
            return 0
        
def find_column(sheet_name, file_name, value):
    with closing(load_workbook(filename=file_name)) as wb:
        ws = wb[sheet_name]
        for row in ws.iter_rows(max_row=ws.max_row, min_col=1):
            for cell in row:
                if (value == cell.value): 
                    
                    return cell.column
                
        else:
            return 0         

def read_excel_cell(sheet_name, file_name, cellcords):
    with closing(load_workbook(filename=file_name)) as wb:
        ws = wb[sheet_name]
        return ws[cellcords].value            
            
def check_sheet(sheet_name, file_name):
    with closing(load_workbook(filename=file_name, read_only=True)) as wb:
        if sheet_name in wb.sheetnames:
            return True
        else:
            return False
        
def find_uuid(sheet_name, file_name):
    with closing(load_workbook(filename=file_name)) as wb:
        ws = wb[sheet_name]
        for row in ws.iter_rows(max_row=ws.max_row, min_col=1):
            for cell in row:
                if ('Distributed' == cell.value):
                    cr = 'C'+str(cell.row)
                    return ws[cr].value
                
        else:
            return 0
			
def find_uuid_AAI(sheet_name, file_name):
    with closing(load_workbook(filename=file_name)) as wb:
        ws = wb[sheet_name]
        for row in ws.iter_rows(max_row=ws.max_row, min_col=1):
            for cell in row:
                if ('Distributed(MSO Verified)' == cell.value):  
                    cr = 'C'+str(cell.row)
                    return ws[cr].value
                
        else:
            return 0        


def get_specific_value_from_excel(sheet_name,file_name,cellcords):
    with closing(load_workbook(filename=file_name)) as wb:
        ws = wb[sheet_name]
        cr = str(cellcords)
        return  ws[cr].value


def get_value_from_excel(sheet_name,file_name,key):
    with closing(load_workbook(filename=file_name)) as wb:
        ws = wb[sheet_name]
        for row in ws.iter_rows(max_row=ws.max_row, min_col=1):
            for cell in row:
                if (str(key) == str(cell.value)):
                    next_col_ascii = ord(cell.column) + 1
                    next_col = chr(next_col_ascii)
                    cr = str(next_col) + str(cell.row)
                    return ws[cr].value
                
        else:
            return 'Key Not Found'   
        
        
def update_value_from_excel(sheet_name,file_name,key, value):
    with closing(load_workbook(filename=file_name)) as wb:
        ws = wb[sheet_name]
        for row in ws.iter_rows(max_row=ws.max_row, min_col=1):
            for cell in row:
                if (str(key) == str(cell.value)):
                    next_col_ascii = ord(cell.column) + 1
                    next_col = chr(next_col_ascii)
                    cr = str(next_col) + str(cell.row)
                    ws[cr] = value
                    wb.save(file_name)
                    return  'Value Updated Successfully'
                
        else:
            return 'Key Not Found'                 
        
        
        

def update_value_from_excel_xlsm(sheet_name,file_name,key, value):
    with closing(load_workbook(filename=file_name, keep_vba=True)) as wb:
        ws = wb[sheet_name]
        for row in ws.iter_rows(max_row=ws.max_row, min_col=1):
            for cell in row:
                if (str(key) == str(cell.value)):
                    next_col_ascii = ord(cell.column) + 1
                    next_col = chr(next_col_ascii)
                    cr = str(next_col) + str(cell.row)
                    ws[cr] = value
                    wb.save(file_name)
                    return  'Value Updated Successfully'
                
        else:
            return 'Key Not Found'             			
