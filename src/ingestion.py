import csv
def load_and_validate(path):
    clean_rows = []
    rejected_rows = []

    with open(path,newline="",encoding="utf-8") as f :
        reader = csv.DictReader(f)
        for Line_no, row in enumerate(reader, start=2):
            pass 
    return clean_rows, rejected_rows