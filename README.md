# Automatic-lottery-robot
face to bilibili

从 uid = 0 开始
获取大于十万粉丝的 up 的 uid
  返回 这些up的 name 和 fans 组成的 字典
  
(分析是否会进行抽奖 返回uid)
进行关注(手动实现)
  返回(状态码)

从 我的动态中 获取 动态内容
  返回dynamic_content

检查含有 抽奖信息 的 动态
  返回dynamic_id

进行 转发 评论
  返回 状态码
  
从 消息 中获取中奖信息
  自动填写中奖信息
  将信息通过发消息的方式返回某个uid

将字典中的信息存入数据库
  粉丝数大于十万的 up :
    up_info 表:#从list中取出 uid 和一个含有 name 和 fans 的字典
      uid  name  fans
