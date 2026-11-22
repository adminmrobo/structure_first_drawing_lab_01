/* 구조 먼저 보는 캐릭터 그리기 연구실 — 실험 패널 모음 (외부 라이브러리 없음) */
(function(){
'use strict';
var NS='http://www.w3.org/2000/svg';
var C={teal:'#0f8f84',orange:'#e8731a',navy:'#1e2f6e',blue:'#2458d6',green:'#13733a',red:'#c9302c',purple:'#6b4fb0',grid:'#e3e8ee',muted:'#5b6874',ink:'#16212b'};
var KFONT='"IBM Plex Sans KR","Malgun Gothic","Noto Sans KR",sans-serif';
var RM=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
var P={};

/* ---------- 공용 도구 ---------- */
function el(tag,a,parent){var e=document.createElementNS(NS,tag);for(var k in a){if(a[k]!=null)e.setAttribute(k,a[k]);}if(parent)parent.appendChild(e);return e;}
function ktxt(p,x,y,s,a){a=a||{};var t=el('text',{x:x,y:y,'font-size':a.size||13,fill:a.fill||C.muted,'font-family':KFONT,'text-anchor':a.anchor||'start','font-weight':a.weight||'normal'},p);t.textContent=s;return t;}
function svgOf(h,W,H,label){h.innerHTML='';return el('svg',{viewBox:'0 0 '+W+' '+H,role:'img','aria-label':'실험 그림: '+(label||noteOf(h))},h);}
function noteOf(h){var n=h.parentNode&&h.parentNode.querySelector('.ph small');return n?n.textContent:'';}
function canvasOf(h,W,H,mw){h.innerHTML='';var c=document.createElement('canvas');c.width=W;c.height=H;c.style.width='100%';c.style.maxWidth=(mw||W*1.2)+'px';c.style.margin='0 auto';c.style.height='auto';c.style.display='block';c.style.borderRadius='10px';c.setAttribute('role','img');c.setAttribute('aria-label','실험 그림: '+noteOf(h));h.appendChild(c);return c;}
function out(h){return h.parentNode.querySelector('.readout');}
function ctl(h){return h.parentNode.querySelector('.ctrl');}
function f2(v,d){d=d==null?2:d;if(d===0)return String(Math.round(v));var m=Math.pow(10,d);var s=(Math.round(v*m)/m).toFixed(d);s=s.replace(/\.?0+$/,'');if(s==='-0')s='0';return s;}
function num(v,d){return v<0?'−'+f2(-v,d):f2(v,d);}
function clamp(v,a,b){return Math.max(a,Math.min(b,v));}
function lerp(a,b,t){return a+(b-a)*t;}
function hex(c){c=c.replace('#','');return[parseInt(c.substr(0,2),16),parseInt(c.substr(2,2),16),parseInt(c.substr(4,2),16)];}
function rgb(a){return 'rgb('+a.map(function(v){return Math.round(clamp(v,0,255));}).join(',')+')';}
function mix(c1,c2,t){var a=hex(c1),b=hex(c2);return rgb([lerp(a[0],b[0],t),lerp(a[1],b[1],t),lerp(a[2],b[2],t)]);}
function shade(c,k){var a=hex(c);return rgb([a[0]*k,a[1]*k,a[2]*k]);}
function rad(d){return d*Math.PI/180;}
function seg(h,sel,cb){var bs=ctl(h).querySelectorAll(sel);bs.forEach(function(b){b.addEventListener('click',function(){bs.forEach(function(x){x.classList.remove('on');});b.classList.add('on');cb(b);});});}
function rng(seed){var s=seed>>>0||1;return function(){s=(s*1664525+1013904223)>>>0;return s/4294967296;};}
function onIn(inp,f){inp.addEventListener('input',f);}
function svgPt(s,e){var m=s.getScreenCTM().inverse();var q=s.createSVGPoint();q.x=e.clientX;q.y=e.clientY;return q.matrixTransform(m);}

/* ---------- 캐릭터 얼굴(가슴 위) 그리기 — 캔버스 ---------- */
var CH={
 haru:{hair:'#E9909A',hair2:'#D9707E',streak:'#1E2F5C',buns:true,ahoge:true,eye:'#3D8BE0',skin:'#F6D3B8',outfit:'hoodie',long:true},
 sia:{hair:'#1E1B22',hair2:'#4A4656',eye:'#7A7680',skin:'#F6D9C4',outfit:'maid',long:true,earring:true},
 moa:{hair:'#D8C09A',hair2:'#B89C74',eye:'#B07A3E',skin:'#F8DCC8',outfit:'cardigan',long:true,headband:true,ribbon:'L',wavy:true}
};
function cfg(name,over){var o={};var b=CH[name];for(var k in b)o[k]=b[k];for(var j in over)o[j]=over[j];return o;}
function drawBust(ctx,W,H,o){
  var cx=W/2,s=W/200;ctx.save();ctx.clearRect(0,0,W,H);ctx.fillStyle=o.bg||'#f4f6f9';ctx.fillRect(0,0,W,H);
  var ln=o.line||2.2*s;ctx.lineJoin='round';ctx.lineCap='round';ctx.strokeStyle=o.ink||'#2a2230';ctx.lineWidth=ln;
  function E(x,y,rx,ry,fill,stroke){ctx.beginPath();ctx.ellipse(x,y,rx,ry,0,0,Math.PI*2);if(fill){ctx.fillStyle=fill;ctx.fill();}if(stroke!==false)ctx.stroke();}
  // 뒷머리
  if(o.long){ctx.fillStyle=o.hair;ctx.beginPath();ctx.moveTo(cx-48*s,78*s);ctx.quadraticCurveTo(cx-62*s,150*s,cx-52*s,200*s);ctx.lineTo(cx+52*s,200*s);ctx.quadraticCurveTo(cx+62*s,150*s,cx+48*s,78*s);ctx.closePath();ctx.fill();ctx.stroke();}
  else{ctx.fillStyle=o.hair;ctx.beginPath();ctx.moveTo(cx-46*s,80*s);ctx.quadraticCurveTo(cx-50*s,120*s,cx-36*s,128*s);ctx.lineTo(cx+36*s,128*s);ctx.quadraticCurveTo(cx+50*s,120*s,cx+46*s,80*s);ctx.closePath();ctx.fill();ctx.stroke();}
  // 몸·옷
  var body=o.outfit==='maid'?'#34363F':o.outfit==='cardigan'?'#D4B48A':o.outfit==='generic'?'#8a93a6':'#A99AC8';
  ctx.fillStyle=body;ctx.beginPath();ctx.moveTo(cx-70*s,200*s);ctx.quadraticCurveTo(cx-66*s,150*s,cx-26*s,140*s);ctx.lineTo(cx+26*s,140*s);ctx.quadraticCurveTo(cx+66*s,150*s,cx+70*s,200*s);ctx.closePath();ctx.fill();ctx.stroke();
  if(o.outfit==='hoodie'&&o.coat!==false){ctx.fillStyle='#fbfbfd';ctx.beginPath();ctx.moveTo(cx-70*s,200*s);ctx.quadraticCurveTo(cx-66*s,150*s,cx-30*s,141*s);ctx.lineTo(cx-18*s,200*s);ctx.closePath();ctx.fill();ctx.stroke();ctx.beginPath();ctx.moveTo(cx+70*s,200*s);ctx.quadraticCurveTo(cx+66*s,150*s,cx+30*s,141*s);ctx.lineTo(cx+18*s,200*s);ctx.closePath();ctx.fill();ctx.stroke();
    ctx.strokeStyle='#ffffff';ctx.beginPath();ctx.moveTo(cx-8*s,150*s);ctx.lineTo(cx-10*s,175*s);ctx.moveTo(cx+8*s,150*s);ctx.lineTo(cx+10*s,175*s);ctx.stroke();ctx.strokeStyle=o.ink||'#2a2230';}
  if(o.outfit==='maid'){ctx.fillStyle='#fbfbfd';ctx.fillRect(cx-16*s,136*s,32*s,12*s);ctx.strokeRect(cx-16*s,136*s,32*s,12*s);ctx.fillStyle='#8C8C94';E(cx-12*s,154*s,12*s,8*s,'#8C8C94');E(cx+12*s,154*s,12*s,8*s,'#8C8C94');E(cx,154*s,5*s,5*s,'#77777f');
    ctx.fillStyle='#F4F2EE';ctx.beginPath();ctx.moveTo(cx-30*s,200*s);ctx.lineTo(cx-24*s,172*s);ctx.lineTo(cx+24*s,172*s);ctx.lineTo(cx+30*s,200*s);ctx.closePath();ctx.fill();ctx.stroke();}
  if(o.outfit==='cardigan'){ctx.fillStyle='#ffffff';ctx.beginPath();ctx.moveTo(cx-18*s,142*s);ctx.lineTo(cx,175*s);ctx.lineTo(cx+18*s,142*s);ctx.closePath();ctx.fill();ctx.stroke();ctx.fillStyle='#A8323C';ctx.beginPath();ctx.moveTo(cx,150*s);ctx.lineTo(cx-12*s,144*s);ctx.lineTo(cx-12*s,158*s);ctx.closePath();ctx.moveTo(cx,150*s);ctx.lineTo(cx+12*s,144*s);ctx.lineTo(cx+12*s,158*s);ctx.closePath();ctx.fill();ctx.stroke();
    ctx.fillStyle='#FAF8F4';ctx.beginPath();ctx.moveTo(cx-34*s,200*s);ctx.lineTo(cx-28*s,178*s);ctx.lineTo(cx+28*s,178*s);ctx.lineTo(cx+34*s,200*s);ctx.closePath();ctx.fill();ctx.stroke();}
  // 목·얼굴
  ctx.fillStyle=o.skin;ctx.fillRect(cx-11*s,118*s,22*s,24*s);ctx.beginPath();ctx.moveTo(cx-11*s,118*s);ctx.lineTo(cx-11*s,140*s);ctx.moveTo(cx+11*s,118*s);ctx.lineTo(cx+11*s,140*s);ctx.stroke();
  ctx.beginPath();ctx.moveTo(cx-38*s,70*s);ctx.quadraticCurveTo(cx-40*s,112*s,cx,128*s);ctx.quadraticCurveTo(cx+40*s,112*s,cx+38*s,70*s);ctx.closePath();ctx.fillStyle=o.skin;ctx.fill();ctx.stroke();
  // 눈
  [-1,1].forEach(function(d){var ex=cx+d*17*s,ey=96*s;E(ex,ey,8.5*s,10.5*s,'#ffffff');E(ex,ey+1*s,6.5*s,8.5*s,o.eye,false);E(ex,ey+2*s,3.4*s,4.6*s,shade(o.eye,0.45),false);E(ex-2.4*s,ey-3*s,2.2*s,2.2*s,'#ffffff',false);
    ctx.beginPath();ctx.moveTo(ex-10*s,ey-10*s);ctx.quadraticCurveTo(ex,ey-14*s,ex+10*s,ey-9*s);ctx.lineWidth=ln*1.4;ctx.stroke();ctx.lineWidth=ln;});
  ctx.beginPath();ctx.moveTo(cx-5*s,116*s);ctx.quadraticCurveTo(cx,119*s,cx+5*s,116*s);ctx.stroke();
  if(o.blush!==false){ctx.fillStyle='rgba(240,120,130,.25)';E(cx-26*s,108*s,6*s,3*s,'rgba(240,120,130,.25)',false);E(cx+26*s,108*s,6*s,3*s,'rgba(240,120,130,.25)',false);}
  // 앞머리
  ctx.fillStyle=o.hair;ctx.beginPath();ctx.moveTo(cx-46*s,88*s);ctx.quadraticCurveTo(cx-50*s,34*s,cx,30*s);ctx.quadraticCurveTo(cx+50*s,34*s,cx+46*s,88*s);
  if(o.wavy){ctx.quadraticCurveTo(cx+30*s,76*s,cx+22*s,82*s);ctx.quadraticCurveTo(cx+10*s,72*s,cx,80*s);ctx.quadraticCurveTo(cx-10*s,72*s,cx-22*s,82*s);ctx.quadraticCurveTo(cx-30*s,76*s,cx-46*s,88*s);}
  else{ctx.lineTo(cx+36*s,74*s);ctx.lineTo(cx+24*s,84*s);ctx.lineTo(cx+12*s,72*s);ctx.lineTo(cx,84*s);ctx.lineTo(cx-12*s,72*s);ctx.lineTo(cx-24*s,84*s);ctx.lineTo(cx-36*s,74*s);}
  ctx.closePath();ctx.fill();ctx.stroke();
  ctx.strokeStyle=o.hair2;ctx.beginPath();ctx.moveTo(cx-30*s,44*s);ctx.quadraticCurveTo(cx-20*s,40*s,cx-10*s,46*s);ctx.stroke();ctx.strokeStyle=o.ink||'#2a2230';
  if(o.streak){ctx.fillStyle=o.streak;ctx.beginPath();ctx.moveTo(cx-6*s,31*s);ctx.lineTo(cx+6*s,31*s);ctx.lineTo(cx+5*s,80*s);ctx.lineTo(cx,84*s);ctx.lineTo(cx-5*s,80*s);ctx.closePath();ctx.fill();
    ctx.fillRect(cx-46*s+4*s,100*s,6*s,70*s);ctx.fillRect(cx+46*s-10*s,100*s,6*s,70*s);}
  if(o.buns){E(cx-30*s,30*s,15*s,14*s,o.hair);E(cx+30*s,30*s,15*s,14*s,o.hair);ctx.strokeStyle=o.hair2;ctx.beginPath();ctx.arc(cx-30*s,30*s,8*s,3.6,5.6);ctx.stroke();ctx.beginPath();ctx.arc(cx+30*s,30*s,8*s,3.6,5.6);ctx.stroke();ctx.strokeStyle=o.ink||'#2a2230';}
  if(o.ahoge){ctx.beginPath();ctx.moveTo(cx+2*s,30*s);ctx.quadraticCurveTo(cx+14*s,12*s,cx+4*s,8*s);ctx.lineWidth=ln*1.2;ctx.strokeStyle=o.hair2;ctx.stroke();ctx.lineWidth=ln;ctx.strokeStyle=o.ink||'#2a2230';}
  if(o.headband){ctx.fillStyle='#ffffff';ctx.beginPath();ctx.ellipse(cx,38*s,44*s,12*s,0,Math.PI*1.05,Math.PI*1.95);ctx.lineWidth=7*s;ctx.strokeStyle='#ffffff';ctx.stroke();ctx.lineWidth=ln;ctx.strokeStyle=o.ink||'#2a2230';
    for(var i=-3;i<=3;i++){E(cx+i*11*s,27*s+Math.abs(i)*2.2*s,4.5*s,4*s,'#ffffff');}}
  if(o.ribbon){var side=o.ribbon==='L'?1:-1;var rx=cx+side*44*s,ry=60*s;ctx.fillStyle='#ffffff';ctx.beginPath();ctx.moveTo(rx,ry);ctx.lineTo(rx-10*s,ry-7*s);ctx.lineTo(rx-10*s,ry+7*s);ctx.closePath();ctx.moveTo(rx,ry);ctx.lineTo(rx+10*s,ry-7*s);ctx.lineTo(rx+10*s,ry+7*s);ctx.closePath();ctx.fill();ctx.stroke();}
  if(o.earring){ctx.fillStyle='#c9ccd6';E(cx-39*s,108*s,2.5*s,4*s,'#c9ccd6');E(cx+39*s,108*s,2.5*s,4*s,'#c9ccd6');}
  ctx.restore();
}
function pixelate(src,dst,block){var W=dst.width,H=dst.height,ctx=dst.getContext('2d');if(block<=1){ctx.imageSmoothingEnabled=true;ctx.drawImage(src,0,0,W,H);return;}
  var t=document.createElement('canvas');t.width=Math.max(1,Math.round(W/block));t.height=Math.max(1,Math.round(H/block));var tc=t.getContext('2d');tc.imageSmoothingEnabled=true;tc.drawImage(src,0,0,t.width,t.height);
  ctx.imageSmoothingEnabled=false;ctx.clearRect(0,0,W,H);ctx.drawImage(t,0,0,W,H);ctx.imageSmoothingEnabled=true;}
function offBust(name,over,W){var c=document.createElement('canvas');c.width=W||200;c.height=W||200;drawBust(c.getContext('2d'),c.width,c.height,cfg(name,over||{}));return c;}

/* ---------- 3D 도형 마네킹 ---------- */
function limb(a,b,t,part){var dx=b[0]-a[0],dy=b[1]-a[1];return {c:[(a[0]+b[0])/2,(a[1]+b[1])/2,(a[2]+b[2])/2],s:[t,Math.hypot(dx,dy),t*0.95],rz:Math.atan2(dx,dy)*-1,part:part,ends:[a,b]};}
function mannequin(pose){pose=pose||'hip';
  var B=[];function box(c,s,part){B.push({c:c,s:s,rz:0,part:part});}
  box([0,7.45,0],[0.82,1.0,0.88],'head');box([0,6.78,0],[0.32,0.36,0.32],'neck');box([0,5.95,0],[1.6,1.45,1.0],'chest');box([0,4.62,0],[1.36,1.15,0.85],'pelvis');
  var L=[0.96,6.5,0],R=[-0.96,6.5,0];
  var le=[1.12,5.0,0],lh=[1.18,3.65,0.05];
  var re,rh;if(pose==='up'){re=[-1.15,8.0,0];rh=[-1.2,9.4,0];le=[1.15,8.0,0];lh=[1.2,9.4,0];}else{re=[-1.55,5.35,-0.1];rh=[-0.82,4.75,0.15];}
  B.push(limb(L,le,0.36,'uarm'));B.push(limb(le,lh,0.3,'farm'));B.push(limb(R,re,0.36,'uarm'));B.push(limb(re,rh,0.3,'farm'));
  [0.38,-0.38].forEach(function(x){var hp=[x,4.15,0],kn=[x*1.05,2.2,0.05],an=[x*1.08,0.35,0];B.push(limb(hp,kn,0.5,'thigh'));B.push(limb(kn,an,0.38,'shin'));box([x*1.08,0.14,0.18],[0.34,0.28,0.7],'foot');});
  B.joints={head:[0,7.45,0],neck:[0,6.6,0],ls:L,rs:R,le:le,lh:lh,re:re,rh:rh,lp:[0.38,4.15,0],rp:[-0.38,4.15,0],lk:[0.4,2.2,0.05],rk:[-0.4,2.2,0.05],la:[0.41,0.35,0],ra:[-0.41,0.35,0]};
  return B;}
var FACES=[[0,1,2,3],[4,5,6,7],[0,1,5,4],[2,3,7,6],[1,2,6,5],[0,3,7,4]];
function boxVerts(b){var w=b.s[0]/2,h=b.s[1]/2,d=b.s[2]/2,c=Math.cos(b.rz),s=Math.sin(b.rz);
  var L=[[-w,-h,-d],[w,-h,-d],[w,h,-d],[-w,h,-d],[-w,-h,d],[w,-h,d],[w,h,d],[-w,h,d]];
  return L.map(function(p){var x=p[0]*c-p[1]*s,y=p[0]*s+p[1]*c;return[x+b.c[0],y+b.c[1],p[2]+b.c[2]];});}
function rotY(p,a){var c=Math.cos(a),s=Math.sin(a);return[p[0]*c+p[2]*s,p[1],-p[0]*s+p[2]*c];}
function sub3(a,b){return[a[0]-b[0],a[1]-b[1],a[2]-b[2]];}
function cross(a,b){return[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]];}
function norm(a){var l=Math.hypot(a[0],a[1],a[2])||1;return[a[0]/l,a[1]/l,a[2]/l];}
function dot(a,b){return a[0]*b[0]+a[1]*b[1]+a[2]*b[2];}
var PARTCOL={head:'#E9909A',neck:'#F6D3B8',chest:'#A99AC8',pelvis:'#5b7fb8',uarm:'#fbfbfd',farm:'#fbfbfd',thigh:'#5b7fb8',shin:'#5b7fb8',foot:'#A99AC8'};
function renderMan(s,o){/* o: yaw, mode(shade|flat|edge|depth|blocks|sketch|line|color), W,H,scale,ox,oy, light */
  var B=mannequin(o.pose),yaw=rad(o.yaw||0),Lt=norm(o.light||[-0.55,0.65,0.55]);
  var sc=o.scale||40,ox=o.ox||o.W/2,oy=o.oy||o.H-20;var polys=[];var zmin=1e9,zmax=-1e9;
  B.forEach(function(b){var V=boxVerts(b).map(function(p){return rotY(p,yaw);});
    FACES.forEach(function(f){var a=V[f[0]],bb=V[f[1]],c=V[f[2]];var n=norm(cross(sub3(bb,a),sub3(c,a)));
      var cen=[0,0,0];f.forEach(function(i){cen[0]+=V[i][0]/4;cen[1]+=V[i][1]/4;cen[2]+=V[i][2]/4;});
      // 바깥쪽 법선으로 맞춤
      var bc=rotY(b.c,yaw);if(dot(n,sub3(cen,bc))<0)n=[-n[0],-n[1],-n[2]];
      if(n[2]<=0.001)return;zmin=Math.min(zmin,cen[2]);zmax=Math.max(zmax,cen[2]);
      polys.push({pts:f.map(function(i){return[ox+V[i][0]*sc,oy-V[i][1]*sc];}),z:cen[2],n:n,part:b.part});});});
  polys.sort(function(a,b){return a.z-b.z;});var g=el('g',{},s);var R=rng(7);
  polys.forEach(function(p){var d=p.pts.map(function(q){return q[0].toFixed(1)+','+q[1].toFixed(1);}).join(' ');
    var br=0.28+0.72*Math.max(0,dot(p.n,Lt));var m=o.mode;
    if(m==='shade')el('polygon',{points:d,fill:mix('#3b3f4a','#eef1f6',br),stroke:'#2a2e38','stroke-width':0.8},g);
    else if(m==='flat')el('polygon',{points:d,fill:o.flat||'#f2d9c6',stroke:o.flat||'#f2d9c6','stroke-width':0.6},g);
    else if(m==='blocks')el('polygon',{points:d,fill:'none',stroke:C.blue,'stroke-width':1.3},g);
    else if(m==='sketch'){var q=p.pts.map(function(v){return[v[0]+(R()-.5)*3,v[1]+(R()-.5)*3];});el('polygon',{points:q.map(function(v){return v[0].toFixed(1)+','+v[1].toFixed(1);}).join(' '),fill:'none',stroke:'#8a8f99','stroke-width':1,opacity:.85},g);}
    else if(m==='line')el('polygon',{points:d,fill:'#ffffff',stroke:'#1d1a22','stroke-width':1.4},g);
    else if(m==='color'){var A=hex(PARTCOL[p.part]||'#dddddd');el('polygon',{points:d,fill:rgb(A.map(function(v){return v*(0.6+0.4*br);})),stroke:'#1d1a22','stroke-width':1.2},g);}
    else if(m==='edge')el('polygon',{points:d,fill:'#000',stroke:'#fff','stroke-width':1.1},g);
    else if(m==='depth'){var t=(p.z-zmin)/Math.max(1e-6,zmax-zmin);var v=Math.round(70+t*185);el('polygon',{points:d,fill:'rgb('+v+','+v+','+v+')',stroke:'rgb('+v+','+v+','+v+')','stroke-width':0.6},g);}
  });
  var J={};for(var k in B.joints){var r=rotY(B.joints[k],yaw);J[k]=[ox+r[0]*sc,oy-r[1]*sc,r[2]];}
  return {g:g,J:J};}

