# Linux常用配置

#### 1. 移除不常用软件

``` sh
sudo apt-get remove libreoffice-* firefox* totem rhythmbox empathy brasero simple-scan gnome-mahjongg aisleriot gnome-mines gnome-orca webbrowser-app gnome-sudoku landscape-client-ui-install transmission-* hexchat-common -y
```

#### 2. 更新软件包
``` sh
sudo apt-get update && sudo apt-get upgrade -y
```

####  3. 安装常用软件
``` sh
sudo apt-get install vim automake cmake autoconf build-essential libglu1-mesa-dev gcc g++ gcc-multilib g++-multilib fcitx minicom xinetd nscd tftpd-hpa tftp-hpa openvpn openssh-server net-tools sqlite3 samba-common samba cifs-utils libncurses5-dev zlib1g-dev gawk git-core subversion libssl-dev fcitx-config-gtk fcitx-frontend-all fcitx-module-cloudpinyin fcitx-ui-classic meld -y
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

* [wps套件](http://www.wps.cn/product/wpslinux)
* [搜狗输入法](https://pinyin.sogou.com/linux/?r=pinyin)
* [谷歌浏览器](https://chrome.en.softonic.com/)
* [ShadowsocksR](https://github.com/erguotou520/electron-ssr)
* [福熙阅读器](https://www.foxitsoftware.cn/downloads/)
* [网易云音乐](https://music.163.com/#/download)
* [QT](http://download.qt.io/official_releases/qt/)
* [CLion](http://www.jetbrains.com/clion/)
* [Pycharm](http://www.jetbrains.com/pycharm/)
* [Idea](http://www.jetbrains.com/idea/)
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
* [anaconda](https://www.anaconda.com/distribution/#download-section)
* [typora](https://www.typora.io/#linux) 
* **deep-win-ubuntu**
* **微信**
* **TIM**
* **dingtalk**
* **迅雷极速版**
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
sudo mkdir /mnt/pemt
sudo mount -t cifs -o username='eng022',password='12345r*'  //192.168.0.60/共享盘 /mnt/pemt/
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

  

