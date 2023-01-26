'''
O(n)의 시간 복잡도로 풀어야 한다는 것이 관건
문자열의 시작 지점과 끝 지점을 변경해가면서 찾아야할듯
글자의 중복 여부는 어떻게 알까
글자가 중복될 경우 시작지점을 바꿔야할듯 -> 끝지점은 아무리 늘려봤자 앞부분에 중복된 글자가 있으니.
가장 긴지는 어떻게 알까 -> 길이만 리턴하면 되므로 길이만 저장해가며 한바퀴 돌면 될듯
루프의 정지조건은? -> 중복이 없고.. 문자열의 끝부분이 원본 문자열의 끝부분과 일치할때
복잡도 O(n)인 이유 -> 중복체크는 해시를 써버리면 되니까 O(1), 순회의 경우 최악의경우 end는 원본 문자열 끝까지 n번, start 또한 원본 문자열 끝까지 n번 가기 떄문에 2n이므로 O(n)
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
    def doesRepeat(chars, start, end):

    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = list(s)
        counts = {}
        start = end = 0 
        while end < len(chars) - 1:
