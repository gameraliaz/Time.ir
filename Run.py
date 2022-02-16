import GetData
import SaveData


def main():
    mkey=-1
    Data=[]
    while mkey==-1:
        print("What do you want to do?")
        print("0-Exit")
        print("1-GetEventList")
        print("2-Get...")
        print("3-Get...",'\n',':')
        mkey=input()
        match mkey:
            case '1':
                Data=GetData.ListOfEvents()
            case '0':
                return
            case _:
                mkey=-1
                print(".....wrong.....")
    skey=-1
    while skey==-1:
        print("How do you want your data?")
        print("0-Exit")
        print("1-CSV file")
        print("2-Text file")
        print("3-Print")
        print("4-... file",'\n',':')
        skey=input()
        if skey!=3 and skey!=0:
            location=input("location? (empty=here) \n")
            namefile=input("File name? \n")
        match skey:
            case '1':
                SaveData.ToCSV(location,namefile,Data)
            case '2':
                SaveData.ToText(location,namefile,Data)
            case '3':
                print(Data)
            case '0':
                return
            case _:
                print(".....wrong.....")
                skey=-1