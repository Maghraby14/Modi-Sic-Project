# PASS 1
#---------
import Pass1 
"""
First this function clears code
"""
Pass1.intermidiate_file()
"""
then this function puts the location of the next instruction
"""
Pass1.Pass_1_location_counter()
"""
this function produces the sybol table
"""
Pass1.Symbol_table()

# PASS 2
#---------
import Pass2
"""
This function generates the opcode
"""
Pass2.generating_object_code()
"""
This function makes the HTE record
"""
Pass2.generating_HTE_Record()