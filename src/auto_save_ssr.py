import ssr_utils
from src.common import get_subscribe_url, save_ssr_config

ssr = ssr_utils.SSR()
ssr.load(ssr)


def save_json_config(urls):
    for i in range(len(urls)):
        ssr.url = urls[i]
        print(ssr.config)
        save_ssr_config(i, ssr.config_json_string)
    print("save all json config complete")


if __name__ == "__main__":
    subscribe = get_subscribe_url()
    urls = ssr_utils.get_urls_by_subscribe(subscribe)
    save_json_config(urls)
