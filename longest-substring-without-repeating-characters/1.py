'''
O(n)의 시간 복잡도로 풀어야 한다는 것이 관건
문자열의 시작 지점과 끝 지점을 변경해가면서 찾아야할듯
글자의 중복 여부는 어떻게 알까
글자가 중복될 경우 시작지점을 바꿔야할듯 -> 끝지점은 아무리 늘려봤자 앞부분에 중복된 글자가 있으니.
가장 긴지는 어떻게 알까 -> 길이만 리턴하면 되므로 길이만 저장해가며 한바퀴 돌면 될듯
루프의 정지조건은? -> 중복이 없고.. 문자열의 끝부분이 원본 문자열의 끝부분과 일치할때
복잡도 O(n)인 이유 -> 중복체크는 해시를 써버리면 되니까 O(1), 순회의 경우 최악의경우 end는 원본 문자열 끝까지 n번, start 또한 원본 문자열 끝까지 n번 가기 떄문에 2n이므로 O(n)
루프 이전 혹은 이후에 한번 더 로직을 실행시켜야 할 것 같다. 끝부분에서 에러가 남
'''

'''
pwpwkew -> pwke
[pw]pwkew
[pwp]wkew
p[wp]wkew
p[wpw]kew
pw[pwke]w -> longest
pw[pwkew]
pwp[wkew]
pwpw[kew]
'''

class Solution:
    def doesRepeat(self, counts):
        for char in counts:
            if counts[char] > 1:
                return True
        return False
        
    def increaseCount(self, counts, char):
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1
    
    def decreaseCount(self, counts, char):
        counts[char] -= 1

    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        counts = {}
        start = 0
        end = 1
        max_len = 0

        self.increaseCount(counts, s[end - 1])
        while end <= len(s):
            #print(s[start:end], s, start, end)
            #print(counts)
            #print('before test')
            if self.doesRepeat(counts):
                #print('does repeat')
                self.decreaseCount(counts, s[start])
                start += 1
            else:
                #print('does not repeat')
                max_len = max(max_len, len(s[start:end]))
                end += 1
                if end > len(s): break
                self.increaseCount(counts, s[end - 1])

        return max_len
