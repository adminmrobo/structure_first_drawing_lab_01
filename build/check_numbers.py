# -*- coding: utf-8 -*-
"""본문 '숫자로 한 번 해 보기'와 평가 점수 검산. python3 build/check_numbers.py"""
import math, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from content_a import P1, P2, P3
from content_b import P4, P5, P6
ok = True
def chk(name, got, want, tol=0.01):
    global ok
    good = abs(got - want) <= tol
    ok &= good
    print(("OK " if good else "XX "), name, round(got, 4), "기대", want)
F = [9, 7, 5, 3, 2, 1, 1, 1, 0.5, 0.5]
chk("1-1 합", sum(F), 30); chk("1-1 셋", sum(F[:3]) / 30, 0.70); chk("1-1 다섯", sum(F[:5]) / 30, 0.867, 0.001)
chk("1-4 r1", 1 * 0.35, 0.35); chk("1-4 r6", 6 * 0.35, 2.1); chk("1-4 20도", math.radians(20), 0.35, 0.01)
chk("2-1 7%", (90 - 84) / 84, 0.07, 0.002); chk("2-1 33%", (112 - 84) / 84, 0.333, 0.001); chk("2-1 4.7배", 28 / 6, 4.7, 0.05)
chk("2-3 d4", 2 * math.sqrt(15**2 + 4**2) - 30, 1.05, 0.005); chk("2-3 d8", 2 * math.sqrt(15**2 + 8**2) - 30, 4)
chk("3-1 2배", 2**0.75, 1.68, 0.005); chk("3-1 3배", 3**0.75, 2.28, 0.005); chk("3-1 개수", 30 / (3 * 2**0.75), 6, 0.06)
chk("3-3 5번", 1 - 0.9**5, 0.41, 0.005); chk("3-3 10번", 1 - 0.9**10, 0.65, 0.005); chk("3-3 니트", 1 - 0.98**10, 0.18, 0.005)
chk("3-4 블라우스", 4 * 1.5, 6); chk("3-4 재킷", 4 * 0.5, 2); chk("3-4 조끼", 1 * 0.5, 0.5)
chk("4-1 v2", 2 * 2**2, 8); chk("4-1 v3", 2 * 3**2, 18)
chk("4-2 cos60", math.cos(math.radians(60)), 0.5); chk("4-2 cos120", math.cos(math.radians(120)), -0.5)
chk("4-3 90", 8 * math.pi / 2, 12.6, 0.06); chk("4-3 45", 8 * math.pi / 4, 6.3, 0.06); chk("4-3 다리", 12 * math.pi / 2, 18.8, 0.06)
chk("5-2 전체", 512 * 768, 393216); chk("5-2 비율", 60000 / 393216, 0.153, 0.001); chk("5-2 1.5배", 1.5**2 * 60000 / 393216, 0.34, 0.005)
chk("연습4-2 무릎", 12 * math.radians(120), 25.1, 0.06)
for P in (P1, P2, P3, P4, P5, P6):
    J = P["judge"]; print("   ", P["no"], "부 평가", sum(J["a"][1]), ":", sum(J["b"][1]), J["result"][0][2][:16])
print("전체 통과" if ok else "검산 실패"); sys.exit(0 if ok else 1)
