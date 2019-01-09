import itchat
# 获取数据
def get_data():
   itchat.auto_login()
   friends = itchat.get_friends(
   update=True)
   return friends