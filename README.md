# auto watch video

## requirement
- sudo pacman -S firefox python-pip wmctrl
- sudo pip install ssr-utils
- yay shadowsocksr

## 运行说明
- 开启火狐自动播放功能

## 核心点
- python执行terminal命令
```
os.system('ls -lh' + ' ' + xxx.txt)
```
- 连接VPN
```
ss :    sslocal -s server -p port -k passwd -m mothods
ssr:    sslocal -c ./config/config1.json > /dev/null 2>&1 &
```
- 关闭VPN
```
killall sslocal > /dev/null 2>&1
```
- 如何打开与关闭firefox浏览器
```
firefox https://xxxxxx > /dev/null 2>&1
wmctrl -ic "$(wmctrl -l | grep 'Mozilla Firefox' | tail -1 | awk '{ print $1 }')"
```
  