import sys
input = sys.stdin.readline
import re

html = input().strip()

html = re.sub(r"<main>|<\/main>", "", html)
html = re.sub(r'<div title="([^"]+)">', "title : \g<1>\n", html)

html = re.sub(r"</p>", "\n", html)
html = re.sub(r"</[^>]+>", "", html)
html = re.sub(r"<[^>]+>", "", html)
html = re.sub(r"[ ]+", " ", html)
print(html)
