import time

# file = open('D:\\PycharmProjects\\demoProj\\cn\\test_reader.txt', 'r', encoding='utf-8')
# lines = file.readlines()
# for line in lines:
#     print(line, end='')
#     time.sleep(1)
# # print(file.read())
# file.close()

with open('D:\\PycharmProjects\\demoProj\\cn\\test_reader.txt', 'a', encoding='utf-8') as s:
    content = '\n标题：《致橡树》'
    content += '\n作者：舒婷'
    content += '\n时间：1977年3月'
    content += '\nwritten in ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    s.write(content)
    print('成功写入以下内容 => ' + content)
