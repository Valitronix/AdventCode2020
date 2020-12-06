with open('data') as my_data:
    seatIDs = []
    for boarding_pass in my_data.read().splitlines():
        row_num = boarding_pass[0:7].replace('F', '0').replace('B', '1')
        seat_num = boarding_pass[7:].replace('L', '0').replace('R', '1')
        seatIDs.append(int(row_num, 2) * 8 + int(seat_num, 2))
    
print("Max seat ID is ", max(seatIDs))

