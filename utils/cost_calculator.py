from openpyxl import Workbook

def generate_excel():
    wb = Workbook()
    ws = wb.active

    ws.append(["Item", "Cost"])
    ws.append(["Material", 500000])
    ws.append(["Labour", 200000])

    file = "Sajals_Estimator_BOQ.xlsx"
    wb.save(file)

    return file
