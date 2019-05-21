'''excel的读写，用于读取接口用例和写入接口请求响应值'''
import  xlrd,openpyxl,xlwt,os
from openpyxl import load_workbook
BASE_PATH = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + '\..')
excel_path=BASE_PATH+r'\config\interface_testcases.xlsx'
class Excel:
    def __init__(self):
        self.filename=excel_path

    def read_excel(self):
        excel=xlrd.open_workbook(self.filename)
        sheet=excel.sheet_by_index(0)
        rows=sheet.nrows
        cols=sheet.ncols
        headers=sheet.row_values(0)
        caseInfo=[]
        for i in range(1,rows):
            case_info = {}
            for j in range(0,cols):
                case_info[headers[j]]=sheet.row_values(i)[j]
            caseInfo.append(case_info)
        return caseInfo

    def write_respone(self,row,respone):
        wb = load_workbook(self.filename)
        wb1 = wb.active
        wb1.cell(row,8,respone)
        wb.save(self.filename)

    def write_result(self,row,result):
        wb = load_workbook(self.filename)
        wb1 = wb.active
        if result:
            wb1.cell(row,10,'pass')
        else:
            wb1.cell(row,10,'fail')
        wb.save(self.filename)
