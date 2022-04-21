import re

#
# # regexp = re.compile("the|The")
# # regexp = re.compile("(t|T)he")
# regexp = re.compile("[tT]he")
# count = 0
# file = open("moby_01.txt", 'r')
# for line in file.readlines():
#     if regexp.search(line):
#         count = count + 1
# file.close()
# print(count)
#
# import re
#
#
# def add_code(match_obj):
#     return ("+1-" + match_obj.group('phone'))
#
#
# # re.sub(r"(?P<phone>(\d{3}-)?\d{3}-\d{4})", add_code, "111-222-3333")
# regexp = re.compile(
#     r"(?P<last>[-a-zA-Z]+)," r" (?P<first>[-a-zA-Z]+)" r"( (?P<middle>([-a-zA-Z]+)))?" r":(?P<phone> (\+\d{1,3}-)?(\d{3}-)?\d{3}-\d{4})")
# file = open("textfile", 'r')
# for line in file.readlines():
#     result = regexp.search(line)
#     if result == None:
#         print("Oops, I don't think this is a record")
#     else:
#         lastname = result.group('last')
#         firstname = result.group('first')
#         middlename = result.group('middle')
#         if middlename == None:
#             middlename = ""
#         phonenumber = result.group('phone')
#         phonenumber = re.sub(r" (?P<phone>(\d{3}-)?\d{3}-\d{4})", add_code, phonenumber)
#         print('Name:', firstname, middlename, lastname, ' Number:', phonenumber)
# file.close()
#
# string = "If the the problem is textual, use the the re module"
# pattern = r"the the"
# regexp = re.compile(pattern)
# print(regexp.sub("the", string))
#
# int_string = "1 2 3 4 5"
#
#
# def int_match_to_float(match_obj):
#     return (match_obj.group('num') + ".0")
#
#
# pattern = r"(?P<num>[0-9]+)"
# regexp = re.compile(pattern)
# print(regexp.sub(int_match_to_float, int_string))

test_numbers = ["+1 223-456-7890", "1-223-456-7890", "+1 223 456-7890", "(223) 456-7890", "1 223 456 7890",
                "223.456.7890", "1-989-111-2222"]


def return_number(match_obj):
    cod_country = match_obj.group('cod_country')
    if not cod_country:
        cod_country = 1
    cod_city = match_obj.group('cod_city')
    phoneNumber1 = match_obj.group('phoneNumber1')
    phoneNumber2 = match_obj.group('phoneNumber2')
    if not re.match(r'[2-9][0-8]\d', cod_city):
        raise ValueError('not valid cod_city ' + cod_city)
    if not re.match(r'[2-9]\d{2}', phoneNumber1):
        raise ValueError('not valid number exchange ' + phoneNumber1)
    return ('{}-{}-{}-{}').format(cod_country, cod_city, phoneNumber1, phoneNumber2)


regexp = re.compile(
    r'\+?(?P<cod_country>\d{1,3})?[- .]?\(?(?P<cod_city>\d{3})\)?[- .](?P<phoneNumber1>\d{3})[- .](?P<phoneNumber2>\d{4})')
for number in test_numbers:
    # result = regexp.search(number)
    print(regexp.sub(return_number, number))
