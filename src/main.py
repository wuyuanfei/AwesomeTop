import os
import time
import random
import ssr_utils
from datetime import datetime

# SS_JSON_CFG = "../config/ss/config"
SSR_JSON_CFG = "../config/ssr/config"
# VEMSS_JSON_CFG = "../config/vmess/config"

SUBSCRIBE_PATH = "../res/subscribe.txt"
PLAY_LIST_PATH = "../res/playlist.txt"

MAX_VIDEOS_SIZE = 100

MIN_PER_SEC = 60
MIN_SCAN_MIN = 10 * MIN_PER_SEC
MAX_SCAN_MIN = 20 * MIN_PER_SEC


def get_subscribe_url():
    file = open(SUBSCRIBE_PATH, 'r')
    for line in file.readlines():
        return line.strip(line[-1])
    file.close()


def save_ssr_config(index, config):
    file = open(SSR_JSON_CFG + str(index) + ".json", 'w')
    file.write(config)
    file.close()


def save_json_config():
    for i in range(len(urls)):
        ssr.url = urls[i]
        save_ssr_config(i, ssr.config_json_string)
    print("save all json config complete")


subscribe = get_subscribe_url()
urls = ssr_utils.get_urls_by_subscribe(subscribe)
MAX_CONFIG_JSON_SIZE = len(urls)

MAX_VIDEO_SIZE = 0


def do_main_task(ssr, playlist, param, scan_time):
    ssr.url = urls[param['cfg_id']]

    # print("============> config[%d], video[%d]" % (param['cfg_id'], param['video_id']))
    print("\n*************************************************************")
    print("* json file : config%d.json" % param['cfg_id'])
    print("* Datetime  : %s" % datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("* Server    : %s" % ssr.server)
    print("* IP        : %s" % ssr.server_ip)
    print("* remarks   : %s" % ssr.remarks)
    print("* video{%03d}: %s" % (param['video_id'], playlist[param['video_id']]))
    print("* scan second: %d" % (scan_time))
    print("*************************************************************\n")

    # 1. close all sslocal
    print("[%s] close sslocal and all firefox now" % (datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    os.system('killall sslocal > /dev/null 2>&1')

    # 2. close firefox
    os.system('wmctrl -ic $(wmctrl -l | grep \'Mozilla Firefox\' | tail -1 | awk \'{ print $1 }\')')  # gracefuly close
    time.sleep(3)

    # 3. start new sslocal and play videos
    print("[%s] start new sslocal and play videos" % (datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    os.system('sslocal -c ' + SSR_JSON_CFG + str(param['cfg_id']) + '.json' + ' > /dev/null 2>&1 &')
    os.system('firefox ' + playlist[param['video_id']] + ' &')

    # 3. update config and videos index
    if param['video_id'] >= MAX_VIDEO_SIZE - 1:
        param['video_id'] = 0
        if param['cfg_id'] >= MAX_CONFIG_JSON_SIZE - 1:
            param['cfg_id'] = 0
        else:
            param['cfg_id'] += 1
    else:
        param['video_id'] += 1


if __name__ == "__main__":
    print("Welcome to auto watch videos! ")
    ssr = ssr_utils.SSR()
    ssr.load(ssr)

    playlist = list()
    param = {'cfg_id': 0, 'video_id': 0}

    save_json_config()

    videos_file = open(PLAY_LIST_PATH, 'r')
    for line in videos_file.readlines():
        video = line.strip('\n')
        MAX_VIDEO_SIZE += 1
        playlist.append(video)

    start_time = time.time()
    scan_time = 0
    while 1:
        if time.time() % 10 < 1.0:  # time.time() is not int
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("[%s] now[%d] start[%d] diff[%04d], scan[%d]s"
                  % (now, time.time(), start_time, time.time() - start_time, scan_time))

        if param["cfg_id"] == 0 and param["video_id"] == 0:
            scan_time = random.randrange(MIN_SCAN_MIN, MAX_SCAN_MIN)
            do_main_task(ssr, playlist, param, scan_time)
        elif time.time() - start_time > scan_time:
            scan_time = random.randrange(MIN_SCAN_MIN, MAX_SCAN_MIN)
            start_time = time.time()
            do_main_task(ssr, playlist, param, scan_time)

        time.sleep(1)
