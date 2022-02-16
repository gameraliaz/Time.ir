import csv;
def ToCSV(location,filename,data):
    with open(f"{location}\{filename}.csv" if location !='' else f"{filename}.csv", 'w' , encoding='utf-8-sig' , newline='') as out_file:
        headers = [ 
            "day",
            "discription",
            "holiday"
        ] 
        writer = csv.DictWriter(out_file, headers)
        writer.writeheader()
        writer.writerows(data)
def ToText(location,filename,data):
    with open(f"{location}\{filename}.txt" if location !='' else f"{filename}.txt", 'w' , encoding='utf-8-sig' , newline='') as out_file:
        out_file.writelines(data)