from fileinput import FileInput
import re 
import sys

def getRoot(url):
    for i in range(1,len(url)):
        if url[-i] == '/' or url[-i] =='\\':
            return url[:-i]
def getTitle(context):
    title = ''
    for char in context:
        if char != '\n':
            title += char
        else:
            return title[4:]


#  首先读取需要拆分的md文件，将所有内容提取至一个字符串中
markdownPath = sys.argv[1]
# markdownPath = r'D:/ObsidianNote/前端学习/001.HTML - 超文本标记语言 - 网页结构/基础知识/2.HTML介绍/HTML介绍.md'
try:
    f= open(markdownPath,encoding="utf-8")
    markdownContent = ''
    while True:
        line = f.readline()
        if line:
            markdownContent += line
        else:
            break
    f.close()
    # print(markdownContent)
        
    # 查找字符串中的所有"####_"，记录其对应位置    
    pattern = re.compile("####\s\d+\.\s\w*")
    f = re.finditer(pattern, markdownContent)
    indexs = []
    contents = []
    for i in f:
        indexs.append(i.span()[0])

    # 根据所记录的索引，将内容进行分割
    for i in range(len(indexs) - 1):
        startIndex = indexs[i]
        endIndex = indexs[i+1]
        contents.append(markdownContent[startIndex:endIndex])
    contents.append(markdownContent[indexs[-1]:])
    # for content in contents:
    #     print(content)
    #     print("------------------------------------")

    # 将创建一个markdown文件
    # 在相应目录下创建相应的md文档并将内容写入
    iRoot = getRoot(markdownPath)
    for content in contents:
        title = getTitle(content)
        fileName = f"{iRoot}/{title}.md"
        file = open(fileName,'w',encoding='utf-8')
        file.write(content)
        # print(fileName)
        print(title)
except:
    print("Something Wrong!")
        