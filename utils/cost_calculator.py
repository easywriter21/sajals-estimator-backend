from openpyxl import Workbook


def generate_excel():
    wb = Workbook()
    ws = wb.active
    ws.title = "Estimate"

    ws.append(["Item", "Cost"])
    ws.append(["Material", 500000])
    ws.append(["Labour", 200000])
    ws.append(["Total", 700000])

    file_path = "estimate.xlsx"
    wb.save(file_path)

    return file_path
