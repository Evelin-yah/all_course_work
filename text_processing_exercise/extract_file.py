filepath = input().split('\\')

file = filepath[-1]
file_name, extension = file.split('.')

print(f'File name: {file_name}')
print(f'File extension: {extension}')