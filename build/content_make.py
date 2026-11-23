# -*- coding: utf-8 -*-
"""부마다 '프롬프트로 직접 만들어 보기' 실습. A 프롬프트는 make_requests.py(이 페이지 그림을 실제로 만든 프롬프트)에서 가져온다."""

def T(key, title, goal, b_title, b_text, check, tip=None, img=None, b_imgs=None):
    return dict(key=key, title=title, goal=goal, b_title=b_title, b_text=b_text, check=check, tip=tip, img=img or key, b_imgs=[key + "_b"] if b_imgs is None else b_imgs)

MAKE = {
1: [
 T("p1_moa_photo_vs_drawing", "사진·큰 주름·완성 그림을 한 장에", "사진처럼 보이는 모델과, 큰 주름 셋만 고른 그림, 완성 그림을 나란히 만들어 '고르기'를 눈으로 확인합니다.",
   "B — 원리 빼기: 사진의 주름을 전부 옮기게 하기", "Same characters, same layout and pose. Change only: in the center and right panels, copy every small wrinkle and seam line from the photo panel. Still no text.",
   [("가운데 그림에 큰 주름 세 개(팔꿈치 모임·어깨 당김·허리 처짐)가 표시되었나", "#s1"), ("오른쪽 완성 그림의 선 수가 애니풍 알맞은 구간(3~6)인가, B 결과는 '베낀 느낌'인가", "#s2"), ("사진 패널이 실존 인물과 닮지 않았나(닮았으면 다시 생성)", None)]),
 T("p1_moa_shadow_steps", "그림자 다섯 단계 — 한 장씩 나눠 요청하기", "한 장에 다섯 단계를 몰아 요청하면 차이가 약하게 나옵니다(이 페이지 그림이 그 예). 같은 대화에서 단계마다 한 장씩 요청하는 방법을 연습합니다.",
   "B — 단계별 요청(같은 대화에서 차례로)", "1) Upper body of Moa (same character as the reference), flat colors only, no shadows at all, light from the upper left.\n2) Same image. Add only cast shadows: under the chin, under the collar and under the sleeves. Nothing else.\n3) Same image. Add large form shadows on the right side of the body and arms.\n4) Same image. Add a few small floating island shadows on the cardigan folds.\n5) Same image. Add a darker second shadow only in the deepest creases. Keep everything else unchanged.",
   [("단계마다 그림자가 하나씩만 더해졌나(한 번에 여러 개가 바뀌지 않았나)", "#s3"), ("④ 진한 2차 그림자가 가장 깊은 골에만 아주 조금 들어갔나", "#s3"), ("모든 그림자가 빛(왼쪽 위)의 반대쪽에 있나", "02_fit.html#s4")],
   b_imgs=["p1_moa_shadow_step%d" % i for i in range(1, 6)],
   tip="한 번의 요청에 여러 변화를 넣을수록 도구는 차이를 뭉개기 쉽습니다. 바꿀 것을 한 문장에 하나씩 주는 것이 요령입니다."),
],
2: [
 T("p2_haru_tee_fit_compare", "딱 맞는 티셔츠와 헐렁한 티셔츠", "같은 사람, 같은 자세에서 핏만 바꿔 남는 천이 주름을 어떻게 바꾸는지 실제 그림으로 봅니다.",
   "B — 원리 빼기: 핏 낱말 지우기", "Same image. Change only: make both t-shirts exactly the same ordinary size; do not describe them as fitted or oversized. Still no text.",
   [("오른쪽(헐렁)에 어깨에서 내려오는 굵은 처짐 주름이 있나", "#s1"), ("왼쪽(딱 맞음)은 힘받는 곳에 가는 당김 주름만 있나", "#s1"), ("B 결과에서 두 사람이 구별되지 않는 것을 확인", None)]),
 T("p2_haru_tee_poses", "자세 네 가지 — 접점이 옮겨 가는지", "팔 올리기·팔짱·허리 젖히기·밑단 잡기에서 주름의 시작점이 바뀌는지 봅니다.",
   "B — 원리 빼기: 옷을 굳혀 두기", "Same image. Change only: keep the t-shirt exactly the same in all four panels — same folds and the same hem height. Still no text.",
   [("팔 올리기: 어깨에 모임 주름, 밑단이 올라가고 배는 평평한가", "#s2"), ("팔짱: 주름이 팔이 닿은 쪽으로 모이나 / 밑단 잡기: 손가락으로 대각선 주름", "#s2"), ("B 결과가 '얼어붙은 옷'으로 보이는지 비교", None)]),
 T("p2_haru_loose_tee_shading", "선 대신 그림자로", "작은 주름을 선 없이 그림자만으로 그려, 빛 방향만으로 볼록함이 살아나는지 봅니다.",
   "B — 원리 빼기: 모든 주름을 선으로", "Same image. Change only: draw every fold with a dark line and remove all fold shadows. Still no text.",
   [("주름 그림자가 모두 산의 오른쪽 아래(빛 반대쪽)에 있나", "#s4"), ("선은 큰 주름 세 개 정도만 남았나", "#s4"), ("B 결과가 더 복잡하고 납작해 보이는지 비교", None)]),
],
3: [
 T("p3_moa_knit_vs_coat", "니트와 울 코트", "같은 팔 굽히기에서 두께가 주름 간격과 굵기를 바꾸는지 봅니다.",
   "B — 원리 빼기: 코트에 니트 주름", "Same image. Change only: draw the wool coat with the same many small folds as the knit cardigan. Still no text.",
   [("코트는 굵은 주름 2~3개, 니트는 잔주름 여러 개인가", "#s1"), ("코트 앞판이 매끈하고 각이 서 있나", "#s1"), ("B 결과에서 코트가 얇은 천처럼 보이는지 비교(6부 f2와 같은 실패)", "06_failure_lab.html#f2_coat")]),
 T("p3_doctor_shirt_diamond", "빳빳한 셔츠의 마름모 그림자", "셔츠 소매의 그림자가 둥근 덩어리가 아니라 각진 조각으로 나오는지 봅니다.",
   "B — 원리 빼기: 그림자를 둥글게", "Same image. Change only: make every shadow on the shirt soft and rounded like on a knit sweater. Still no text.",
   [("팔꿈치·겨드랑이 그림자가 마름모·삼각형처럼 각졌나", "#s2"), ("조끼 앞판은 주름이 거의 없나(소매 없는 겉옷)", "#s4"), ("박사가 꼬마 체형이 아닌 성인 남성 비율인가", None)]),
 T("p3_moa_coat_memory", "입던 코트의 버릇 주름", "팔을 펴도 팔꿈치 안쪽에만 옅은 자국이 남는지 봅니다.",
   "B — 비교: 새 코트로 바꾸기", "Same image. Change only: it is a brand-new coat — no memory creases anywhere. Still no text.",
   [("팔꿈치 안쪽에만 옅은 자국과 물결 그림자가 있나", "#s3"), ("주름 없는 앞판에는 섬 그림자가 없나", "#s3"), ("B(새 코트)와 나란히 놓으면 '입던 옷'이 구별되나", None)]),
],
4: [
 T("p4_sia_walk_skirt", "걷는 시아 — 치마의 공기와 흐름", "걷는 동작에서 치마가 부풀고 밑단이 뒤로 흐르는지 봅니다.",
   "B — 비교: 속도 올리기", "Same character, same side view. Change only: she is running fast; the skirt and apron hem lift much higher and flow strongly backward. Still no text.",
   [("허리에서 꿰맨 곳까지는 붙고 그 아래부터 부풀었나", "#s1"), ("밑단이 걷는 방향의 반대쪽으로 흐르나, 프릴이 퍼짐을 따르나", "#s1"), ("B(뛰기)에서 들림이 훨씬 커졌나 — 속도² 규칙", "#s1")]),
 T("p4_sia_sit_bend", "앉은 시아 — 굽힌 관절의 주름", "팔꿈치와 무릎을 굽힐 때 안쪽은 모이고 바깥은 당기는지 봅니다.",
   "B — 비교: 펴고 서기", "Same character and outfit. Change only: she stands up straight with arms relaxed. Still no text.",
   [("팔꿈치 안쪽과 무릎 뒤에 모임 주름이 있나", "#s3"), ("팔꿈치 바깥쪽 소매가 팽팽하게 당겨졌나", "#s3"), ("B(선 자세)에서 그 주름이 사라지는지 비교", None)]),
 T("p4_sia_bag_props", "가방과 넥타이 — 새 접점", "소품이 옷을 누르거나 당기는 곳에서 주름이 시작되는지 봅니다.",
   "B — 비교: 백팩으로 바꾸기", "Same image. Change only: Sia carries a backpack instead of the shoulder bag — straps on both shoulders, the bottom of the bag pushing up the dress at the lower back. Still no text.",
   [("숄더백 끈이 어깨를 누르고, 거기서 주름이 가슴 쪽으로 퍼지나", "#s4"), ("박사가 넥타이를 당길 때 깃만 끌려가고 셔츠 몸판은 거의 그대로인가", "#s4"), ("B(백팩)에서 허리 쪽에 모임 주름이 생겼나", "#s4")]),
],
5: [
 T("p5_outfit_swap_lineup", "세 사람 옷 바꿔 입기", "옷 문장(종류·핏·소재)을 갖춘 프롬프트로 옷을 바꿔 입히고, 이름만 쓴 프롬프트와 비교합니다. 1단계 조립기로 만든 문장을 써도 됩니다.",
   "B — 원리 빼기: 이름만 쓰기", "Three anime girls standing in a row: Haru wearing Moa's outfit, Sia wearing Haru's outfit, Moa wearing Sia's outfit. No text.",
   [("하루의 머리 번·남색 줄, 모아의 왼쪽 리본이 그대로인가", "#s1"), ("카디건은 니트의 둥근 주름, 헐렁한 티셔츠는 큰 처짐 주름인가", "03_material.html#s1"), ("B 결과에서 옷이 엉뚱하거나 사람이 바뀌는지 비교 — AI는 '모아의 옷'이 무엇인지 모릅니다", "#s1")]),
 T("p5_haru_inpaint_steps", "옷만 다시 그리기 — 부분 수정 기능으로", "한 장짜리 설명 그림이 아니라, 실제 도구의 '부분 수정(인페인팅)' 기능으로 옷만 바꿔 봅니다. 이 페이지 그림은 가운데 단계의 가림 영역이 주황 옷처럼 그려졌습니다 — 설명 그림과 실제 기능은 다릅니다.",
   "실제 순서 — 부분 수정 기능에서", "1) 하루 그림(예: 앞 시리즈의 애니풍 기준 전신)을 올립니다.\n2) 수정 붓으로 몸통과 팔만 칠합니다. 얼굴·머리 번·남색 줄은 피하고, 옷보다 조금 넉넉하게.\n3) 프롬프트: camel knit cardigan over a white blouse, red and navy plaid bow tie, soft thick knit with broad rounded folds, light from the upper left. Keep the face and hair unchanged.\n4) 결과가 이음매를 보이면 칠한 영역을 조금 넓히거나 경계를 흐리게 해 다시.",
   [("얼굴·머리 번·남색 줄이 원본과 똑같은가", "#s2"), ("옷 경계(목·손목)에 이음매나 옛 옷의 흔적이 없나", "#s2"), ("새 카디건이 니트답게(둥근 잔주름) 그려졌나", "03_material.html#s1")],
   b_imgs=["p5_haru_inpaint_real"],
   tip="도구마다 이 기능의 이름이 다릅니다(부분 수정, 인페인팅, 영역 편집 등). 영역을 칠하는 붓이 있으면 같은 기능입니다."),
 T("p5_vfx_fabric_presets", "소재 네 가지를 한 장에", "같은 크기의 천 네 장이 소재마다 다른 주름을 만드는지 봅니다. 그림 생성 AI는 천을 계산하지 않으므로, 결과는 '소재를 말로 얼마나 잘 전했나'를 보여 줍니다.",
   "B — 원리 빼기: 소재 하나로", "Same scene. Change only: all four samples are the same plain cotton fabric. Still no text.",
   [("울은 굵은 주름 한두 개, 실크는 잔주름과 긴 처짐인가", "#s3"), ("빳빳한 면은 주름이 적고 각이 서 있나", "03_material.html#s2"), ("B 결과에서 네 장이 구별되지 않는지 비교", None)],
   tip="실제 천 계산은 VFX 도구(의상 시뮬레이션)에서 무게·뻣뻣함 값으로 합니다. 3단계 실험과 연습장 소재 실험실이 그 연습입니다."),
 T("p5_sia_style_pixel", "같은 옷, 네 가지 화풍", "아래 프롬프트의 'Art style' 줄만 바꿔 네 번 만들고, 주름의 위치는 그대로인데 양만 달라지는지 봅니다.",
   "B — 화풍 줄만 바꾸기(나머지는 그대로)", "애니풍: Art style: high-quality anime illustration, clean lineart, two-tone cel shading; three to five large folds.\n반실사: Art style: semi-realistic 2.5D digital painting, six to eight folds including smaller ones, soft gradient shading.\n실사풍: Art style: photorealistic studio photograph of a fictional adult model in her early twenties cosplaying this original character; not resembling any real celebrity.",
   [("네 장 모두 자세·빛(왼쪽 위)·주름 위치가 같은가", "#s4"), ("픽셀은 주름 2~3개·그림자 2단계, 실사풍은 실제 천의 모든 주름인가", "#s4"), ("실사풍이 실존 인물과 닮지 않았나", None)],
   b_imgs=["p5_sia_style_anime", "p5_sia_style_semireal", "p5_sia_style_photo"]),
],
6: [
 T("f2_coat_like_silk", "실패 만들고 고치기 ① — 하늘거리는 코트", "일부러 소재를 뒤바꾼 그림을 만든 뒤, 실패 카드의 '고치는 조각'을 같은 대화에 넣어 고칩니다.",
   "B — 고치기(같은 대화에 이어서)", "Same character and pose. Fix: thick heavy wool coat, only a few broad folds, matte texture, structured shoulders. Still no text.",
   b_imgs=["f2_fixed"], check=[("A 결과: 코트가 실크처럼 가는 S자 주름으로 흘러내리나(실패 재현)", "#f2_coat"), ("B 결과: 굵은 주름 몇 개와 각진 어깨로 바뀌었나", "03_material.html#s1"), ("점검표 ③ 소재에서 처음 걸리는지 확인", "#s1")]),
 T("f8_mask_changed_face", "실패 만들고 고치기 ② — 다른 사람이 된 결과", "옷만 바꾸려다 사람이 바뀐 결과를 만들어 보고, 고칠 곳이 프롬프트가 아니라 가림 영역이라는 것을 확인합니다.",
   "B — 고치기", "5부 2단계 실습 순서대로, 원본 하루 그림에서 옷 영역만 칠하고 다시 그립니다. 프롬프트에 캐릭터 고정 문장(머리 번 두 개, 앞머리 가운데 남색 줄, 파란 눈)을 함께 넣습니다.",
   b_imgs=["p5_haru_inpaint_real"], check=[("A 결과: 머리 번·남색 줄이 사라지고 다른 얼굴이 되었나(실패 재현)", "#f8_mask"), ("B 결과: 얼굴과 머리는 원본 그대로, 옷만 바뀌었나", "05_ai_vfx.html#s2"), ("점검표 ⑤ 정보량·가림 영역에서 처음 걸리는지 확인", "#s1")]),
 T("f5_fold_shadow_wrong_side", "실패가 재현되지 않을 때 — 그림자 방향", "이 실패는 도구가 스스로 고쳐 버리기 쉽습니다(이 페이지 그림이 그 예). 두 번까지 시도해 보고, 고쳐져 나오면 그것도 기록합니다.",
   "B — 그래도 확인하기", "결과가 맞게 나와도 매번 직접 확인합니다: 빛이 오는 쪽을 정하고, 주름 산마다 그림자가 반대쪽 비탈에 있는지 하나씩 봅니다. 잘못된 모습은 2부 4단계 실험에서 빛을 옮겨 보면 볼 수 있습니다.",
   b_imgs=[], check=[("A 결과에서 그림자가 빛 쪽 비탈에 있나, 아니면 도구가 고쳐 그렸나", "#f5_fold"), ("고쳐 그렸다면: 같은 요청도 결과가 매번 다르다는 기록으로 남기기", None), ("점검표 ④ 빛 항목으로 결과를 다시 채점", "#s1")],
   tip="실패 그림을 일부러 만드는 이유는 '틀린 모습을 알아보는 눈'을 기르기 위해서입니다. 도구가 고쳐 주더라도 확인 습관은 그대로 둡니다."),
],
}

RES = {'p1_moa_photo_vs_drawing': '실제 결과: B에서는 가운데 그림의 색 선(큰 주름 표시)만 사라지고 나머지는 A와 거의 같았습니다. 같은 대화에서는 도구가 앞 그림을 따라가려 해서 차이가 약해집니다. 새 대화에서 A 문장 끝에 B 문장을 붙여 처음부터 만들면 차이가 더 잘 보입니다.', 'p1_moa_shadow_steps': "실제 결과: 1→4단계로 갈수록 그림자가 한 겹씩 쌓였습니다(4단계에서 가장 깊은 곳이 진해짐). 5단계에서는 도구가 상반신을 전신으로 바꿔 버렸습니다. 단계마다 'keep the same framing'을 덧붙이면 구도가 흔들리지 않습니다.", 'p2_haru_tee_fit_compare': '실제 결과: B에서는 두 사람이 똑같아져 구별되지 않았습니다. 핏 낱말이 빠지면 핏의 차이도 사라집니다.', 'p2_haru_tee_poses': '실제 결과: B에서 밑단 잡기 그림의 대각선 당김 주름이 사라졌습니다(손가락이 접점이 되지 못함). 팔 올리기의 밑단은 그대로 올라가 있어, 도구가 옷을 완전히 굳히지는 못했습니다.', 'p2_haru_loose_tee_shading': '실제 결과: B는 주름마다 선이 생기고 그림자가 줄어, 더 복잡하고 납작해 보입니다.', 'p3_moa_knit_vs_coat': "실제 결과: B에서도 코트는 크게 바뀌지 않았습니다. 도구가 '울 코트는 굵은 주름'이라는 상식을 고집한 셈입니다. 차이가 약할 때는 6부 f2처럼 소재 낱말 자체를 바꿔 보세요.", 'p3_doctor_shirt_diamond': '실제 결과: B는 A와 거의 같았습니다. 그림자 모양만 바꾸라는 요청은 도구가 잘 따르지 않습니다. 각진 그림자와 둥근 그림자의 차이는 3부 2단계 실험에서 확인하세요.', 'p3_moa_coat_memory': "실제 결과: 새 코트(B)는 팔꿈치 자국까지 사라져 매끈합니다. A와 나란히 보면 '입던 옷'이 구별됩니다.", 'p4_sia_walk_skirt': '실제 결과: 뛰는 B에서 치마와 앞치마가 크게 들리고 뒤로 흘렀습니다. 속도의 제곱 규칙 그대로입니다.', 'p4_sia_sit_bend': '실제 결과: 선 자세(B)에서는 팔꿈치 안쪽과 무릎 뒤의 모임 주름이 사라졌습니다.', 'p4_sia_bag_props': '실제 결과: 백팩으로 바꾸자 끈이 두 어깨에 걸렸습니다. 허리 아래 모임 주름은 가방에 가려 잘 보이지 않습니다.', 'p5_outfit_swap_lineup': "실제 결과: 이름만 넣은 B에서는 전혀 다른 세 사람이 나왔고, 가운데는 학교 교복 같은 옷까지 입었습니다. AI는 '하루·모아의 옷'이 무엇인지 모릅니다. 6부 '옷 이름 하나로 나이가 달라 보인다'와 같은 이유입니다.", 'p5_haru_inpaint_steps': '실제 결과: 얼굴·머리 번·남색 줄은 그대로 두고 옷만 니트 카디건으로 바뀌었습니다.', 'p5_vfx_fabric_presets': '실제 결과: 네 장이 모두 같은 흰 면이 되어 구별되지 않았습니다. 소재 낱말이 소재의 차이를 만듭니다.', 'f2_coat_like_silk': '실제 결과: 고친 B는 굵은 주름 몇 개와 각진 어깨의 울 코트가 되었습니다.', 'f8_mask_changed_face': "실제 결과: B 그림은 5부 '옷만 다시 그리기' 실습과 같은 결과입니다. 얼굴과 머리는 원본 그대로입니다."}
for _v in MAKE.values():
    for _t in _v:
        _t['res'] = RES.get(_t['key'])
