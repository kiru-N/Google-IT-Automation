def domino_set():
    total_combination = 0
    for first_block in range(7):
        for second_block in range(first_block, 7):
            print(first_block, second_block)
            total_combination += 1
    print("Total_combination: ", total_combination)
    

domino_set()
