from Crypto import Random
from Crypto.PublicKey import RSA
import base64

def encode_base64(p):
    return base64.b64encode(p).decode('ascii')

# 32바이트 (256비트) 랜덤 비밀키 생성
secret = Random.get_random_bytes(32)

rsa = RSA.generate(2048) # RSA 2048 키 생성 시작

pubkey = rsa.public_key() # 공개키 export
# export 공개키 저장(생성된 public key를 pubkey.key라는 파일명으로 export)
f = open("pubkey.key",'wb')
f.write(pubkey.exportKey('PEM'))#base64로 인코딩된 것을 넣기
f.close()

#prikey = rsa.exportKey('PEM')
# 개인키 export(생성된 private key를 prikey.key라는 파일명으로 export)
prikey = rsa
f = open("prikey.key",'wb')
f.write(prikey.exportKey('PEM'))
f.close()


print(encode_base64(secret) + '\n')
print(encode_base64(pubkey) + '\n')
print(encode_base64(prikey) + '\n')
