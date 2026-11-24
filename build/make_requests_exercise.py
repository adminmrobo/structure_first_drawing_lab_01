# -*- coding: utf-8 -*-
"""'연습 문제 — 프롬프트로 직접 풀기' 예상 결과 그림 요청 꾸러미(docs/image_requests_exercise) 생성."""
import os, csv, sys
sys.path.insert(0, os.path.dirname(__file__))
from content_exercise import EX
from make_requests import HEAD_ANI
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, "docs", "image_requests_exercise")
os.makedirs(os.path.join(D, "prompts"), exist_ok=True)
PAGES = {1: "01_photo_to_drawing.html", 2: "02_fit.html", 3: "03_material.html", 4: "04_motion.html", 5: "05_ai_vfx.html", 6: "06_failure_lab.html", 7: "practice/index.html"}
rows = []; n = 0
for no, xs in EX.items():
    cid = f"X0{no}_part{no}"
    md = f"# X0{no} · {no}부 연습 문제 예상 결과 — " + ", ".join(x["key"] for x in xs) + f"\n\n**Genspark에 먼저 붙여 넣기 ↓**\n```\n{HEAD_ANI}\n```\n"
    for i, x in enumerate(xs, 1):
        n += 1; rows.append([n, cid[:3], x["key"], PAGES[no] + f"#ex{i}", x["ratio"], ""])
        md += f"\n---\n## {i}) {x['key']} — 연습 {i} · {x['title']}\n첨부: {x['attach']}\n예상 결과(이렇게 나오면 성공): {x['expect']}\n```\n{x['prompt']}\n```\n"
    if no == 6:
        md += "\n---\n**실패 그림 주의:** 왼쪽 패널은 일부러 틀린 그림입니다. 도구가 실수를 고쳐 버리면 두 번까지만 다시 시도하고, 그래도 안 되면 그대로 주셔도 됩니다.\n"
    open(os.path.join(D, "prompts", cid + ".md"), "w").write(md)
with open(os.path.join(D, "checklist.csv"), "w", newline="") as f:
    w = csv.writer(f); w.writerow(["order", "conversation", "file", "page", "ratio", "status"]); w.writerows(rows)
open(os.path.join(D, "README.md"), "w").write(f"""# 그림 요청 꾸러미 3 — '연습 문제' 예상 결과 그림 ({n}장)

1~7부마다 새로 넣은 '연습 문제 — 프롬프트로 직접 풀기' 2개씩의 **예상 결과** 그림입니다. 각 그림은 페이지의 '③ 완성 예시 프롬프트'와 같은 프롬프트로 만듭니다.

## 요청 순서 (Genspark 대화 하나 = 파일 하나, 2장씩)
| 순서 | 파일 | 그림 |
|---|---|---|
""" + "".join(f"| {no} | prompts/X0{no}_part{no}.md | " + ", ".join(x['key'] + f" ({x['ratio']})" for x in xs) + " |\n" for no, xs in EX.items()) + """
## 규칙
- 본문 그림 규칙과 같습니다: 애니풍(5부 연습 2는 픽셀아트), 모두 20대 성인(박사는 성인 남성, 꼬마 체형 아님), 노출·교복 느낌·글자 금지.
- 각 파일 위에 적힌 참고 그림을 첨부하세요(`refs/`).
- 6부 두 장은 왼쪽이 일부러 틀린 그림, 오른쪽이 고친 그림입니다.

## 저장 이름
`checklist.csv`의 `file` 열 이름 그대로(png·jpg) 저장해 zip으로 주세요. 받으면 WebP로 바꿔 넣고 다시 올립니다.
""")
print("exercise images", n)
