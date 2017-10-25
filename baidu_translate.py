import requests
import json


"""

{'ara': '阿拉伯语',
 'bul': '保加利亚语',
 'cht': '中文繁体',
 'cs': '捷克语',
 'dan': '丹麦语',
 'de': '德语',
 'el': '希腊语',
 'en': '英语',
 'est': '爱沙尼亚语',
 'fin': '芬兰语',
 'fra': '法语',
 'hu': '匈牙利语',
 'it': '意大利语',
 'jp': '日语',
 'kor': '韩语',
 'nl': '荷兰语',
 'pl': '波兰语',
 'pt': '葡萄牙语',
 'rom': '罗马尼亚语',
 'ru': '俄语',
 'slo': '斯洛文尼亚语',
 'spa': '西班牙语',
 'swe': '瑞典语',
 'th': '泰语',
 'vie': '越南语',
 'wyw': '文言文',
 'yue': '粤语',
 'zh': '中文'}
"""


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537."
                         "36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.3",
           "Origin": "http://fanyi.baidu.com",
           "Host": "fanyi.baidu.com",
           "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
           }


def get_result(words, tolan="kor"):
    s = requests.session()
    detect_res = s.post("http://fanyi.baidu.com/langdetect", data={"query": words[:48]}, headers=headers)
    detect_dict = json.loads(detect_res.text)
    if detect_dict.get("error") == 0:
        lan = detect_dict.get("lan")
        if lan ==tolan:

            return words
        translate_data = {"from": lan, "to": tolan, "query": words, "transtype": 'realtime', "simple_means_flag": 3}
        res = s.post("http://fanyi.baidu.com/v2transapi", data=translate_data)
        return  res.json()["trans_result"]['data'][0]['dst']
    else:
        print("lanuage detect get error")
        return detect_res.json()


if __name__ == '__main__':
    print(get_result("你知道我在懂你吗，你如果真的在乎我，就不会让我如此难受",tolan="ru"))
