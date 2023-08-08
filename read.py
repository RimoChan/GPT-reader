import time
import logging
import chardet

from rimo_storage.cache import disk_cache

import openai
openai.api_key = 'xxxxxx'


@disk_cache()
def 问(s, u, a, temperature):
    messages = [
        {"role": "system", "content": s},
        {"role": "user", "content": u},
        {"role": "assistant", "content": a},
    ]
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, temperature=temperature, max_tokens=300)
    return chat.choices[0].message.content


def 超问(s, u, a):
    for temperature in [0, 0.3, 0.6, 0.9, 0.92, 0.94, 0.96, 0.98, 1]:
        r = 问(s, u, a, temperature=temperature)
        if r[-1] == '。':
            return r
    return r


def good_open(path, mode='r', encoding=None):
    if mode == 'r' and encoding is None:
        with open(path, 'rb') as f:
            a = chardet.detect(f.read())
            if a['encoding'] == 'GB2312':
                a['encoding'] = 'GBK'
        if a['confidence'] < 0.75:
            try:
                open(path).read()
            except UnicodeDecodeError:
                logging.warning(f'没能自动识别「{path}」的编码，尝试用utf8编码打开。')
                return open(path, encoding='utf8')
            else:
                logging.warning(f'没能自动识别「{path}」的编码，尝试用默认编码打开。')
                return open(path)
        else:
            return open(path, encoding=a['encoding'])
    return open(path, mode=mode, encoding=encoding)


def 读(fname):
    with good_open(fname) as f:
        data = [*f]
    别 = []
    for line in data:
        if not 别 or len(别[-1]) + len(line) > 2000:
            别.append(line)
        else:
            别[-1] += line
    头 = '你是一个小说压缩器。用户每次会输入一段约2000字的小说，你需要将这段话缩写到200字以下。\n你应当忽略输入中的章节名和卷名等meta信息。\n你不能直接引用人物对话，而要进行总结。\n你应该尽可能使用名字指代每个人物，除非你不知道名字。'
    过去的剧情 = []
    for i, u in enumerate(别):
        if i == 0:
            s = f'{头}'
            a = '本部分的剧情如下:'
        else:
            过去剧情的切片 = ''
            for j in 过去的剧情[::-1]:
                if len(过去剧情的切片) + len(j) < 1200:
                    过去剧情的切片 = '- ' + j + '\n' + 过去剧情的切片
                else:
                    break
            if i > 0:
                s = f'{头}\n\n\n以下是之前的剧情: \n{过去剧情的切片}\n你不需要输出之前的剧情，只需总结新增部分的剧情。'
            a = '本部分的新增剧情如下:'
        print('=====================================')
        print(s)
        print('-------------------------------------')
        while True:
            try:
                r = 超问(s, u, a)
            except Exception as e:
                print('Exception:', e)
                time.sleep(10)
            else:
                break
        r = r.replace('\n', ' ')
        过去的剧情.append(r)
        with open(f'剧情_{fname}', 'w', encoding='utf8') as f:
            f.write('\n\n'.join(过去的剧情))
        print(r)
        print('\n\n')


读('游戏人生 第1卷.txt')
