import xlwt
import os
    # 设置表格样式
proDir = os.path.split(os.path.realpath(__file__))[0]
excelPath = os.path.join(proDir, "../common/data.xlsx")
class write_excel:
    def set_style(name, height, bold=False):
        style = xlwt.XFStyle()
        font = xlwt.Font()
        font.name = name
        font.bold = bold
        font.color_index = 4
        font.height = height
        style.font = font
        return style
    # 写Excel
    def write_excel_data(examID_list,id_list,questionId_list,score_list):
        f = xlwt.Workbook()
        sheet1 = f.add_sheet('app_test_data', cell_overwrite_ok=True)
        row0 = ['examId', 'id','questionId','score']
        colum0 = examID_list
        colum1 = id_list
        colum2 = questionId_list
        colum3 = score_list
        # 写第一行
        for i in range(0, len(row0)):
            sheet1.write(0, i, row0[i],write_excel.set_style('Times New Roman', 220, True))
        # 写列
        for i in range(0, len(colum0)):
            sheet1.write(i + 1, 0, colum0[i], write_excel.set_style('Times New Roman', 220, True))
            sheet1.write(i + 1, 1, colum1[i], write_excel.set_style('Times New Roman', 220, True))
            sheet1.write(i + 1, 2, colum2[i], write_excel.set_style('Times New Roman', 220, True))
            sheet1.write(i + 1, 3, colum3[i], write_excel.set_style('Times New Roman', 220, True))
            # sheet1.write(i + 1, 3, colum3[i], write_excel.set_style('Times New Roman', 220, True))
            # print("写入")
        print("写入成功")
        f.save("data.xls")

if __name__ == '__main__':
    write_excel.write_excel_data()
