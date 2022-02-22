from RPA.Excel.Files import Files

lib = Files()


def read_excel_worksheet(path, worksheet):
    lib.open_workbook(path)
    return lib.read_worksheet_as_table(worksheet)


result = read_excel_worksheet("/home/usman/Downloads/EZ1-Mapping-File.xlsx", "Document Type")
citation = []
petition = []
for i in result:
    for (key, value) in i.items():
        if (key, value) == ("B", "Citation"):
            citation.append(i["A"])
        elif (key, value) == ("B", "Petition"):
            petition.append(i["A"])
print(citation)
print(petition)
print("the program ended")