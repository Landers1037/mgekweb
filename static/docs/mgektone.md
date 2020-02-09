# Mgektone

Mgektone是一个辅助arduino音符数组生成脚本

### 常量定义

```c
#define NOTE_D0 -1
#define NOTE_D1 294
#define NOTE_D2 330
#define NOTE_D3 350
#define NOTE_D4 393
#define NOTE_D5 441
#define NOTE_D6 495
#define NOTE_D7 556

#define NOTE_DL1 147
#define NOTE_DL2 165
#define NOTE_DL3 175
#define NOTE_DL4 196
#define NOTE_DL5 221
#define NOTE_DL6 248
#define NOTE_DL7 278

#define NOTE_DH1 589
#define NOTE_DH2 661
#define NOTE_DH3 700
#define NOTE_DH4 786
#define NOTE_DH5 882
#define NOTE_DH6 990
#define NOTE_DH7 112
```

### 处理脚本

```python
import json
import os

tone = []
def toneGen(file):
    print('音符数组生成')
    if file:
        with open(file,'r',encoding='utf8') as f:
            datas= f.readline()
            for data in datas:
               if data == '0':
                   tone.append('NOTE_D0')
               elif data == '1':
                   tone.append('NOTE_D1')
               elif data == '2':
                   tone.append('NOTE_D2')
               elif data == '3':
                   tone.append('NOTE_D3')
               elif data == '4':
                   tone.append('NOTE_D4')
               elif data == '5':
                   tone.append('NOTE_D5')
               elif data == '6':
                   tone.append('NOTE_D6')
               elif data == '7':
                   tone.append('NOTE_D7')
               elif data == 'l1':
                   tone.append('NOTE_DL1')
               elif data == 'l2':
                   tone.append('NOTE_DL2')
               elif data == 'l3':
                   tone.append('NOTE_DL3')
               elif data == 'l4':
                   tone.append('NOTE_DL4')
               elif data == 'l5':
                   tone.append('NOTE_DL5')
               elif data == 'l6':
                   tone.append('NOTE_DL6')
               elif data == 'l7':
                   tone.append('NOTE_DL7')
               elif data == 'h1':
                   tone.append('NOTE_DH1')
               elif data == 'h2':
                   tone.append('NOTE_DH2')
               elif data == 'h3':
                   tone.append('NOTE_DH3')
               elif data == 'h4':
                   tone.append('NOTE_DH4')
               elif data == 'h5':
                   tone.append('NOTE_DH5')
               elif data == 'h6':
                   tone.append('NOTE_DH6')
               elif data == 'h7':
                   tone.append('NOTE_DH7')
    else:
        print('需要传入文件')

def format():
    formattone = ''
    for tonelist in tone:
        formattone = formattone +','+ tonelist
    formattone = formattone[1:]
    return formattone

if __name__=='__main__':
    filename = input('音符文件名\n')
    toneGen(filename)
    print(format())
```

### 示例

将乐谱按照高低音写成文档放在文本文件里，如

```xml
1 2 3 4 5 6 7 l1 l2 h3 h4
```

低音为l，高音为h

将文本文件保存后命名为xxx.txt，命令行执行

```shell
$ python mgektone.py xxx.txt
```

