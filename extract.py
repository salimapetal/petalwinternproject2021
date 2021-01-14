def extract_address():
    address='This is demo program for address extraction it contians some data john smith  831 S. Linden Drive East Elmhurst, NY 11370 utility bill generated by spectrum mobile. '
    lastname = 'smith'
    splits_text = address.split()
    start_index : int = -1
    end_index: int = -1
    count: int = 0
    while count < len(splits_text):
        text_data = splits_text[count]
        # print(f'index={count} and text={text_data}')
        if lastname == text_data :
            start_index = count + 1
        if len(text_data) == 5 and text_data.isnumeric():
            end_index = count + 1
        count = count + 1
    print(f'address is {" ".join(splits_text[start_index:end_index])}')
    print(f'start={start_index} and end={end_index}')
if __name__ == "__main__":
    extract_address()





