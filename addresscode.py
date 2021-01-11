import imagetotext
import SplitUtilityBill

def extract_address():
    address= imagetotext.ocr_core()
    lastname = 'COPNEY'
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