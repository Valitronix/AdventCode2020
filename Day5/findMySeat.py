with open('data') as my_data:
    seatIDs = ['0'] * (int('1111111', 2) * 8 + int('111', 2))
    print(seatIDs)
    for boarding_pass in my_data.read().splitlines():
        row_num = boarding_pass[0:7].replace('F', '0').replace('B', '1')
        seat_num = boarding_pass[7:].replace('L', '0').replace('R', '1')
        seatIDs[int(row_num, 2) * 8 + int(seat_num, 2)] = '1'
    
print("Empty seat ID is ", ("".join(seatIDs).find('101') + 1) )