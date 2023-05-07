import requests
import json

def kakao_to_me():
    print("111")
    url = 'https://kauth.kakao.com/oauth/token'
    client_id = 'e485b4ece1dfd26d6d17793412696d2a'
    redirect_uri = 'https://example.com/oauth'
    code = 'KjR9_BCW-tR1rXj4a5jx60885TGptDmtjz3AzPywKiDaFLnczbAAt3HIUDh6FVHbVnlKWwoqJU8AAAGGr6BAhw'

    data = {
        'grant_type':'authorization_code',
        'client_id': client_id,
        'redirect_uri': redirect_uri,
        'code': code,
        }

    response = requests.post(url, data=data)
    tokens = response.json()

    #발행된 토큰 저장
    with open("token.json", "w") as kakao:
        json.dump(tokens, kakao)
    print("222")
    # 발행한 토큰 불러오기
    with open("token.json", "r") as kakao:
        tokens = json.load(kakao)
    print("333")
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

    headers = {
        "Authorization": "Bearer " + tokens["access_token"]
    }

    data = {
        "template_object": json.dumps({"object_type": "text",
                                       "text": "뿌엥.",
                                       "link": {
                                           "web_url": "www.naver.com"
                                       }
                                       })
    }

    response = requests.post(url, headers=headers, data=data)
    print(response.status_code)
    if response.json().get('result_code') == 0:
        print('메시지를 성공적으로 보냈습니다.')
    else:
        print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))
    print("444")

def kakao_to_friend():
    # step1
    print("step1")
    client_id = '0b2c35b13a3fc144a72e7b37c1bb1579'
    redirect_uri = 'https://example.com/oauth'
    # 계속 갱신
    code = 'At0bprktGuWW5f9S4CrEzqv_A_w2vWWB8U8vm7fK1edsSD2WR8Iedi6fP4NEGB5hInI38gorDNIAAAGGr9zEqw'

    url = "https://kauth.kakao.com/oauth/token"
    data = {
        "grant_type": "authorization_code",
        "client_id": client_id,
        "redirect_url": redirect_uri,
        "code": code
    }
    response = requests.post(url, data=data)
    tokens = response.json()
    print(tokens)

    # step2
    print("step2")
    data = {
        "grant_type": "refresh_token",
        "client_id": client_id,
        "refresh_token": tokens["refresh_token"]
    }
    response = requests.post(url, data=data)
    tokens = response.json()
    # kakao_code.json 파일 저장
    with open("kakao_code.json", "w") as fp:
        json.dump(tokens, fp)

    # step3
    print("step3")
    with open("kakao_code.json", "r") as fp:
        tokens = json.load(fp)
    print(tokens["access_token"])

    # step4
    print("step4")
    url = "https://kapi.kakao.com/v1/api/talk/friends"  # 친구 목록 가져오기
    header = {"Authorization": 'Bearer ' + tokens["access_token"]}
    result = json.loads(requests.get(url, headers=header).text)
    print("list", requests.get(url, headers=header).text)
    friends_list = result.get("elements")
    print(friends_list)

    #step5
    print("step5")
    friend_id = friends_list[0].get("uuid")
    print(friend_id)

    #step6
    print("step6")
    url = "https://kapi.kakao.com/v1/api/talk/friends/message/default/send"
    header = {"Authorization": 'Bearer ' + tokens["access_token"]}
    data = {
        'receiver_uuids': '["{}"]'.format(friend_id),
        "template_object": json.dumps({
            "object_type": "text",
            "text": "딥러닝 뉴스",
            "link": {
                "web_url": "https://www.google.co.kr/search?q=deep+learning&source=lnms&tbm=nws",
                "mobile_web_url": "https://www.google.co.kr/search?q=deep+learning&source=lnms&tbm=nws"
            },
            "button_title": "뉴스 보기"
        })
    }
    response = requests.post(url, headers=header, data=data)
    response.status_code

def line_to_me():
    print("line")