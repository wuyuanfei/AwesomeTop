SUBSCRIBE_PATH = "../res/subscribe.txt"

# SS_JSON_CFG = "../config/ss/config"
SSR_JSON_CFG = "../config/ssr/config"
# VEMSS_JSON_CFG = "../config/vmess/config"


def get_subscribe_url():
    file = open(SUBSCRIBE_PATH, 'r')
    for line in file.readlines():
        return line.strip(line[-1])
    file.close()
