# 【GPT-reader】让GPT帮你读小说吧！

大家知道这样1句话吗，「书是能使兽变成人，使人变成神的东西」。

可是我读了这么多轻小说，怎么没有变成神？说不定我本来就不是人……错了，说不定是我读的书不够多！

但是书上的字太多了，读起来很费劲，这样慢慢地读，要读到什么时候才会变成神啊……

于是我就想，啊，那干脆让GPT来帮我读好了！


## 使用效果

把小说下载回来给GPT看，GPT读完之后，会帮你把小说总结到原本1/10的长度，然后你再看。

这样1来，看1句就等于看原来的10句，就可以轻松地把小说读完啦！

我把《游戏人生》的第1卷给GPT看了以后，它总结出来了这些内容: 

> 这是一个关于一个叫"空白"的玩家的都市传说。据说他在超过280种游戏中创下了无法打破的纪录，但他的真实身份和背景一直是个谜。他的对手们无法预测他的打法，甚至连国际西洋棋大师也不是他的对手。尽管有人调查他的战绩，但他从未发表过任何言论，也没有提供任何信息。因此，他的真实身份和能力成为了一个谜团，也加速了这个都市传说的传播。
> 
> 这段剧情描述了一个兄妹沉迷于网络游戏的情景。兄弟空和妹妹白在房间里玩游戏，他们互相帮助，但也有些矛盾。他们都是游戏废人，没有工作和学校。他们的真实身份是游戏玩家"空白"。故事还提到了一个关于游戏玩家的都市传说，说强大的玩家会收到一封邮件，邀请他们参加一个神秘的游戏。
> 
> 兄妹俩在玩游戏时收到了一封新邮件，主题是致他们兄妹。他们对此感到困惑，因为他们没有朋友。他们打开邮件后发现了一个陌生的URL，内容让他们感到不寻常和恐怖。妹妹对此不太在意，但也觉得有些奇怪。
> 
> 兄妹收到一封邮件，里面有一个链接，他们打开后发现是一个简单的西洋棋棋盘。兄弟开始下棋，但妹妹突然接手并展现出了惊人的实力。兄弟意识到对手是个人类，而不是电脑程序，提醒妹妹要冷静对战。他们进行了长达六小时的激烈对弈，最终分出胜负。
> 
> 兄妹在激烈的对弈后获胜，感到非常满足。他们对对手的实力感到惊讶，并对对手的身份产生了兴趣。他们收到了一封邮件，内容让他们感到不安。他们回复了邮件，表达了对邮件的不满。他们觉得自己生活在一个无聊的游戏中，无法被他人理解。他们感到沮丧和无助。当他们准备关闭电脑时，又收到了一封新的邮件。
> 
> 兄妹收到一封邮件，打开后发现了一个陌生的URL。他们看到了一个关于一个以游戏为中心的世界的描述，感到向往。他们回复了邮件，然后突然房间发生了异常的事情。他们被拉进了电脑画面中，然后重生在一个飞浮着岛屿的世界中。他们发现自己正在高空跳伞，而一个自称为神的少年欢迎他们来到这个理想国度。
> 
> 兄妹在梦中被神邀请到了一个奇异的世界，他们意识到这不是梦。他们感到困惑和愤怒，觉得自己生活在一个无聊的游戏中。他们被拉进了一个飞浮着岛屿的世界，发现自己正在高空跳伞。他们意识到他们被招待到了一个异世界。同时，故事还提到了一个关于游戏玩家的都市传说，说强大的玩家会收到一封邮件，邀请他们参加一个神秘的游戏。



下面还比较长我就不放啦，大家可以自己到[这里](./output/剧情_游戏人生_第1卷.txt)看完整的输出。

就前面几段来看，效果还不错，也有1些错误的地方，比如「哥哥」有时候会变成「兄弟」，真奇怪。


## 使用方法

你需要准备这些:
- 1个Python3
- 1个openai的帐号
- 1本txt格式的小说

首先把这个仓库clone回去，然后`pip install -r requirements.txt`。

接下来打开`read.py`，把`openai.api_key`替换成你的key，再把小说文件路径替换成你的小说，然后直接运行就可以啦。


## 原理

原理其实很简单，由于GPT3.5 1次只能处理4096个token，因此我把小说按照行进行切分成块，让每块的大小都尽可能不超过2000个字符，然后让GPT每次对这1块进行总结，最后把每块的总结都汇总起来就可以了。

只是这样的话，GPT缺少上文信息，容易出现剧情不通顺的情况。因此还需要对prompt做一些改造。

我把之前的块中已总结的剧情存了下来，做成1个滑动窗口，窗口总字数不超过1500，再把这个窗口的文本加入system prompt，为GPT提供上文，这样1来生成的故事情节就比较连贯了。

嗯，就是这样，非常简单吧！


## 还有我突然想到1个笑话

大家平时会把显示文本的软件叫做「阅读器」吗？

其实不对，因为是人在阅读，所以那个软件是显示文本器，人才是阅读器！


## 结束

就这样，大家88，我要回去把猫变成人了！
