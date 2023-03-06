 파이썬의 cryptography 모듈에서 지원하는 rsa의 경우, key_size가 x 비트이고, 패딩 을 위한 해시 알고리즘이 y 비트를 사용한다고 할 때, 암호화할 수 있는 최대 메시 지의 길이는 x/8 – 2*y/8 – 2 바이트이다. 예를 들면, key_size가 2048비트이고 SHA256 해시 알고리즘을 패딩으로 사용할 경우, 메시지의 최대 길이는 190바이트이다. 
 이때 암호화할 파일의 크기가 190바이트를 넘어갈 경우, 강의 노트에 나온 방식 으로 단순하게 암호화를 진행하면 오류가 발생한다.
 이를 해결하기 위하여 다음과 같은 암호화 정책을 사용할 수 있다.
 가. 길이가 긴 메시지는 AES를 이용하여 암호화한다. ← enc_msg 
 나. 공개키를 이용하여 AES의 키(aes_key)를 암호화한다. ← enc_key 
 다. enc_msg와 enc_key를 insecure channel로 수신자에게 전달한다. 
 라. 수신자는 개인키를 이용하여 enc_key를 복호화한다. ← aes_key 
 마. aes_key를 이용하여 enc_msg를 복호화하여 평문을 복원한다.
위의 과정을 수행하는 파이썬 프로그램을 작성하라. 
평문 메시지는 사용자 입력으 로 받고, RSA의 공개키와 개인키는 첨부한 public_key.pem 파일과 private_key.pem 파일에 저장된 키를 이용한다. 
enc_msg의 복호화 결과를 출력하여, 사용자 입력 메 시지와 동일함을 보이면 된다.