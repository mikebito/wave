import re

# rを付けることを推奨。
# バックスラッシュをそのままで分かりやすいため。
content = r'/smc play.minecraft.jp'
# ()で取りたい文字を
print(content.split(' ',2)[1])