# -*- coding: utf-8 -*-
"""Genspark 그림 요청 꾸러미(docs/image_requests) 생성. python3 build/make_requests.py"""
import os, csv
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, "docs", "image_requests")
PIX = "Art style (required, always): 16-bit RPG style pixel art with clearly visible square pixels, limited palette, bold dark outline, 2–3 tone shading, small highlights; no smooth gradients, no painterly, vector, watercolor or 3D look.\nMatch the characters' proportions and colors of the attached reference images exactly, drawn in this same pixel-art style.\nBright daytime laboratory mood, soft natural sunlight through large windows, clean white walls, light lavender, mint and pink accents."
ANI = "Art style: high-quality anime illustration, clean confident lineart, two-tone cel shading with a darker second shadow only in the deepest folds, natural adult proportions.\nMatch the attached reference images exactly (face, hair, colors, accessories). All characters are adults in their early twenties (the Professor is an adult man); modest outfits exactly as described."
END = "No text, no letters, no numbers, no logos, no watermark, no revealing clothing, not childlike, no school uniform, not resembling any famous anime character."
ENDC = "No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands."
SAFE = "Composition: every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); bottom-left corner plain and bright."
CH = {
 "haru": "Haru (adult lab assistant, long straight pink hair with navy streaks and a thick navy streak down the center of the bangs, two round hair buns on top, small ahoge, big blue eyes)",
 "sia": "Sia (adult maid intern, long straight jet-black hair, no headdress, gray eyes, small silver earrings)",
 "moa": "Moa (adult maid intern, long ash-beige wavy hair, white frilled maid headband with a white ribbon over her LEFT ear, amber eyes)",
 "doctor": "the Professor (adult male scientist, dark charcoal spiky hair with a white streak at the front, very thick black eyebrows, teal rectangular glasses)",
 "fly": "the Fruit Fly researcher (tiny cartoon fruit fly, large red compound eyes, retro dark blue helmet with a yellow-white stripe, colorful dangling cables, tiny white lab coat, translucent wings)",
 "bot": "AbaBot (boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes, short antenna topped with a red-brown abacus bead, gray segmented arms, small tank treads)",
 "judges": "three small cute dark navy silhouette judges with white dot eyes (one with a pink side-ponytail bow, one with a beret and teal round glasses, one with a cat-ear hood and yellow pompoms) holding blank score paddles",
}
OUT = {"haru": "lavender hoodie with white drawstrings over a white t-shirt, open white knee-length lab coat, rolled-up jeans, lavender sneakers",
       "sia": "charcoal-black long-sleeved maid dress, large gray bow at the collar, long white frilled apron",
       "moa": "camel knit cardigan over a white blouse, red and navy plaid bow tie, white frilled apron, black skirt",
       "doctor": "white lab coat over a black vest, white shirt and black tie"}
def who(k, outfit=None): return CH[k] + ", wearing " + (outfit or OUT[k])
CONV = []  # (id, title, ratio, attach, items[(file, page, part, alt, prompt, style)])
def cover(file, page, part, alt, scene, chars, meta, mood):
    p = f"Website top cover illustration, wide 16:9.\n{PIX}\nScene: {scene}\nCharacters:\n  " + ";\n  ".join(chars) + f".\nVisual metaphor: {meta}\n{SAFE}\nMood: {mood}\n{ENDC}"
    return (file, page, part, alt, p, "pixel")
def body(file, page, part, alt, ratio, scene, extra=""):
    p = ("Illustration, " + ("vertical 2:3." if ratio == "2:3" else "wide 16:9.") + f"\n{ANI}\n{scene}\n" + (extra + "\n" if extra else "") + "Plain off-white studio background or a bright clean lab interior.\n" + END)
    return (file, page, part, alt, p, "anime")
C1 = [
 cover("cover_index", "index.html", "목차", "낮의 연구실 옷장 앞에서 하루·시아·모아가 옷을 대 보고, 초파리와 주판봇이 이젤 앞에, 박사가 셔츠 차림으로, 평가단이 뒤에 앉은 장면",
   "a sunny corner of the laboratory turned into a dressing room: an open wooden wardrobe full of clothes on hangers (t-shirts, a knit cardigan, a wool coat, a maid dress, a dress shirt), a full-length mirror, two easels with canvases seen from the back, a clothes rail.",
   [who("haru") + ", in the center holding a plain white t-shirt up against herself", who("sia") + ", holding a folded camel wool coat", who("moa") + ", standing in front of the mirror",
    who("doctor", "light blue dress shirt with sleeves rolled up, gray vest and black tie") + ", at the back center holding a clipboard", CH["fly"] + ", on the left facing right at the left easel", CH["bot"] + ", on the right facing left at the right easel", CH["judges"] + " sitting at a small table in the back right"],
   "the same white t-shirt shown on a hanger and held up on Haru — same garment, different fit.", "cheerful, friendly rivalry, the moment before the fitting starts."),
 cover("cover_01", "01_photo_to_drawing.html", "1부 사진을 그림으로", "모아가 카디건 차림으로 사진 촬영 자세를 하고, 초파리가 사진 출력물 위에 큰 주름 세 개를 색 펜으로 표시하는 장면",
   "a small photo corner in the lab studio: a camera on a tripod, a softbox light, a printed photo pinned to a board.",
   [who("moa") + ", posing in the center with one elbow bent", CH["fly"] + ", on the left facing right, marking three big curved lines on the pinned printed photo with a teal marker", CH["bot"] + ", on the right facing left, holding a huge stack of tiny marker lines and looking overwhelmed", who("doctor") + ", at the back pointing at the board"],
   "only three big lines chosen out of many on the printed photo.", "curious, focused."),
 cover("cover_02", "02_fit.html", "2부 붙는 옷과 헐렁한 옷", "하루가 딱 맞는 흰 티셔츠와 헐렁한 흰 티셔츠를 양손에 들고, 주판봇과 초파리가 줄자로 둘레를 재는 장면",
   "a fitting room in the lab with a curtain, a tape measure, a clothes rail.",
   [who("haru", "white t-shirt and rolled-up jeans, lab coat hung on a hook") + ", in the center holding a fitted white t-shirt in one hand and a loose oversized white t-shirt in the other", CH["fly"] + ", on the left facing right, holding one end of a long yellow tape measure", CH["bot"] + ", on the right facing left, holding the other end of the tape measure", who("doctor") + ", at the back nodding"],
   "two t-shirts of the same color but different widths.", "playful, bright."),
 cover("cover_03", "03_material.html", "3부 소재감", "모아가 니트 카디건과 두꺼운 울 코트를 번갈아 걸쳐 보고, 박사가 셔츠와 조끼 차림으로 소매를 걷는 장면",
   "the lab wardrobe with fabric swatches pinned on a board (knit, cotton, wool, silk).",
   [who("moa", "thick camel wool coat over her outfit") + ", in the center bending one elbow", who("doctor", "light blue dress shirt with sleeves rolled up, gray vest and black tie") + ", on the right side rolling up his sleeve", CH["fly"] + ", on the left facing right, holding a magnifying glass to a fabric swatch", CH["bot"] + ", at the back right, holding a silk scarf that drapes into many fine folds"],
   "a thick coat with a few broad folds next to a light scarf with many fine folds.", "calm, curious."),
]
C2 = [
 cover("cover_04", "04_motion.html", "4부 움직임과 주름", "시아가 메이드복 차림으로 복도를 걸어가며 앞치마 밑단이 뒤로 물결치고, 초파리가 바람개비를 들고 따라가는 장면",
   "a long bright lab corridor with large windows.",
   [who("sia") + ", walking to the right in mid-stride, the skirt and apron hem flowing backward", CH["fly"] + ", flying behind her holding a small pinwheel that spins", CH["bot"] + ", on the left rolling along carrying a shoulder bag for her", who("doctor") + ", at the far end holding a stopwatch"],
   "fabric that moves one beat after the body.", "lively, gentle breeze."),
 cover("cover_05", "05_ai_vfx.html", "5부 AI와 VFX로 옷 갈아입히기", "하루·시아·모아가 서로 옷을 바꿔 입고, 큰 모니터에 천 시뮬레이션 격자가 떠 있는 장면",
   "the lab control desk with a big monitor showing a simple grid of cloth hanging from two pins, and a second monitor showing a character silhouette with only the clothing area highlighted.",
   [who("haru", "camel knit cardigan over a white blouse with rolled-up jeans") + ", in the center", who("sia", "loose white t-shirt and an open white lab coat, black skirt") + ", on the left", who("moa", "charcoal-black long-sleeved maid dress with a long white frilled apron") + " (she keeps her white frilled headband and the ribbon over her LEFT ear), on the right", CH["bot"] + ", typing at the desk", CH["fly"] + ", hovering near the monitor"],
   "the same three people, swapped outfits.", "fun, surprised."),
 cover("cover_06", "06_failure_lab.html", "6부 실패 사례 실험실", "옷 그림 실패작이 쌓인 책상에서 초파리가 돋보기로 살펴보고, 주판봇이 머리를 긁는 장면",
   "a work table piled with crumpled drawings of clothes, a few drawings pinned on a board with red circles (drawn as simple shapes only, no readable text).",
   [CH["fly"] + ", in the center holding a big magnifying glass over a drawing", CH["bot"] + ", on the right facing left, scratching its head", CH["judges"] + " on the left holding blank paddles", who("doctor") + ", at the back pointing at the board"],
   "finding the exact spot where a drawing went wrong.", "detective-like, friendly."),
 cover("cover_07", "practice/index.html", "7부 실전 연습장", "하루가 옷장 조종 책상 앞에 앉아 화면 네 개(피팅룸·천·문장·진단)를 다루고, 박사가 뒤에서 지켜보는 장면",
   "the lab control desk with four small monitors showing simple icons: a t-shirt outline, a hanging cloth grid, a speech-bubble shape, a magnifying glass (icons only, no text).",
   [who("haru") + ", sitting at the desk in the center operating the controls — Haru with pink hair and two hair buns must be the one in the chair", who("doctor") + ", standing behind her with arms crossed, smiling", CH["fly"] + ", on the left", CH["bot"] + ", on the right"],
   "four workshops controlled from one desk.", "confident, final chapter."),
]
C3 = [
 body("p1_moa_photo_vs_drawing", "01_photo_to_drawing.html", "1부 1단계", "왼쪽에 카디건을 입은 모아의 실사풍 사진, 오른쪽에 같은 자세의 애니풍 그림, 가운데 그림 위에 큰 주름 세 개만 색 선으로 표시된 비교", "16:9",
   "A side-by-side comparison in three panels of the same pose: LEFT a photorealistic studio photo of a fictional adult model in her early twenties cosplaying Moa; CENTER the anime version with only three big folds highlighted by thick teal lines (one at the bent left elbow, one diagonal from the shoulder, one hanging at the waist); RIGHT the finished anime illustration.\n" + who("moa") + ", standing in three-quarter view, left elbow bent with the hand near the chest.",
   "The photo panel shows many small natural wrinkles; the drawing panels keep only the large folds. Not resembling any real celebrity."),
 body("p1_moa_shadow_steps", "01_photo_to_drawing.html", "1부 3단계", "모아의 상반신 채색이 떨어지는 그림자, 입체 그림자, 섬 그림자, 진한 2차 그림자, 완성의 다섯 단계로 나란히 바뀌는 그림", "16:9",
   "Five small panels in a row showing the same upper-body drawing of Moa getting shadows step by step, light from the upper left: 1) cast shadows only (under the chin and under the collar, under the sleeves), 2) plus large form shadows on the right side, 3) plus small floating island shadows on the cardigan folds, 4) plus a darker second shadow only in the deepest creases, 5) the clean finished image.\n" + who("moa") + ".",
   "Each panel separated by a thin gap, same framing, no numbers or labels."),
]
C4 = [
 body("p2_haru_tee_fit_compare", "02_fit.html", "2부 1단계", "같은 자세의 하루가 왼쪽은 몸에 맞는 흰 티셔츠, 오른쪽은 헐렁한 흰 티셔츠를 입은 비교", "16:9",
   "Two full-body figures of the same person side by side in the same relaxed standing pose: LEFT wearing a fitted plain white crew-neck t-shirt (close to the body, only a few thin tension folds), RIGHT wearing a loose oversized plain white t-shirt (dropped shoulder seams, large soft drape folds hanging from the shoulders).\n" + who("haru", "plain white t-shirt, rolled-up jeans, lavender sneakers (no lab coat, no hoodie)") + ".",
   "Light from the upper left, fold shadows on the lower right side of each fold."),
 body("p2_haru_tee_poses", "02_fit.html", "2부 2단계", "흰 티셔츠를 입은 하루가 팔 올리기, 팔짱, 허리 젖히기, 밑단 잡기의 네 자세를 한 그림", "16:9",
   "Four small upper-body panels of the same person in a plain white t-shirt: 1) both arms raised above the head (folds gather at the shoulders, the hem rides up, the belly area is smooth), 2) arms crossed (folds pulled toward the arms), 3) leaning back slightly (folds from chest and armpits toward the waist), 4) pinching the hem with one hand (diagonal tension folds from the shoulder to the fingers).\n" + who("haru", "plain white t-shirt and rolled-up jeans (no lab coat, no hoodie)") + ".",
   "Same framing in each panel, light from the upper left, no labels."),
 body("p2_haru_loose_tee_shading", "02_fit.html", "2부 4단계", "헐렁한 흰 티셔츠를 입은 하루의 상반신, 주름을 선 없이 연보라 그림자만으로 표현하고 왼쪽 위에서 빛이 오는 그림", "2:3",
   "Upper body of the character in a loose oversized white t-shirt, one hand resting on her head. Most small folds are drawn WITHOUT lines, only as soft lavender island shadows on the lower right side of each fold ridge; only three large folds keep a thin line.\n" + who("haru", "loose plain white t-shirt and rolled-up jeans (no lab coat, no hoodie)") + ".",
   "Light clearly from the upper left."),
]
C5 = [
 body("p3_moa_knit_vs_coat", "03_material.html", "3부 1단계", "같은 자세로 팔을 굽힌 모아가 왼쪽은 니트 카디건(잔주름 여러 개), 오른쪽은 두꺼운 울 코트(굵은 주름 몇 개)를 입은 비교", "16:9",
   "Two figures side by side, same pose with the left elbow bent: LEFT " + who("moa") + " — the knit cardigan shows many small rounded folds at the elbow; RIGHT the same Moa wearing a thick heavy camel wool double-breasted coat over her outfit — only two or three broad folds at the elbow, smooth structured front panels.",
   "Light from the upper left."),
 body("p3_doctor_shirt_diamond", "03_material.html", "3부 2단계", "셔츠 소매를 걷어 올리고 조끼와 넥타이를 한 박사의 상반신, 팔꿈치와 겨드랑이에 각진 마름모·삼각형 그림자", "2:3",
   "Upper body of " + who("doctor", "light blue crisp cotton dress shirt with sleeves rolled up to the elbows, a gray sleeveless vest and a black tie (no lab coat)") + ", one hand at the back of his neck. The crisp shirt has sharp angular folds with diamond- and triangle-shaped shadows at the elbow and under the arm; the vest front stays smooth with almost no folds.",
   "Adult man in his thirties, normal proportions (not chibi). Light from the upper left."),
 body("p3_moa_coat_memory", "03_material.html", "3부 3단계", "두꺼운 울 코트를 입은 모아가 팔을 편 채 서 있고, 팔꿈치 안쪽에 옅은 버릇 주름과 물결 모양 그림자가 남은 그림", "2:3",
   "Full body of " + who("moa", "thick camel wool double-breasted coat over her outfit, a plaid scarf") + ", standing straight with arms relaxed at her sides. The coat is mostly smooth; only the inner elbows keep faint memory creases with small wavy shadows. No island shadows on the smooth front panels.",
   "Light from the front, soft."),
]
C6 = [
 body("p4_sia_walk_skirt", "04_motion.html", "4부 1단계", "메이드복을 입은 시아가 오른쪽으로 걷는 옆모습, 치마와 앞치마 밑단이 뒤쪽으로 부드럽게 물결치는 그림", "2:3",
   "Full body side view of " + who("sia") + ", walking briskly to the right in mid-stride. The skirt is close to the body down to where it is sewn, then puffs out; the hem and the apron frills flow backward in a soft wave, frill folds fanning along the flare of the skirt; a soft shadow under the puffed area.",
   "Light from the upper left."),
 body("p4_sia_sit_bend", "04_motion.html", "4부 3단계", "메이드복을 입은 시아가 의자에 앉아 무릎과 팔꿈치를 굽힌 모습, 소매 안쪽과 무릎 뒤에 모임 주름", "2:3",
   "Full body of " + who("sia") + ", sitting upright on a simple wooden chair, knees bent, one elbow bent with the hand holding a teacup. Fabric bunches into gathered folds inside the bent elbow and behind the knees; the sleeve is pulled taut over the outside of the elbow.",
   "Modest pose, skirt covering the knees. Light from the upper left."),
 body("p4_sia_bag_props", "04_motion.html", "4부 4단계", "메이드복의 시아가 숄더백을 메고, 옆에서 박사가 넥타이를 느슨하게 당기는 장면, 끈 아래와 셔츠 깃에 주름", "16:9",
   "Two characters side by side: LEFT " + who("sia") + ", carrying a brown leather shoulder bag — the strap presses into her shoulder and folds radiate from it toward the chest; RIGHT " + who("doctor", "light blue dress shirt with sleeves rolled up, gray vest, black tie") + ", loosening his tie with one finger — only the collar is pulled along, the shirt body stays almost smooth.",
   "The Professor is an adult man in his thirties, normal proportions (not chibi). Light from the upper left."),
]
C7 = [
 body("p5_outfit_swap_lineup", "05_ai_vfx.html", "5부 1단계", "하루·시아·모아가 서로 옷을 바꿔 입은 단체 그림 — 하루는 카디건, 시아는 헐렁한 흰 티셔츠와 랩코트, 모아는 검은 메이드복", "16:9",
   "Three characters standing in a row, full body, each wearing another member's outfit: " + who("haru", "camel knit cardigan over a white blouse, red and navy plaid bow tie, rolled-up jeans") + "; " + who("sia", "loose oversized white t-shirt under an open white knee-length lab coat, black skirt") + "; " + who("moa", "charcoal-black long-sleeved maid dress with a large gray bow and a long white frilled apron") + " — Moa keeps her white frilled headband with the ribbon over her LEFT ear.",
   "Each outfit keeps its own fabric feel: knit with soft rounded folds, loose t-shirt with large drape folds, maid dress with crisp pleats. Light from the upper left."),
 body("p5_haru_inpaint_steps", "05_ai_vfx.html", "5부 2단계", "하루의 원본 그림, 옷 부분만 반투명 주황으로 가린 그림, 후드티가 니트 카디건으로 바뀐 결과의 세 단계 비교", "16:9",
   "Three panels of the same upper-body portrait: 1) " + who("haru") + "; 2) the same image with only the clothing area (torso and arms) covered by a semi-transparent orange overlay with slightly soft edges, the face, hair buns and navy streaks clearly outside the overlay; 3) the result: identical face and hair, but the hoodie and lab coat replaced by a camel knit cardigan over a white blouse.",
   "Face and hair must be pixel-identical in all three panels. No labels."),
 body("p5_vfx_fabric_presets", "05_ai_vfx.html", "5부 3단계", "같은 천 조각이 저지·면·울·실크 네 가지 소재로 두 고리에 걸려 서로 다른 주름을 만든 3D 렌더, 옆에서 모아가 비교", "16:9",
   "A clean 3D render style scene: four identical square fabric samples hanging from two metal hooks each, in a row: soft cotton jersey (medium rounded folds), crisp cotton (fewer, angular folds), thick wool (one or two broad heavy folds), light silk (many fine long flowing folds). " + who("moa") + " stands at the right side in anime style, pointing at the wool sample.",
   "Neutral gray studio, soft light from the upper left."),
]
STY = {"pixel": "Art style: detailed 16-bit SNES-era pixel art with clearly visible square pixels, limited palette, bold dark outline, 2–3 tone shading; only the two or three largest folds of the apron and skirt are shown.",
       "anime": "Art style: high-quality anime illustration, clean lineart, two-tone cel shading; three to five large folds with a darker second shadow only in the deepest folds.",
       "semireal": "Art style: semi-realistic 2.5D digital painting, realistic proportions and fabric textures, slightly stylized face; six to eight folds including smaller ones, soft gradient shading.",
       "photo": "Art style: photorealistic studio photograph of a fictional adult model in her early twenties cosplaying this original character, 50mm lens, natural skin texture, real fabric with all natural folds; not resembling any real celebrity."}
C8 = []
for k, nm in [("pixel", "픽셀아트"), ("anime", "애니풍"), ("semireal", "반실사"), ("photo", "실사풍")]:
    p = ("Full body character illustration, vertical 2:3.\n" + STY[k] + "\nMatch the attached reference images exactly (face, hair, colors, accessories).\n" + who("sia") + ", standing in a relaxed three-quarter pose, one hand lightly holding the edge of the apron.\nSame pose, same framing and same lighting (soft light from the upper left) as the other three images of this set.\nPlain off-white studio background.\n" + END)
    C8.append(("p5_sia_style_" + k, "05_ai_vfx.html", "5부 4단계", f"{nm} 전신 시아 — 같은 자세, 화풍마다 주름의 양이 다름", p, k))
FAILNOTE = "This is an intentional FAILURE example for a teaching page: draw the mistake described below clearly and convincingly, while everything else stays correct."
def fail(file, alt, scene, mistake):
    p = f"Illustration, vertical 2:3.\n{ANI}\n{FAILNOTE}\n{scene}\nIntentional mistake: {mistake}\nPlain off-white studio background.\n{END}"
    return (file, "06_failure_lab.html", "6부 실패", alt, p, "anime")
C9 = [
 fail("f1_traced_too_many", "애니풍인데 모아의 카디건 전체가 잔주름과 솔기 선으로 빽빽하게 덮인 그림", "Upper body of " + who("moa") + ", left elbow bent.", "the simple anime face and hair, but the knit cardigan is covered with dozens of tiny wrinkle lines and seam lines everywhere, like a traced photo — far too much detail for the style."),
 fail("f2_coat_like_silk", "두꺼운 울 코트인데 실크처럼 가늘고 긴 S자 잔주름이 흘러내리는 코트를 입은 모아", "Full body of " + who("moa", "a camel coat over her outfit") + ".", "the coat is supposed to be thick heavy wool, but it is drawn like thin silk: many fine, long, flowing S-shaped folds and a shiny drape."),
 fail("f3_loose_tee_clinging", "헐렁한 오버핏 티셔츠라고 했는데 몸에 딱 붙어 주름이 없는 흰 티셔츠를 입은 하루", "Full body of " + who("haru", "an 'oversized' white t-shirt and rolled-up jeans (no lab coat, no hoodie)") + ".", "the shoulder seams are dropped like an oversized shirt, but the body of the t-shirt clings tightly to the body with no drape folds at all, like painted on (modest, no exaggerated body)."),
 fail("f4_floating_strap", "숄더백 끈이 시아의 어깨 위에 떠 있고 옷에는 끈이 누른 자국이나 주름이 없는 그림", "Full body of " + who("sia") + ", carrying a brown shoulder bag.", "the bag strap floats slightly above her shoulder without touching it, and the dress shows no pressure or folds where the strap should press."),
]
C10 = [
 fail("f5_fold_shadow_wrong_side", "빛은 왼쪽 위인데 티셔츠 주름 산의 왼쪽 비탈에 그림자가 있어 주름이 오목해 보이는 하루", "Upper body of " + who("haru", "a loose white t-shirt (no lab coat, no hoodie)") + ", a visible lamp glow at the upper left.", "the face and body are lit from the upper left, but every fold shadow on the t-shirt is placed on the UPPER LEFT side of each fold ridge (the lit side), so the folds look dented instead of raised."),
 fail("f6_frill_against_flare", "시아의 메이드복 치마는 아래로 퍼지는데 앞치마 프릴 주름이 퍼짐과 반대 방향으로 기운 그림", "Full body of " + who("sia") + ", standing.", "the skirt flares outward toward the hem, but the apron frill folds slant inward, against the flare, as if gathered the wrong way."),
 fail("f7_pleats_both_sides", "한 방향 주름치마인데 주름마다 양쪽 뒷면이 다 보이고 그림자도 양쪽에 있어 줄무늬처럼 보이는 그림", "Full body of " + who("moa", "camel knit cardigan over a white blouse and a navy side-pleated skirt below the knee") + ", seen slightly from her right.", "the skirt is supposed to have all pleats folded in one direction, but both inner faces of every pleat are visible with shadows on both sides, so it looks like flat stripes."),
 fail("f8_mask_changed_face", "하루의 후드티만 카디건으로 바꾸려 했는데 머리 번과 남색 줄이 사라지고 얼굴도 달라진 결과", "Upper body portrait wearing a camel knit cardigan over a white blouse.", "this was supposed to be Haru with only her clothes changed, but the result is a different person: pink hair WITHOUT the two hair buns and WITHOUT the navy streaks, a different face shape and eye color (green eyes)."),
]
CONV = [("C01_covers_A", "표지 A (픽셀아트, 16:9)", "16:9", "refs 전부", C1), ("C02_covers_B", "표지 B (픽셀아트, 16:9)", "16:9", "refs 전부 + C01에서 받은 cover_index", C2),
        ("C03_part1_photo", "1부 사진을 그림으로", "16:9", "refs/moa_anime_base.png, refs/moa_sheet.png", C3), ("C04_part2_fit", "2부 붙는 옷과 헐렁한 옷", "16:9·2:3", "refs/haru_anime_base.png, refs/haru_sheet.png", C4),
        ("C05_part3_material", "3부 소재감", "16:9·2:3", "refs/moa_anime_base.png, refs/doctor_sheet.png", C5), ("C06_part4_motion", "4부 움직임과 주름", "2:3·16:9", "refs/sia_anime_base.png, refs/doctor_sheet.png", C6),
        ("C07_part5_ai_vfx", "5부 AI와 VFX", "16:9", "refs/haru_anime_base.png, refs/sia_anime_base.png, refs/moa_anime_base.png", C7), ("C08_part5_styles", "5부 화풍 4종(시아)", "2:3", "refs/sia_anime_base.png, refs/sia_sheet.png", C8),
        ("C09_fail_A", "6부 실패 A", "2:3", "해당 캐릭터의 refs/*_anime_base.png", C9), ("C10_fail_B", "6부 실패 B", "2:3", "해당 캐릭터의 refs/*_anime_base.png", C10)]
HEAD_PIX = "웹페이지 맨 위에 거는 표지 그림을 한 장씩 차례로 만들어 줘.\n- 비율 16:9, 가로 1920px 이상\n- 그림체는 반드시 16비트 RPG풍 픽셀아트 (네모 픽셀이 보이게, 매끈한 일러스트·벡터·수채화·3D 금지)\n- 첨부한 참고 이미지의 캐릭터를 같은 외형으로 그릴 것\n- 그림 안에 글자·숫자·로고 금지\n- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게\n아래 영어 프롬프트를 하나씩 써 줘."
HEAD_ANI = "해설 페이지 본문에 넣을 그림을 한 장씩 차례로 만들어 줘.\n- 비율은 각 프롬프트 첫 줄을 따를 것(16:9는 가로 1920px 이상, 2:3은 세로 1536px 이상)\n- 첨부한 참고 이미지의 캐릭터 외형(얼굴·머리·색·장식)을 똑같이 지킬 것\n- 등장인물은 모두 20대 성인(박사는 성인 남성). 노출·과장된 체형·교복 느낌 금지\n- 그림 안에 글자·숫자·로고 금지, 유명 애니 캐릭터와 닮으면 다시 만들 것\n아래 영어 프롬프트를 하나씩 써 줘."
PROMPTS = {it[0]: it for _c in CONV for it in _c[4]}
CONV_OF = {it[0]: _c[0] for _c in CONV for it in _c[4]}
ATTACH_OF = {_c[0]: _c[3] for _c in CONV}

if __name__ == "__main__":
    os.makedirs(os.path.join(D, "prompts"), exist_ok=True)
    rows = []; n = 0
    for cid, title, ratio, att, items in CONV:
        pix = items[0][5] == "pixel"
        md = f"# {cid[:3]} · {title} — " + ", ".join(i[0] for i in items) + f"\n\n**첨부:** {att}\n\n**Genspark에 먼저 붙여 넣기 ↓**\n```\n{HEAD_PIX if pix else HEAD_ANI}\n```\n"
        for k, (file, page, part, alt, prompt, style) in enumerate(items):
            n += 1; rows.append([n, cid[:3], file, page, part, "16:9" if "16:9" in prompt.split("\n")[0] else "2:3", style, ""])
            md += f"\n---\n## {k+1}) {file} — {part}\nalt: {alt}\n```\n{prompt}\n```\n"
        if cid.startswith("C09") or cid.startswith("C10"):
            md += "\n---\n**실패 그림 주의:** 도구가 실수를 자동으로 고쳐 버리면 두 번까지만 다시 시도해 주세요. 그래도 안 되면 그대로 주셔도 됩니다(페이지에서 '결과는 매번 달라진다'는 사례로 설명합니다).\n"
        open(os.path.join(D, "prompts", cid + ".md"), "w").write(md)
    with open(os.path.join(D, "checklist.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["order", "conversation", "file", "page", "part", "ratio", "style", "status"]); w.writerows(rows)
    print("prompts", len(CONV), "images", n)
