SEQ_NOT_VALID = -1

# def toAlphabet(num):
#     return ord(num+96)

def decode(encoded_string):
    '''
    This function takes in an encoded string and returns an array of possible decodings
    :param encoded_string:
    :return:
    '''
    if len(encoded_string) == 0:
        return 1
    elif encoded_string[0] is '0':
        return SEQ_NOT_VALID
    elif len(encoded_string) == 1:
        return 1 #toAlphabet(int(encoded_string))

    total_cases = 0
    # Case 1
    seq_end = decode(encoded_string[1:])
    if seq_end!=SEQ_NOT_VALID:
        total_cases+=seq_end

    # Case 2
    if int(encoded_string[0:2])>26:
        return SEQ_NOT_VALID
    seq_end = decode(encoded_string[2:])
    if seq_end!=SEQ_NOT_VALID:
        total_cases+=seq_end

    return total_cases

def test_solution():
    assert decode('111') == 3

