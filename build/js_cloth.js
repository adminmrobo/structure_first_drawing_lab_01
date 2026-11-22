/* ===================== 3부: 천 시뮬레이션 ===================== */
function Cloth(nx,ny,sp){this.nx=nx;this.ny=ny;this.sp=sp;this.p=[];this.o=[];this.pin={};var r=rng(3);
  for(var j=0;j<ny;j++)for(var i=0;i<nx;i++){var v=[(i-(nx-1)/2)*sp,-j*sp,(r()-.5)*0.6];this.p.push(v.slice());this.o.push(v.slice());}}
Cloth.prototype.idx=function(i,j){return j*this.nx+i;};
Cloth.prototype.step=function(g,stiff,wind){var n=this.p.length,k,p,o;for(k=0;k<n;k++){if(this.pin[k])continue;p=this.p[k];o=this.o[k];var vx=(p[0]-o[0])*0.985,vy=(p[1]-o[1])*0.985,vz=(p[2]-o[2])*0.985;o[0]=p[0];o[1]=p[1];o[2]=p[2];p[0]+=vx+(wind||0);p[1]+=vy-g;p[2]+=vz;}
  var nx=this.nx,ny=this.ny,sp=this.sp,self=this;
  function sat(a,b,rest,w){var A=self.p[a],B=self.p[b];var dx=B[0]-A[0],dy=B[1]-A[1],dz=B[2]-A[2];var d=Math.sqrt(dx*dx+dy*dy+dz*dz)||1e-6;var df=(d-rest)/d*0.5*w;var pa=self.pin[a]?0:1,pb=self.pin[b]?0:1;if(!pa&&!pb)return;var s2=pa&&pb?1:2;
    if(pa){A[0]+=dx*df*s2;A[1]+=dy*df*s2;A[2]+=dz*df*s2;}if(pb){B[0]-=dx*df*s2;B[1]-=dy*df*s2;B[2]-=dz*df*s2;}}
  for(var it=0;it<6;it++){for(var j=0;j<ny;j++)for(var i=0;i<nx;i++){var a=this.idx(i,j);if(i<nx-1)sat(a,a+1,sp,1);if(j<ny-1)sat(a,a+nx,sp,1);if(i<nx-1&&j<ny-1){sat(a,a+nx+1,sp*1.41421,0.9);sat(a+1,a+nx,sp*1.41421,0.9);}
      if(stiff>0){if(i<nx-2)sat(a,a+2,2*sp,stiff);if(j<ny-2)sat(a,a+2*nx,2*sp,stiff);}}
    for(var key in this.pin){var q=this.pin[key];this.p[key][0]=q[0];this.p[key][1]=q[1];this.p[key][2]=q[2];}}};
Cloth.prototype.draw=function(ctx,W,H,sc,ox,oy){ctx.fillStyle='#fbfcfd';ctx.fillRect(0,0,W,H);var L=norm([-0.5,0.55,0.7]);var nx=this.nx,ny=this.ny,quads=[];
  for(var j=0;j<ny-1;j++)for(var i=0;i<nx-1;i++){var a=this.p[this.idx(i,j)],b=this.p[this.idx(i+1,j)],c=this.p[this.idx(i+1,j+1)],d=this.p[this.idx(i,j+1)];var n=norm(cross(sub3(b,a),sub3(d,a)));if(n[2]<0)n=[-n[0],-n[1],-n[2]];quads.push({q:[a,b,c,d],z:(a[2]+b[2]+c[2]+d[2])/4,n:n});}
  quads.sort(function(a,b){return a.z-b.z;});quads.forEach(function(Q){var br=0.25+0.75*Math.max(0,dot(Q.n,L));ctx.fillStyle=mix('#4a5470','#eef0f8',br);ctx.beginPath();Q.q.forEach(function(v,k){var X=ox+v[0]*sc,Y=oy-v[1]*sc;if(k)ctx.lineTo(X,Y);else ctx.moveTo(X,Y);});ctx.closePath();ctx.fill();ctx.strokeStyle='rgba(40,46,60,.18)';ctx.lineWidth=0.6;ctx.stroke();});
  for(var key in this.pin){var v=this.p[key];ctx.fillStyle='#8c8f9a';ctx.beginPath();ctx.arc(ox+v[0]*sc,oy-v[1]*sc,7,0,7);ctx.fill();ctx.strokeStyle='#2a2e38';ctx.lineWidth=1.5;ctx.stroke();}};
Cloth.prototype.folds=function(){var j=Math.floor(this.ny*0.6),c=0,prev=0;for(var i=1;i<this.nx-1;i++){var dz=this.p[this.idx(i+1,j)][2]-this.p[this.idx(i-1,j)][2];var sgn=dz>0.15?1:dz<-0.15?-1:0;if(sgn&&prev&&sgn!==prev)c++;if(sgn)prev=sgn;}return c;};
Cloth.prototype.sag=function(){var j=0,mid=this.p[this.idx(Math.floor(this.nx/2),0)];var top=Math.max.apply(null,Object.keys(this.pin).map(function(k){return this.p[k][1];},this));return top-mid[1];};
function runCloth(h,setup,opts){var W=520,H=400;var cv=canvasOf(h,W,H),ctx=cv.getContext('2d');var cl,raf=null,frames=0,grab=null;
  function reset(){cl=new Cloth(19,15,1);setup(cl);frames=0;loop();}
  function tick(){var o=opts();for(var k=0;k<2;k++)cl.step(o.g,o.stiff,o.wind||0);if(grab)cl.pin[grab.k]=grab.pos;}
  function render(){cl.draw(ctx,W,H,18,W/2,60);var o=opts();if(o.report)o.report(cl);}
  function loop(){if(raf)cancelAnimationFrame(raf);if(RM){for(var i=0;i<220;i++)tick();render();return;}
    (function f(){tick();frames++;render();if(frames<260||grab)raf=requestAnimationFrame(f);else raf=null;})();}
  function pos(e){var r=cv.getBoundingClientRect();return[((e.clientX-r.left)*W/r.width-W/2)/18,-((e.clientY-r.top)*H/r.height-60)/18];}
  cv.addEventListener('pointerdown',function(e){var q=pos(e),best=-1,bd=4;cl.p.forEach(function(v,k){var d=Math.hypot(v[0]-q[0],v[1]-q[1]);if(d<bd&&!cl.pin[k]){bd=d;best=k;}});if(best>=0){grab={k:best,pos:[q[0],q[1],cl.p[best][2]]};cv.setPointerCapture&&cv.setPointerCapture(e.pointerId);loop();}});
  cv.addEventListener('pointermove',function(e){if(!grab)return;var q=pos(e);grab.pos=[q[0],q[1],grab.pos[2]];});
  cv.addEventListener('pointerup',function(){if(grab){delete cl.pin[grab.k];grab=null;frames=0;loop();}});
  reset();return {reset:reset,get:function(){return cl;}};}
function pinMode(cl,m){var nx=cl.nx,sp=cl.sp,i;cl.pin={};function pin(i,j,pos){var k=cl.idx(i,j);cl.pin[k]=pos||cl.p[k].slice();cl.p[k]=cl.pin[k].slice();cl.o[k]=cl.pin[k].slice();}
  if(m===1)pin(Math.floor(nx/2),0);
  if(m===2){pin(0,0,[-(nx-1)/2*sp*0.7,0,0]);pin(nx-1,0,[(nx-1)/2*sp*0.7,0,0]);}
  if(m===3){pin(0,0,[-(nx-1)/2*sp*0.7,0,0]);pin(nx-1,0,[(nx-1)/2*sp*0.7,-6,0]);}
  if(m===4){for(i=0;i<nx;i++){pin(i,0,[(i-(nx-1)/2)*sp*0.42,0,(i%2?0.35:-0.35)]);}}}
