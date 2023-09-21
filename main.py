import difflib
def read(file_path):                                      #读取txt文件
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
    return data

def Return_similarity(text1, text2):                               #对比两个txt文件内容的相似度
    # 计算相似度
    similarity = difflib.SequenceMatcher(None, text1, text2).ratio()
    temp= "{:.2f}".format(similarity)
    return temp


def result(file_dir, content):                             #保存结果txt文件
    with open(file_dir, 'w', encoding='utf-8') as file:
        file.write(content)

# 读取文件内容
file1_dir=input('请输入第一个txt文件的绝对路径：')
file2_dir=input('请输入第二个txt文件的绝对路径：')


file1 = read(file1_dir)    #函数调用
file2 = read(file2_dir)
similarity = str(Return_similarity(file1, file2))
result(r'C:\Users\Administrator\Desktop\result.txt',similarity)
print(r'结果路径：C:\Users\Administrator\Desktop\result.txt')
