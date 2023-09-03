def intermidiate_file():
    file=open("input.txt","r")
    the_intermidiate_file=[]
    for line in file :
        line=line[3:]
        line=line.replace("\t"," ")
        line=line.strip(" ")
        my_new=[]
        if line.startswith("."):
            continue
        else:
            temp_list=line.split()
            temp_list=temp_list[:3]
            try:
                temp_list=temp_list[0]+" "+temp_list[1]+" "+temp_list[2]+"\n"
            except:
                pass
        
            the_intermidiate_file.append(temp_list)
    the_intermidiate_file.append("End")
    file=open("intermidiate.txt","w")
    for line in the_intermidiate_file:
        file.write(line)
    return the_intermidiate_file

def Pass_1_location_counter():
    the_intermidiate_file=intermidiate_file()
    splited_list=[]
    for element in the_intermidiate_file:
        splited_list.append(element.split())
    starting_address=int(splited_list[0][2],base=16)
    my_first_pass=["Address"+" "+the_intermidiate_file[0]]
    i=0
    n=starting_address
    for line in the_intermidiate_file:
        temp_list=line.split()
        
        if i==0:
            i+=1
            continue
        elif temp_list[0].lower() == "end":
            n+=3
        else:
            s=hex(n)
            new_line=str(s)+" "+line
            my_first_pass.append(new_line)
            if temp_list[0].lower() != "end":
                if temp_list[1].lower()=="byte":
                    if temp_list[2].lower().startswith("x"):
                        n+=int((len(temp_list[2].lower().strip('x'))-2)/2)
                    elif temp_list[2].lower().startswith("c"):
                        n+=int((len(temp_list[2].lower().strip('c'))-2))
                elif temp_list[1]=="word":
                    n+=3
                elif temp_list[1].lower()=="resb":
                    n+=int(temp_list[2])
                elif temp_list[1].lower()=="resw":
                    n+=int(temp_list[2])*3
                elif temp_list[1].lower() in ['fix','float','hio','norm','sio','tio']:
                    n+=1
                else:
                    n+=3
            else: n+=3               
    file=open("pass_one.txt","w")
    for line in my_first_pass:
        file.write(line)
    return my_first_pass
def Symbol_table():
    my_first_pass=Pass_1_location_counter()
    temp_list_1=[]
    for line in my_first_pass:
        temp_list_1.append(line.split())
    symbol_table=[]
    symbol_table.append("loc  label\n")
    for i in range(1,len(temp_list_1)):
        if temp_list_1[i][1]!="-":
            temp_list_2=temp_list_1[i][0]+" "+temp_list_1[i][1]
            symbol_table.append(temp_list_2)
    file=open("symboltable.txt","w")
    for line in symbol_table:
        file.write(line+"\n")
    return symbol_table
