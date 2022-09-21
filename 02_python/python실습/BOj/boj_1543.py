#문서 검색
str_ = input()
search = input()
cnt = 0
start = 0
while start <= len(str_) - len(search) :      # 시작점이 문자열에서 검색하려는 단어의 길이를 뺸 값보다 크다면 종료됨 
  if str[start:start+len(search)] == search : # 시작점부터 검색하려고 하는 단어의 길이만큼의 지점까지 
    cnt += 1                                  # 검색이 되면 카운트 +1
    start += len(search)                      # 시작점 이동 -> 중복을 방지하기 위해 검사가 끝난 문자는 다시 사용하지 않음.
  else :                                      # 검색이 안되는 경우 찾는 단어가 아닌경우
    start += 1                                # 문자열의 다음 문자로 이동. -> 사용하지 않았기 때문

print(cnt)