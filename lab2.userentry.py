

def display_main_menu():
    print("display_main_menu")

def get_user_input():
    userinput=input("enter numbers=")
    string_list =userinput.split(",")
    userinputlist=[]
    for i in string_list:
        userinputlist.append(float(i))
    return userinputlist

def calc_average(userinput):
    
    average= sum(userinput)/len(userinput)
    return average

def find_min_max(userinput):
    
    maxx=max(userinput)
    minn=min(userinput)
    return maxx, minn

def sort_temperature(userinput):
    newlist1 = sorted(userinput)
    newlist2 = sorted(userinput,reverse=True)
    return newlist1, newlist2

def main():
    display_main_menu()
    userinput= get_user_input()
    
    print("average",calc_average(userinput))
    print("min and max ",find_min_max(userinput))
    print("sort temperature",sort_temperature(userinput) )

 
if __name__ == "__main__":

    main() 





    
