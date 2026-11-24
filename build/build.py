# -*- coding: utf-8 -*-
"""구조 먼저 그리기 연구실 01 · 옷장 편 — 페이지 빌드.
python3 build/build.py 로 index.html, 01~06 페이지, practice/index.html 을 다시 만든다.
그림 파일(assets/img/{키}.webp)이 있으면 넣고, 없으면 '그림 준비 중' 자리만 둔다."""
import json, os, html, sys
sys.path.insert(0, os.path.dirname(__file__))
from content_a import P1, P2, P3
from content_b import P4, P5, P6
from content_make import MAKE
from content_exercise import EX, RETRY, RETRY2
from make_requests_retry import R as RETRY_R
from make_requests import PROMPTS, CONV_OF, ATTACH_OF
STYLES = [("pixel", "픽셀"), ("anime", "애니풍"), ("semireal", "반실사"), ("photo", "실사풍")]

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VER = "v1.0"
DATE = "2026-11-23"
SITE = "https://adminmrobo.github.io/structure_first_drawing_lab_01/"
PREV_SITE = "https://adminmrobo.github.io/adminmrobo-structure_first_drawing_lab/"
REPO = "https://github.com/adminmrobo/structure_first_drawing_lab_01"
AUTHOR_URL = "https://adminmrobo.github.io/who_am_i/who_am_i.html"
RENDER = "https://adminmrobo.github.io/ai_rendering/"
FISH = "https://adminmrobo.github.io/unsupervised_fish_lab/"
CHARREPO = "https://github.com/adminmrobo/fruitfly-lab-expressions"
SERIES = "구조 먼저 그리기 연구실 01 · 옷장 편"
E = html.escape
PARTS = [P1, P2, P3, P4, P5, P6]

CH = {
 "doctor": ("박사", "해설 + 손님 모델(3·5부). 셔츠·조끼·넥타이 차림"),
 "haru": ("조수 하루", "모델(2부) + 수식 상자 담당. 어려운 식을 대신 묻는다"),
 "sia": ("시아", "인턴1 · 모델(4부). 메이드복 치마와 앞치마 프릴로 움직임을 보여 준다"),
 "moa": ("모아", "인턴2 · 모델(1·3부). 니트 카디건과 울 코트의 주인공"),
 "jupanbot": ("주판봇", "화가 A. 성급하게 결과부터 그린다 — 흔한 실수 담당"),
 "fruitfly": ("초파리 연구원", "화가 B. 구조부터 의심한다. \"이걸 눌러 봐\""),
 "x1": ("X1", "평가단. 닮음을 본다"),
 "x2": ("X2", "평가단. 입체감을 본다"),
 "x3": ("X3", "평가단. 자연스러움을 본다"),
}
COLOR = {"doctor": "doc", "haru": "asst", "fruitfly": "fly", "jupanbot": "robo", "sia": "sia", "moa": "moa", "x1": "x", "x2": "x", "x3": "x"}

def face(k, e="e13", pre="", cls=""):
    n = CH[k][0]
    return f'<img src="{pre}assets/chars/{k}_{e}.webp" alt="{E(n)}" width="96" height="96" loading="lazy"{(" class=%s" % cls) if cls else ""}>'

def has_img(key):
    return os.path.exists(os.path.join(ROOT, "assets", "img", key + ".webp"))

def art(key, alt, ar="16/9", cap=None, pre="", cls=""):
    cap_html = f"<figcaption>{E(cap)}</figcaption>" if cap else ""
    if has_img(key):
        return f'<figure class="art {cls}" data-img="{key}"><img src="{pre}assets/img/{key}.webp" alt="{E(alt)}" loading="lazy" decoding="async">{cap_html}</figure>'
    return (f'<figure class="art {cls}" data-img="{key}"><div class="ph-art" style="--ar:{ar}" role="img" aria-label="{E(alt)}">'
            f'<b>그림 준비 중 · {key}</b><span>{E(alt)}</span></div>{cap_html}</figure>')

def head(title, desc, og, path, pre=""):
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<meta property="og:type" content="article"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}">
<meta property="og:image" content="{SITE}assets/og/{og}"><meta property="og:url" content="{SITE}{path}"><meta name="twitter:card" content="summary_large_image">
<meta name="author" content="안상선">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{pre}assets/lab.css">
</head>
<body data-root="{pre}">
<div id="prog"></div>
"""

def nav(links, pre=""):
    a = "".join(f'<a href="{h}">{E(t)}</a>' for h, t in links)
    return f'<nav class="top"><div class="row"><a class="logo" href="{pre}index.html">구조 먼저 그리기 <i>· 옷장 편</i></a><div class="links">{a}</div></div></nav>\n'

def cover(key, cap, cast, pre=""):
    if has_img(key):
        return f'<div class="cover"><div class="frame" data-img="{key}"><img class="art" src="{pre}assets/img/{key}.webp" alt="{E(cap)}" width="1600" height="900" fetchpriority="high" decoding="async"></div></div>\n'
    # 그림이 오기 전 픽셀 대체 표지: 네모 격자 + 상자·원기둥 마네킹(픽셀 블록) + 픽셀 캐릭터
    cells = []
    for x in range(0, 1600, 40):
        for y in range(0, 900, 40):
            if (x // 40 + y // 40) % 2 == 0:
                cells.append(f'<rect x="{x}" y="{y}" width="40" height="40" fill="#f3f6fa"/>')
    blocks = [(1180, 140, 80, 100, "#c9d3e6"), (1200, 240, 40, 30, "#d8dfeb"), (1150, 270, 140, 140, "#b9c6df"), (1160, 410, 120, 90, "#a9b8d6"),
              (1110, 280, 40, 120, "#cdd6e8"), (1290, 280, 40, 120, "#cdd6e8"), (1100, 400, 40, 100, "#dfe5ef"), (1300, 400, 40, 100, "#dfe5ef"),
              (1170, 500, 50, 170, "#b9c6df"), (1230, 500, 50, 170, "#b9c6df"), (1170, 670, 50, 130, "#a9b8d6"), (1230, 670, 50, 130, "#a9b8d6")]
    bl = "".join(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{c}" stroke="#1e2f6e" stroke-width="6"/>' for x, y, w, h, c in blocks)
    easel = '<rect x="240" y="180" width="300" height="380" fill="#ffffff" stroke="#8a5a2b" stroke-width="12"/><rect x="270" y="560" width="20" height="260" fill="#8a5a2b"/><rect x="490" y="560" width="20" height="260" fill="#8a5a2b"/>' + \
            "".join(f'<rect x="{300+i*40}" y="{240+j*40}" width="40" height="40" fill="{c}"/>' for i, j, c in [(1,0,"#e9909a"),(2,0,"#e9909a"),(1,1,"#f6d3b8"),(2,1,"#f6d3b8"),(0,2,"#a99ac8"),(1,2,"#a99ac8"),(2,2,"#a99ac8"),(3,2,"#a99ac8"),(1,3,"#fbfbfd"),(2,3,"#fbfbfd"),(1,4,"#5b7fb8"),(2,4,"#5b7fb8")])
    imgs = "".join(face(k, e, pre) for k, e in cast)
    return f"""<div class="cover"><div class="frame" data-img="{key}"><svg class="grid" viewBox="0 0 1600 900" preserveAspectRatio="xMidYMid slice" aria-hidden="true" shape-rendering="crispEdges">{''.join(cells)}{easel}{bl}</svg>
<span class="cap">{E(cap)}</span><span class="badge">표지 그림 준비 중 · {key}</span><div class="cast" style="image-rendering:pixelated">{imgs}</div></div></div>
"""

def three(a, b, c, abbr):
    dl = "".join(f"<dt>{E(x)}</dt><dd>{E(y)}</dd>" for x, y in abbr)
    return f"""<div class="three"><h2>처음 오신 분께 — 세 줄 요약</h2><ul>
<li><b>무엇을</b>: {E(a)}</li><li><b>왜 알아야 하나</b>: {E(b)}</li><li><b>어디에 쓰나</b>: {E(c)}</li></ul>
<p>그림 실력·코드·수식을 몰라도 됩니다. 실험을 눌러 보며 따라오세요.</p>
<details class="abbr"><summary>낱말·약어 풀이 (펼치기)</summary><dl>{dl}</dl></details></div>\n"""

ABBR = [("접점", "천이 몸·손·소품에 걸리거나 눌린 곳. 주름의 시작점"), ("여유율", "옷 둘레가 몸 둘레보다 넉넉한 비율"), ("핏", "옷이 몸에 붙는 정도(딱 맞음·보통·헐렁함)"),
        ("입체 그림자", "빛을 등진 면에 생기는 그림자"), ("떨어지는 그림자", "다른 물체가 빛을 가려 생기는 그림자"), ("섬 그림자", "선에 붙지 않고 떠 있는 작은 그림자(애니 채색 용어)"),
        ("약속된 그림자", "빛 계산과 상관없이 그림 관례로 넣는 그림자(목 아래 등)"), ("버릇 주름", "자주 굽힌 곳에 힘을 빼도 남는 주름 자국"), ("사이드 플리츠", "주름을 한 방향으로 접은 주름치마"),
        ("가림 영역(마스크)", "AI가 다시 그릴 부분을 표시한 영역"), ("천 시뮬레이션", "무게·뻣뻣함 값으로 천의 움직임을 계산하는 VFX 기법"), ("VFX", "영화·영상의 시각 효과(Visual Effects)")]

def talk(lines, pre=""):
    out = []
    for k, e, t in lines:
        side = " r" if k in ("moa", "sia") else ""
        out.append(f'<div class="line{side}">{face(k, e, pre)}<div class="bub"><b style="color:var(--c-{COLOR[k]})">{E(CH[k][0])}</b>{E(t)}</div></div>')
    return '<div class="talk">' + "".join(out) + "</div>"

def quiz(q, opts, ans, ok, no):
    b = "".join(f'<button type="button">{E(o)}</button>' for o in opts)
    return f'<div class="quiz" data-ans="{ans}"><div class="qq">확인 퀴즈 — {E(q)}</div><div class="opts">{b}</div><div class="fb" aria-live="polite"></div><span class="qok" hidden>{E(ok)}</span><span class="qno" hidden>{E(no)}</span></div>'

def panel(no, i, p):
    return (f'<div class="panel"><div class="ph"><b>실험 {no}-{i}</b><small>{E(p["note"])}</small></div>'
            f'<div id="pp-{p["key"]}" data-panel="{p["key"]}"></div><div class="ctrl">{p["ctrl"]}</div><div class="readout" aria-live="polite"></div></div>')

def mathbox(m):
    tries = "".join(f"<div>{E(t)}</div>" for t in m["tries"])
    pcs = "".join(f"<tr><td class='m'>{E(a)}</td><td>{E(b)}</td></tr>" for a, b in m["pieces"])
    return f"""<div class="box mathbox"><h4>수식이 어려운 조수가 대신 묻습니다</h4>
<div class="q">{face('haru','e04')}<div><b>조수</b> {E(m['ask'])}</div></div>
<div class="easy"><b>말로 하면</b> — {E(m['words'])}</div>
<p><b>학교 수학으로 보면</b> — {E(m['school'])}</p>
<div class="fx">{E(m['formula'])}</div>
<table><thead><tr><th>식 조각</th><th>뜻</th></tr></thead><tbody>{pcs}</tbody></table>
<div class="try"><b>숫자로 한 번 해 보기</b>{tries}</div>
<div class="q">{face('haru','e16')}<div><b>조수</b> {E(m['comment'])}</div></div></div>"""

def gallery():
    rows = []
    for who, nm in [("haru", "하루"), ("sia", "시아"), ("moa", "모아")]:
        cells = "".join(art(f"p5_{who}_{st}", f"{nm}의 {sn} 전신 — 같은 자세, 왼쪽 위 빛", "2/3", sn) for st, sn in STYLES)
        rows.append(f'<h4 style="margin:14px 0 6px">{nm}</h4><div class="artrow">{cells}</div>')
    return '<div class="box" style="background:#fff">' + "".join(rows) + '<p class="hint" style="margin-top:8px">실사풍은 이 캐릭터를 코스프레한 가상의 성인 모델 사진으로 만든 것입니다. 실존 인물이 아닙니다.</p></div>'

EXAMPLE_PROMPT = """Full body character illustration, vertical 2:3.
High-quality anime illustration, clean confident lineart, two-tone cel shading with soft highlights, natural proportions of a young adult woman in her early twenties.
Character (match the attached reference sheet exactly): Haru, a cheerful lab assistant, long straight pink hair reaching the waist with navy blue streaks, including a thick navy streak down the center of the bangs, two round slightly messy hair buns on top of the head, a small ahoge, big bright blue eyes, lavender hoodie with white drawstrings over a white t-shirt, open white knee-length lab coat, rolled-up blue jeans, lavender sneakers. Modest outfit exactly as described.
Pose: standing upright in a three-quarter view turned slightly to the right, left arm relaxed at her side, right hand resting on her hip.
Lighting: soft daylight from the upper left, form shadows on the right side of the body, a soft cast shadow on the floor toward the lower right.
Background: plain off-white studio background.
No text, no letters, no logos, no watermark, no revealing clothing, not resembling any famous anime character, no pixel art."""

def step(P, i, s):
    no = P["no"]
    labels = ["무엇이 문제인가", "그냥 하면 막히는 곳", "이렇게 푼다"]
    why = "".join(f"<li><b>{labels[k]}</b> — {E(x)}</li>" for k, x in enumerate(s["why"]))
    whybox = f'<div class="box why"><h4>왜 이렇게 하나</h4><ol>{why}</ol><div class="easy"><b>쉽게 말하면</b> — {E(s["easy"])}</div></div>'
    calm = talk([("doctor", "e08", "여기서 한 번 멈춰도 괜찮아요. 식이 낯설면 건너뛰고 아래 실험부터 눌러 보세요. 숫자는 실험이 대신 계산해 줍니다.")])
    duo = f'<div class="duo">{whybox}{mathbox(s["math"])}</div>{calm}' if s.get("math") else f'<div style="margin:16px 0">{whybox}</div>'
    solve = "".join(f"<p>{E(x)}</p>" for x in s["solve"])
    extra = ""
    if s.get("gallery"):
        extra += gallery()
    if s.get("imgs"):
        extra += '<div class="box" style="background:#fff"><div class="artrow">' + "".join(art(k, al, "2/3", cp) for k, al, cp in s["imgs"]) + '</div><p class="hint" style="margin-top:8px">실사풍은 캐릭터를 코스프레한 가상의 성인 모델 사진으로 만든 것입니다. 실존 인물이 아닙니다.</p></div>'
    if s.get("prompts"):
        extra += f'<div class="promptbox"><b>예시 — 이 시리즈의 그림 요청문(하루, 애니풍 기준 전신)</b><p class="hint">고정값 → 자세 → 빛(그림자 방향까지) → 화풍 → 금지 순서입니다.</p><pre>{E(EXAMPLE_PROMPT)}</pre></div>'
    img = art(s["img"][0], s["img"][1], s["img"][2], s["img"][1], cls="tall" if s["img"][2] == "2/3" else "") if s.get("img") else ""
    q = s["quiz"]
    return f"""<section class="room" id="{s['id']}"><div class="wrap">
<div class="roomno">{no}부 · {i}단계</div>
<h2>{E(s['title'])}</h2><p class="muted">{E(s['sub'])}</p>
<div class="tags"><span class="tag how">{E(s['how'])}</span><span class="tag day">{E(s['day'])}</span></div>
{duo}
<div class="pair"><div class="box"><h4>일상으로 치면</h4><p>{E(s['daily'])}</p></div><div class="box ml"><h4>그림·VFX 현장에서는</h4><p>{E(s['field'])}</p></div></div>
{talk(s['talk'])}
{panel(no, i, s['panel'])}
<div class="solve"><h4>풀이</h4>{solve}</div>
{extra}{img}
<div class="solve"><h4>AI 결과, 그대로 써도 될까?</h4><p>{E(s['ai'][0])}</p><details class="code"><summary>답 보기</summary><p>{E(s['ai'][1])}</p></details></div>
<div class="limit"><b>주의할 점</b> — {E(s['limit'])}</div>
{quiz(q[0], q[1], q[2], q[3], q[4])}
</div></section>
"""

def judge(J):
    rows = ""
    for idx, item in enumerate(J["items"]):
        a, b = J["a"][1][idx], J["b"][1][idx]
        mx = 8 if "8개" in item else 10
        rows += f'<span>{E(item)}</span><span class="bar" title="{J["a"][0]} {a}"><i style="width:{a/mx*100:.0f}%"></i></span><span class="bar" title="{J["b"][0]} {b}"><i style="width:{b/mx*100:.0f}%;background:var(--teal)"></i></span>'
    sa, sb = sum(J["a"][1]), sum(J["b"][1])
    tbl = "".join(f"<tr><td>{E(it)}</td><td>{J['a'][1][k]}</td><td>{J['b'][1][k]}</td></tr>" for k, it in enumerate(J["items"]))
    return f"""<section class="room" id="judge"><div class="wrap"><div class="roomno">평가단 채점</div><h2>{E(J['title'])}</h2>
{talk(J['setup'])}
<div class="judge"><h4>평가단 X1·X2·X3 채점</h4>
<div class="score"><span></span><b>{E(J['a'][0])}</b><b>{E(J['b'][0])}</b>{rows}</div>
<div class="tbl" style="margin-top:10px"><table><thead><tr><th>항목</th><th>{E(J['a'][0])}</th><th>{E(J['b'][0])}</th></tr></thead><tbody>{tbl}<tr><th>합계</th><th>{sa}</th><th>{sb}</th></tr></tbody></table></div>
{talk(J['comments'])}</div>
{talk(J['result'])}
<p class="hint">점수는 이야기 속 예시입니다. 실제 그림을 평가한 값이 아닙니다.</p>
</div></section>
"""

def summary(P):
    rows = "".join(f"<tr><td>{E(a)}</td><td>{E(b)}</td><td>{E(c)}</td></tr>" for a, b, c in P["summary"])
    return f"""<section id="sum"><div class="wrap"><h2>{P['no']}부 정리</h2>
<div class="tbl"><table><thead><tr><th>주제</th><th>한 줄</th><th>작업에서는</th></tr></thead><tbody>{rows}</tbody></table></div></div></section>
"""

def outro(P):
    return f"""<section id="outro"><div class="wrap"><h2>다음으로</h2>{talk(P['outro'])}
<div class="next"><a href="{P['prev'][0]}">{E(P['prev'][1])}</a><a href="{P['next'][0]}">{E(P['next'][1])}</a></div></div></section>
"""

def failcard(f):
    note = f'<p class="hint">{E(f["note"])}</p>' if f.get("note") else ""
    return f"""<div class="failcard" id="{f['key'][:7]}"><h3>{E(f['title'])}</h3><div class="failgrid">
{art(f['key'], f['alt'], f['ar'])}
<div><p><span class="chip">증상</span>{E(f['symptom'])}</p>
{quiz(f['q'], f['opts'], f['ans'], f['ok'], f['no'])}
<p><span class="chip">연결된 원리</span><a href="{f['link'][0]}">{E(f['link'][1])}</a></p>
<div class="promptbox"><b>고치는 프롬프트 조각</b><pre>{E(f['fix'])}</pre></div>{note}</div></div></div>"""

# ---------------- 지식 색인
KG = [
 ("concept/big-folds-first", "Method", "큰 주름부터 고르기", "Picking the dominant folds first", "01_photo_to_drawing.html", "#s1", "세기 순서로 큰 주름 몇 개가 옷 모양 대부분을 설명한다"),
 ("concept/detail-level", "Concept", "그림체와 정보량", "Detail level by drawing style", "01_photo_to_drawing.html", "#s2", "실사풍은 잔주름을 더하고 단순풍은 덜어 덩어리로"),
 ("method/shadow-order", "Method", "그림자 다섯 단계", "Five-step shadow layering", "01_photo_to_drawing.html", "#s3", "떨어지는·약속된 → 입체 → 섬 → 진한 2차 → 정리"),
 ("concept/soft-edge", "Concept", "그림자 경계 흐림", "Soft shadow edges on rounded forms", "01_photo_to_drawing.html", "#s4", "흐린 폭 ≈ 둥근 반지름 × 경계 각도 폭"),
 ("concept/ease", "Concept", "여유율", "Garment ease", "02_fit.html", "#s1", "(옷 둘레 − 몸 둘레) ÷ 몸 둘레, 남는 천만큼 주름이 생긴다"),
 ("concept/contact-points", "Concept", "자세별 접점", "Contact points by pose", "02_fit.html", "#s2", "자세가 바뀌면 천이 걸리는 시작점이 바뀐다"),
 ("concept/hem-rise", "Concept", "몸의 볼륨과 밑단", "Hem rise over body volume", "02_fit.html", "#s3", "튀어나온 곳을 돌아가는 길이만큼 밑단이 올라간다"),
 ("method/shadow-instead-of-line", "Method", "선 대신 그림자", "Replacing lines with fold shadows", "02_fit.html", "#s4", "주름 산의 빛 반대쪽 비탈에만 그림자"),
 ("concept/wrinkle-wavelength", "Concept", "두께와 주름 간격", "Wrinkle wavelength vs thickness", "03_material.html", "#s1", "간격 ∝ 두께^(3/4)"),
 ("concept/crisp-diamond", "Concept", "빳빳한 천의 마름모 그림자", "Angular shadows on crisp fabric", "03_material.html", "#s2", "날카롭게 꺾인 면이 각진 그림자를 만든다"),
 ("concept/fabric-memory", "Concept", "버릇 주름", "Fabric memory creases", "03_material.html", "#s3", "남은 자국 = 1 − (1 − p)ⁿ"),
 ("method/layered-garments", "Method", "겹쳐 입기의 주름 배분", "Fold distribution in layered garments", "03_material.html", "#s4", "예상 주름 수 ≈ 접점 개수 × 부드러움"),
 ("concept/skirt-airflow", "Concept", "걸을 때 치마의 공기", "Skirt lift from airflow", "04_motion.html", "#s1", "들림 ∝ 속도², 밑단은 움직임 반대쪽으로"),
 ("concept/pleat-visibility", "Concept", "주름치마의 보이는 뒷면", "Visible faces of side pleats", "04_motion.html", "#s2", "cos(사이각) > 0인 면만 보인다"),
 ("concept/bend-length", "Concept", "굽힘의 안팎 길이 차이", "Inner and outer length at a bent joint", "04_motion.html", "#s3", "길이 차이 = 두께 × 굽힌 각(라디안)"),
 ("concept/prop-contacts", "Concept", "소품이 닿는 곳의 접점", "Contacts created by props", "04_motion.html", "#s4", "가방 끈·백팩·셔츠 넣기·넥타이가 새 시작점이 된다"),
 ("method/outfit-prompt", "Method", "옷 고정 문장", "Structured outfit prompt", "05_ai_vfx.html", "#s1", "종류·핏·소재·동작과 접점·주름·금지"),
 ("method/inpaint-mask", "Method", "가림 영역으로 옷만 다시 그리기", "Inpainting with a clothing mask", "05_ai_vfx.html", "#s2", "바뀌는 비율 = 가린 넓이 ÷ 전체 넓이"),
 ("method/cloth-presets", "Method", "VFX 소재표", "Cloth simulation material presets", "05_ai_vfx.html", "#s3", "무게·뻣뻣함·늘어남을 숫자로"),
 ("method/style-detail", "Method", "화풍별 주름의 양", "Fold detail per art style", "05_ai_vfx.html", "#s4", "위치는 원리에 따라, 양은 화풍에 따라"),
 ("method/garment-diagnosis", "Method", "옷 그림 진단 순서", "Garment drawing diagnosis checklist", "06_failure_lab.html", "#s1", "접점·흐름 → 핏 → 소재 → 빛 → 정보량·가림"),
 ("application/garment-failures", "Application", "옷 그림 실패 8종", "Eight garment drawing failures", "06_failure_lab.html", "#fails", "잔주름 과다·소재 뒤바뀜·핏 무시·접점 무시·그림자 반대·프릴 역방향·주름치마 양면·가림 과다"),
 ("open/garment-age-drift", "OpenQuestion", "옷 이름이 나이를 바꾸는 현상", "Garment words shifting apparent age", "06_failure_lab.html", "#drift", "학교 옷 이름 대신 소재·핏·형태와 나이를 적는다"),
 ("application/practice", "Application", "실전 연습장", "Practice simulator", "practice/index.html", "#fitting", "피팅룸·소재 실험실·옷 문장 공방·진단 데스크"),
 ("analogy/main-roads", "Analogy", "큰길 세 개", "Three main roads on a map", "01_photo_to_drawing.html", "#s1", "큰길만 그려도 길을 찾을 수 있다"),
 ("analogy/curtain", "Analogy", "커튼 주름", "Curtain fullness", "02_fit.html", "#s1", "창보다 넓게 달수록 주름이 많다"),
 ("analogy/book-spine", "Analogy", "책 등", "Book spine", "04_motion.html", "#s3", "펼치면 등은 당겨지고 안쪽은 모인다"),
]
KG_EDGES = [("concept/big-folds-first","motivates","concept/detail-level"),("concept/detail-level","motivates","method/shadow-order"),("method/shadow-order","motivates","concept/soft-edge"),
 ("concept/ease","motivates","concept/contact-points"),("concept/contact-points","motivates","concept/hem-rise"),("concept/hem-rise","motivates","method/shadow-instead-of-line"),
 ("concept/wrinkle-wavelength","motivates","concept/crisp-diamond"),("concept/crisp-diamond","motivates","concept/fabric-memory"),("concept/fabric-memory","motivates","method/layered-garments"),
 ("concept/skirt-airflow","motivates","concept/pleat-visibility"),("concept/pleat-visibility","motivates","concept/bend-length"),("concept/bend-length","motivates","concept/prop-contacts"),
 ("concept/prop-contacts","motivates","method/outfit-prompt"),("method/outfit-prompt","motivates","method/inpaint-mask"),("method/inpaint-mask","motivates","method/cloth-presets"),("method/cloth-presets","motivates","method/style-detail"),
 ("method/style-detail","motivates","method/garment-diagnosis"),("method/garment-diagnosis","usedIn","application/garment-failures"),("method/outfit-prompt","explains","open/garment-age-drift"),
 ("concept/detail-level","explains","method/style-detail"),("concept/contact-points","explains","concept/prop-contacts"),("concept/wrinkle-wavelength","explains","method/cloth-presets"),
 ("method/shadow-instead-of-line","explains","concept/pleat-visibility"),("analogy/main-roads","explains","concept/big-folds-first"),("analogy/curtain","explains","concept/ease"),
 ("analogy/book-spine","explains","concept/bend-length"),("method/outfit-prompt","usedIn","application/practice"),("method/cloth-presets","usedIn","application/practice")]
REFS = [
 dict(id="date_2018_wrinkles", title="デジタルツールで描く！服のシワと影の描き方", author="ダテナオト", year=2018, note="マイナビ出版. 2장 실례편의 원리(사진에서 주름·그림자를 옮기는 순서, 핏·체형·소재·동작에 따른 주름)를 참고. 책의 사진·그림·문장·도식은 옮기지 않고 연구실 캐릭터와 실험으로 새로 구성"),
 dict(id="cerda_2003_wrinkling", title="Geometry and Physics of Wrinkling", author="E. Cerda, L. Mahadevan", year=2003, note="Physical Review Letters 90, 074302 — 주름 간격이 굽힘 강성의 네제곱근에 비례(간격 ∝ 두께^(3/4))"),
 dict(id="lambert_1760", title="Photometria (Lambert's cosine law)", author="Johann Heinrich Lambert", year=1760, note="면의 밝기·보이는 면 = cos θ. https://en.wikipedia.org/wiki/Lambert%27s_cosine_law"),
 dict(id="baraff_1998_cloth", title="Large Steps in Cloth Simulation", author="David Baraff, Andrew Witkin", year=1998, note="SIGGRAPH 1998 — 무게·뻣뻣함 값으로 천을 계산하는 VFX 천 시뮬레이션의 기초"),
 dict(id="jakobsen_2001_verlet", title="Advanced Character Physics", author="Thomas Jakobsen", year=2001, note="GDC 2001 — 이 페이지 실험의 점과 막대(베를레) 천 계산"),
 dict(id="lugmayr_2022_repaint", title="RePaint: Inpainting using Denoising Diffusion Probabilistic Models", author="Andreas Lugmayr et al.", year=2022, note="CVPR 2022. arXiv:2201.09865 — 가림 영역만 다시 그리는 방식"),
 dict(id="rombach_2022_ldm", title="High-Resolution Image Synthesis with Latent Diffusion Models", author="Robin Rombach et al.", year=2022, note="CVPR 2022. arXiv:2112.10752 — 글 지시로 그림을 만드는 확산 모델(인페인팅 포함)"),
 dict(id="prev_series", title="구조 먼저 보는 캐릭터 그리기 연구실", author="안상선", year=2026, note="앞 시리즈. 구조·빛·주름 기초와 확산 모델·프롬프트 기초. https://adminmrobo.github.io/adminmrobo-structure_first_drawing_lab/"),
]

def kg_block(page, pages):
    nodes = [dict(id="lab:" + i, type=t, label=dict(ko=ko, en=en), page=p, anchor=a, definition=dict(ko=d), source="lab:work/structure_first_drawing_01")
             for i, t, ko, en, p, a, d in KG if p in pages]
    ids = {n["id"] for n in nodes}
    edges = [dict(s="lab:" + s, p=p, o="lab:" + o) for s, p, o in KG_EDGES if "lab:" + s in ids and "lab:" + o in ids]
    raw = dict(version="1.3", page=page, series=SERIES, nodes=nodes, edges=edges)
    ld = {"@context": {"@vocab": "urn:lab:", "skos": "http://www.w3.org/2004/02/skos/core#", "schema": "https://schema.org/"},
          "@graph": [{"@id": "urn:" + n["id"], "@type": n["type"], "skos:prefLabel": [{"@value": n["label"]["ko"], "@language": "ko"}, {"@value": n["label"]["en"], "@language": "en"}],
                      "skos:definition": n["definition"]["ko"], "schema:url": SITE + n["page"] + n["anchor"]} for n in nodes]}
    meta = dict(title=page, series=SERIES, creator=[dict(name="안상선", role="author", affiliation="(주)M-Robo")], date=DATE, version=VER, license="캐릭터·그림 무단 사용 금지")
    J = lambda o: json.dumps(o, ensure_ascii=False).replace("</", "<\\/")
    return f"""<section id="kg"><div class="wrap"><h2>지식 색인 — 이 페이지의 낱말 찾기</h2>
<p class="muted">이 페이지에 나온 개념·방법·비유·쓰임을 모았습니다. 검색하고, "설명 보러 가기"로 본문에 돌아갑니다.</p><div id="kg-mount"></div></div></section>
<section id="export"><div class="wrap"><h2>온톨로지·서지 꾸러미 내려받기</h2>
<p class="muted">지식 색인을 출처와 함께 파일로 내려받습니다. 서지 관리는 BibTeX·RIS, 온톨로지 편집은 Turtle, 그래프 도구는 CSV, 여러 페이지 합치기는 kg.json입니다.</p><div id="export-mount"></div></div></section>
<script type="application/json" id="kg-raw">{J(raw)}</script>
<script type="application/ld+json" id="kg-ld">{J(ld)}</script>
<script type="application/json" id="refs-csl">{J(REFS)}</script>
<script type="application/json" id="page-meta">{J(meta)}</script>
"""

FOOT_LINKS = [("index.html", "목차")] + [(P["file"], f"{P['no']}부") for P in PARTS] + [("practice/index.html", "7부 실전 연습장")]

def footer(pre=""):
    links = " · ".join(f'<a href="{pre}{h}">{E(t)}</a>' for h, t in FOOT_LINKS) + f' · <a href="{REPO}">저장소</a>'
    refs = "".join(f"<tr><td>[{i+1}]</td><td>{E(r['author'])} ({r['year']}). {E(r['title'])}</td><td>{E(r['note'])}</td></tr>" for i, r in enumerate(REFS))
    return f"""<footer><div class="wrap">
<h3>출처·참고</h3>
<div class="tbl"><table><thead><tr><th>#</th><th>자료</th><th>어디에 썼나</th></tr></thead><tbody>{refs}</tbody></table></div>
<h3>예시값·설명용 숫자</h3>
<p>주름 세기, 여유율, 몸 치수, 부드러움 계수, 자국 비율 p, 들림 높이, 소재값, 화풍별 주름 개수, 평가단 점수는 모두 원리를 보이기 위한 예시값입니다. 실제 값은 옷·도구마다 다릅니다.</p>
<p>등장인물은 모두 20대 성인 연구원입니다. 실사풍 그림은 캐릭터를 코스프레한 가상의 성인 모델이며 실존 인물이 아닙니다. 다른 작품의 캐릭터를 닮은 그림은 만들지 않습니다.</p>
<p>캐릭터 이름·설정·그림은 저작권자 안상선의 허락 없이 사용할 수 없습니다. 캐릭터 그림: <a href="{CHARREPO}">fruitfly-lab-expressions</a>.</p>
<p>글 · 안상선 ((주)M-Robo 대표) · <a href="{AUTHOR_URL}">저자 소개</a> · {DATE} · {VER}</p>
<p>{links}</p>
</div></footer>
<script src="{pre}assets/panels.js"></script>
</body></html>
"""

REFS_DL = ["haru_anime_base.png", "sia_anime_base.png", "moa_anime_base.png", "haru_sheet.png", "sia_sheet.png", "moa_sheet.png", "doctor_sheet.png", "fruitfly_sprites_6.png", "jupanbot_ref_genspark_v0.png", "pixel_style_ref_prev_cover.png"]
def make_section(P):
    tasks = MAKE.get(P["no"])
    if not tasks:
        return ""
    refs = " · ".join(f'<a href="assets/refs/{f}" download>{f.replace(".png", "")}</a>' for f in REFS_DL)
    out = f"""<section class="room" id="make"><div class="wrap"><div class="roomno">{P['no']}부 · 직접 만들기</div><h2>프롬프트로 직접 만들어 보기</h2>
<div class="box"><p>이 부에서 배운 원리를 그림 생성 AI(Genspark 등)로 직접 확인합니다. <b>A</b>는 이 페이지 그림을 실제로 만든 프롬프트, <b>B</b>는 원리를 하나 빼거나 바꾼 비교용 문장입니다.</p>
<ol style="margin:6px 0 0;padding-left:20px"><li>새 대화를 열고 아래 '첨부'에 적힌 참고 그림을 올립니다.</li><li>A를 붙여 넣어 만들고, 확인표로 결과를 점검합니다.</li><li>같은 대화에 B를 이어 붙여 다시 만들고, A 결과와 나란히 비교합니다.</li><li>결과는 매번 다릅니다. 두세 번 만들어 가장 나은 것을 고르세요.</li></ol>
<p class="hint" style="margin-top:8px">참고 그림 내려받기: {refs}</p></div>"""
    for i, t in enumerate(tasks, 1):
        A = PROMPTS[t["key"]][4]
        att = ATTACH_OF[CONV_OF[t["key"]]]
        ar = "16/9" if "16:9" in A.split("\n")[0] else "2/3"
        alt = PROMPTS[t["img"]][3]
        chk = "".join(f'<li>{E(c)}' + (f' <a href="{l}">원리 보기</a>' if l else "") + "</li>" for c, l in t["check"])
        bimgs = ""
        if t["b_imgs"]:
            bimgs = '<div class="artrow">' + "".join(art(k, ("비교 결과 — " + t["b_title"]) if k not in PROMPTS else PROMPTS[k][3], ar if not k.startswith(("p1_moa_shadow_step", "p5_haru_inpaint_real", "f2_fixed", "f8_fixed")) else "2/3", "B 결과" if len(t["b_imgs"]) == 1 else f"B 결과 {j}") for j, k in enumerate(t["b_imgs"], 1)) + "</div>"
        tip = f'<p class="hint">{E(t["tip"])}</p>' if t.get("tip") else ""
        if t.get("res"):
            tip = f'<p style="background:#fff7ec;border-left:4px solid var(--orange);padding:8px 12px;border-radius:6px">{E(t["res"])}</p>' + tip
        bbox = f'<div class="promptbox"><b>{E(t["b_title"])}</b><pre>{E(t["b_text"])}</pre><button type="button" class="btn copy">복사하기</button></div>'
        if len(t["b_imgs"]) == 1:
            k = t["b_imgs"][0]
            bpart = f'<div class="pair">{bbox}<div>{art(k, ("비교 결과 — " + t["b_title"]) if k not in PROMPTS else PROMPTS[k][3], "2/3" if k.startswith(("p5_haru_inpaint_real", "f2_fixed")) else ar, "B 결과")}</div></div>'
        else:
            bpart = bbox + bimgs
        out += f"""<div class="failcard" id="make{i}"><h3>실습 {i} · {E(t['title'])}</h3><p>{E(t['goal'])}</p>
<div class="pair"><div class="promptbox"><b>A — 이 페이지 그림을 만든 프롬프트</b><p class="hint">첨부: {E(att)}</p><pre>{E(A)}</pre><button type="button" class="btn copy">복사하기</button></div>
<div>{art(t['img'], alt, ar, "A 결과 — Genspark로 만든 실제 그림")}</div></div>
{bpart}<h4>결과에서 확인할 것</h4><ol>{chk}</ol>{tip}</div>"""
    return out + "</div></section>"

def retry_box(x, pre=""):
    if x["key"] not in RETRY:
        return ""
    gid, verdict, res = RETRY[x["key"]]
    g = [r for r in RETRY_R if r[0] == gid][0]
    imgs = '<div class="artrow">' + "".join(art(k, f"다시 시도한 결과 — {k}", "16/9" if ratio == "16:9" else "2/3", ("다시 시도 · " + step), pre) for k, ratio, att, step, prm in g[3]) + "</div>"
    prompts = "".join(f'<div class="promptbox"><b>{E(k)}</b> <span class="hint">({E(step)} · 첨부: {E(att)})</span><pre>{E(prm)}</pre><button type="button" class="btn copy">복사하기</button></div>' for k, ratio, att, step, prm in g[3])
    return f"""<div class="box" style="border-left:4px solid var(--teal)"><b>다시 시도한 결과 — {E(verdict)}</b>
<p style="margin:6px 0"><b>바꾼 방법:</b> {E(g[2])}</p>{imgs}<p style="margin:8px 0 0">{E(res)}</p>
<details style="margin-top:8px"><summary><b>다시 시도한 프롬프트 보기</b></summary>{prompts}</details></div>""" + retry2_box(x, pre)

def retry2_box(x, pre=""):
    if x["key"] not in RETRY2:
        return ""
    k, title, how, res, prm = RETRY2[x["key"]]
    return f"""<div class="box" style="border-left:4px solid var(--amber,#d97706)"><b>{E(title)}</b>
<p style="margin:6px 0"><b>바꾼 방법:</b> {E(how)}</p><div class="artrow">{art(k, "두 번째 시도 결과 — 팔짱은 꼈지만 팔 쪽으로 끌려가는 주름이 없는 티셔츠", "2/3", "두 번째 시도 · 실패한 그대로", pre)}</div><p style="margin:8px 0 0">{E(res)}</p>
<details style="margin-top:8px"><summary><b>두 번째 시도 프롬프트 보기</b></summary><div class="promptbox"><b>{E(k)}</b> <span class="hint">(새 대화 · 첨부: e6_2_retry_fixed.png + haru_anime_base.png)</span><pre>{E(prm)}</pre><button type="button" class="btn copy">복사하기</button></div></details></div>"""

def exercise_section(no, pre=""):
    xs = EX.get(no)
    if not xs:
        return ""
    def L(l):
        return l if l.startswith("#") or not pre else pre + l
    out = f"""<section class="room" id="exercise"><div class="wrap"><div class="roomno">{no}부 · 연습 문제</div><h2>연습 문제 — 프롬프트로 직접 풀기</h2>
<div class="box"><p>'직접 만들어 보기'가 이 페이지 그림을 다시 만들어 보는 것이었다면, 연습 문제는 <b>새 상황을 스스로 풀어 보는</b> 것입니다. 정답 그림은 하나가 아니므로, 아래 '예상 결과'는 완성 예시 프롬프트로 실제로 만든 한 가지 예입니다.</p>
<ol style="margin:6px 0 0;padding-left:20px"><li><b>원리로 먼저 예상하기</b> — 질문을 읽고 답을 떠올린 뒤 펼쳐 봅니다.</li><li><b>빈자리 채워 쓰기</b> — 틀의 [ ] 안을 내 말로 채워 프롬프트를 씁니다.</li><li><b>완성 예시와 비교</b> — 내 문장과 비교하고, 빠진 조각을 보탭니다.</li><li><b>만들고 확인하기</b> — 그림 생성 AI(Genspark 등)에 참고 그림을 첨부해 만들고, 확인표로 점검합니다.</li><li><b>막히면</b> — 흔한 실패와 고치는 문장을 같은 대화에 이어 붙입니다.</li></ol>
<p class="hint" style="margin-top:8px">참고 그림 내려받기: {" · ".join(f'<a href="{pre}assets/refs/{f}" download>{f.replace(".png", "")}</a>' for f in REFS_DL)}</p></div>"""
    for i, x in enumerate(xs, 1):
        pred = "".join(f'<details style="margin:6px 0"><summary><b>{E(q)}</b></summary><p style="margin:6px 0 0 14px">{E(a)}</p></details>' for q, a in x["predict"])
        chk = "".join(f"<li>{E(c)}" + (f' <a href="{L(l)}">원리 보기</a>' if l else "") + "</li>" for c, l in x["check"])
        stuck = "".join(f'<tr><td>{E(a)}</td><td><code style="white-space:pre-wrap">{E(b)}</code></td></tr>' for a, b in x["stuck"])
        ar = "16/9" if x["ratio"] == "16:9" else "2/3"
        out += f"""<div class="failcard" id="ex{i}"><h3>연습 {i} · {E(x['title'])} <small class="muted" style="font-weight:500">({E(x['level'])})</small></h3><p>{E(x['goal'])}</p>
<h4>① 원리로 먼저 예상하기</h4>{pred}
<h4>② 빈자리 채워 쓰기</h4><div class="promptbox"><pre>{E(x['template'])}</pre></div>
<h4>③ 완성 예시 프롬프트</h4><div class="promptbox"><p class="hint">첨부: {E(x['attach'])}</p><pre>{E(x['prompt'])}</pre><button type="button" class="btn copy">복사하기</button></div>
<h4>④ 예상 결과</h4><div class="pair"><div>{art(x['key'], x['expect'], ar, ("처음 결과 — 완성 예시 프롬프트로 Genspark가 만든 그림" if x['key'] in RETRY else "완성 예시 프롬프트로 Genspark가 만든 실제 그림"), pre)}</div><div class="box" style="background:#fff7ec;border-left:4px solid var(--orange)"><b>이렇게 나오면 성공</b><p style="margin:6px 0 0">{E(x['expect'])}</p>{('<p style="margin:10px 0 0"><b>' + ('처음 결과' if x['key'] in RETRY else '실제로 나온 결과') + '</b> — ' + E(x['res']) + '</p>') if x.get('res') else ''}</div></div>
{retry_box(x, pre)}<h4>⑤ 결과에서 확인할 것</h4><ol>{chk}</ol>
<h4>막히면</h4><div class="tbl"><table><thead><tr><th>증상</th><th>같은 대화에 이어 붙일 문장</th></tr></thead><tbody>{stuck}</tbody></table></div></div>"""
    return out + "</div></section>"

def build_part(P):
    t = f"{SERIES} {P['no']}부 — {P['title']}"
    s = head(t, P["desc"], P["og"], P["file"])
    navl = [(f"#{x['id']}", f"{k+1}단계") for k, x in enumerate(P["steps"])]
    if P.get("fails"): navl += [("#fails", "실패 8종")]
    navl += [("#make", "직접 만들기"), ("#exercise", "연습 문제"), ("#judge", "평가"), ("#sum", "정리"), (P["next"][0], "다음 →")]
    s += nav(navl)
    s += cover(P["cover_key"], P["cover_cap"], P["cover_cast"])
    s += f"""<header class="hero"><div class="wrap"><span class="kicker">{E(P['kicker'])}</span><h1>{E(P['title'])}</h1><p class="lead">{E(P['lead'])}</p>
<p class="byline">글 · 안상선 ((주)M-Robo 대표) · <a href="{AUTHOR_URL}">저자 소개</a> · {DATE} · {VER}</p></div></header>
<section><div class="wrap">{three(*P['three'], ABBR)}</div></section>
<section><div class="wrap"><h2>오늘의 과제</h2>{talk(P['intro'])}{flow_strip(P['no'])}</div></section>
"""
    for k, st in enumerate(P["steps"]):
        s += step(P, k + 1, st)
    if P.get("fails"):
        s += '<section class="room" id="fails"><div class="wrap"><div class="roomno">6부 · 2단계</div><h2>옷 그림 실패 8종 진단</h2><p class="muted">그림마다 증상을 보고 원인을 고른 뒤, 연결된 원리와 고치는 프롬프트 조각을 확인합니다.</p>'
        s += "".join(failcard(f) for f in P["fails"])
        d = P["drift"]
        s += f'<div class="failcard" id="drift"><h3>{E(d["title"])}</h3>' + "".join(f"<p>{E(x)}</p>" for x in d["body"]) + '<p><span class="chip">연결된 원리</span><a href="05_ai_vfx.html#s1">5부 1단계 옷 고정 문장</a></p></div></div></section>'
    s += make_section(P)
    s += exercise_section(P["no"])
    s += judge(P["judge"]) + summary(P) + outro(P)
    s += kg_block(P["file"].replace(".html", ""), [P["file"]])
    s += footer()
    open(os.path.join(ROOT, P["file"]), "w").write(s)

FLOW = [
 (1, "사진을 그림으로", "참고 사진의 주름을 다 옮기면 베낀 그림이 된다", "큰 주름부터·정보량·그림자 순서"),
 (2, "붙는 옷과 헐렁한 옷", "옮기는 순서를 알아도 핏이 다르면 주름 수가 다르다", "여유율·접점·몸의 볼륨"),
 (3, "소재감", "핏이 같아도 니트와 코트는 주름이 다르다", "두께·꺾임·버릇 주름·겹쳐 입기"),
 (4, "움직임과 주름", "서 있는 옷을 움직이는 장면에 쓰면 얼어붙어 보인다", "공기·접힌 뒷면·굽힘·소품"),
 (5, "AI와 VFX로 옷 갈아입히기", "AI와 VFX 도구는 원리를 모른다. 말과 숫자로 정확히 알려 줘야 한다", "옷 문장·가림 영역·소재표·화풍별 양"),
 (6, "실패 사례 실험실", "프롬프트를 써도 옷은 틀릴 수 있다", "진단 순서와 고치는 조각"),
 (7, "실전 연습장", "배운 것을 한 화면에서 함께 다뤄 본다", "피팅룸·소재 실험실·공방·진단"),
]
def flow_strip(cur=None, pre=""):
    files = {P["no"]: P["file"] for P in PARTS}
    files[7] = "practice/index.html"
    cells = []
    for n, t, _, _ in FLOW:
        mark = ' style="border-color:var(--orange);background:var(--orange-soft)"' if n == cur else ""
        cells.append(f'<a href="{pre}{files[n]}"{mark}><b>{n}부</b>{E(t)}</a>')
    return '<div class="flowgrid" style="grid-template-columns:repeat(auto-fit,minmax(130px,1fr));margin-top:16px">' + "".join(cells) + "</div>"

def build_index():
    t = f"{SERIES} — 같은 원리, 다른 옷"
    d = "사진 속 옷을 그림으로 옮기는 순서, 핏·체형·소재·동작에 따라 달라지는 주름을 실험으로 익히고, AI 프롬프트·가림 영역·VFX 천 시뮬레이션으로 옷을 갈아입혀 봅니다. 옷 그림 실패 8종 진단까지."
    s = head(t, d, "og_index.jpg", "index.html")
    s += nav([("#howto", "읽는 법"), ("#parts", "편 목록"), ("#map", "전체 흐름"), ("#cast", "등장인물"), ("#source", "원리와 출처")])
    s += cover("cover_index", "연구실 옷장 · 화가 둘, 모델 셋, 손님 모델 박사, 평가단 셋", [("fruitfly", "e09"), ("haru", "e01"), ("sia", "e13"), ("moa", "e19"), ("jupanbot", "e16")])
    s += f"""<header class="hero"><div class="wrap"><span class="kicker">연구실 특별편 · 그리기와 렌더링 · 두 번째 시리즈</span>
<h1>구조 먼저 그리기 연구실 01<br>옷장 편 — 같은 원리, 다른 옷</h1>
<p class="lead">앞 시리즈에서 몸을 도형으로 잡고, 빛과 주름의 기초를 익혔습니다. 이번에는 옷장을 엽니다. <b>사진 속 옷을 그림으로 옮기는 순서</b>, 딱 맞는 옷과 헐렁한 옷, 니트와 코트, 걷고 앉을 때의 주름을 실험으로 보고, <b>AI와 VFX로 옷을 갈아입혀</b> 봅니다.</p>
<p class="byline">글 · 안상선 ((주)M-Robo 대표) · <a href="{AUTHOR_URL}">저자 소개</a> · {DATE} · {VER}</p></div></header>
<section><div class="wrap">{three("참고 사진에서 주름을 골라 옮기는 순서, 핏·체형·소재·동작이 주름을 바꾸는 원리를 실험으로 익히고, 그 원리를 AI 프롬프트와 VFX 소재값으로 옮깁니다.", "옷은 캐릭터의 인상을 정합니다. 주름이 원리와 어긋나면 옷이 몸과 따로 놀거나, 소재가 바뀌어 보입니다.", "캐릭터 의상 설정, 참고 사진으로 그리기, AI 그림의 의상 바꾸기와 검수, 3D 의상 소재 설정에 씁니다.", ABBR)}</div></section>
<section id="howto"><div class="wrap"><h2>읽는 순서와 시간</h2><div class="box"><ul style="margin:0;padding-left:20px">
<li><b>처음부터 차례로</b>(권장): 부마다 실험을 눌러 보며 20~30분, 전체 3시간 안팎입니다.</li>
<li><b>앞 시리즈를 안 봤다면</b>: <a href="{PREV_SITE}">구조 먼저 보는 캐릭터 그리기 연구실</a>의 2부(빛과 그림자)와 3부(옷 주름)를 먼저 보면 낱말이 편합니다. 안 봐도 읽을 수 있게 다시 설명합니다.</li>
<li><b>손 그림 원리만</b>: 1~4부. <b>AI·VFX가 급하다면</b>: 5부 → 6부 → 7부, 막히는 낱말은 각 단계의 링크로 되짚어 보세요.</li>
<li>각 부 끝의 <b>평가단 채점</b>은 이야기 속 예시 점수입니다. 확인 퀴즈와 실전 연습장 미션으로 스스로 점검하세요.</li></ul></div></div></section>
<section id="parts"><div class="wrap"><h2>편 목록</h2>
<p class="muted">모델은 하루·시아·모아(3·5부에는 박사가 손님 모델), 화가는 주판봇과 초파리, 평가단은 X1·X2·X3, 해설은 박사입니다. 부마다 두 화가가 겨루고 평가단이 점수를 매깁니다.</p>
<div class="cards">
<a class="card" href="01_photo_to_drawing.html">{face("moa","e01")}<span class="n">1부 · 모델 모아</span><h3>사진을 그림으로</h3><p>큰 주름부터, 그림체별 정보량, 그림자 다섯 단계, 어디를 흐리게.</p></a>
<a class="card" href="02_fit.html">{face("haru","e01")}<span class="n">2부 · 모델 하루</span><h3>붙는 옷과 헐렁한 옷</h3><p>여유율, 자세별 접점, 몸의 볼륨과 밑단, 선 대신 그림자.</p></a>
<a class="card" href="03_material.html">{face("moa","e19")}<span class="n">3부 · 모델 모아 · 손님 박사</span><h3>소재감</h3><p>두께와 주름 간격, 마름모 그림자, 버릇 주름, 겹쳐 입기.</p></a>
<a class="card" href="04_motion.html">{face("sia","e13")}<span class="n">4부 · 모델 시아</span><h3>움직이면 주름도 움직인다</h3><p>걸을 때 공기, 주름치마의 뒷면, 굽힘의 길이 차이, 가방과 넥타이.</p></a>
<a class="card" href="05_ai_vfx.html">{face("haru","e19")}<span class="n">5부 · 모델 셋 모두</span><h3>AI와 VFX로 옷 갈아입히기</h3><p>옷 고정 문장, 가림 영역, VFX 소재표, 화풍별 주름의 양.</p></a>
<a class="card" href="06_failure_lab.html">{face("jupanbot","e20")}<span class="n">6부 · 의도적 실패 8종</span><h3>실패 사례 실험실</h3><p>증상 → 원인 → 원리 → 고치는 조각. 옷 그림 진단 순서.</p></a>
<a class="card" href="practice/index.html">{face("x2","e16")}<span class="n">7부 · 마지막 장</span><h3>실전 연습장</h3><p>피팅룸·소재 실험실·옷 문장 공방·진단 데스크를 직접 운영합니다.</p></a>
</div></div></section>
<section id="map"><div class="wrap"><h2>전체 흐름 — 1부부터 7부까지 이어지는 순서</h2>{flow_strip()}
<div class="tbl" style="margin-top:16px"><table><thead><tr><th>부</th><th>제목</th><th>이 부를 배우는 까닭</th><th>핵심</th></tr></thead><tbody>
{''.join(f"<tr><td>{n}</td><td>{E(t)}</td><td>{E(a)}</td><td>{E(b)}</td></tr>" for n, t, a, b in FLOW)}</tbody></table></div>
<p class="muted" style="margin-top:12px">기초부터 보고 싶다면: <a href="{PREV_SITE}">구조 먼저 보는 캐릭터 그리기 연구실(구조·빛·주름·확산 모델)</a> · <a href="{RENDER}">AI 렌더링 연구실</a></p></div></section>
<section id="cast"><div class="wrap"><h2>등장인물</h2><div class="cast-grid">{''.join(f'<div class="who">{face(k, "e01" if k in ("haru","sia","moa") else "e13")}<b>{E(CH[k][0])}</b><span>{E(CH[k][1])}</span></div>' for k in ["doctor","haru","sia","moa","jupanbot","fruitfly","x1","x2","x3"])}</div>
<p class="hint" style="margin-top:10px">모델은 모두 20대 성인 연구원입니다. 원리 실습은 연구실 의상(랩코트·티셔츠·카디건·울 코트·메이드복·셔츠와 조끼)으로 합니다.</p></div></section>
<section id="source"><div class="wrap"><h2>원리와 출처</h2>
<p>1~4부의 그리기 원리(사진에서 주름을 고르는 순서, 그림자를 쌓는 순서, 핏·체형·소재·동작에 따른 주름)는 일반적인 드로잉 원리이며, 다테 나오토의 작법서 『デジタルツールで描く！服のシワと影の描き方』(マイナビ) 2장 실례편을 참고해 정리했습니다. 책의 사진·그림·문장·도식은 옮기지 않았고, 연구실 캐릭터와 직접 움직이는 실험으로 새로 구성했습니다. 책의 학교 교복 예시는 같은 원리를 연구실 의상으로 바꿔 다뤘습니다.</p>
<p>주름 간격 식은 얇은 판의 주름 연구(Cerda·Mahadevan, 2003), 천 시뮬레이션과 가림 영역 다시 그리기는 VFX·확산 모델 연구를 바탕으로 쉽게 풀었습니다(아래 출처). 페이지의 그림 34장(표지 8장은 픽셀아트, 본문은 애니풍·반실사·실사풍)은 Genspark로 만들었습니다. 실험 패널은 모두 페이지 안에서 직접 계산해 그립니다.</p></div></section>
"""
    s += kg_block("index", [P["file"] for P in PARTS] + ["practice/index.html"])
    s += footer()
    open(os.path.join(ROOT, "index.html"), "w").write(s)

def build_practice():
    pre = "../"
    t = f"{SERIES} 7부 — 실전 연습장"
    d = "피팅룸(핏·체형), 소재 실험실(천 시뮬레이션), 옷 문장 공방(프롬프트), 진단 데스크(실패 맞히기) 네 곳을 직접 운영하며 1~6부를 함께 연습합니다."
    s = head(t, d, "og_07.jpg", "practice/index.html", pre)
    s += nav([("#fitting", "피팅룸"), ("#fabric", "소재 실험실"), ("#workshop", "공방"), ("#desk", "진단 데스크"), ("#exercise", "연습 문제"), ("#wrap", "마무리")], pre)
    s += cover("cover_07", "연구실 옷장 조종 책상 · 실전 연습장", [("haru", "e19"), ("doctor", "e16"), ("fruitfly", "e09"), ("jupanbot", "e16")], pre)
    s += f"""<header class="hero"><div class="wrap"><span class="kicker">7부 · 마지막 장</span><h1>실전 연습장</h1>
<p class="lead">네 곳의 작업장을 직접 운영합니다. <span style="color:var(--green)">초록 조작판</span>은 주어진 환경, <span style="color:var(--blue)">파랑 조작판</span>은 내 결정입니다. 미션은 직접 조작해야 판정됩니다.</p>
<p class="byline">글 · 안상선 ((주)M-Robo 대표) · <a href="{AUTHOR_URL}">저자 소개</a> · {DATE} · {VER}</p></div></header>
<section id="practice"><div class="wrap">
<div class="tabs" role="tablist"><button type="button" data-t="fitting">피팅룸</button><button type="button" data-t="fabric">소재 실험실</button><button type="button" data-t="workshop">옷 문장 공방</button><button type="button" data-t="desk">진단 데스크</button></div>
"""
    def sc(id_, title, situ, env, me, missions, back, extra_g1=""):
        ms = "".join(f"<li>{E(m)}</li>" for m in missions)
        bk = " · ".join(f'<a href="{pre}{h}">{E(t)}</a>' for h, t in back)
        return f"""<div class="scene" id="{id_}"><h2>{E(title)}</h2><div class="box"><b>상황</b> — {E(situ)}</div>
<div class="panel"><div class="ph"><b>조작판</b><small>초록 = 환경 · 파랑 = 내 결정</small></div>
<div class="ctrl ctl-env">{env}</div><div class="ctrl ctl-me">{me}</div>
<div class="board" aria-live="polite"></div>
<div class="pair"><div class="g1">{extra_g1}</div><div class="g2"></div></div>
<div class="talk"></div>
<h4>미션</h4><ol class="missions">{ms}</ol></div>
<p class="muted">배운 곳 다시 보기: {bk}</p></div>
"""
    s += sc("fitting", "피팅룸 — 핏과 체형 맞추기", "모델의 몸 치수는 주어집니다. 옷 둘레와 소재, 자세를 정해 원하는 핏과 주름을 만듭니다.",
            '<label>몸 둘레(cm) <input type="range" name="body" min="76" max="100" step="2" value="84"></label><label>앞쪽 볼륨(cm) <input type="range" name="vol" min="0" max="10" step="1" value="4"></label>',
            '<label>옷 둘레(cm) <input type="range" name="cloth" min="76" max="130" step="2" value="92"></label><label>소재 <select name="mat"><option value="knit">니트(부드러움 1.5)</option><option value="jersey" selected>저지 티셔츠(1.2)</option><option value="shirt">면 셔츠(1)</option><option value="coat">울 코트(0.5)</option></select></label><label>자세 <select name="pose"><option value="stand">차렷</option><option value="up">팔 올리기</option><option value="cross">팔짱</option></select></label>',
            ["여유율 25~40%의 오버핏 만들기", "밑단이 3cm 이상 올라가게 하기(볼륨과 자세)", "울 코트로 바꿔 예상 주름 수 3개 이하 만들기"],
            [("02_fit.html#s1", "2부 1단계 여유율"), ("02_fit.html#s3", "2부 3단계 몸의 볼륨"), ("03_material.html#s4", "3부 4단계 겹쳐 입기")])
    s += sc("fabric", "소재 실험실 — 천 걸어 보기", "천 한 장을 고리에 걸어 소재별 주름을 만듭니다. 바람은 주어지고, 소재값과 거는 방식은 내가 정합니다.",
            '<label>바람 <input type="range" name="wind" min="0" max="100" step="10" value="0"></label>',
            '<label>무게 <input type="range" name="wt" min="10" max="100" step="10" value="40"></label><label>뻣뻣함 <input type="range" name="stiff" min="0" max="100" step="10" value="20"></label><label>고정점 간격 <input type="range" name="gap" min="40" max="100" step="10" value="70"></label><label><input type="checkbox" name="gather"> 한곳에 모으기</label>',
            ["두 점으로 걸어 가운데 처짐 4 이상 만들기", "무게 그대로 뻣뻣함만 70 이상으로 올려 가운데 처짐을 4 미만으로 줄이기", "모으기 + 뻣뻣함 30 이하로 주름 굴곡 3개 이상 만들기"],
            [("03_material.html#s1", "3부 1단계 두께와 간격"), ("05_ai_vfx.html#s3", "5부 3단계 VFX 소재표")])
    s += sc("workshop", "옷 문장 공방 — 요청서 조립", "요청 상황에 맞춰 옷 문장을 조립합니다. 점검표 6항목을 채우고, 상황에 꼭 필요한 항목을 넣습니다.",
            '<label>요청 상황 <select name="job"><option value="swap">옷 바꿔 입히기(핏·소재 중요)</option><option value="action">동작 장면(동작·주름 중요)</option><option value="goods">굿즈 그림(화풍 양·금지 중요)</option></select></label>',
            '<div class="ow" style="width:100%"></div>',
            ["점검표 6 / 6 채우기", "헐렁한 핏 + 팔 올리기로 '밑단이 올라간다' 문장 넣기", "울 코트를 고르고 금지 목록에 잔주름 금지가 들어가는지 확인"],
            [("05_ai_vfx.html#s1", "5부 1단계 옷 고정 문장"), ("05_ai_vfx.html#s4", "5부 4단계 화풍별 양")],
            '<div class="promptbox"><b>조립된 옷 문장</b><pre aria-live="polite"></pre><button type="button" class="btn copy">복사하기</button></div>')
    s += sc("desk", "진단 데스크 — 원인 맞히기", "옷 그림 실패의 증상이 하나씩 들어옵니다. 원인을 고르세요. 순서: 접점·흐름 → 핏 → 소재 → 빛 → 정보량·가림.",
            '<span class="hint">환경: 증상은 무작위로 들어옵니다.</span>',
            '<div style="width:100%"><p class="sym" style="font-weight:600"></p><div class="opts deskopts"></div></div>',
            ["3개 연속 정답", "8종 원인을 모두 한 번 이상 맞히기", "틀리지 않고 5개 맞히기"],
            [("06_failure_lab.html#s1", "6부 진단 순서"), ("06_failure_lab.html#fails", "6부 실패 8종")])
    s += f"""</div></section>
"""
    s += exercise_section(7, pre)
    s += f"""<section id="wrap"><div class="wrap"><h2>마무리 — 네 작업장을 하나로 묶으면</h2>
<div class="box"><p>피팅룸에서 정한 여유율과 자세는 공방의 옷 문장에서 '핏'과 '동작·접점'이 되고, 소재 실험실의 값은 '소재' 문장과 VFX 소재표가 됩니다. 진단 데스크에서 틀린 원인은 대부분 앞의 세 곳 중 하나가 빠진 경우입니다. 옷 그림은 결국 <b>천이 어디에 걸려(접점), 얼마나 남아서(핏), 어떻게 접히는가(소재·동작)</b>의 기록입니다.</p>
<p><b>실제 그림으로 이어 가기</b> — 옷 문장 공방에서 조립한 문장을 복사해 그림 생성 AI에 넣어 보세요. 결과는 각 부의 '프롬프트로 직접 만들어 보기' 확인표로 점검합니다: <a href="{pre}01_photo_to_drawing.html#make">1부</a> · <a href="{pre}02_fit.html#make">2부</a> · <a href="{pre}03_material.html#make">3부</a> · <a href="{pre}04_motion.html#make">4부</a> · <a href="{pre}05_ai_vfx.html#make">5부</a> · <a href="{pre}06_failure_lab.html#make">6부</a></p>
<p class="hint">한계: 이 연습장의 주름 수·밑단 높이·천 계산은 원리를 보이기 위해 크게 단순화했습니다. 숫자는 교육용 예시이며, 실제 옷과 도구의 값과 다릅니다.</p></div>
<div class="next"><a href="{pre}06_failure_lab.html">← 6부 실패 사례 실험실</a><a href="{pre}index.html">목차로</a></div></div></section>
"""
    s += kg_block("practice_index", ["practice/index.html"])
    s += footer(pre)
    open(os.path.join(ROOT, "practice", "index.html"), "w").write(s)

if __name__ == "__main__":
    JS = ["js_base.js", "js_cloth.js", "js_parts.js", "js_practice_util.js", "js_tail.js"]
    open(os.path.join(ROOT, "assets", "panels.js"), "w").write("".join(open(os.path.join(ROOT, "build", f)).read() for f in JS))
    build_index()
    for P in PARTS:
        build_part(P)
    build_practice()
    print("built", len(PARTS) + 2, "pages")


# ── 분야 뼈대 다시 걸기 (kg/rehang.json, ai-lab-retrofit 15장) ──
# 빌드가 페이지를 다시 쓴 뒤, 덧씌우기를 kg-raw·kg-ld에 다시 적용한다. 파일이 없으면 아무것도 하지 않는다.
if __name__ == "__main__":
    import os as _os, sys as _sys, subprocess as _sp
    _r = _os.path.dirname(_os.path.abspath(__file__))
    for _i in range(3):
        if _os.path.exists(_os.path.join(_r, "kg", "rehang.json")): break
        _r = _os.path.dirname(_r)
    if _os.path.exists(_os.path.join(_r, "kg", "rehang.json")):
        _sp.run([_sys.executable, _os.path.join(_r, "kg", "rehang.py"), "apply", _r])
