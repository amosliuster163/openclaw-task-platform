#!/usr/bin/env python3
import re

with open('index.html', 'r') as f:
    content = f.read()

# 修改标题
content = content.replace('用OpenClaw轻松接单赚钱', '程序员发挥技术力量，轻松接单赚钱')

# 修改页脚
content = content.replace('基于OpenClaw构建', '')
content = content.replace('OpenClaw智能助手', '爱默如深')

with open('index.html', 'w') as f:
    f.write(content)

print("Done!")