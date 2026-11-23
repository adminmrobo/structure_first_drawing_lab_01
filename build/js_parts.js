
/* ===================== 공용: 앞에서 본 상반신(SVG) ===================== */
var SH={sk:'#F6D3B8',ink:'#2a2230',tee:'#fbfbfd',teeS:'#d9dbe6',fold:'#7d7a99',hot:'#e8731a'};
function torso(s,o){o=o||{};var pose=o.pose||'stand',cx=o.cx||260,top=o.top||70,k=o.k||1,col=o.col||SH.tee,loose=o.loose||0;
  var g=el('g',{},s);var sw=95*k+loose*10,hip=78*k+loose*16,len=(o.len||230)*k,hemUp=o.hemUp||0;
  var arms={stand:[[-1,[sw+6,top+20],[sw+20,top+120],[sw+18,top+210]],[1,[sw+6,top+20],[sw+20,top+120],[sw+18,top+210]]],
    up:[[-1,[sw,top+10],[sw-10,top-80],[sw-30,top-160]],[1,[sw,top+10],[sw-10,top-80],[sw-30,top-160]]],
    cross:[[-1,[sw+6,top+20],[sw+16,top+110],[-20,top+130]],[1,[sw+6,top+20],[sw+16,top+118],[-10,top+122]]],
    arch:[[-1,[sw+4,top+16],[sw+30,top-40],[sw-10,top-110]],[1,[sw+4,top+16],[sw+30,top-40],[sw-10,top-110]]],
    pinch:[[-1,[sw+6,top+20],[sw+20,top+120],[sw+18,top+210]],[1,[sw+6,top+20],[sw+22,top+110],[30,top+len-8]]]}[pose]||[];
  // 목·머리
  el('rect',{x:cx-16*k,y:top-38*k,width:32*k,height:40*k,fill:SH.sk,stroke:SH.ink,'stroke-width':2},g);
  el('ellipse',{cx:cx,cy:top-70*k,rx:42*k,ry:48*k,fill:SH.sk,stroke:SH.ink,'stroke-width':2},g);
  if(o.hair)el('path',{d:'M'+(cx-46*k)+','+(top-60*k)+' Q'+cx+','+(top-150*k)+' '+(cx+46*k)+','+(top-60*k)+' L'+(cx+40*k)+','+(top-85*k)+' Q'+cx+','+(top-100*k)+' '+(cx-40*k)+','+(top-85*k)+'Z',fill:o.hair,stroke:SH.ink,'stroke-width':2},g);
  // 팔(소매 포함)
  arms.forEach(function(a){var d=a[0];var P_=function(q){return [cx+d*q[0],q[1]];};var p0=P_(a[1]),p1=P_(a[2]),p2=P_(a[3]);
    el('path',{d:'M'+p0+' L'+p1+' L'+p2,fill:'none',stroke:SH.ink,'stroke-width':30*k+2,'stroke-linecap':'round','stroke-linejoin':'round'},g);
    el('path',{d:'M'+p0+' L'+p1+' L'+p2,fill:'none',stroke:SH.sk,'stroke-width':30*k-2,'stroke-linecap':'round','stroke-linejoin':'round'},g);
    var sl=[p0[0]+(p1[0]-p0[0])*0.42,p0[1]+(p1[1]-p0[1])*0.42];
    el('path',{d:'M'+p0+' L'+sl,fill:'none',stroke:SH.ink,'stroke-width':36*k+2+loose*6,'stroke-linecap':'butt'},g);
    el('path',{d:'M'+p0+' L'+sl,fill:'none',stroke:col,'stroke-width':36*k-2+loose*6,'stroke-linecap':'butt'},g);
    a.pts=[p0,p1,p2];});
  // 몸판
  var y2=top+len-hemUp;var body='M'+(cx-sw)+','+(top+18)+' Q'+cx+','+(top-6)+' '+(cx+sw)+','+(top+18)+' L'+(cx+hip)+','+y2+' L'+(cx-hip)+','+y2+'Z';
  el('path',{d:body,fill:col,stroke:SH.ink,'stroke-width':2.4},g);
  el('path',{d:'M'+(cx-20*k)+','+(top+4)+' Q'+cx+','+(top+22*k)+' '+(cx+20*k)+','+(top+4),fill:'none',stroke:SH.ink,'stroke-width':2},g);
  if(o.pants!==false){el('path',{d:'M'+(cx-hip+4)+','+y2+' L'+(cx-hip+8)+','+(y2+90)+' L'+(cx-6)+','+(y2+90)+' L'+cx+','+(y2+30)+' L'+(cx+6)+','+(y2+90)+' L'+(cx+hip-8)+','+(y2+90)+' L'+(cx+hip-4)+','+y2+'Z',fill:'#5b7fb8',stroke:SH.ink,'stroke-width':2},g);}
  return {g:g,cx:cx,top:top,sw:sw,hip:hip,y2:y2,arms:arms};}
function dot2(s,x,y,r){return el('circle',{cx:x,cy:y,r:r||8,fill:SH.hot,stroke:'#fff','stroke-width':2.5},s);}
function arrow(s,x1,y1,x2,y2,col,w){col=col||C.purple;var a=Math.atan2(y2-y1,x2-x1),L=9;var g=el('g',{},s);el('line',{x1:x1,y1:y1,x2:x2,y2:y2,stroke:col,'stroke-width':w||2.6,'stroke-linecap':'round'},g);
  el('path',{d:'M'+x2+','+y2+' L'+(x2-L*Math.cos(a-0.45))+','+(y2-L*Math.sin(a-0.45))+' L'+(x2-L*Math.cos(a+0.45))+','+(y2-L*Math.sin(a+0.45))+'Z',fill:col},g);return g;}
function foldLine(s,d,col,w,op){return el('path',{d:d,fill:'none',stroke:col||SH.fold,'stroke-width':w||2,'stroke-linecap':'round',opacity:op==null?1:op},s);}

/* ===================== 1부 ===================== */
var FOLDS1=[[9,'모임','M150,250 Q170,262 186,250 M146,266 Q168,280 190,266 M150,282 Q170,292 186,284'],[7,'당김','M330,96 Q300,150 268,200'],[5,'처짐','M230,300 Q236,340 228,382 M290,300 Q286,342 294,382'],
 [3,'모임','M366,250 Q352,262 336,252 M370,268 Q350,280 334,268'],[2,'처짐','M200,384 Q214,372 228,386'],[1,'당김','M190,100 Q210,140 236,170'],[1,'처짐','M330,330 Q332,356 326,380'],[1,'모임','M246,120 Q256,128 270,120'],[0.5,'처짐','M210,220 Q214,240 210,262'],[0.5,'당김','M300,250 Q306,232 316,220']];
P.p1_rank=function(h){var inp=ctl(h).querySelector('input'),W=560,H=420;var tot=FOLDS1.reduce(function(a,f){return a+f[0];},0);
  function draw(){var k=+inp.value;var s=svgOf(h,W,H);el('rect',{x:0,y:0,width:W,height:H,fill:'#fbfcfd'},s);
    // 카디건 몸판
    el('path',{d:'M170,70 Q260,50 350,70 L380,390 L140,390Z',fill:'#D4B48A',stroke:SH.ink,'stroke-width':2.4},s);
    el('path',{d:'M170,74 L130,200 L150,300 L182,296 L190,210Z',fill:'#D4B48A',stroke:SH.ink,'stroke-width':2.2},s);
    el('path',{d:'M350,74 L390,200 L372,300 L340,296 L332,210Z',fill:'#D4B48A',stroke:SH.ink,'stroke-width':2.2},s);
    el('path',{d:'M236,62 L260,170 L284,62',fill:'#fbfbfd',stroke:SH.ink,'stroke-width':2},s);
    var sum=0;FOLDS1.forEach(function(f,i){var on=i<k;if(on)sum+=f[0];foldLine(s,f[2],on?C.teal:'#b7a58a',on?1.2+f[0]*0.55:1.2,on?1:0.55);});
    // 막대
    var bx=410,bw=80;ktxt(s,bx,24,'주름 세기(큰 순)',{size:12.5,fill:C.ink,weight:700});
    FOLDS1.forEach(function(f,i){var on=i<k;el('rect',{x:bx,y:34+i*30,width:f[0]/9*bw,height:18,rx:3,fill:on?C.teal:'#dfe4ea'},s);ktxt(s,bx+f[0]/9*bw+4,48+i*30,f2(f[0],1)+' '+f[1],{size:11.5,fill:on?C.ink:C.muted});});
    var pct=sum/tot*100;el('rect',{x:20,y:400,width:380,height:10,rx:5,fill:'#e3e8ee'},s);el('rect',{x:20,y:400,width:380*pct/100,height:10,rx:5,fill:C.orange},s);
    ktxt(s,20,392,'잡힌 비율 '+f2(pct,0)+'%',{size:13,fill:C.ink,weight:700});
    out(h).innerHTML='큰 것 <b>'+k+'</b>개의 세기 합 '+f2(sum,1)+' ÷ 전체 '+tot+' = <b>'+f2(pct,1)+'%</b>'+(k===3?' — 모임·당김·처짐 세 종류가 모두 들어 있습니다.':'')+(pct>=95?' 나머지는 거의 장식입니다.':'');}
  onIn(inp,draw);draw();};

P.p1_detail=function(h){var inp=ctl(h).querySelector('input'),mode='anime',W=560,H=400;var RANGE={simple:[1,3,'단순풍'],anime:[3,6,'애니풍'],real:[6,9,'실사풍']};
  var LINES=['M200,120 Q214,170 206,220','M318,120 Q306,170 314,220','M150,170 Q166,178 182,170','M370,170 Q354,178 338,170','M240,96 Q250,110 262,98','M224,160 Q232,190 226,210','M290,150 Q296,176 292,206','M180,206 Q190,214 198,206','M330,206 Q340,214 348,208','M256,190 Q262,204 256,216'];
  seg(h,'button',function(b){mode=b.dataset.m;draw();});
  function draw(){var n=+inp.value;var s=svgOf(h,W,H);el('rect',{x:0,y:0,width:W,height:H,fill:'#fbfcfd'},s);
    el('path',{d:'M170,80 Q260,60 350,80 L362,236 L158,236Z',fill:'#F4F2EE',stroke:SH.ink,'stroke-width':2.4},s);
    el('path',{d:'M170,84 L130,210 L160,214 L188,140Z M350,84 L390,210 L360,214 L332,140Z',fill:'#F4F2EE',stroke:SH.ink,'stroke-width':2.2},s);
    // 치마
    var pleats=Math.max(0,Math.round(n*1.8));el('path',{d:'M158,236 L362,236 L404,380 L116,380Z',fill:'#34363F',stroke:SH.ink,'stroke-width':2.4},s);
    if(n>3)el('path',{d:'M150,258 Q260,272 370,258',fill:'none',stroke:'#c8cad6','stroke-width':1.6},s);
    for(var i=1;i<=pleats;i++){var t=i/(pleats+1);el('line',{x1:158+t*204,y1:240,x2:116+t*288,y2:376,stroke:'#8d90a0','stroke-width':1.3},s);}
    for(var j=0;j<Math.min(n,LINES.length);j++)foldLine(s,LINES[j],'#8a8578',1.8);
    if(n>=7){foldLine(s,'M260,84 L260,236','#b5ae9e',1.2);foldLine(s,'M188,140 L182,236 M332,140 L338,236','#b5ae9e',1.2);}
    var r=RANGE[mode],st=n<r[0]?'비닐 느낌(너무 적음)':n>r[1]?'베낀 느낌(너무 많음)':'알맞음';
    ktxt(s,20,30,r[2]+' 알맞은 구간 '+r[0]+'~'+r[1],{size:13,fill:C.ink,weight:700});
    out(h).innerHTML='정보량 <b>'+n+'</b> · 주름치마 선 '+pleats+'줄 → '+r[2]+' 기준 <b>'+st+'</b>'+(n<=3?' · 허리 부푼 선을 지워 옷이 몸에 붙어 보이고, 치마가 한 덩어리로 읽힙니다.':'')+(n>=7?' · 솔기 선까지 보입니다.':'');}
  onIn(inp,draw);draw();};

P.p1_order=function(h){var W=520,H=420;var done=[],warn='';
  var bs=ctl(h).querySelectorAll('button');bs.forEach(function(b){b.addEventListener('click',function(){var v=b.dataset.s;if(v==='r'){done=[];warn='';draw();return;}v=+v;if(done.indexOf(v)>=0)return;
    if(v!==done.length)warn='순서가 어긋났습니다! 지금은 '+['① 떨어지는·약속된','② 입체','③ 섬','④ 진한 2차','⑤ 정리'][done.length]+' 차례입니다. 진한 그림자를 먼저 넣으면 넓은 그림자가 갈 곳이 없어집니다.';else warn='';
    done.push(v);draw();});});
  function draw(){var s=svgOf(h,W,H);el('rect',{x:0,y:0,width:W,height:H,fill:'#fbfcfd'},s);
    var T=torso(s,{cx:260,top:120,col:'#D4B48A',pants:false,len:240});
    var on=function(i){return done.indexOf(i)>=0;};var sh='#9c7f5c',sh2='#6e573c';
    if(on(0)){el('path',{d:'M222,124 Q260,150 298,124 L292,140 Q260,160 228,140Z',fill:sh,opacity:.85},s);el('path',{d:'M175,152 L195,170 L190,200 L172,190Z',fill:sh,opacity:.8},s);}
    if(on(1)){el('path',{d:'M330,140 Q350,150 355,138 L343,360 L320,360 Q330,250 330,140Z',fill:sh,opacity:.8},s);}
    if(on(2)){[[240,220],[275,262],[230,300],[290,320]].forEach(function(p){el('path',{d:'M'+p[0]+','+p[1]+' q10,-6 18,4 q-8,12 -18,-4Z',fill:sh,opacity:.85},s);});}
    if(on(3)){el('path',{d:'M340,170 L346,174 L338,330 L332,330Z',fill:sh2},s);el('path',{d:'M226,130 Q260,146 294,130 L292,134 Q260,150 228,134Z',fill:sh2},s);}
    if(on(4)){el('path',{d:'M200,150 Q220,140 236,150',fill:'none',stroke:'#fff7e8','stroke-width':4,opacity:.9},s);}
    var order=done.every(function(v,i){return v===i;});
    ktxt(s,20,30,'쌓은 순서: '+(done.length?done.map(function(v){return ['①','②','③','④','⑤'][v];}).join(' → '):'(아직 없음)'),{size:13,fill:order?C.ink:C.red,weight:700});
    out(h).innerHTML=(warn?'<span class="alert">'+warn+'</span> ':'')+(done.length===5&&order?'<b>다섯 단계 완성!</b> 넓은 그림자 위에 작은 그림자가 차곡차곡 쌓였습니다.':done.length===5?'완성했지만 순서가 섞였습니다. ‘처음부터’를 눌러 순서대로 다시 해 보세요.':'다음 단계를 누르세요.');}
  draw();};

P.p1_blur=function(h){var c=ctl(h),inp=c.querySelector('input[type=range]'),chk=c.querySelector('input[type=checkbox]'),W=520,H=300;var cv=canvasOf(h,W,H),ctx=cv.getContext('2d');
  function draw(){var r=+inp.value,w=r*0.35,PX=22;ctx.fillStyle='#fbfcfd';ctx.fillRect(0,0,W,H);
    function shape(x0,rad,label){var wpx=rad*0.35*PX,R=rad*PX/2+20;var cx=x0+110,y0=50,y1=230;
      for(var x=cx-R;x<=cx+R;x++){var u=(x-cx)/R;if(Math.abs(u)>1)continue;var nx=u;var lam=-0.6*nx+0.8*Math.sqrt(1-nx*nx);var term=0.15;var dist=(lam-term);var soft=wpx/R;var t=clamp(0.5+dist/(soft+0.001),0,1);
        for(var y=y0;y<y1;y+=2){var base=chk.checked?lerp(1,0.86,(y-y0)/(y1-y0)):1;var v=lerp(0.55,1,t)*base;ctx.fillStyle=rgb([212*v,180*v,138*v]);ctx.fillRect(x,y,1.2,2);}}
      ctx.strokeStyle='#2a2230';ctx.lineWidth=2;ctx.strokeRect(cx-R,y0,2*R,y1-y0);ctx.fillStyle='#16212b';ctx.font='13px '+KFONT;ctx.textAlign='center';ctx.fillText(label+' · 흐린 폭 '+f2(rad*0.35,2)+'cm',cx,y1+22);}
    shape(10,1,'날카로운 주름(반지름 1)');shape(270,r,'반지름 '+r);
    out(h).innerHTML='흐린 폭 = '+r+' × 0.35 = <b>'+f2(w,2)+'cm</b> (왼쪽 기준 0.35cm의 <b>'+f2(w/0.35,1)+'배</b>)'+(chk.checked?' · 바탕 그라데이션이 위아래 입체를 한 번 더 강조합니다.':'');}
  onIn(inp,draw);chk.addEventListener('change',draw);draw();};

/* ===================== 2부 ===================== */
P.p2_ease=function(h){var inp=ctl(h).querySelector('input');var api;var last={};
  function setup(cl){var e=+inp.value/100;var nx=cl.nx,sp=cl.sp,half=(nx-1)/2*sp/(1+e);cl.pin={};
    for(var i=0;i<nx;i+=1){if(i%3!==0&&i!==nx-1)continue;var k=cl.idx(i,0);var x=-half+i*(2*half/(nx-1));cl.pin[k]=[x,0,0];cl.p[k]=cl.pin[k].slice();cl.o[k]=cl.pin[k].slice();}}
  function opts(){return {g:0.012,stiff:0.25,report:function(cl){var e=+inp.value;var f=cl.folds();var body=84;out(h).innerHTML='여유율 <b>'+e+'%</b> · 몸 둘레 84cm라면 옷 둘레 '+f2(body*(1+e/100),1)+'cm, 남는 천 <b>'+f2(body*e/100,1)+'cm</b> · 아래쪽 주름 굴곡 <b>'+f+'</b>개'+(e<=10?' — 남는 천이 적어 거의 평평합니다.':e>=30?' — 남는 천이 처지며 굵은 주름이 됩니다.':'');}};}
  api=runCloth(h,setup,opts);inp.addEventListener('change',function(){api.reset();});};

var POSE2={stand:{c:[[-1,0],[1,0]],f:[[[-90,40],[-80,190]],[[90,40],[86,190]],[[-30,60],[-36,200]]],t:'차렷: 어깨가 유일한 큰 접점 → 처짐 주름이 아래로 흐릅니다.',hem:0},
 up:{c:[[-1,-14],[1,-14],[-0.82,30],[0.82,30]],f:[[[-70,20],[-40,40]],[[70,20],[40,40]],[[-80,60],[-60,120]],[[80,60],[60,120]]],t:'팔 올리기: 어깨에 모임 주름, 옷이 위로 당겨져 배는 평평하고 밑단이 올라갑니다.',hem:22},
 cross:{c:[[-0.4,120],[0.4,118],[-1,0],[1,0]],f:[[[-90,40],[-30,118]],[[90,40],[30,116]],[[-60,150],[-30,128]],[[60,150],[30,126]]],t:'팔짱: 팔이 닿은 곳이 접점 → 주름이 팔 쪽으로 모입니다.',hem:6},
 arch:{c:[[-0.9,190],[0.9,190],[-1,0],[1,0]],f:[[[-40,60],[-80,180]],[[40,60],[80,180]],[[0,70],[-60,186]],[[0,70],[60,186]]],t:'허리 젖히기: 허리가 접점 → 가슴과 겨드랑이에서 허리 쪽으로 당김 주름, 밑단이 조금 올라갑니다.',hem:10},
 pinch:{c:[[0.3,222],[-1,0]],f:[[[-90,30],[28,216]],[[-40,90],[26,214]],[[60,120],[32,212]]],t:'밑단 잡기: 손가락이 접점 → 어깨에서 그 점으로 비스듬한 당김 주름이 모입니다.',hem:0}};
P.p2_contacts=function(h){var pose='stand',W=520,H=440;seg(h,'button',function(b){pose=b.dataset.p;draw();});
  function draw(){var s=svgOf(h,W,H);el('rect',{x:0,y:0,width:W,height:H,fill:'#fbfcfd'},s);var p=POSE2[pose];var top=pose==='up'||pose==='arch'?200:150;
    var T=torso(s,{cx:260,top:top,pose:pose,hair:'#E9909A',hemUp:p.hem,len:230});
    p.f.forEach(function(f){arrow(s,260+f[0][0],top+f[0][1],260+f[1][0],top+f[1][1],C.purple,2.4);});
    p.c.forEach(function(c){var x=260+c[0]*T.sw*0.92,y=top+c[1]+(c[1]===0?10:0);dot2(s,x,y);});
    out(h).innerHTML=p.t+' · 접점 <b>'+p.c.length+'</b>곳'+(p.hem?', 밑단 약 '+Math.round(p.hem/8)+'cm 올라감':'');}
  draw();};

P.p2_hem=function(h){var c=ctl(h),inp=c.querySelector('input'),body='mid',W=540,H=420;
  c.querySelectorAll('button').forEach(function(b){b.addEventListener('click',function(){c.querySelectorAll('button').forEach(function(x){x.classList.remove('on');});b.classList.add('on');body=b.dataset.b;inp.value={slim:1,mid:4,muscle:6}[body];draw();});});
  function draw(){var d=+inp.value,L=30,rise=2*Math.sqrt(Math.pow(L/2,2)+d*d)-L,S=10;var s=svgOf(h,W,H);el('rect',{x:0,y:0,width:W,height:H,fill:'#fbfcfd'},s);
    var x0=200,y0=50,yb=y0+L*S;// 몸 단면(옆)
    var bump=body==='muscle'?'M'+x0+','+y0+' Q'+(x0+d*S*1.2)+','+(y0+60)+' '+(x0+d*S)+','+(y0+110)+' Q'+(x0+d*S*0.4)+','+(y0+180)+' '+(x0+8)+','+(yb)+'':'M'+x0+','+y0+' Q'+(x0+d*S*1.15)+','+(y0+L*S/2)+' '+x0+','+yb;
    el('path',{d:bump+' L'+(x0-90)+','+yb+' L'+(x0-90)+','+y0+'Z',fill:SH.sk,stroke:SH.ink,'stroke-width':2},s);
    // 옷 선: 어깨 → 튀어나온 점 → 아래
    var px=x0+d*S+6,py=y0+L*S/2;var hy=yb-rise*S;
    el('path',{d:'M'+(x0+4)+','+y0+' L'+px+','+py+' L'+(x0+4+d*S*0.15)+','+hy,fill:'none',stroke:C.teal,'stroke-width':4,'stroke-linejoin':'round'},s);
    el('line',{x1:x0+4,y1:y0,x2:x0+4,y2:yb,stroke:'#b9c0ca','stroke-dasharray':'5 5','stroke-width':2},s);
    el('line',{x1:x0+20,y1:yb,x2:x0+120,y2:yb,stroke:C.muted,'stroke-width':1.5},s);el('line',{x1:x0+20,y1:hy,x2:x0+120,y2:hy,stroke:C.orange,'stroke-width':1.5},s);
    if(rise>0.2)arrow(s,x0+110,yb,x0+110,hy+4,C.orange,2);ktxt(s,x0+126,(yb+hy)/2+4,'밑단 '+f2(rise,2)+'cm ↑',{size:13,fill:C.orange,weight:700});
    if(d>0){dot2(s,px,py,7);ktxt(s,px+12,py-8,'새 접점',{size:12,fill:SH.hot});foldLine(s,'M'+px+','+(py+8)+' Q'+(px-6)+','+(py+50)+' '+(px-10)+','+(py+90),C.purple,2);}
    ktxt(s,20,24,'옆에서 본 단면 · 어깨에서 밑단까지 30cm',{size:12.5,fill:C.ink});
    out(h).innerHTML='2 × √(15² + '+d+'²) − 30 = <b>'+f2(rise,2)+'cm</b> 올라감 · '+({slim:'마른 체형: 접점이 적어 처짐 주름이 조금',mid:'보통 체형: 튀어나온 곳 아래로 처짐 주름',muscle:'근육형: 가슴근육·어깨가 접점, 허리에 남는 천이 고임'})[body];}
  onIn(inp,draw);draw();};

P.p2_shade=function(h){var c=ctl(h),inp=c.querySelector('input'),mode='shade',W=540,H=400;seg(h,'button',function(b){mode=b.dataset.m;draw();});
  function draw(){var a=+inp.value;var s=svgOf(h,W,H);el('rect',{x:0,y:0,width:W,height:H,fill:'#fbfcfd'},s);var Lx=Math.sin(rad(a)),Ly=Math.cos(rad(a));
    // 단면
    var x0=40,x1=500,yb=120,A=26,N=5;var pts=[];for(var x=x0;x<=x1;x+=2){var u=(x-x0)/(x1-x0)*N*2*Math.PI;pts.push([x,yb-A*(0.5+0.5*Math.sin(u-Math.PI/2))]);}
    for(var i=1;i<pts.length;i++){var p=pts[i-1],q=pts[i];var tx=q[0]-p[0],ty=q[1]-p[1],l=Math.hypot(tx,ty);var nx=ty/l,ny=-tx/l;if(ny>0){nx=-nx;ny=-ny;}var br=nx*(-Lx)+(-ny)*Ly;// 빛은 위(−y)에서
      el('line',{x1:p[0],y1:p[1],x2:q[0],y2:q[1],stroke:br<0.75?'#6b4fb0':'#d9d2ee','stroke-width':6},s);}
    var lx=270-Lx*80,ly=20;arrow(s,lx,ly,lx+Lx*50,ly+Ly*40,C.orange,3);ktxt(s,lx-30,16,'빛',{size:13,fill:C.orange,weight:700});
    ktxt(s,40,150,'주름 단면 — 진한 보라가 그림자 비탈',{size:12,fill:C.muted});
    // 앞에서 본 모습
    el('rect',{x:40,y:170,width:460,height:210,fill:'#fbfbfd',stroke:SH.ink,'stroke-width':2},s);var lines=0;
    for(var k=0;k<N;k++){var cx=x0+(k+0.5)*(x1-x0)/N;var side=a<0?1:-1;
      if(mode!=='line'){var sx=cx+side*6;el('path',{d:'M'+sx+',190 q'+(side*16)+',90 '+(side*4)+',170 q'+(side*-10)+',-80 '+(side*-4)+',-170Z',fill:'#c9c2e6',opacity:Math.abs(a)<5?0.3:0.95},s);}
      if(mode!=='shade'){foldLine(s,'M'+cx+',186 q6,90 0,180','#5a5470',2);lines++;}}
    out(h).innerHTML='빛 '+(a<0?'왼쪽':a>0?'오른쪽':'바로 위')+(a===0?' — 양쪽 비탈이 비슷해 주름이 약하게 보입니다.':' → 그림자는 각 산의 <b>'+(a<0?'오른쪽':'왼쪽')+' 비탈</b>')+' · 선 '+lines+'줄'+(mode==='line'?' — 다섯 줄이 같은 무게라 복잡합니다.':mode==='shade'?' — 선 없이도 볼록함이 보입니다.':'');}
  onIn(inp,draw);draw();};

/* ===================== 3부 ===================== */
P.p3_wave=function(h){var c=ctl(h),inp=c.querySelector('input'),W=540,H=320;
  c.querySelectorAll('button').forEach(function(b){b.addEventListener('click',function(){c.querySelectorAll('button').forEach(function(x){x.classList.remove('on');});b.classList.add('on');inp.value={knit:1,shirt:1.5,coat:3}[b.dataset.t];draw();});});
  function draw(){var t=+inp.value,lam=3*Math.pow(t,0.75),n=30/lam;var s=svgOf(h,W,H);el('rect',{x:0,y:0,width:W,height:H,fill:'#fbfcfd'},s);
    var x0=30,x1=510,S=(x1-x0)/30,A=6+lam*3.2;var d='',d2='';for(var x=0;x<=30;x+=0.05){var y=160-A*Math.sin(x/lam*2*Math.PI);d+=(x?'L':'M')+(x0+x*S)+','+y;d2+=(x?'L':'M')+(x0+x*S)+','+(y+4+t*3);}
    el('path',{d:d+' '+d2.replace('M','L').split('L').reverse().filter(Boolean).map(function(q,i){return (i?'L':'L')+q;}).join(''),fill:'#D4B48A',stroke:'none',opacity:.6},s);
    el('path',{d:d,fill:'none',stroke:SH.ink,'stroke-width':2},s);el('path',{d:d2,fill:'none',stroke:SH.ink,'stroke-width':2},s);
    arrow(s,6,160,26,160,C.purple,3);arrow(s,534,160,514,160,C.purple,3);
    for(var k=0;k<=Math.floor(n);k++){var xx=x0+k*lam*S;if(xx>x1)break;el('line',{x1:xx,y1:250,x2:xx,y2:262,stroke:C.teal,'stroke-width':2},s);}
    el('line',{x1:x0,y1:256,x2:x1,y2:256,stroke:C.teal,'stroke-width':1.5},s);ktxt(s,270,284,'폭 30cm · 주름 간격 '+f2(lam,2)+'cm',{size:13,anchor:'middle',fill:C.ink});
    out(h).innerHTML='두께 <b>'+t+'배</b> → 간격 = 3 × '+t+'^(3/4) = <b>'+f2(lam,2)+'cm</b>('+f2(Math.pow(t,0.75),2)+'배) · 폭 30cm에 주름 약 <b>'+Math.round(n)+'</b>개';}
  onIn(inp,draw);draw();};

P.p3_diamond=function(h){var inp=ctl(h).querySelector('input'),W=300,H=220;var cv=canvasOf(h,W,H,520),ctx=cv.getContext('2d');
  function g(u,k){var c=Math.cos(u);var sq=c>=0?1:-1;var soft=Math.max(-1,Math.min(1,c*(1+k*12)));return lerp(c,soft,k);}
  function draw(){var k=+inp.value/100;var img=ctx.createImageData(W,H),D=img.data;var dark=0,tot=0;
    for(var y=0;y<H;y++)for(var x=0;x<W;x++){var u=(x+0.75*y)*0.075,v=(x-0.75*y)*0.075+1.3;var val=g(u,k)+g(v,k);var sh=val<-0.9;tot++;if(sh)dark++;
      var col=sh?[178,170,206]:[244,242,238];var i=(y*W+x)*4;D[i]=col[0];D[i+1]=col[1];D[i+2]=col[2];D[i+3]=255;}
    ctx.putImageData(img,0,0);
    out(h).innerHTML='꺾임 <b>'+Math.round(k*100)+'</b> → 그림자 모양: <b>'+(k<0.35?'둥근 덩어리(니트·저지)':k<0.7?'반쯤 각진 모양':'각진 마름모(셔츠·정장)')+'</b> · 두 방향 주름의 그림자 비탈이 겹친 곳만 어둡습니다 · 그림자 면적 '+Math.round(dark/tot*100)+'%';}
  onIn(inp,draw);draw();};

var MEM={knit:[0.02,'니트'],shirt:[0.05,'셔츠'],coat:[0.1,'울 코트']};
P.p3_memory=function(h){var c=ctl(h),inp=c.querySelector('input'),mat='coat',W=540,H=360;
  c.querySelectorAll('button').forEach(function(b){b.addEventListener('click',function(){c.querySelectorAll('button').forEach(function(x){x.classList.remove('on');});b.classList.add('on');mat=b.dataset.t;draw();});});
  function draw(){var n=+inp.value,p=MEM[mat][0],m=1-Math.pow(1-p,n);var s=svgOf(h,W,H);el('rect',{x:0,y:0,width:W,height:H,fill:'#fbfcfd'},s);
    var col=mat==='coat'?'#8a6a4a':mat==='shirt'?'#f4f6fb':'#D4B48A';
    el('path',{d:'M30,70 L300,70 Q312,100 300,130 L30,130Z',fill:col,stroke:SH.ink,'stroke-width':2.4},s);ktxt(s,40,58,'편 팔 · 팔꿈치는 가운데',{size:12,fill:C.muted});
    for(var i=0;i<4;i++){var x=150+i*9;el('path',{d:'M'+x+',76 q6,12 0,24 q-6,12 0,24',fill:'none',stroke:SH.ink,'stroke-width':1.6,opacity:m},s);el('path',{d:'M'+(x+3)+',80 q8,10 2,20 q-6,10 0,18 q-4,-10 -2,-18Z',fill:'#5a4630',opacity:m*0.55},s);}
    // 곡선
    var gx=330,gy=40,gw=190,gh=140;el('rect',{x:gx,y:gy,width:gw,height:gh,fill:'#fff',stroke:'#d5dbe2'},s);
    Object.keys(MEM).forEach(function(kk){var d='';for(var t=0;t<=30;t++){var v=1-Math.pow(1-MEM[kk][0],t);d+=(t?'L':'M')+(gx+t/30*gw)+','+(gy+gh-v*gh);}el('path',{d:d,fill:'none',stroke:kk===mat?C.orange:'#c3cad4','stroke-width':kk===mat?3:1.5},s);});
    el('circle',{cx:gx+n/30*gw,cy:gy+gh-m*gh,r:5,fill:C.orange},s);ktxt(s,gx,gy+gh+18,'굽힌 횟수 0 → 30',{size:11.5});ktxt(s,gx,gy-6,'남은 자국',{size:11.5});
    ktxt(s,30,200,MEM[mat][1]+' · p = '+p,{size:14,fill:C.ink,weight:700});
    out(h).innerHTML='남은 자국 = 1 − (1 − '+p+')<sup>'+n+'</sup> = <b>'+f2(m,2)+'</b>'+(m>0.5?' — 팔을 펴도 자국이 뚜렷합니다. 물결 그림자로 살짝 넣습니다.':m>0.2?' — 옅은 자국이 남습니다.':' — 거의 매끈합니다.');}
  onIn(inp,draw);draw();};

var SOFT={blouse:1.5,shirt:1,knit:1.5,vest:0.5,jacket:0.5,cardigan:1.5};var NAME3={blouse:'블라우스',shirt:'셔츠',knit:'니트',vest:'조끼',jacket:'재킷',cardigan:'카디건',none:'없음'};
P.p3_layers=function(h){var c=ctl(h),sel=c.querySelectorAll('select'),chk=c.querySelector('input'),W=540,H=300;
  function draw(){var inn=sel[0].value,outr=sel[1].value,bent=chk.checked;var sc=bent?4:2;var reg=[];
    var hasSleeve=outr==='jacket'||outr==='cardigan';
    if(outr==='none'){reg.push([NAME3[inn]+' 소매',sc,SOFT[inn]]);reg.push([NAME3[inn]+' 몸판',1,SOFT[inn]]);}
    else{if(hasSleeve)reg.push([NAME3[outr]+' 소매',sc,SOFT[outr]]);else reg.push([NAME3[inn]+' 소매',sc,SOFT[inn]]);reg.push([NAME3[outr]+' 몸판',1,SOFT[outr]]);}
    var H2=70+reg.length*70;var s=svgOf(h,W,H2);el('rect',{x:0,y:0,width:W,height:H2,fill:'#fbfcfd'},s);var mx=0,best='';var tot=0;
    reg.forEach(function(r,i){var v=r[1]*r[2];tot+=v;if(v>mx){mx=v;best=r[0];}el('rect',{x:170,y:40+i*70,width:v/6*330,height:36,rx:6,fill:i===0?C.teal:C.purple},s);ktxt(s,160,64+i*70,r[0],{size:13,anchor:'end',fill:C.ink});ktxt(s,176+v/6*330,64+i*70,r[1]+' × '+r[2]+' = '+f2(v,2),{size:12.5,fill:C.ink});});
    ktxt(s,20,24,'보이는 부위의 예상 주름 수 (접점 × 부드러움)',{size:12.5,fill:C.muted});
    out(h).innerHTML='주름이 가장 많이 몰리는 곳: <b>'+best+'</b>('+f2(mx,2)+')'+(outr==='vest'?' · 조끼는 소매가 없어 접점이 어깨 1곳뿐입니다.':'')+(!bent?' · 팔을 펴면 소매 접점이 2곳으로 줄어듭니다.':'');}
  sel.forEach(function(x){x.addEventListener('change',draw);});chk.addEventListener('change',draw);chk.checked=true;draw();};

/* ===================== 4부 ===================== */
P.p4_skirt=function(h){var c=ctl(h),ins=c.querySelectorAll('input[type=range]'),chk=c.querySelector('input[type=checkbox]'),W=540,H=400;
  function draw(){var v=+ins[0].value,ph=+ins[1].value/100,lift=2*v*v;var s=svgOf(h,W,H);el('rect',{x:0,y:0,width:W,height:H,fill:'#fbfcfd'},s);
    var cx=250,wy=110,hemY=300-lift*3,sw=Math.sin(ph*2*Math.PI);
    // 다리
    var fl=[cx+40*sw,380],bl=[cx-40*sw,380];el('line',{x1:cx+10,y1:250,x2:fl[0],y2:fl[1],stroke:'#2a2230','stroke-width':22,'stroke-linecap':'round'},s);el('line',{x1:cx-10,y1:250,x2:bl[0],y2:bl[1],stroke:'#2a2230','stroke-width':22,'stroke-linecap':'round'},s);
    // 치마(옆에서, 오른쪽으로 걷는 중): 앞쪽은 다리에 걸리고 뒤쪽은 흐름
    var back=cx-60-lift*2.2,front=cx+56;var hem=[];for(var i=20;i>=0;i--){var t=i/20;var x=lerp(back,front,t);var y=hemY+Math.sin(t*Math.PI*3+ph*6)*(2+lift*0.9)*(1-t*0.6);hem.push(x.toFixed(1)+','+y.toFixed(1));}
    el('path',{d:'M'+(cx-34)+','+wy+' L'+(cx+34)+','+wy+' L'+hem.join(' L')+' Z',fill:'#34363F',stroke:SH.ink,'stroke-width':2.2},s);
    el('path',{d:'M'+(cx-30)+','+(wy+30)+' L'+(cx+30)+','+(wy+30),stroke:'#8d90a0','stroke-width':1.5},s);ktxt(s,cx+40,wy+30,'꿰맨 곳 — 여기부터 부풂',{size:11.5});
    // 앞치마 프릴(앞쪽 밑단 근처)
    for(var k=0;k<6;k++){var t2=k/5;var x0=lerp(cx-10,front-4,t2),y0=hemY-26;var ang=chk.checked?lerp(-0.25,0.45,t2):lerp(0.45,-0.25,t2);el('line',{x1:x0,y1:y0,x2:x0+Math.sin(ang)*22,y2:y0+Math.cos(ang)*22,stroke:'#f4f2ee','stroke-width':3},s);}
    if(v>0)[0,1,2].forEach(function(k){arrow(s,cx+150,hemY-60+k*20,cx+110,hemY-60+k*20+6,'#9fb4d8',2);});ktxt(s,cx+120,hemY-80,'공기',{size:12,fill:'#5f7fb8'});
    arrow(s,40,40,100,40,C.ink,2);ktxt(s,40,30,'걷는 방향',{size:12});
    out(h).innerHTML='들림 = 2 × '+v+'² = <b>'+f2(lift,1)+'cm</b>'+(v>0?' · 밑단은 뒤쪽으로 물결칩니다.':' · 서 있으면 곧게 내려옵니다.')+(chk.checked?' 프릴은 치마가 퍼지는 방향을 따릅니다.':' <span class="alert">프릴이 퍼짐과 반대로 기울어 어색합니다.</span>');}
  ins.forEach(function(i){onIn(i,draw);});chk.addEventListener('change',draw);draw();};

P.p4_pleats=function(h){var c=ctl(h),inp=c.querySelector('input'),mode='side',W=540,H=420;seg(h,'button',function(b){mode=b.dataset.m;draw();});
  function draw(){var phi=rad(+inp.value),N=16,R=110,cx=270,cy=130;var s=svgOf(h,W,H);el('rect',{x:0,y:0,width:W,height:H,fill:'#fbfcfd'},s);
    ktxt(s,20,24,'위에서 본 치마 (아래쪽이 보는 사람)',{size:12,fill:C.muted});var vis=0,cols=[];
    for(var i=0;i<N;i++){var a=i/N*2*Math.PI;var a2=(i+1)/N*2*Math.PI;var dir=mode==='side'?1:(i%2?1:-1);
      var p1=[cx+Math.sin(a)*R,cy+Math.cos(a)*R],p2=[cx+Math.sin(a2)*R,cy+Math.cos(a2)*R],pin=[cx+Math.sin(a+(dir>0?0.6:0.4)*(a2-a))*(R-16),cy+Math.cos(a+(dir>0?0.6:0.4)*(a2-a))*(R-16)];
      // 바깥 면 p1→pin? 톱니: p1 → pin(안쪽) → p2
      var nOut=a+(a2-a)/2,nBack=nOut+dir*rad(70);var seeO=Math.cos(nOut-phi)>0,seeB=Math.cos(nBack-phi)>0&&Math.cos(nOut-phi)>-0.2;
      el('path',{d:'M'+p1+' L'+pin+' L'+p2,fill:'none',stroke:'#34363F','stroke-width':2},s);
      if(seeB&&Math.cos(nOut-phi)>-0.2){el('line',{x1:(dir>0?pin:p1)[0],y1:(dir>0?pin:p1)[1],x2:(dir>0?p2:pin)[0],y2:(dir>0?p2:pin)[1],stroke:C.blue,'stroke-width':4},s);vis++;}
      var xs=Math.sin(nOut-phi);if(Math.cos(nOut-phi)>0)cols.push([xs,seeB,dir]);}
    var ex=cx+Math.sin(phi)*(R+70),ey=cy+Math.cos(phi)*(R+70);el('circle',{cx:ex,cy:ey,r:9,fill:C.orange},s);ktxt(s,ex+12,ey+4,'눈',{size:12,fill:C.orange});
    // 앞에서 본 띠
    var y0=290,y1=400,x0=60,x1=480;el('rect',{x:x0,y:y0,width:x1-x0,height:y1-y0,fill:'#34363F'},s);cols.sort(function(p,q){return p[0]-q[0];});
    cols.forEach(function(cc){var x=lerp(x0,x1,(cc[0]+1)/2);el('line',{x1:x,y1:y0,x2:x,y2:y1,stroke:'#8d90a0','stroke-width':1.2},s);if(cc[1])el('rect',{x:x+(cc[2]>0?0:-9),y:y0,width:9,height:y1-y0,fill:'#1d2030'},s);});
    ktxt(s,x0,y0-8,'앞에서 본 모습 — 검은 띠가 보이는 뒷면(그림자)',{size:12,fill:C.muted});
    out(h).innerHTML=(mode==='side'?'한 방향 접기':'맞주름')+' · 보이는 뒷면 <b>'+vis+'</b>개'+(mode==='side'?' — 모두 같은 쪽을 향합니다. 보는 방향을 반대로 돌리면 반대쪽 절반에서 보입니다.':' — 양쪽 방향 뒷면이 짝지어 보입니다.');}
  onIn(inp,draw);draw();};

P.p4_bend=function(h){var ins=ctl(h).querySelectorAll('input'),W=540,H=380;
  function draw(){var th=+ins[0].value,T=+ins[1].value,diff=T*rad(th);var s=svgOf(h,W,H);el('rect',{x:0,y:0,width:W,height:H,fill:'#fbfcfd'},s);
    var S=6,jx=290,jy=230,len=190,r=T*S/2;var a=rad(th);
    // 위팔(왼쪽 수평), 아래팔(회전)
    var ux=jx-len,ex=jx+Math.cos(-a)*len,ey=jy+Math.sin(-a)*len;
    el('line',{x1:ux,y1:jy,x2:jx,y2:jy,stroke:'#34363F','stroke-width':T*S,'stroke-linecap':'round'},s);el('line',{x1:jx,y1:jy,x2:ex,y2:ey,stroke:'#34363F','stroke-width':T*S,'stroke-linecap':'round'},s);
    // 안쪽(위) 모임 주름, 바깥(아래) 당김
    var nG=Math.max(0,Math.round(diff/3));for(var i=0;i<nG;i++){var t=(i+1)/(nG+1);var ang=-a*t;var px=jx+Math.cos(ang+Math.PI/2*-1)*0+Math.cos(ang)*(-14+28*t),py=jy-r+4;
      foldLine(s,'M'+(jx-30+i*10)+','+(jy-r+2)+' q4,'+(10+t*6)+' 8,0','#c9ccd6',2);}
    if(th>10){foldLine(s,'M'+(jx-70)+','+(jy+r-4)+' L'+(jx-6)+','+(jy+r-2),'#9aa0b4',1.6);foldLine(s,'M'+(jx+40*Math.cos(-a))+','+(jy+40*Math.sin(-a)+r-4)+' L'+(jx+6)+','+(jy+r-2),'#9aa0b4',1.6);}
    el('path',{d:'M'+(jx-r)+','+jy+' A'+r+','+r+' 0 0 0 '+(jx+r*Math.cos(Math.PI/2-a)*0+r*Math.sin(a)*0+r)+','+jy,fill:'none'},s);
    ktxt(s,40,jy-r-40,'안쪽: 모임 주름 '+nG+'줄',{size:13,fill:C.teal,weight:700});ktxt(s,40,jy+r+30,'바깥: 관절 쪽으로 당김',{size:13,fill:C.purple,weight:700});
    out(h).innerHTML='길이 차이 = '+T+' × '+f2(rad(th),3)+' = <b>'+f2(diff,1)+'cm</b>'+(th===0?' — 곧게 펴면 차이가 없습니다.':' — 안쪽에 남고, 바깥쪽은 모자라 팽팽합니다.');}
  ins.forEach(function(i){onIn(i,draw);});draw();};

P.p4_props=function(h){var cks=ctl(h).querySelectorAll('input'),W=520,H=460;
  function draw(){var on={};cks.forEach(function(x){on[x.dataset.k]=x.checked;});var s=svgOf(h,W,H);el('rect',{x:0,y:0,width:W,height:H,fill:'#fbfcfd'},s);
    var top=150;var T=torso(s,{cx:260,top:top,hair:'#1E1B22',col:'#fbfbfd',len:on.tuck?200:240});var cx=260,list=[];
    if(on.tuck){el('rect',{x:cx-T.hip-4,y:T.y2-4,width:2*T.hip+8,height:12,fill:'#3a2a1e'},s);[-50,-20,20,50].forEach(function(dx){foldLine(s,'M'+(cx+dx)+','+(T.y2-34)+' q'+(dx>0?6:-6)+',16 0,28',C.purple,2);});dot2(s,cx-T.hip+10,T.y2+2,6);dot2(s,cx+T.hip-10,T.y2+2,6);list.push('셔츠 넣기: 허리띠가 접점, 허리에 천이 고임');}
    else{[-50,40].forEach(function(dx){foldLine(s,'M'+(cx+dx)+','+(top+40)+' q'+(dx>0?-4:4)+',100 0,190',C.purple,2);});list.push('셔츠 꺼내기: 어깨에서 밑단까지 길게 처짐');}
    if(on.bag){var sx=cx-T.sw+16,sy=top+12;el('line',{x1:sx,y1:sy,x2:cx+T.hip+30,y2:top+250,stroke:'#7a4b2a','stroke-width':9},s);el('rect',{x:cx+T.hip+10,y:top+240,width:70,height:56,rx:8,fill:'#a0683e',stroke:SH.ink,'stroke-width':2},s);dot2(s,sx,sy);
      [[30,40],[60,24],[46,70]].forEach(function(d){arrow(s,sx+4,sy+8,sx+d[0],sy+d[1]+20,C.purple,2);});list.push('숄더백: 끈이 어깨를 눌러 접점, 주름이 몸통 쪽으로');}
    if(on.pack){[-1,1].forEach(function(d){el('line',{x1:cx+d*(T.sw-20),y1:top+6,x2:cx+d*(T.sw-14),y2:top+200,stroke:'#2e3442','stroke-width':8},s);dot2(s,cx+d*(T.sw-20),top+8,6);});dot2(s,cx-T.hip+6,top+200,7);dot2(s,cx+T.hip-6,top+200,7);
      [-1,1].forEach(function(d){foldLine(s,'M'+(cx+d*(T.hip-8))+','+(top+196)+' q'+(-d*16)+',-6 '+(-d*28)+',4',C.purple,2);});list.push('백팩: 어깨 끈 + 허리 뒤가 접점, 허리 옆에 모임 주름');}
    if(on.tie){el('path',{d:'M'+cx+','+(top+14)+' L'+(cx-10)+','+(top+28)+' L'+(cx+30)+','+(top+150)+' L'+(cx+40)+','+(top+140)+' L'+(cx+6)+','+(top+26)+'Z',fill:'#8a2b36',stroke:SH.ink,'stroke-width':1.5},s);arrow(s,cx+40,top+144,cx+90,top+170,C.orange,2.4);dot2(s,cx-6,top+12,6);foldLine(s,'M'+(cx-24)+','+(top+10)+' q10,10 18,4',C.purple,2);list.push('넥타이 당기기: 깃만 따라 끌려가고 셔츠 몸판은 거의 그대로');}
    out(h).innerHTML='접점 변화: '+list.map(function(t){return '<b>'+t.split(':')[0]+'</b>'+t.slice(t.indexOf(':'));}).join(' · ');}
  cks.forEach(function(x){x.addEventListener('change',draw);});draw();};

/* ===================== 5부 ===================== */
var OW={who:{haru:"Haru (adult lab assistant in her early twenties, long straight pink hair with navy streaks and a thick navy streak down the center of the bangs, two round hair buns, blue eyes)",sia:"Sia (adult maid intern in her early twenties, long straight jet-black hair, no headdress, gray eyes)",moa:"Moa (adult maid intern in her early twenties, long ash-beige wavy hair, white frilled headband with a white ribbon over the LEFT ear, amber eyes)",doctor:"the Professor (adult male scientist, dark charcoal spiky hair with a white streak, thick black eyebrows, teal rectangular glasses)"},
 gar:{tee:"a plain white crew-neck t-shirt with rolled-up jeans",cardigan:"a camel knit cardigan over a white blouse",coat:"a thick camel wool coat, double-breasted",vest:"a light blue cotton dress shirt with sleeves rolled up, a gray vest and a black tie",maid:"a charcoal-black long-sleeved maid dress with a long white frilled apron"},
 fit:{fitted:["fitted (about 7% ease), fabric close to the body, only thin tension folds where force is applied","딱 맞음"],regular:["regular fit (about 15% ease), a few medium folds","보통"],loose:["loose oversized fit (about 30% ease), dropped shoulder seams, fabric hanging away from the body with large soft drape folds","헐렁함"]},
 mat:{jersey:["soft medium-weight cotton jersey, rounded S-shaped folds, rounded soft shadows","부드러운 저지"],knit:["soft thick knit, broad rounded folds","니트"],crisp:["crisp cotton, sharp angular folds, diamond- and triangle-shaped shadows","빳빳한 면"],wool:["thick heavy wool, only a few broad folds, matte texture, slight memory creases at the elbows","두꺼운 울"],silk:["light silk, many fine flowing folds, long drape","가벼운 실크"]},
 act:{stand:["standing relaxed; folds start at the shoulders and drape down by gravity","서기"],up:["both arms raised; folds gather at the shoulders, the torso fabric is pulled up and flat, the hem rides up","팔 올리기"],walk:["walking to the right; the hem lifts slightly and flows backward, the front leg pulls the fabric","걷기"],sit:["sitting on a chair; fabric bunches behind the bent knees and inside the elbows, pulled taut over the knees","앉기"],bag:["carrying a shoulder bag; the strap presses into the shoulder and folds radiate from it toward the chest","가방 메기"]},
 light:{ul:"Lighting: soft daylight from the upper left; fold shadows on the lower right side of each fold ridge",ur:"Lighting: soft daylight from the upper right; fold shadows on the lower left side of each fold ridge"}};
function outfitPrompt(o){var parts=[],score=0,miss=[];
  if(o.who)parts.push('Character (keep exactly): '+OW.who[o.who]+'.');
  if(o.gar){parts.push('Outfit: '+OW.gar[o.gar]+'.');score++;}else miss.push('① 옷 종류');
  if(o.fit){parts.push('Fit: '+OW.fit[o.fit][0]+'.');score++;}else miss.push('② 핏');
  if(o.mat){parts.push('Fabric: '+OW.mat[o.mat][0]+'.');score++;}else miss.push('③ 소재');
  if(o.act){parts.push('Pose and contacts: '+OW.act[o.act][0]+'.');score++;}else miss.push('④ 동작과 접점');
  if(o.light){parts.push(OW.light[o.light]+'.');score++;}else miss.push('⑤ 빛과 주름 그림자');
  var neg=['no text','no logos','no watermark'];if(o.neg){neg.push('no revealing clothing','adult proportions, not childlike','no school uniform look');if(o.mat==='wool')neg.push('no fine crumpled wrinkles');if(o.fit==='loose')neg.push('no skin-tight fabric');score++;}else miss.push('⑥ 금지 목록');
  parts.push('Negative: '+neg.join(', ')+'.');return {text:parts.join('\n'),score:score,miss:miss};}
function outfitForm(host,onchange){var form=document.createElement('div');form.style.cssText='display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:8px 14px;width:100%';host.appendChild(form);
  var defs=[['who','캐릭터',[['haru','하루'],['sia','시아'],['moa','모아'],['doctor','박사']]],['gar','① 옷 종류',[['','(고르기)'],['tee','흰 티셔츠'],['cardigan','카디건'],['coat','울 코트'],['vest','셔츠와 조끼'],['maid','메이드복']]],
   ['fit','② 핏',[['','(고르기)'],['fitted','딱 맞음'],['regular','보통'],['loose','헐렁함']]],['mat','③ 소재',[['','(고르기)'],['jersey','부드러운 저지'],['knit','니트'],['crisp','빳빳한 면'],['wool','두꺼운 울'],['silk','가벼운 실크']]],
   ['act','④ 동작',[['','(고르기)'],['stand','서기'],['up','팔 올리기'],['walk','걷기'],['sit','앉기'],['bag','가방 메기']]],['light','⑤ 빛',[['','(고르기)'],['ul','왼쪽 위'],['ur','오른쪽 위']]]];
  var S={};defs.forEach(function(d){var l=document.createElement('label');l.style.cssText='display:flex;flex-direction:column;font-size:14px';l.innerHTML='<span>'+d[1]+'</span>';var sl=document.createElement('select');sl.name=d[0];sl.setAttribute('aria-label',d[1]);d[2].forEach(function(o){var op=document.createElement('option');op.value=o[0];op.textContent=o[1];sl.appendChild(op);});l.appendChild(sl);form.appendChild(l);S[d[0]]=sl;sl.addEventListener('change',onchange);});
  var nl=document.createElement('label');nl.style.cssText='display:flex;gap:6px;align-items:center;font-size:14px';nl.innerHTML='<input type="checkbox" name="neg"> ⑥ 금지 목록 넣기';form.appendChild(nl);var neg=nl.querySelector('input');neg.addEventListener('change',onchange);
  return function(){var o={};for(var k in S)o[k]=S[k].value;o.neg=neg.checked;return o;};}
P.p5_outfit=function(h){h.innerHTML='';var get=outfitForm(h,draw);var pb=document.createElement('div');pb.className='promptbox';pb.innerHTML='<b>조립된 옷 문장</b><pre aria-live="polite"></pre><button type="button" class="btn">복사하기</button> <span class="hint"></span>';h.appendChild(pb);
  pb.querySelector('button').addEventListener('click',function(){var t=pb.querySelector('pre').textContent,hint=pb.querySelector('.hint');if(navigator.clipboard)navigator.clipboard.writeText(t).then(function(){hint.textContent='복사했습니다.';},function(){hint.textContent='직접 선택해 복사하세요.';});else hint.textContent='직접 선택해 복사하세요.';});
  function draw(){var o=get();var r=outfitPrompt(o);pb.querySelector('pre').textContent=r.text;out(h).innerHTML='점검표 <b>'+r.score+' / 6</b>'+(r.miss.length?' · 빠진 조각: '+r.miss.join(', '):' <span class="alert">빠진 조각이 없습니다!</span>')+(o.mat==='silk'&&o.gar==='coat'?' · <span class="alert">울 코트에 실크 소재? 소재가 뒤바뀌었습니다(6부 f2).</span>':'');}
  draw();};
window.__lab={outfitPrompt:outfitPrompt};

P.p5_mask=function(h){var ins=ctl(h).querySelectorAll('input'),W=300,H=450;var cv=canvasOf(h,W,H,340),ctx=cv.getContext('2d');var K=W/512;
  function figure(){ctx.fillStyle='#fbfcfd';ctx.fillRect(0,0,W,H);ctx.lineWidth=2;ctx.strokeStyle='#2a2230';
    ctx.fillStyle='#A99AC8';ctx.beginPath();ctx.moveTo(156*K,250*K);ctx.lineTo(356*K,250*K);ctx.lineTo(380*K,560*K);ctx.lineTo(132*K,560*K);ctx.closePath();ctx.fill();ctx.stroke();
    ctx.fillStyle='#fbfbfd';ctx.fillRect(140*K,255*K,40*K,300*K);ctx.fillRect(332*K,255*K,40*K,300*K);
    ctx.fillStyle='#5b7fb8';ctx.fillRect(150*K,560*K,210*K,200*K);ctx.fillStyle='#F6D3B8';ctx.fillRect(236*K,200*K,40*K,52*K);
    ctx.beginPath();ctx.ellipse(256*K,150*K,62*K,70*K,0,0,7);ctx.fill();ctx.stroke();ctx.fillStyle='#E9909A';ctx.beginPath();ctx.ellipse(256*K,112*K,70*K,46*K,0,Math.PI,0);ctx.fill();
    ctx.beginPath();ctx.arc(208*K,74*K,24*K,0,7);ctx.arc(304*K,74*K,24*K,0,7);ctx.fill();ctx.fillStyle='#1E2F5C';ctx.fillRect(250*K,70*K,12*K,52*K);}
  function draw(){var sc=+ins[0].value/100,fe=+ins[1].value;figure();var mw=200*sc,mh=300*sc,mx=256-mw/2,my=255+150-mh/2-10*(sc-1)*10;my=405-mh/2;
    ctx.save();ctx.filter=fe?'blur('+(fe*K)+'px)':'none';ctx.fillStyle='rgba(232,115,26,.38)';ctx.fillRect(mx*K,my*K,mw*K,mh*K);ctx.restore();
    ctx.strokeStyle='#e8731a';ctx.setLineDash([6,4]);ctx.strokeRect(mx*K,my*K,mw*K,mh*K);ctx.setLineDash([]);
    var ratio=mw*mh/393216*100;var face=my<220,seam=sc<0.8;
    out(h).innerHTML='가림 영역 '+Math.round(mw)+' × '+Math.round(mh)+' = '+Math.round(mw*mh).toLocaleString()+' ÷ 393,216 = <b>'+f2(ratio,1)+'%</b>'+(face?' · <span class="alert">얼굴·머리까지 가려 다시 그려집니다.</span>':'')+(seam?' · <span class="alert">옷보다 작아 옛 옷의 소매·끈이 남습니다(이음매).</span>':'')+(!face&&!seam?' · 옷만 바뀌고 얼굴은 그대로입니다.':'')+(fe?' · 경계 '+fe+'px 흐림으로 이음매를 숨깁니다.':' · 경계를 흐리지 않으면 이음매가 보일 수 있습니다.');}
  ins.forEach(function(i){onIn(i,draw);});draw();};

var PRESET={jersey:[40,20,'저지(티셔츠)'],cotton:[50,50,'면 셔츠'],wool:[90,80,'울 코트'],silk:[15,0,'실크']};
P.p5_vfx=function(h){var c=ctl(h),wt=c.querySelector('[name=wt]'),st=c.querySelector('[name=st]'),api,name='저지(티셔츠)';
  c.querySelectorAll('button').forEach(function(b){b.addEventListener('click',function(){c.querySelectorAll('button').forEach(function(x){x.classList.remove('on');});b.classList.add('on');var p=PRESET[b.dataset.p];wt.value=p[0];st.value=p[1];name=p[2];api.reset();});});
  function setup(cl){pinMode(cl,2);}
  function opts(){var w=+wt.value/100,s=+st.value/100;return {g:0.004+0.016*w,stiff:0.02+0.9*s,report:function(cl){out(h).innerHTML='<b>'+name+'</b> · 무게 '+wt.value+' · 뻣뻣함 '+st.value+' → 가운데 처짐 <b>'+f2(cl.sag(),1)+'</b>, 주름 굴곡 <b>'+cl.folds()+'</b>개';}};}
  api=runCloth(h,setup,opts);[wt,st].forEach(function(x){x.addEventListener('change',function(){name='직접 고른 값';c.querySelectorAll('button').forEach(function(b){b.classList.remove('on');});api.reset();});});};

var STY5={pixel:[3,2,10,'픽셀','only 2–3 large folds, 2-tone shading, limited palette'],anime:[5,3,1,'애니풍','3–5 large folds, two-tone cel shading with a darker second shadow in the deepest folds'],semireal:[8,0,1,'반실사','6–8 folds including smaller ones, soft gradient shading'],photo:[12,0,1,'실사풍','all natural folds and fabric texture, realistic soft light']};
P.p5_style=function(h){var sty='anime',W=320,H=240;var cv=canvasOf(h,W,H,520),ctx=cv.getContext('2d');seg(h,'button',function(b){sty=b.dataset.s;draw();});
  function draw(){var p=STY5[sty];var t=document.createElement('canvas');t.width=W;t.height=H;var c=t.getContext('2d');c.fillStyle='#fbfcfd';c.fillRect(0,0,W,H);
    // 소매(원기둥) 음영
    for(var x=40;x<280;x++){for(var y=60;y<180;y+=1){var u=(y-120)/60;var b=-0.5*u+0.85*Math.sqrt(Math.max(0,1-u*u));var fold=0;for(var k=0;k<p[0];k++){var fx=60+k*(200/p[0])+((k*37)%11);var w=k<3?14:6;fold+=Math.exp(-Math.pow((x-fx)/w,2))*(k<3?0.5:0.25)*(0.75+0.25*Math.sin((y-60)/120*Math.PI));}var v=b-fold;
      if(p[1]===2)v=v>0.35?1:0.62;else if(p[1]===3)v=v>0.5?1:v>0.15?0.72:0.52;else v=0.5+0.5*clamp(v,0,1);if(sty==='photo')v+=((x*7+y*13)%9-4)/90;
      c.fillStyle=rgb([169*v+30,154*v+30,200*v+30]);c.fillRect(x,y,1,1);}}
    c.strokeStyle='#2a2230';c.lineWidth=2;c.strokeRect(40,60,240,120);ctx.clearRect(0,0,W,H);if(p[2]>1)pixelate(t,cv,p[2]);else ctx.drawImage(t,0,0);
    out(h).innerHTML='<b>'+p[3]+'</b>: 주름 '+p[0]+'개 · '+(p[1]?'그림자 '+p[1]+'단계':'부드러운 그라데이션')+' · 화풍 문장에 넣을 양: <code>'+p[4]+'</code>';}
  draw();};

/* ===================== 6부 ===================== */
var CHECK=['① 접점·흐름(주름이 어디서 시작하나)','② 핏(남는 천)','③ 소재(간격·꺾임·자국)','④ 빛(그림자가 빛 반대쪽인가)','⑤ 정보량·가림 영역'];
var FAILAT=[4,2,1,0,3,0,0,4];var FAILWHY=['그림체에 비해 잔주름 선이 너무 많습니다.','두꺼운 코트인데 실크처럼 잔주름이 흐릅니다.','오버핏인데 남는 천이 없습니다.','가방 끈이 옷을 누르지 않습니다 — 접점이 없습니다.','주름 그림자가 빛 쪽 비탈에 있습니다.','프릴이 치마 퍼짐과 반대로 기울었습니다.','한 방향 주름인데 양쪽 뒷면이 다 보입니다.','가림 영역이 얼굴·머리까지 닿았습니다.'];
P.p6_check=function(h){var c=ctl(h),sel=c.querySelector('select');h.innerHTML='';var list=document.createElement('div');list.style.cssText='display:flex;flex-direction:column;gap:6px';h.appendChild(list);var done=0;
  function build(){list.innerHTML='';done=0;CHECK.forEach(function(t,i){var b=document.createElement('button');b.type='button';b.className='btn';b.style.textAlign='left';b.textContent=t;b.addEventListener('click',function(){press(i,b);});list.appendChild(b);});out(h).innerHTML='점검표를 <b>위에서부터</b> 눌러 보세요.';}
  function press(i,b){var f=+sel.value,at=FAILAT[f];if(i!==done){out(h).innerHTML='순서대로! 먼저 <b>'+CHECK[done]+'</b>을 보세요. 큰 원리에서 작은 표현 순서입니다.';return;}
    if(i<at){b.style.borderColor=C.green;b.style.background='#ecf7ef';b.textContent=CHECK[i]+' — 통과';done++;out(h).innerHTML=CHECK[i]+' 통과. 다음 항목으로.';}
    else{b.style.borderColor=C.red;b.style.background='#fdeceb';b.textContent=CHECK[i]+' — 여기서 걸림';done=99;out(h).innerHTML='<b>'+CHECK[i]+'</b>에서 처음 걸렸습니다: '+FAILWHY[f]+' 아래 실패 카드 f'+(f+1)+'에서 고치는 조각을 보세요.';}}
  sel.addEventListener('change',build);build();};

/* ===================== 실전 연습장 ===================== */
function practice(){var root=document.getElementById('practice');if(!root)return;var tabs=root.querySelectorAll('.tabs button'),scenes=root.querySelectorAll('.scene');
  function show(id){tabs.forEach(function(b){b.classList.toggle('on',b.dataset.t===id);});scenes.forEach(function(s){s.classList.toggle('on',s.id===id);});if(history.replaceState)history.replaceState(null,'','#'+id);}
  tabs.forEach(function(b){b.addEventListener('click',function(){show(b.dataset.t);});});var hsh=(location.hash||'').slice(1);show([].some.call(scenes,function(s){return s.id===hsh;})?hsh:'fitting');
  fitting();fabric();workshop();desk();}
var MATP={knit:[1.5,1,'니트'],jersey:[1.2,1,'저지'],shirt:[1,1.5,'면 셔츠'],coat:[0.5,3,'울 코트']};
function fitting(){var S=document.getElementById('fitting');if(!S)return;var q=function(n){return S.querySelector('[name='+n+']');};var touched=false;
  function upd(){var body=+q('body').value,vol=+q('vol').value,cloth=+q('cloth').value,mat=q('mat').value,pose=q('pose').value;var ease=(cloth-body)/body*100;
    var rise=2*Math.sqrt(225+vol*vol)-30+(pose==='up'?3:0);var m=MATP[mat];var contacts={stand:3,up:4,cross:5}[pose]+(vol>=5?1:0);var folds=Math.max(0,contacts*m[0]*clamp(0.4+Math.max(0,ease)/40,0.4,1.4));var thick=3*Math.pow(m[1],0.75);
    board(S.querySelector('.board'),[['여유율',f2(ease,1)+'%',ease>=0],['밑단 올라감',f2(rise,1)+'cm',rise<6],['예상 주름 수',f2(folds,1)+'개',folds>0],['주름 간격',f2(thick,1)+'cm',true]]);
    var s=el('svg',{viewBox:'0 0 360 300',role:'img','aria-label':'피팅 모습'});var g1=S.querySelector('.g1');g1.innerHTML='';g1.appendChild(s);el('rect',{x:0,y:0,width:360,height:300,fill:'#fbfcfd'},s);
    var T=torso(s,{cx:180,top:pose==='up'?150:110,k:0.62,pose:pose==='cross'?'cross':pose,loose:clamp(ease/10,0,4),hemUp:rise*4,col:mat==='coat'?'#c49a6c':mat==='knit'?'#D4B48A':'#fbfbfd',hair:'#E9909A',len:200});
    var nF=Math.round(folds);for(var i=0;i<nF;i++){var x=180-T.hip+10+i*(2*T.hip-20)/Math.max(1,nF-1);foldLine(s,'M'+x+','+(T.top+40)+' q'+(i%2?5:-5)+','+(60)+' 0,'+(T.y2-T.top-50),C.purple,mat==='coat'?3.2:1.8);}
    var s2=el('svg',{viewBox:'0 0 360 200',role:'img','aria-label':'여유율과 주름 수 막대'});var g2=S.querySelector('.g2');g2.innerHTML='';g2.appendChild(s2);
    [['여유율 %',clamp(ease,0,50)/50,C.teal],['밑단 cm',clamp(rise,0,10)/10,C.orange],['주름 수',clamp(folds,0,8)/8,C.purple]].forEach(function(b,i){el('rect',{x:90,y:30+i*50,width:240*b[1],height:26,rx:5,fill:b[2]},s2);ktxt(s2,84,48+i*50,b[0],{size:12.5,anchor:'end',fill:C.ink});});
    var M=[ease>=25&&ease<=40,rise>=3,mat==='coat'&&folds<=3];if(touched)missions(S.querySelector('.missions'),M,true);
    say(S.querySelector('.talk'),[['doctor','e10','박사','여유율 '+f2(ease,1)+'%. '+(ease<10?'딱 맞는 핏이다. 접힐 천이 적다.':ease>25?'헐렁한 핏이다. 처짐 주름이 굵다.':'보통 핏이다.')],['haru','e10','조수','밑단은 2 × √(15² + '+vol+'²) − 30'+(pose==='up'?' + 팔 올리기 3':'')+' = '+f2(rise,1)+'cm 올라가요. 예상 주름 수는 접점 '+contacts+' × 부드러움 '+m[0]+' × 여유 보정 '+f2(clamp(0.4+Math.max(0,ease)/40,0.4,1.4),2)+' = '+f2(folds,1)+'개예요(여유 보정 = 0.4 + 여유율 ÷ 40, 0.4~1.4 사이 예시값).'],['fruitfly','e09','초파리',mat==='coat'?'울 코트는 간격이 넓어 주름이 굵고 적지.':'소재를 코트로 바꾸면 주름 수가 확 줄 거야.'],['jupanbot','e16','주판봇',ease<0?'옷이 몸보다 작아요! 그래도 입히겠습니다!':'주름은 많을수록 좋…지 않다고 배웠습니다!']]);}
  S.querySelectorAll('input,select').forEach(function(i){i.addEventListener(i.tagName==='SELECT'?'change':'input',function(){touched=true;upd();});});upd();}
function fabric(){var S=document.getElementById('fabric');if(!S)return;var q=function(n){return S.querySelector('[name='+n+']');};var host=S.querySelector('.g1'),g2=S.querySelector('.g2');var touched=false;var W=520,H=380;var cv=document.createElement('canvas');cv.width=W;cv.height=H;cv.style.cssText='width:100%;border-radius:10px';cv.setAttribute('role','img');cv.setAttribute('aria-label','천 시뮬레이션 그림');host.innerHTML='';host.appendChild(cv);var ctx=cv.getContext('2d');var cl,raf;
  function setup(){var gap=+q('gap').value/100,gather=q('gather').checked;cl=new Cloth(19,15,1);var nx=cl.nx;cl.pin={};function pin(i,pos){var k=cl.idx(i,0);cl.pin[k]=pos;cl.p[k]=pos.slice();cl.o[k]=pos.slice();}
    if(gather){for(var i=0;i<nx;i++)pin(i,[(i-(nx-1)/2)*0.42,0,(i%2?0.35:-0.35)]);}else{var half=(nx-1)/2*gap;pin(0,[-half,0,0]);pin(nx-1,[half,0,0]);}}
  function stats(){var folds=cl.folds(),sag=cl.sag();var st=+q('stiff').value;
    board(S.querySelector('.board'),[['가운데 처짐',f2(sag,1),sag>=3],['주름 굴곡',folds+'개',true],['뻣뻣함',st,true],['무게',q('wt').value,true]]);
    var M=[!q('gather').checked&&sag>=4,!q('gather').checked&&st>=70&&sag<4,q('gather').checked&&st<=30&&folds>=3];if(touched)missions(S.querySelector('.missions'),M,true);
    var s=el('svg',{viewBox:'0 0 360 200',role:'img','aria-label':'가운데 줄 단면(앞뒤 굴곡)'});g2.innerHTML='';g2.appendChild(s);el('rect',{x:20,y:20,width:330,height:150,fill:'#fbfcfd',stroke:'#d5dbe2'},s);var j0=Math.floor(cl.ny*0.6),d='';for(var i2=0;i2<cl.nx;i2++){var v=cl.p[cl.idx(i2,j0)];d+=(i2?'L':'M')+(30+i2*(310/(cl.nx-1)))+','+(95-v[2]*14);}el('path',{d:d,fill:'none',stroke:C.purple,'stroke-width':2.5},s);ktxt(s,185,190,'아래쪽 가로줄의 앞뒤 굴곡(주름 단면)',{size:12,anchor:'middle'});
    say(S.querySelector('.talk'),[['doctor','e10','박사',q('gather').checked?'모으면 남는 천이 세로 모임 주름이 된다. 뻣뻣할수록 굵고 적다.':'두 점 사이로 처진다. 무거울수록 많이 처진다.'],['moa','e10','모아','주름 굴곡 '+folds+'개, 가운데 처짐 '+f2(sag,1)+'이에요.'],['fruitfly','e09','초파리',st>=70?'뻣뻣함이 크면 울 코트처럼 굵은 주름만 남아.':'뻣뻣함을 올려 봐. 굴곡이 줄어들걸.'],['jupanbot','e16','주판봇',+q('wind').value>0?'바람이 불면 천이 한쪽으로 쏠립니다!':'값을 한꺼번에 다 바꾸면… 무엇 때문인지 모르겠군요.']]);}
  function run(){setup();var n=0;if(raf)cancelAnimationFrame(raf);function opts(){var st=+q('stiff').value/100,wt=+q('wt').value/100;return {g:0.004+0.016*wt,stiff:0.02+0.9*st,wind:+q('wind').value/100*0.004};}
    if(RM){for(var i=0;i<240;i++){var o=opts();cl.step(o.g,o.stiff,o.wind);}cl.draw(ctx,W,H,17,W/2,50);stats();return;}
    (function f(){var o=opts();cl.step(o.g,o.stiff,o.wind);cl.step(o.g,o.stiff,o.wind);cl.draw(ctx,W,H,17,W/2,50);n++;if(n%10===0)stats();if(n<240)raf=requestAnimationFrame(f);else stats();})();}
  S.querySelectorAll('input').forEach(function(i){i.addEventListener('change',function(){touched=true;run();});});run();}
function workshop(){var S=document.getElementById('workshop');if(!S)return;var touched=false;var get=outfitForm(S.querySelector('.ow'),function(){touched=true;upd();});var job=S.querySelector('[name=job]');job.addEventListener('change',function(){touched=true;upd();});
  function upd(){var o=get();var r=outfitPrompt(o);S.querySelector('.g1 pre').textContent=r.text;var need={swap:['fit','mat'],action:['act','light'],goods:['neg','light']}[job.value];var jobOk=need.every(function(k){return o[k];});
    board(S.querySelector('.board'),[['점검표',r.score+' / 6',r.score===6],['요청 상황 맞춤',jobOk?'맞음':'부족',jobOk],['소재 충돌',o.gar==='coat'&&o.mat==='silk'?'있음':'없음',!(o.gar==='coat'&&o.mat==='silk')],['나이 표기',o.neg?'성인 명시':'없음',o.neg]]);
    var s=el('svg',{viewBox:'0 0 360 200',role:'img','aria-label':'점검표 막대'});var g2=S.querySelector('.g2');g2.innerHTML='';g2.appendChild(s);['종류','핏','소재','동작','빛','금지'].forEach(function(t,i){var ok=[o.gar,o.fit,o.mat,o.act,o.light,o.neg][i];el('rect',{x:70,y:14+i*30,width:ok?260:40,height:20,rx:4,fill:ok?C.teal:'#e3e8ee'},s);ktxt(s,64,29+i*30,t,{size:12.5,anchor:'end',fill:C.ink});});
    var M=[r.score===6,o.fit==='loose'&&o.act==='up'&&/hem rides up/.test(r.text),o.mat==='wool'&&o.neg&&/no fine crumpled wrinkles/.test(r.text)];if(touched)missions(S.querySelector('.missions'),M,true);
    say(S.querySelector('.talk'),[['doctor','e10','박사','요청 상황: '+job.options[job.selectedIndex].text+'. '+(jobOk?'필요한 조각이 들어 있다.':'이 상황에 꼭 필요한 조각이 빠졌다.')],['haru','e10','조수','점검표 '+r.score+' / 6'+(r.miss.length?', 빠진 것: '+r.miss.join(', '):'!')],['fruitfly','e09','초파리',o.neg?'금지 목록에 성인 비율이 들어가 있어 나이가 흔들리지 않아.':'금지 목록이 없으면 옷 이름 때문에 나이가 바뀔 수도 있어.'],['jupanbot','e16','주판봇',r.score===6?'여섯 조각 완성! 이번엔 제가 이깁니다!':'조각이 남았습니다! 하나씩 채우겠습니다!']]);}
  var cp=S.querySelector('.copy');if(cp)cp.addEventListener('click',function(){var t=S.querySelector('.g1 pre').textContent;if(navigator.clipboard)navigator.clipboard.writeText(t).then(function(){cp.textContent='복사했습니다';},function(){cp.textContent='직접 선택해 복사하세요';});});upd();}
var DESK_CA=['정보량 과다','소재 뒤바뀜','핏(여유) 무시','접점 무시(소품)','그림자 방향 반대','흐름 무시(프릴)','접힘 방향 무시','가림 영역 과다'];
var DESK_SYM=['애니풍인데 카디건이 잔주름 선 수십 개로 덮여 사진을 베낀 것 같다','두꺼운 울 코트가 실크처럼 가는 S자 주름으로 흘러내린다','오버핏 티셔츠라는데 몸에 딱 붙어 주름이 없다','숄더백 끈이 어깨 위에 떠 있고 옷에 변화가 없다','빛은 왼쪽 위인데 주름 그림자가 빛 쪽 비탈에 있다','치마는 아래로 퍼지는데 프릴 선이 반대로 기울었다','한 방향 주름치마인데 양쪽 뒷면이 다 보인다','옷만 바꿨는데 머리 번과 얼굴이 달라졌다'];
function desk(){var S=document.getElementById('desk');if(!S)return;var CA=DESK_CA,SYM=DESK_SYM;
  var cur=0,streak=0,seen={},wrong=0,right=0,touched=false;var r=rng(Date.now()%9999+1);
  function next(){cur=Math.floor(r()*8);S.querySelector('.sym').textContent='증상: '+SYM[cur];var o=S.querySelector('.opts');o.innerHTML='';
    var opts=[cur];while(opts.length<4){var k=Math.floor(r()*8);if(opts.indexOf(k)<0)opts.push(k);}opts.sort(function(){return r()-.5;});
    opts.forEach(function(k){var b=document.createElement('button');b.type='button';b.textContent=CA[k];b.addEventListener('click',function(){touched=true;if(k===cur){streak++;right++;seen[cur]=1;b.classList.add('ok');setTimeout(next,500);}else{streak=0;wrong++;b.classList.add('no');}upd();});o.appendChild(b);});}
  function upd(){var n=Object.keys(seen).length;board(S.querySelector('.board'),[['연속 정답',streak,streak>=3],['맞힌 종류',n+' / 8',n===8],['맞힘',right,right>0],['틀림',wrong,wrong===0]]);
    var M=[streak>=3,n===8,right>=5&&wrong===0];if(touched)missions(S.querySelector('.missions'),M,true);
    var s=el('svg',{viewBox:'0 0 360 200',role:'img','aria-label':'맞힌 실패 종류'});var g=S.querySelector('.g2');g.innerHTML='';g.appendChild(s);CA.forEach(function(t,i){el('rect',{x:16+(i%4)*86,y:20+Math.floor(i/4)*90,width:78,height:70,rx:8,fill:seen[i]?'#e8f6ec':'#f2f4f7',stroke:seen[i]?C.green:'#d5dbe2'},s);ktxt(s,55+(i%4)*86,60+Math.floor(i/4)*90,'f'+(i+1)+(seen[i]?' ✓':''),{size:14,anchor:'middle',fill:seen[i]?C.green:C.muted,weight:700});});
    say(S.querySelector('.talk'),[['doctor','e10','박사','순서: 접점·흐름 → 핏 → 소재 → 빛 → 정보량·가림.'],['haru','e10','조수','연속 '+streak+'개, 맞힌 종류 '+n+' / 8이에요.'],['x2','e09','평가단 X2',wrong?'틀린 건 6부 실패 카드에서 다시 보세요.':'아직 틀린 게 없어요!'],['jupanbot','e16','주판봇',streak>=3?'연속 정답! 제가 만든 실패작이라 잘 압니다!':'다음 문제는 제가 맞힙니다!']]);}
  next();upd();}

/* 프롬프트 복사 버튼(직접 만들기 실습) */
document.addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('.promptbox .copy');if(!b||b.closest('#workshop'))return;var pre=b.parentNode.querySelector('pre');if(!pre)return;var t=pre.textContent;
  if(navigator.clipboard)navigator.clipboard.writeText(t).then(function(){b.textContent='복사했습니다';},function(){b.textContent='직접 선택해 복사하세요';});else b.textContent='직접 선택해 복사하세요';});
