import requests

cookies = {
    'spid': '1710386501834_0db0dfeeeee921ea383d74a2b475b01e_lig2b1cf6mg48nnk',
    'spsn': '1710386773864_7b2276657273696f6e223a22332e342e32222c227369676e223a226564646634346238653834343861386362623239376432323333376637353033222c22706c6174666f726d223a224d6163496e74656c222c2262726f7773657273223a5b226368726f6d65225d2c2273636f7265223a302e357d',
    '_ym_uid': '1710387178434487227',
    '_ym_d': '1710387178',
    'device_id': 'b493ae28-e1b3-11ee-bb2a-fa163e5515d9',
    'ecom_token': '7d38cd36-7103-4cea-b737-05eeeec38bd0',
    'sbermegamarket_token': '7d38cd36-7103-4cea-b737-05eeeec38bd0',
    'isOldUser': 'true',
    'adspire_uid': 'AS.1932505593.1710387244',
    'ssaid': 'b5a10b90-e1b3-11ee-b8a5-2d398e0ce1d4',
    '_sa': 'SA1.0afa6adf-b411-4f96-961f-3de9dce9e36f.1710387246',
    'tmr_lvid': '833d2eab9333bc8b0379f5e02db7ce6e',
    'tmr_lvidTS': '1710387247241',
    'adrcid': 'ARvfXEzxg7yaLzHMpYLmG3Q',
    '_gpVisits': '{"isFirstVisitDomain":true,"idContainer":"10002472"}',
    'rrpvid': '861105740483026',
    '_gcl_au': '1.1.316160871.1710387268',
    'rcuid': '63e4c8439562c1e4a19fa995',
    'flocktory-uuid': 'b76d32f6-3a18-45a4-bef4-bd6ac5b4fd5a-2',
    'adid': '171038730170345',
    'uxs_uid': 'd7161bd0-e1b3-11ee-8f3f-4f3d9df8c5bc',
    '_ym_visorc': 'b',
    '_ym_isad': '1',
    'spsc': '1710905985956_39babb24b7a33f5c52abca69084030a0_2dc4c47e5beb4aae25be080fa9d16c8093e7e989cef732b63b8bada59af3d7da',
    '_gid': 'GA1.2.650427167.1710906172',
    'adrdel': '1',
    '__tld__': 'null',
    'tmr_detect': '0%7C1710906285847',
    '__zzatw-smm': 'MDA0dC0cTHtmcDhhDHEWTT17CT4VHThHKHIzd2UbN1ddHBEkWA4hPwsXXFU+NVQOPHVXLw0uOF4tbx5mSFkoQ1tPCSsbEQhnFRtQSxgvS18+bX0yUCs5Lmw=QvG54Q==',
    'region_info': '%7B%22displayName%22%3A%22%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C%22%2C%22kladrId%22%3A%225000000000000%22%2C%22isDeliveryEnabled%22%3Atrue%2C%22geo%22%3A%7B%22lat%22%3A55.755814%2C%22lon%22%3A37.617635%7D%2C%22id%22%3A%2250%22%7D',
    '_gp10002472': '{"hits":2,"vc":1,"ac":1,"a6":1}',
    '_ga_W49D2LL5S1': 'GS1.1.1710906130.4.1.1710906287.33.0.0',
    '_ga': 'GA1.2.70211477.1710387243',
    '_ga_VD1LWDPWYX': 'GS1.2.1710906325.3.0.1710906325.0.0.0',
    'cfidsw-smm': 'bKrwW0Nh2W5OQmYjlAO2bjK6gwX1+zueuPURCZPlV9umr5iKrNMLkRyX8GyslSXQs36nrOoZIdT/uc3ETv7E0xiPlhp3JTa11xH7aEYLwAH0m7x7Yr15PcTQqueu/WqO/f+RioxvoY6kCy6bR9y2X5l/Ey0VBjL4oHvVIg==',
    'cfidsw-smm': 'bKrwW0Nh2W5OQmYjlAO2bjK6gwX1+zueuPURCZPlV9umr5iKrNMLkRyX8GyslSXQs36nrOoZIdT/uc3ETv7E0xiPlhp3JTa11xH7aEYLwAH0m7x7Yr15PcTQqueu/WqO/f+RioxvoY6kCy6bR9y2X5l/Ey0VBjL4oHvVIg==',
}

headers = {
    'authority': 'megamarket.ru',
    'accept': 'application/json',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5',
    'content-type': 'application/json',
    # 'cookie': 'spid=1710386501834_0db0dfeeeee921ea383d74a2b475b01e_lig2b1cf6mg48nnk; spsn=1710386773864_7b2276657273696f6e223a22332e342e32222c227369676e223a226564646634346238653834343861386362623239376432323333376637353033222c22706c6174666f726d223a224d6163496e74656c222c2262726f7773657273223a5b226368726f6d65225d2c2273636f7265223a302e357d; _ym_uid=1710387178434487227; _ym_d=1710387178; device_id=b493ae28-e1b3-11ee-bb2a-fa163e5515d9; ecom_token=7d38cd36-7103-4cea-b737-05eeeec38bd0; sbermegamarket_token=7d38cd36-7103-4cea-b737-05eeeec38bd0; isOldUser=true; adspire_uid=AS.1932505593.1710387244; ssaid=b5a10b90-e1b3-11ee-b8a5-2d398e0ce1d4; _sa=SA1.0afa6adf-b411-4f96-961f-3de9dce9e36f.1710387246; tmr_lvid=833d2eab9333bc8b0379f5e02db7ce6e; tmr_lvidTS=1710387247241; adrcid=ARvfXEzxg7yaLzHMpYLmG3Q; _gpVisits={"isFirstVisitDomain":true,"idContainer":"10002472"}; rrpvid=861105740483026; _gcl_au=1.1.316160871.1710387268; rcuid=63e4c8439562c1e4a19fa995; flocktory-uuid=b76d32f6-3a18-45a4-bef4-bd6ac5b4fd5a-2; adid=171038730170345; uxs_uid=d7161bd0-e1b3-11ee-8f3f-4f3d9df8c5bc; _ym_visorc=b; _ym_isad=1; spsc=1710905985956_39babb24b7a33f5c52abca69084030a0_2dc4c47e5beb4aae25be080fa9d16c8093e7e989cef732b63b8bada59af3d7da; _gid=GA1.2.650427167.1710906172; adrdel=1; __tld__=null; tmr_detect=0%7C1710906285847; __zzatw-smm=MDA0dC0cTHtmcDhhDHEWTT17CT4VHThHKHIzd2UbN1ddHBEkWA4hPwsXXFU+NVQOPHVXLw0uOF4tbx5mSFkoQ1tPCSsbEQhnFRtQSxgvS18+bX0yUCs5Lmw=QvG54Q==; region_info=%7B%22displayName%22%3A%22%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C%22%2C%22kladrId%22%3A%225000000000000%22%2C%22isDeliveryEnabled%22%3Atrue%2C%22geo%22%3A%7B%22lat%22%3A55.755814%2C%22lon%22%3A37.617635%7D%2C%22id%22%3A%2250%22%7D; _gp10002472={"hits":2,"vc":1,"ac":1,"a6":1}; _ga_W49D2LL5S1=GS1.1.1710906130.4.1.1710906287.33.0.0; _ga=GA1.2.70211477.1710387243; _ga_VD1LWDPWYX=GS1.2.1710906325.3.0.1710906325.0.0.0; cfidsw-smm=bKrwW0Nh2W5OQmYjlAO2bjK6gwX1+zueuPURCZPlV9umr5iKrNMLkRyX8GyslSXQs36nrOoZIdT/uc3ETv7E0xiPlhp3JTa11xH7aEYLwAH0m7x7Yr15PcTQqueu/WqO/f+RioxvoY6kCy6bR9y2X5l/Ey0VBjL4oHvVIg==; cfidsw-smm=bKrwW0Nh2W5OQmYjlAO2bjK6gwX1+zueuPURCZPlV9umr5iKrNMLkRyX8GyslSXQs36nrOoZIdT/uc3ETv7E0xiPlhp3JTa11xH7aEYLwAH0m7x7Yr15PcTQqueu/WqO/f+RioxvoY6kCy6bR9y2X5l/Ey0VBjL4oHvVIg==',
    'origin': 'https://megamarket.ru',
    'referer': 'https://megamarket.ru/catalog/videokarty/set-rtx-4060/',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

json_data = {
    'requestVersion': 7,
    'auth': {
        'locationId': '50',
        'appPlatform': 'WEB',
        'appVersion': 1710469695,
        'experiments': {
            '8': '1',
            '55': '2',
            '58': '2',
            '62': '1',
            '68': '1',
            '69': '1',
            '79': '3',
            '98': '1',
            '99': '1',
            '107': '2',
            '109': '2',
            '119': '1',
            '120': '2',
            '121': '2',
            '122': '1',
            '126': '1',
            '128': '1',
            '132': '1',
            '144': '3',
            '154': '2',
            '173': '2',
            '178': '1',
            '184': '3',
            '186': '1',
            '190': '2',
            '192': '2',
            '194': '3',
            '200': '2',
            '205': '2',
            '209': '1',
            '218': '1',
            '235': '2',
            '237': '2',
            '243': '1',
            '645': '3',
            '5779': '2',
            '20121': '1',
            '67319': '2',
            '70070': '2',
            '85160': '2',
        },
        'os': 'UNKNOWN_OS',
    },
}

response = requests.post(
    'https://megamarket.ru/api/mobile/v2/cartService/cart/search',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

print(response.json())