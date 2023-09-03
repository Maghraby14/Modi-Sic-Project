import Pass1
def generating_object_code():
    the_first_pass = Pass1.Pass_1_location_counter()
    prev_symbol_table = Pass1.Symbol_table()
    instruction_set={
    "ADD":"18",
    "AND":"40",
    "COMP":"28",
    "DIV":"24",
    "J":"3C",
    "JEQ":"30",
    "JGT":"34",
    "JLT":"38",
    "JSUB":"48",
    "LDA":"00",
    "LDCH":"50",
    "LDL":"08",
    "LDX":"04",
    "MUL":"20",
    "OR":"44",
    "RD":"D8",
    "RSUB":"4C",
    "STA":"0C",
    "STCH":"54",
    "STL":"14",
    "STSW":"E8",
    "STX":"10",
    "SUB":"1C",
    "TD":"E0",
    "TIX":"2C",
    "WD":"DC",
    "FIX":"C4",
    "FLOAT":"C0",
    "HIO":"F4",
    "NORM":"C8",
    "SIO":"F0",
    "TIO":"F8"   
    }
    my_second_pass=[]
    for i in range (0,len(the_first_pass)):
        my_second_pass.append(the_first_pass[i].split())
    symbol_table=[]
    for i in range(0,len(prev_symbol_table)):
        symbol_table.append(prev_symbol_table[i].split())    
    #print(my_second_pass)
    #print(symbol_table)
    my_second=[]
    for line in my_second_pass:
        if line[2].lower()=='byte':
            if line[3].lower().startswith("x"):
                line.append(line[3].strip("X").strip("'"))
                my_second.append(line)
            else:
                s=line[3].strip("C").strip("'")
                l=""
                for letter in s:
                    l+=format(ord(letter),"x")
                line.append(l)
                my_second.append(line)
        elif line[2].lower()=='word':
            objectcode=hex(int(line[3]))
            objectcode=str(objectcode)[2:]
            while len(objectcode) !=6:
                objectcode="0"+objectcode
            else:
                line.append(objectcode)
                my_second.append(line)

        elif line[2].lower() in ['resb','resw']:
            line.append("No-Object code")
            my_second.append(line)
        elif line[0].lower()=='address':
            my_second.append(line)
        elif line[2].lower()=="rsub":
            line.append(instruction_set['RSUB']+"0000")
            my_second.append(line)
        elif line[3].lower().endswith(",x"):
            opcode=instruction_set[line[2]]
            for i in range(1,len(symbol_table)):
                if symbol_table[i][1].lower()==line[3].lower().rstrip(",x"):
                    address=symbol_table[i][0]
                    address=str(int(address[2:])+8000)
            object_code=opcode+address
            line.append(object_code)
            my_second.append(line)
        elif line[3].lower().startswith("#"):
            opcode=instruction_set[line[2]]
            opcode=hex(int(bin(int(opcode,16))[2:].zfill(8)[:7]+"1",2))
            address=line[3].lower().strip("#")
            if(len(address)!=4):
                address="0"+address
                object_code=opcode+address
                line.append(object_code)
                my_second.append(line)        
        else:
            opcode=instruction_set[line[2]]
            for i in range(1,len(symbol_table)):
                if symbol_table[i][1].lower()==line[3].lower():
                    address=symbol_table[i][0]
            object_code=opcode+address[2:]
            line.append(object_code)
            my_second.append(line)
    the_objectcode_table=[]
    for line in my_second:
        l=""
        for ins in line :
            l+=ins+"\t"
        the_objectcode_table.append(l)
    file=open("out_pass2.txt","w")
    for line in the_objectcode_table:
        file.write(line+"\n")
    return my_second
def generating_HTE_Record():
    the_second_pass=generating_object_code()
    h_record=["H",".",the_second_pass[0][1],".",the_second_pass[1][0],".",the_second_pass[len(the_second_pass)-1][0]]
    e_record=["E",".",the_second_pass[1][0]]
    t_rec=[]
    start=the_second_pass[1][0]
    #print(hex(int(start,16)-int("0x101e",16)))
    i=1
    rsub_inst=[]
    for j in range(1,len(the_second_pass)):
        if j-i==10:
            t_rec.append(start)
            length=hex(int(the_second_pass[j][0],16)-int(start,16))
            t_rec.append(length)
            while i<j:
                if the_second_pass[i][4]=="No-Object code":
                    t_rec.reverse()
                    index=t_rec.index("T")
                    add=len(t_rec)-index-1+2
                    t_rec.reverse()
                    #print(t_rec[add])
                    rsub_inst.append(the_second_pass[i-1][0])
                    i+=1
                    continue
                else:
                    t_rec.append(the_second_pass[i][4])
                    i+=1
            t_rec.append("T")
            i=j
            start=the_second_pass[i][0]
        if j==len(the_second_pass)-1:
            t_rec.append(start)
            length=hex(int(the_second_pass[j][0],16)-int(start,16))
            t_rec.append(length)
            while i<=j:
                
                t_rec.append(the_second_pass[i][4])
                i+=1
            break
    t_rec[add]=hex(int(rsub_inst[0],16)-int(t_rec[add],16))  


    file=open("HTE Record.txt","w")
    for element in h_record:
        file.write(element)
    file.write("\n")
    file.write("T")

    for i in range(0,len(t_rec)-1):
        if t_rec[i]=="T":
            t_rec[i]="\n"+t_rec[i]
        
    #print(t_rec)
    for element in t_rec:
        file.write(element+".")

    file.write("\n")  
    for element in e_record:
        file.write(element)
