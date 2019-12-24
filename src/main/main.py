#  -*-  coding:utf-8  -*-
import jieba
import string
import re


def remove_punctuation(line, strip_all=True):
    if strip_all:
        rule = re.compile("[^a-zA-Z0-9\u4e00-\u9fa5]")
        line = rule.sub('', line)
    else:
        punctuation = """！？｡＂＃＄％＆＇（）＊＋－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏"""
        re_punctuation = "[{}]+".format(punctuation)
        line = re.sub(re_punctuation, "", line)

    return line.strip()


def removePunctuation(text):
    temp = []
    for c in text:
        if c not in string.punctuation:
            temp.append(c)
    newText = ''.join(temp)
    return newText


def read_txt(file_name):
    text = str(open(file_name, 'r').read().split(" "))
    new_text = remove_punctuation(text)
    return new_text


def read(file_name):
    text = str(open(file_name, 'r').read().split(" "))
    return text


def solve(num):
    jieba.del_word('小')
    file_path = "testdata\Q" + str(num) + "/KeyPoints.txt"
    ans_path = "testdata\Q" + str(num) + "/Answer.txt"
    pro_path = "testdata\Q" + str(num) + "/Problem.txt"
    tmp = str(read_txt(file_path))
    kp = jieba.lcut(tmp)
    tmp2 = str(read_txt(ans_path))
    ans = jieba.lcut(tmp2)
    pro_text = read(pro_path)
    ans_text = read(ans_path)
    kp_text = read(file_path)
    print("第" + str(num) + "题:")
    print("问题:" + str(pro_text))
    print("得分点:" + str(kp))
    print("作答者回答:" + str(ans_text))
    ans_text = read_txt(ans_path)
    count = 0
    count_no = 0
    for p in kp:
        f = 0
        index = ans_text.find(p)
        if index != -1:
            #print(ans_text[index-2:index])
            if index >= 1:
                if ans_text[index-1] == '不':
                    f = 1
                    #print(ans_text[index - 1:index + len(p)])
            if index >= 2:
                if f == 1:
                    continue
                if ans_text[index-2:index] == '不是':
                    f = 1
                    #print(ans_text[index - 2:index + len(p)])
            if f == 0:
                count += 1
    count_no += ans.count("不")
    count_no += ans.count("不是")
    point = count / len(kp) * 10.0
    print("否定词个数为:" + str(count_no))
    print("第" + str(num) + "题回答者得分为:" + str("%.2f" % point) + " / 10.00")
    print('\n')


if __name__ == '__main__':
    data_size = 4
    x=2.0
    print("%.2f %.2f"%(x,x))
    for i in range(data_size):
        solve(i + 1)
