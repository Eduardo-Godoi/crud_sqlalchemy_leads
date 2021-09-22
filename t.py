import re 


# telefone = "(41)90000-00011"
# padrao = "([0-9]{2,3})?(\([0-9]{2}\))([0-9]{4,5})-([0-9]{4})"

# result = re.fullmatch(padrao, telefone).group()
# print(result == re.Match)
# print(result)


# def validate_phone(phone):
#     try:
#         pattern = "([0-9]{2,3})?(\([0-9]{2}\))([0-9]{4,5})-([0-9]{4})"
#         re.fullmatch(pattern, phone).group()
#     except AttributeError:
#         msg = {'erro': 'Telefone Invalido formato aceito (00)12345-6789'}
#         return msg, 400



# print(type(validate_phone("(41)92000-00070")))