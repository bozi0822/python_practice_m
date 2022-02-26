import requests
import base64
import json

token_url = 'https://fsservice.wjj.foshan.gov.cn/fw2/foying/wechatpublic/wx/user/getTokenByCh5'
body = {
    "orderChannel": "ch5"
}
token_header = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 wechatdevtools/1.05.2105170 MicroMessenger/7.0.4 Language/zh_CN webview/1623847089654601 webdebugger port/25481 token/892aecfbe65576c6e32a6dd618a37d78",
    'Content-Type': "application/json"
}

url1 = 'https://fsservice.wjj.foshan.gov.cn/fw2/foying/wechatpublic/wx/user/captchaImage/'
header1 = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 wechatdevtools/1.05.2105170 MicroMessenger/7.0.4 Language/zh_CN webview/1623847089654601 webdebugger port/25481 token/892aecfbe65576c6e32a6dd618a37d78",
    'Content-Type': "image/jpeg",
    "Referer": 'https://fsservice.wjj.foshan.gov.cn/fw/content/wxOrder/index.html?state=ch5',
    'Accept':'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'Content-Security-Policy': "default-src 'self';script-src 'self' 'unsafe-inline' 'unsafe-eval' ;style-src 'self' 'unsafe-inline' ;connect-src 'self' ;worker-src 'self' ;img-src 'self' ;frame-src 'self' ;"
}


def get_pic_code():
    token_res = requests.post(token_url, headers=token_header, data=json.dumps(body))
    # print(token_res.content)
    data = token_res.content
    dataObj = json.loads(data)
    token = dataObj["entity"]["token"]
    print(token)

    res = requests.get(url1 + token, headers=header1)
    # print(res.content)
    base_data = base64.encodebytes(res.content)
    image_data = base64.b64decode(base_data)

    with open('pic_code.jpeg', 'wb') as f:
        f.write(image_data)

if __name__ == "__main__":
    get_pic_code()