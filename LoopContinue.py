loop_count = 0
Continue = input("Do you want to continue?")

#will keep reading data until input is neither "Y" or "y"
while (Continue == "Y" or Continue == "y"):
    loop_count += 1
    Continue = input("Do you want to continue?")
print ("Loop ran",loop_count,"times")
