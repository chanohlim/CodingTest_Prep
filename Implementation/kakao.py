from PyKakao import Message

# 메시지 API 인스턴스 생성
MSG = Message(service_key = "REST API 키")

# 카카오 인증코드 발급 URL 생성
auth_url = MSG.get_url_for_generating_code()
print(auth_url)

# 카카오 인증코드 발급 URL 접속 후 리다이렉트된 URL
url = ""

# 위 URL로 액세스 토큰 추출
access_token = MSG.get_access_token_by_redirected_url(url)

# 액세스 토큰 설정
MSG.set_access_token(access_token)

# 1. 나에게 보내기 API - 텍스트 메시지 보내기 예시
message_type = "text" # 메시지 유형 - 텍스트
text = "텍스트 영역입니다. 최대 200자 표시 가능합니다." # 전송할 텍스트 메시지 내용
link = {
  "web_url": "https://developers.kakao.com",
  "mobile_web_url": "https://developers.kakao.com",
}
button_title = "바로 확인" # 버튼 타이틀

MSG.send_message_to_me(
    message_type=message_type, 
    text=text,
    link=link,
    button_title=button_title,
)

# 2. 친구에게 보내기 API - 텍스트 메시지 보내기 예시 (친구의 UUID 필요)
message_type = "text" # 메시지 유형 - 텍스트
receiver_uuids = [] # 메시지 수신자 UUID 목록
text = "텍스트 영역입니다. 최대 200자 표시 가능합니다." # 전송할 텍스트 메시지 내용
link = {
  "web_url": "https://developers.kakao.com",
  "mobile_web_url": "https://developers.kakao.com",
}
button_title = "바로 확인" # 버튼 타이틀

MSG.send_message_to_friend(
    message_type=message_type, 
    receiver_uuids=receiver_uuids,
    text=text,
    link=link,
    button_title=button_title,
)