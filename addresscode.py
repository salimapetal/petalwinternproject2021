from SplitUtilityBill import split_utility_bill

def extract_address(filename,last_name,zip_code):
    words_in_file = split_utility_bill(filename)
    print('- - - - - - - - - -')
    start_index : int = -1
    end_index: int = -1
    count: int = 0

    while count < len(words_in_file) and (start_index == -1 or end_index == -1):
        text_data = words_in_file[count]
        print(f'index={count} and text={text_data}')
        if last_name in text_data :
            start_index = count + 1
        if zip_code == text_data:
            end_index = count + 1
        count = count + 1
    address = " ".join(words_in_file[start_index:end_index])
    print(f'address is {address}')
    print(f'start={start_index} and end={end_index}')
    return address
    
if __name__ == "__main__":
    extract_address()