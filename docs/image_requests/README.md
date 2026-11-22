# 그림 요청 꾸러미 — 구조 먼저 그리기 연구실 01 · 옷장 편

저장소: `adminmrobo/structure_first_drawing_lab_01` (페이지는 완성 — 그림 자리는 '그림 준비 중'으로 비어 있음)
만드는 도구: Genspark 이미지 · 받은 그림은 zip으로 돌려주시면 됩니다(대화 단위로 나눠 여러 번 주셔도 됩니다).

## 1. 이번 시리즈의 그림 규칙
| 항목 | 규칙 |
|---|---|
| 그림체 | **표지 8장은 16비트 픽셀아트**. **본문 그림은 애니풍(일부 반실사·실사풍)** — 이 시리즈 예외 |
| 배경 | 흰색·밝은 낮 분위기 (밤·네온 금지) |
| 캐릭터 고정값 | `refs/`의 설정 시트·앞 시리즈 애니풍 기준 전신과 같게. 하루: 정수리 번 2개 + 앞머리 가운데 남색 줄 / 시아: 흑발·머리 장식 없음 / 모아: 흰 프릴 머리띠 + **왼쪽** 귀 위 흰 리본 / 박사: 흰 줄 있는 짙은 머리, 굵은 눈썹, 청록 사각 안경 |
| 나이·노출 | 모두 20대 성인(박사는 성인 남성, 본문 그림에서는 꼬마 체형 아님). 노출·과장된 체형·**교복 느낌 금지** |
| 글자 | 그림 안에 글자·숫자·로고 금지 |
| 유명 캐릭터 | 실존 애니 캐릭터 이름·디자인을 넣지 않음. 닮아 보이면 다시 생성 |
| 실사풍 | 캐릭터를 코스프레한 **가상의 성인 모델**. 실존 인물과 닮으면 다시 생성 |

## 2. 등장인물 역할
- **모델:** 인턴2 모아(1·3부), 조수 하루(2부), 인턴1 시아(4부), 5부는 셋 모두 / **손님 모델:** 박사(3·5부, 셔츠·조끼·넥타이)
- **화가:** 주판봇(성급한 화가), 초파리 연구원(원리부터 보는 화가) · **평가단:** X1·X2·X3 · **해설:** 박사

## 3. 요청 순서 (Genspark 대화 하나 = 파일 하나)
| 순서 | 파일 | 그림 수 | 비율 | 첨부할 참고 그림 |
|---|---|---|---|---|
| 1 | `prompts/C01_covers_A.md` | 4 | 16:9 픽셀 | refs 전부 |
| 2 | `prompts/C02_covers_B.md` | 4 | 16:9 픽셀 | refs 전부 + C01의 cover_index |
| 3 | `prompts/C03_part1_photo.md` | 2 | 16:9 | moa_anime_base, moa_sheet |
| 4 | `prompts/C04_part2_fit.md` | 3 | 16:9·2:3 | haru_anime_base, haru_sheet |
| 5 | `prompts/C05_part3_material.md` | 3 | 16:9·2:3 | moa_anime_base, doctor_sheet |
| 6 | `prompts/C06_part4_motion.md` | 3 | 2:3·16:9 | sia_anime_base, doctor_sheet |
| 7 | `prompts/C07_part5_ai_vfx.md` | 3 | 16:9 | 세 사람 anime_base |
| 8 | `prompts/C08_part5_styles.md` | 4 | 2:3 | sia_anime_base, sia_sheet |
| 9 | `prompts/C09_fail_A.md` | 4 | 2:3 | 해당 캐릭터 anime_base |
| 10 | `prompts/C10_fail_B.md` | 4 | 2:3 | 해당 캐릭터 anime_base |

합계 **34장**. 앞 시리즈에서 확정한 애니풍 기준 전신(`refs/*_anime_base.png`)이 이번 본문 그림의 기준입니다. 새로 기준을 만들 필요가 없습니다.

## 4. 저장 이름
`checklist.csv`의 `file` 열 이름 그대로 저장해 주세요(확장자 png 또는 jpg). 이름만 맞으면 제가 크기 변환·WebP·페이지 반영을 합니다.

## 5. 고칠 때 (같은 대화에서)
`Same character, same style and composition. Change only: {고칠 점}. Still no text.`

## 6. 돌려주는 법
- `checklist.csv`의 이름 그대로 저장해 zip으로 주세요. 한 번에 어려우면 대화 단위(C01~C10)로 나눠 주셔도 됩니다.
- 받으면 `assets/img/{이름}.webp`로 넣고 다시 빌드합니다. 표지가 들어오면 공유 미리보기(og)도 표지에서 다시 만듭니다.
