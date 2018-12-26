# 출처: https://wkdtjsgur100.github.io/RSA-algorithm/

# 유클리드 호제법을 이용해 최대공약수를 구하는 함수
# e계산 시 필요함
def gcd(a, b):
    while b!=0:
        a, b = b, a%b
    return a

#암호문을 평문으로 만드는 함수
def decrypt(pk, ciphertext):
    #Unpack the key into its components
    key, n = pk
    #평문을 암호문으로 만들어줌, 개인키와 n값을 이용함
    plain = [chr((char ** key) % n) for char in ciphertext]
    #Return the array of bytes as a string
    return ''.join(plain)

#평문을 암호문으로 만드는 함수
def encrypt(pk, plaintext):
    #Unpack the key into it's components
    key, n = pk
    #암호문을 평문으로 만들어줌, 공개키와 n을 이용함
    cipher = [(ord(char) ** key) % n for char in plaintext]
    #Return the array of bytes
    return cipher

#개인키를 만드는 함수
def get_private_key(e, tot):
    k=1
    while (e*k)%tot != 1 or k == e:
        k+=1
    return k

#공개키를 만드는 함수 
def get_public_key(totient):
    e=2
    while e<totient and gcd(e, totient)!=1:
        e += 1
    return e

#사용자가 입력한 소수를 판별하는 함수
def is_prime(n: int) -> bool:
    if n<2:
        return False
    for i in range(2, n):
        if n%i is 0:
            return False
    return True

#암호화 시킬 문장을 입력받음
m = input("Enter the text to be encrypted: ")

#P와 Q를 소수로 입력할때까지 반복
while(1):
    #1. 소수를 입력받음
    p = int(input("Enter the P: "))
    q = int(input("Enter the Q: "))
    
    if(is_prime(p) and is_prime(q)):
        break;
    else:
        if(not is_prime(p) and is_prime(q)):
            print("P is not prime number")
        elif(not is_prime(q) and is_prime(p)):
            print("Q is not prime number")
        else:
            print("P and Q are not prime number")
        
print("\nTwo prime numbers(p and q) are:", str(p), "and", str(q))

#2. n값 계산
n = p*q
print("n(p*q)=", str(p), "*", str(q), "=", str(n))

#3. 서로소인 totient계산 
totient = (p-1)*(q-1)
print("(p-1)*(q-1)=", str(totient))

# 4. 공개키 e값 계산
e = get_public_key(totient)
print("Public key(n, e):("+str(n)+","+str(e)+")")

# 5. 개인키 d값 계산
d = get_private_key(e, totient)
print("Private key(n, d):("+str(n)+","+str(d)+")")

# 6. 사용자가 입력한 메세지를 암호화
encrypted_msg = encrypt((e,n), m)
print('Encrypted Message:', ''.join(map(lambda x: str(x), encrypted_msg)))

# 7. 암호화된 메세지 복호화 
print('Decrypted Message:', decrypt((d,n),encrypted_msg))