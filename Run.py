import GetData
import SaveData
import ModifyData


def main():
    mkey=-1
    Data=[]
    while mkey==-1:
        print("What do you want to do?")
        print("0-Exit")
        print("1-Get current month events list")
        print("2-Get current year events list")
        print("3-Get input month events list")
        print("4-Get day events list")
        mkey=input()
        match mkey:
            case '1':
                Data.append(GetData.ListOfCurrentMonthEvents())
            case '2':
                Data=GetData.ListOfCurrentYearEvents()
            case '3':
                year=input("Year : ")
                month=input("Month : ")
                Data.append(GetData.ListOfMonthEvents(year,month))
            case '4':
                year=input("Year : ")
                month=input("Month : ")
                day=input("Day : ")
                Data.append(GetData.ListOfDayEvents(year,month,day))
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
        skey=input()
        if skey!=3 and skey!=0:
            location=input("location? (empty=here) \n")
            for i in range(len(Data)):
                Data[i]=ModifyData.OptimizeDayData(Data[i])
        match skey:
            case '1':
                for i in range(len(Data)):
                    SaveData.ToCSV(location,str(i+1),Data[i])
            case '2':
                for i in range(len(Data)):
                    SaveData.ToText(location,str(i+1),Data[i])
            case '3':
                print(str(Data))
            case '0':
                return
            case _:
                print(".....wrong.....")
                skey=-1

main()