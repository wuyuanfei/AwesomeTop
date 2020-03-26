import ssr_utils
import subprocess

from src.common import save_ssr_config, get_subscribe_url

ssr = ssr_utils.SSR()
ssr.load(ssr)


def get_server_ping(idx, server):
    ret = subprocess.getoutput('ping -c 1 -W 1 ' + server)
    # print(ret)
    if ret.find('time=') == -1:  # not fount
        print("server[%02d] ping %s TIMEOUT" % (idx, server))
        return -1
    else:
        str1 = ret.split('time=')
        str2 = str1[1].split(' ms')
        # print("times[%02d] ping[%.2f]ms" % (i, float(str2[0])))
        print("server[%02d] ping %s time=%.2fms" % (idx, server, float(str2[0])))
        return float(str2[0])


def auto_start_ssr(urls):
    flag = False
    for i in range(len(urls)):
        ssr.url = urls[i]
        ping = get_server_ping(i, ssr.server_domain)
        if ping - 50 < 0.001 and -1 != ping and not flag:
            flag = True
            print("=====> select ssr server %s, ping %.2f <=====", ssr.server_domain, ping)
            save_ssr_config(-1, ssr.config_json_string)
            subprocess.getoutput('echo "yzzsjc520" | sudo -S cp ../config/ssr/config.json /etc/shadowsocksr/')
            subprocess.getoutput('echo "yzzsjc520" | sudo -S systemctl restart autosslocal.service')


if __name__ == "__main__":
    subscribe = get_subscribe_url()
    urls = ssr_utils.get_urls_by_subscribe(subscribe)
    auto_start_ssr(urls)
