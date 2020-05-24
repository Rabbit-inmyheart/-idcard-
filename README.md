# -idcard-
炉石传说 idcard及其对应中文名的爬取，
用到了requests lxml 以及pickle 三个库，
这个脚本是从炉石传说中文维基上爬取炉石所有的 Idcard 所对应的名称并永久存储，
需要注意的是爬下来的字典key是中文名，而value是idcard，因为同一个idcard可能对应不止一个名称。
另外爬的可能不完整，新版本的卡可能没有。
