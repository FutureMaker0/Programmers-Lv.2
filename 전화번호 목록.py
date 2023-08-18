# 해시는 딕셔너리다.

def solution(phone_book):
    headers = {}
    
    for phone_number in phone_book:
        headers[phone_number] = 1
    # print(headers)
    
    for phone_number in phone_book:
        header = ''
        for number in phone_number:
            header += number
            if header in headers and header != phone_number:
                return False
    return True


'''
안된다

def solution(phone_book):
    phone_book.sort()
    # print(phone_book)

    for p1, p2 in zip(phone_book, phone_book[1:]):
#         print(p1, type(p1))
#         print(p2, type(p2))

        if p2.startswitch(p1): return False
    return True
'''
