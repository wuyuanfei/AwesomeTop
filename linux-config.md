# Linux常用配置

[TOC]

#### 1. 移除不常用软件

``` sh
sudo apt-get remove libreoffice-* firefox* totem rhythmbox empathy brasero simple-scan gnome-mahjongg aisleriot gnome-mines gnome-orca webbrowser-app gnome-sudoku landscape-client-ui-install transmission-* hexchat-common gimp*　-y
```

#### 2. 更新软件包
``` sh
sudo apt-get update && sudo apt-get upgrade -y
```

####  3. 安装常用软件
``` sh
sudo apt-get install vim automake cmake autoconf build-essential libglu1-mesa-dev gcc g++ gcc-multilib g++-multilib fcitx minicom xinetd nscd tftpd-hpa tftp-hpa openvpn openssh-server net-tools sqlite3 samba-common samba cifs-utils libncurses5-dev zlib1g-dev gawk git-core subversion libssl-dev fcitx-config-gtk fcitx-frontend-all fcitx-module-cloudpinyin sogoupinyin fcitx-ui-classic meld electron-ssr google-chrome-stable wps-office netease-cloud-music flameshot zeal virtualbox-6.0 -y
```

#### 4. 清除安装包
``` sh
sudo apt-get autoremove && sudo apt-get autoclean
```

#### 5. 安装windows字体

``` sh
sudo cp winfonts /usr/share/fonts/ -a
cd /usr/share/fonts/winfonts/
sudo chmod 644 *
sudo mkfontscale
sudo mkfontdir
sudo fc-cache -fv 
```

#### 6. 安装第三方软件

* [福熙阅读器](https://www.foxitsoftware.cn/downloads/)
* [QT](http://download.qt.io/official_releases/qt/)
* [CLion](http://www.jetbrains.com/clion/)
* [Pycharm](http://www.jetbrains.com/pycharm/)
* [Idea](http://www.jetbrains.com/idea/)
* [anaconda](https://www.anaconda.com/distribution/#download-section)
* [typora](https://www.typora.io/#linux) 
* [deep-win-ubuntu](https://github.com/wszqkzqk/deepin-wine-ubuntu)
* **微信**
* **TIM**
* **dingtalk**
* **旺旺**
* **百度云盘**

#### 7. Markdown编辑器
``` sh
wget -qO - https://typora.io/linux/public-key.asc | sudo apt-key add -
sudo add-apt-repository 'deb https://typora.io/linux ./'
sudo apt-get update
sudo apt-get install typora
```

#### 8. 挂载window共享盘
``` sh
sudo mount -t cifs -o username='xxxxx',password='xxxxxx'  //192.168.xx.xx/共享盘 /mnt/
```

#### 9. 后期配置
- 添加当前用户到vboxuser组

``` sh
sudo adduser yeapht vboxusers
cat /etc/group | grep vboxuser
```
* 将当前用户加入到串口所在的用户组dialout
``` sh
sudo adduser yeapht dialout
```
* 修改搜狗输入法

* 网易云问题

  ```sh
  sudo gedit /etc/sudoers
  `最后一行新增yeapht ALL = NOPASSWD: /usr/bin/netease-cloud-music
  sudo gedit /usr/share/applications/netease-cloud-music.desktop
  `修改Exec=netease-cloud-music %U 为 Exec=sudo netease-cloud-music %U
  ```

* 注销后重新登录

#### 10. github相关
- [查询github.com](http://github.com.ipaddress.com/) 
- [查询assets-cdn.github.com]( http://tool.chinaz.com/dns?type=1&host=assets-cdn.github.com&ip=)
- [查询github.global.ssl.fastly.net](http://tool.chinaz.com/dns?type=1&host=assets-cdn.github.com&ip=)
- 刷新缓存
``` sh
sudo apt-get install nscd
sudo /etc/init.d/nscd restart
```

#### 11. 修改python源

```sh
# ~/.pip/pip.conf
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host=mirrors.aliyun.com
```

#### 12. CUDA9.0安装
* 安装最新的NVIDIA显卡
* 降低gcc、g++编译器版本，CUDA9.0要求GCC版本是5.x或者6.x

```sh
sudo apt install gcc-5 g++-5
sudo rm /usr/bin/gcc
sudo rm /usr/bin/g++
sudo ln -s /usr/bin/gcc-5 /usr/bin/gcc
sudo ln -s /usr/bin/g++-5 /usr/bin/g++

sudo rm /usr/bin/gcc
sudo rm /usr/bin/g++
sudo ln -s /usr/bin/gcc-7 /usr/bin/gcc
sudo ln -s /usr/bin/g++-7 /usr/bin/g++
```
* 安装[cuda9.0套件](https://developer.nvidia.com/cuda-90-download-archive?target_os=Linux)
	**不需要安装显卡**

* 安装[cudnn](https://developer.nvidia.com/rdp/form/cudnn-download-survey)
```sh
sudo cp cuda/include/cudnn.h /usr/local/cuda-9.0/include/
sudo cp cuda/lib64/* /usr/local/cuda-9.0/lib64/
```
*  配置环境变量
```sh
export PATH=/usr/local/cuda-9.0/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-9.0/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
```
*  检查
```sh
nvcc -V
```

####   13. python常用第三方包

* numpy

* pandas

* matplotlib

* tensorflow-gpu

* opencv-python

#### 14. macubunt美化

- [**参考**](https://www.noobslab.com/2018/08/macbuntu-1804-transformation-pack-ready.html)

```sh
sudo add-apt-repository ppa:noobslab/macbuntu
sudo apt-get update 
sudo apt-get install macbuntu-os-*
# sudo apt-get install slingscold
sudo ln -s /usr/share/applications/plank.desktop /etc/xdg/autostart/ #开机自启动plank
sudo ln -s /usr/share/applications/cerebro.desktop /etc/xdg/autostart/ #开机自启动plank
sudo apt-get purge xreader*
```

- **[cerebro0.3.2](https://github.com/KELiON/cerebro/releases)配置**

```sh
"plugins": {},				# 新增
"trackingEnabled": false,	# 修改
```

#### 15. 下载工具

```sh
# 1.编译安装aria2
wget https://github.com/aria2/aria2/releases/download/release-1.34.0/aria2-1.34.0.tar.gz
tar -xvf aria2-1.34.0.tar.gz   
cd /aria2-1.34.0
./configure
make
sudo make install

# 2.安装Aria2 for chrome插件
aria2c -D

# 3.uTorrent
sudo tar -zxvf utserver.tar.gz -C /opt/
sudo chmod 777 /opt/utorrent-server-alpha-v3_3/
sudo ln -s /opt/utorrent-server-alpha-v3_3/utserver /usr/bin/utserver
utserver -settingspath /opt/utorrent-server-alpha-v3_3/		# 启动uTorrent
# 登录http://localhost:8080/gui查看，用户名：admin，密码无	
```

> **百度导出插件：https://github.com/acgotaku/BaiduExporter**
>
> ###### AriaNg Web助手：http://ariang.mayswind.net/latest/#!/settings/ariang



#### 16. 程序员离线神器

```sh
sudo add-apt-repository ppa:zeal-developers/ppa
sudo apt-get update
sudo apt-get install zeal
```

#### 17. 图像视频处理

```sh
sudo add-apt-repository ppa:openshot.developers/ppa
sudo add-apt-repository ppa:thomas-schiex/blender
sudo add-apt-repository ppa:kritalime/ppa
sudo apt-get update
sudo apt-get install openshot-qt blender krita
```

