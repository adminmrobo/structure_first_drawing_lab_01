# 재요청 — 연습 문제 실패·부분 성공 5건 (그림 7장)

성공한 그림은 그대로 둡니다. 실패한 그림도 페이지에 '처음 결과'로 남기고, 아래 재시도 결과를 '다시 시도한 결과'로 나란히 싣습니다.

**Genspark에 먼저 붙여 넣기 ↓**
```
해설 페이지의 연습 문제 그림을 다시 만들어 줘(재시도).
- 첨부한 참고 그림의 캐릭터 외형(얼굴·머리·색·장식)을 똑같이 지킬 것
- 등장인물은 모두 20대 성인(박사는 성인 남성). 노출·교복 느낌 금지
- 그림 안에 글자·숫자·로고 금지
- 'Change only'가 있으면 그것만 바꾸고 나머지는 첨부 그림과 같게
```

---
# R01 · 1부 연습 2 — 정보량 두 가지(한 장에 두 화풍이 안 됨)
두 화풍을 한 장에 요청하지 않고, 같은 자세를 두 번 따로 만듭니다. ①을 먼저 만든 뒤 **새 대화**에서 ①의 결과를 첨부해 ②를 만듭니다.

## e1_2_retry_simple (2:3) — ① 새 대화
첨부: refs/haru_anime_base.png
```
Illustration, vertical 2:3.
Art style: high-quality anime illustration, clean confident lineart, two-tone cel shading with a darker second shadow only in the deepest folds, natural adult proportions.
Match the attached reference images exactly (face, hair, colors, accessories). All characters are adults in their early twenties (the Professor is an adult man); modest outfits exactly as described.
Full body of Haru (adult lab assistant, long straight pink hair with navy streaks and a thick navy streak down the center of the bangs, two round hair buns on top, small ahoge, big blue eyes), wearing lavender hoodie with white drawstrings over a white t-shirt, open white knee-length lab coat, rolled-up jeans, lavender sneakers, standing with hands in the hoodie pocket, weight on one leg.
Art style override: very SIMPLE flat anime style — thick clean outlines, flat colors, only 2–3 large folds (elbows and below the shoulders), 2-tone shading, NO small wrinkles, NO seam lines, NO texture. Light from the upper left.
Plain off-white studio background.
No text, no letters, no numbers, no logos, no watermark, no revealing clothing, not childlike, no school uniform, not resembling any famous anime character.
```

## e1_2_retry_semireal (2:3) — ② 새 대화
첨부: e1_2_retry_simple(방금 만든 ①) + refs/haru_anime_base.png
```
Illustration, vertical 2:3.
Art style: high-quality anime illustration, clean confident lineart, two-tone cel shading with a darker second shadow only in the deepest folds, natural adult proportions.
Match the attached reference images exactly (face, hair, colors, accessories). All characters are adults in their early twenties (the Professor is an adult man); modest outfits exactly as described.
Same character, same pose, same framing and same outfit as the attached image.
Art style override: SEMI-REALISTIC 2.5D digital painting — realistic fabric texture, 6–8 folds including many small wrinkles, visible seams and stitching, folds pooling at the cuffs, soft gradient shading with reflected light. The fold POSITIONS stay the same as in the attached image; only the amount of detail increases. Light from the upper left.
Plain off-white studio background.
No text, no letters, no numbers, no logos, no watermark, no revealing clothing, not childlike, no school uniform, not resembling any famous anime character.
```

---
# R02 · 2부 연습 1 — 박사 티셔츠가 덜 헐렁함
앞서 받은 그림을 첨부하고 'Change only' 한 문장으로 헐렁함만 키웁니다.

## e2_1_retry (2:3) — 같은 대화 또는 새 대화에 첨부
첨부: e2_1_doctor_loose_tee_arms_up.png(앞서 받은 그림) + refs/doctor_sheet.png
```
Same image, same man, same pose with both arms raised. Change only: the t-shirt is clearly OVERSIZED, about two sizes too big — dropped shoulder seams far down the upper arms, very wide sleeves, and large soft drape folds hanging under the armpits and across the chest; the hem rides up only slightly. Adult man in his thirties, normal proportions (not chibi). Still no text, no logos.
```

---
# R03 · 2부 연습 2 — 시아 후드티 빛이 약함
앞서 받은 그림을 첨부하고 빛만 세게 바꿉니다.

## e2_2_retry (2:3) — 같은 대화 또는 새 대화에 첨부
첨부: e2_2_sia_hoodie_light_right.png(앞서 받은 그림) + refs/sia_anime_base.png
```
Same image, same character and pose. Change only: STRONG directional sunlight from the UPPER RIGHT (a bright window at the upper right). Clear cel shadows: the left side of her face, neck and body is in shadow; every fold on the hoodie has a soft gray-lavender shadow on its LOWER LEFT side, and the right sides of the folds are brightly lit. Keep most small folds without lines. Still no text, no logos.
```

---
# R04 · 6부 연습 2 — 팔짱 실패가 재현되지 않음
'틀리게 그려라'는 요청은 도구가 고쳐 버립니다. 그래서 ① 팔을 내린 그림(세로 주름)을 먼저 만들고, ② **부분 수정 기능**으로 팔만 칠해 팔짱으로 바꾸면서 티셔츠는 손대지 않게 합니다. 그러면 '옷과 팔이 따로 노는' 실패가 저절로 생깁니다. ③은 고친 그림으로 새로 만듭니다.

## e6_2_retry_fail (2:3) — ① 생성 → ② 부분 수정
첨부: refs/haru_anime_base.png (①은 그림 생성, ②는 부분 수정 기능)
```
① Illustration, vertical 2:3.
Art style: high-quality anime illustration, clean confident lineart, two-tone cel shading with a darker second shadow only in the deepest folds, natural adult proportions.
Match the attached reference images exactly (face, hair, colors, accessories). All characters are adults in their early twenties (the Professor is an adult man); modest outfits exactly as described.
Upper body of Haru (adult lab assistant, long straight pink hair with navy streaks and a thick navy streak down the center of the bangs, two round hair buns on top, small ahoge, big blue eyes), wearing a plain white t-shirt and rolled-up jeans (no lab coat, no hoodie), standing with both arms hanging relaxed at her sides. The t-shirt shows only straight vertical folds falling from the shoulders.
Light from the upper left.
Plain off-white studio background.
No text, no letters, no numbers, no logos, no watermark, no revealing clothing, not childlike, no school uniform, not resembling any famous anime character.

② (부분 수정: 두 팔과 손만 칠하기 — 티셔츠 몸판은 칠하지 않음)
Cross her arms in front of her chest. Do NOT change the t-shirt at all: keep its straight vertical folds exactly as they are.
```

## e6_2_retry_fixed (2:3) — ③ 새 대화
첨부: refs/haru_anime_base.png
```
Illustration, vertical 2:3.
Art style: high-quality anime illustration, clean confident lineart, two-tone cel shading with a darker second shadow only in the deepest folds, natural adult proportions.
Match the attached reference images exactly (face, hair, colors, accessories). All characters are adults in their early twenties (the Professor is an adult man); modest outfits exactly as described.
Upper body of Haru (adult lab assistant, long straight pink hair with navy streaks and a thick navy streak down the center of the bangs, two round hair buns on top, small ahoge, big blue eyes), wearing a plain white t-shirt and rolled-up jeans (no lab coat, no hoodie), arms crossed in front of her chest. The t-shirt folds are clearly pulled toward where the crossed arms press against the torso: diagonal tension folds from both shoulders to the forearms, gathered folds inside both bent elbows, and the fabric bunched slightly above the crossed arms.
Light from the upper left.
Plain off-white studio background.
No text, no letters, no numbers, no logos, no watermark, no revealing clothing, not childlike, no school uniform, not resembling any famous anime character.
```

---
# R05 · 7부 연습 2 — 모아가 니트 스웨터를 안 입음
앞서 받은 그림을 첨부하고 모아의 옷만 바꿉니다. 고정값(머리띠·왼쪽 리본)은 지키되 옷은 바꾼다는 것을 분명히 적습니다.

## e7_2_retry (16:9) — 같은 대화 또는 새 대화에 첨부
첨부: e7_2_trio_three_fabrics.png(앞서 받은 그림) + refs/moa_anime_base.png
```
Same image, same three characters, same positions and lighting. Change only Moa (left): she wears a thick camel CHUNKY KNIT SWEATER (turtleneck or crew neck) and a black skirt — NO cardigan, NO blouse, NO bow tie, NO apron this time. The knit has broad rounded folds and rounded soft shadows. She KEEPS her long ash-beige wavy hair, the white frilled headband and the white ribbon over her LEFT ear. Haru and Sia stay exactly the same. Still no text, no logos.
```

---
## 저장 이름
`checklist.csv`의 이름 그대로(png·jpg). 재시도도 실패하면 그대로 주셔도 됩니다 — 두 번째 결과로 함께 싣습니다.
