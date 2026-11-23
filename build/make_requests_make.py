# -*- coding: utf-8 -*-
"""'프롬프트로 직접 만들어 보기'의 B 결과 그림 요청 꾸러미(docs/image_requests_make) 생성."""
import os, csv, sys
sys.path.insert(0, os.path.dirname(__file__))
from content_make import MAKE
from make_requests import PROMPTS, ATTACH_OF, CONV_OF
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, "docs", "image_requests_make")
os.makedirs(os.path.join(D, "prompts"), exist_ok=True)
HEAD = ("해설 페이지의 '직접 만들어 보기' 비교 그림을 만들어 줘.\n- 첨부한 그림(이미 만든 A 결과)과 똑같은 캐릭터·구도·화풍·빛을 유지하고, 아래 'Change only'에 적힌 것만 바꿀 것\n"
        "- 비율은 첨부한 A 결과와 같게\n- 등장인물은 모두 20대 성인(박사는 성인 남성). 노출·교복 느낌 금지\n- 그림 안에 글자·숫자·로고 금지")
CONVS = [("M01_part1", 1), ("M02_part2", 2), ("M03_part3", 3), ("M04_part4", 4), ("M05_part5", 5), ("M06_part6", 6)]
rows = []; n = 0; seen = set()
for cid, no in CONVS:
    md = f"# {cid[:3]} · {no}부 '직접 만들어 보기' 비교 그림\n\n**Genspark에 먼저 붙여 넣기 ↓**\n```\n{HEAD}\n```\n"
    for t in MAKE[no]:
        for k in t["b_imgs"]:
            if k in PROMPTS or k in seen:
                continue
            seen.add(k); n += 1
            if k.startswith("p1_moa_shadow_step"):
                i = int(k[-1]); step = t["b_text"].split("\n")[i - 1][3:]
                att = "refs/moa_anime_base.png" + ("" if i == 1 else f", 방금 만든 p1_moa_shadow_step{i-1}")
                pr = ("Illustration, vertical 2:3, anime style matching the attached reference exactly.\n" if i == 1 else "") + step + "\nPlain off-white background. No text, no letters, no logos, no watermark."
                ratio = "2:3"; how = "같은 대화에서 1→5 차례로. 각 단계는 바로 앞 결과를 첨부"
            elif k == "p5_haru_inpaint_real":
                att = "refs/haru_anime_base.png (Genspark 이미지 편집·부분 수정 기능에서)"; ratio = "2:3"; how = "그림 생성이 아니라 '부분 수정(영역 칠하기)' 기능으로"
                pr = t["b_text"]
            elif k == "f2_fixed":
                att = "f2_coat_like_silk.png (A 결과) + refs/moa_anime_base.png"; ratio = "2:3"; how = "A 결과를 첨부하고 고치는 문장으로"
                pr = t["b_text"]
            else:
                a = PROMPTS[t["key"]]; ratio = "16:9" if "16:9" in a[4].split("\n")[0] else "2:3"
                if k == "p5_outfit_swap_lineup_b":
                    att = "없음 — 일부러 참고 그림 없이, 새 대화에서"; how = "원리를 뺀 비교: 첨부 없이 이름만"
                else:
                    att = f"{t['key']}.png (A 결과) + {ATTACH_OF[CONV_OF[t['key']]]}"; how = "A 결과를 첨부하고 Change only 문장으로"
                pr = t["b_text"]
            rows.append([n, cid[:3], k, f"{['','01_photo_to_drawing','02_fit','03_material','04_motion','05_ai_vfx','06_failure_lab'][no]}.html#make", ratio, how, ""])
            md += f"\n---\n## {k} — {t['title']}\n첨부: {att}\n방법: {how}\n```\n{pr}\n```\n"
    open(os.path.join(D, "prompts", cid + ".md"), "w").write(md)
with open(os.path.join(D, "checklist.csv"), "w", newline="") as f:
    w = csv.writer(f); w.writerow(["order", "conversation", "file", "page", "ratio", "how", "status"]); w.writerows(rows)
open(os.path.join(D, "README.md"), "w").write(f"""# 그림 요청 꾸러미 2 — '프롬프트로 직접 만들어 보기' 비교 그림 ({n}장)

부마다 새로 넣은 '프롬프트로 직접 만들어 보기' 실습의 **B 결과**(원리를 빼거나 바꾼 비교 그림)입니다. A 결과는 이미 받은 34장을 그대로 씁니다.

## 요청 순서 (Genspark 대화 하나 = 파일 하나)
| 순서 | 파일 | 장수 | 방법 |
|---|---|---|---|
| 1 | prompts/M01_part1.md | 6 | 사진 비교 B 1장 + 그림자 단계 1→5를 같은 대화에서 차례로 |
| 2 | prompts/M02_part2.md | 3 | A 결과를 첨부하고 Change only 문장 |
| 3 | prompts/M03_part3.md | 3 | 같음 |
| 4 | prompts/M04_part4.md | 3 | 같음 |
| 5 | prompts/M05_part5.md | 3 | 옷 바꿔 입기 B는 **첨부 없이 새 대화에서**, 부분 수정은 **편집 기능**으로, 소재 B는 A 첨부 |
| 6 | prompts/M06_part6.md | 1 | f2 실패 그림을 첨부하고 고치는 문장 |

## 저장 이름
`checklist.csv`의 `file` 열 이름 그대로(png·jpg). A 결과 그림(첨부용)은 앞 꾸러미 결과(구조먼저그리기연구실_01_34장.zip)에 있습니다. 참고 그림은 `refs/`.

## 주의
- 'Change only' 문장만 바꾸고 나머지(캐릭터·구도·빛)는 A와 같아야 비교가 됩니다.
- 비교 그림이 A와 거의 같게 나오면 한 번 더 시도해 주세요. 그래도 같으면 그대로 주셔도 됩니다(도구의 한계로 설명합니다).
""")
print("make images", n)
