# add your imports here
import codecs


# reading input (don't forget strip in other challenges!)
str_hex = input().strip()

str_base64 = codecs.encode(codecs.decode(str_hex, 'hex'),
                           'base64').decode()    # your code here

print(str_base64)
