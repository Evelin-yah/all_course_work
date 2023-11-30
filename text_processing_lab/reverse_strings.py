# text = input()
#
# while text != 'end':
#     text_reversed = ''
#     for _ in reversed(text):
#         text_reversed += _
#     print(f'{text} = {text_reversed}')
#     text = input()

word = input()

while word != 'end':
    print(f'{word} = {word[::-1]}')
    word = input()