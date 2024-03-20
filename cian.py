import requests

cookies = {
    '_CIAN_GK': '94c63ded-a282-4949-a2b9-fc737cb9e328',
    '_gcl_au': '1.1.323410645.1710834443',
    'tmr_lvid': '5302648a3193a641de006a283b24ac4d',
    'tmr_lvidTS': '1710834458627',
    'login_mro_popup': '1',
    'sopr_utm': '%7B%22utm_source%22%3A+%22yandex%22%2C+%22utm_medium%22%3A+%22organic%22%7D',
    'uxfb_usertype': 'searcher',
    '_gid': 'GA1.2.648048622.1710834508',
    '_ym_uid': '1710834508159927190',
    '_ym_d': '1710834508',
    '_ym_isad': '1',
    'uxs_uid': '27fca1d0-e5c5-11ee-a6fa-bf1853765323',
    'adrdel': '1',
    'adrcid': 'ARvfXEzxg7yaLzHMpYLmG3Q',
    '__cf_bm': '5r1vgw4fCHK_sVYNZZl.JsmwA.zwdpuoaHKhej.5V7Q-1710838476-1.0.1.1-vZTECJAlGVZ793cfE8DlUKzxx9iSiHHEp7AU4TLdQ5H5rr2MewQsUtdebahuDqB24halQUxLrk.RbFQkb3HnMw',
    'sopr_session': '2dc0fd705be04fac',
    '_ym_visorc': 'b',
    'afUserId': 'ae0ee7c1-152d-4b78-8ece-7fe0388bd2a2-p',
    'cookie_agreement_accepted': '1',
    '_ga': 'GA1.2.1493516238.1710834497',
    'AF_SYNC': '1710838667758',
    '_dc_gtm_UA-30374201-1': '1',
    'session_region_id': '175050',
    'session_main_town_region_id': '175050',
    '_ga_3369S417EL': 'GS1.1.1710838491.2.1.1710838753.60.0.0',
}

headers = {
    'authority': 'api.cian.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5',
    'content-type': 'application/json',
    # 'cookie': '_CIAN_GK=94c63ded-a282-4949-a2b9-fc737cb9e328; _gcl_au=1.1.323410645.1710834443; tmr_lvid=5302648a3193a641de006a283b24ac4d; tmr_lvidTS=1710834458627; login_mro_popup=1; sopr_utm=%7B%22utm_source%22%3A+%22yandex%22%2C+%22utm_medium%22%3A+%22organic%22%7D; uxfb_usertype=searcher; _gid=GA1.2.648048622.1710834508; _ym_uid=1710834508159927190; _ym_d=1710834508; _ym_isad=1; uxs_uid=27fca1d0-e5c5-11ee-a6fa-bf1853765323; adrdel=1; adrcid=ARvfXEzxg7yaLzHMpYLmG3Q; __cf_bm=5r1vgw4fCHK_sVYNZZl.JsmwA.zwdpuoaHKhej.5V7Q-1710838476-1.0.1.1-vZTECJAlGVZ793cfE8DlUKzxx9iSiHHEp7AU4TLdQ5H5rr2MewQsUtdebahuDqB24halQUxLrk.RbFQkb3HnMw; sopr_session=2dc0fd705be04fac; _ym_visorc=b; afUserId=ae0ee7c1-152d-4b78-8ece-7fe0388bd2a2-p; cookie_agreement_accepted=1; _ga=GA1.2.1493516238.1710834497; AF_SYNC=1710838667758; _dc_gtm_UA-30374201-1=1; session_region_id=175050; session_main_town_region_id=175050; _ga_3369S417EL=GS1.1.1710838491.2.1.1710838753.60.0.0',
    'origin': 'https://kostroma.cian.ru',
    'referer': 'https://kostroma.cian.ru/',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
}

json_data = {
    'jsonQuery': {
        '_type': 'flatsale',
        'engine_version': {
            'type': 'term',
            'value': 2,
        },
        'region': {
            'type': 'terms',
            'value': [
                175050,
            ],
        },
        'room': {
            'type': 'terms',
            'value': [
                1,
            ],
        },
    },
}

response = requests.post(
    'https://api.cian.ru/search-offers/v2/search-offers-desktop/',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"jsonQuery":{"_type":"flatsale","engine_version":{"type":"term","value":2},"region":{"type":"terms","value":[175050]},"room":{"type":"terms","value":[1]}}}'
#response = requests.post(
#    'https://api.cian.ru/search-offers/v2/search-offers-desktop/',
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)

print(response.json())