import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from os import chdir
from os import getcwd
from sys import argv

# get argument from user
if len(argv) == 1 :
    aparatlink=BeautifulSoup(requests.get(input('Enter aparat link : ')).content,"html.parser").find_all('a')
    li2=[]
    for i in aparatlink:
        li2.append(i.get('href'))
    def Qua(li):
        d=[]
        for i in li:
            if "mp4" in i:
                d.append(str(i.split('-')[-1].split('.')[0]))
        return d
    print("Choise the Quality :"+",".join(Qua(li2)))
    quality=input("Quality :")
elif len(argv) == 2:
    aparatlink=BeautifulSoup(requests.get(argv[1]).content,"html.parser").find_all('a')
    li2=[]
    for i in aparatlink:
        li2.append(i.get('href'))
    def Qua(li):
        d=[]
        for i in li:
            if "mp4" in i:
                d.append(str(i.split('-')[-1].split('.')[0]))
        return d
    print("Choise the Quality :"+",".join(Qua(li2)))
    quality=input("Quality :")
elif len(argv) == 3:
    aparatlink=BeautifulSoup(requests.get(argv[1]).content,"html.parser").find_all('a')
    li2=[]
    for i in aparatlink:
        li2.append(i.get('href'))
    quality=argv[2]
else :
    print('Enter Correct argumant')

# index.html content
def dl1():
    linea="""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/5.0.0-alpha1/css/bootstrap.min.css" integrity="sha384-r4NyP46KrjDleawBgD5tp8Y7UzmLA05oM1iAEQ17CSuDqnUK2+k9luXQOfXJCJ4I" crossorigin="anonymous"><title>Download</title></head><body><style>@font-face{font-family:MikhakLight;src:url('https://aminabedi68.github.io/Mikhak/Mikhak/Mikhak-Light.woff2') format('woff2')}@font-face{font-family:MikhakMedium;src:url('https://aminabedi68.github.io/Mikhak/Mikhak/Mikhak-Medium.woff2') format('woff2')}body{font-family:MikhakLight;direction:rtl;text-align:right}.dltr{direction:ltr}.ffm{font-family:MikhakMedium}.col-md-12.border-bottom.pt-3.pb-3:hover{box-shadow: 0px 0px 16px #eee;transition: all 0.2s;border-radius: 9px;border-bottom: 1px solid #fff !important;}</style><style>.button1{--background:#4b4b4b;--background-hover:#303030;--text:#fff;--icon:#fff;--particle:#fff;display:-webkit-box;display:flex;outline:none;cursor:pointer;border:0;min-width:113px;padding:14px 12px 14px 37px;border-radius:8px;line-height:24px;font-family:inherit;font-weight:600;font-size:22px;color:var(--text);background:var(--b, var(--background));-webkit-transition:background .4s, -webkit-transform .3s;transition:background .4s, -webkit-transform .3s;transition:transform .3s, background .4s;transition:transform .3s, background .4s, -webkit-transform .3s;-webkit-transform:scale(var(--scale, 1)) translateZ(0);transform:scale(var(--scale, 1)) translateZ(0)}.button1:active{--scale: .95}.button1:hover{--b:var(--background-hover)}.button1 .icon{--arrow-y:0;--arrow-rotate:135;--arrow-top:10px;width:52px;height:24px;position:relative;display:inline-block;vertical-align:top;margin-right:8px;pointer-events:none}.button1 .icon .dot{border-radius:50%;background:#fff;background:var(--particle);position:absolute;left:0;top:0;width:4px;height:4px}.button1 .icon .arrow, .button1 .icon .line{position:absolute;z-index:1}.button1 .icon .arrow{left:11px;top:4px;width:2px;height:12px;border-radius:1px;background:var(--icon);-webkit-transform:translateY(calc(var(--arrow-y) * 1px)) translateZ(0);transform:translateY(calc(var(--arrow-y) * 1px)) translateZ(0)}.button1 .icon .arrow:before, .button1 .icon .arrow:after{content:'';width:2px;height:7px;position:absolute;left:0;top:var(--arrow-top);border-radius:1px;background:inherit;-webkit-transform-origin:1px 1px;transform-origin:1px 1px;-webkit-transform:rotate(var(--r, calc(var(--arrow-rotate) * 1deg)));transform:rotate(var(--r, calc(var(--arrow-rotate) * 1deg)))}.button1 .icon .arrow:after{--r:calc(var(--arrow-rotate) * -1deg)}.button1 .icon .line{width:24px;height:24px;display:block;left:0;top:7px;fill:none;stroke:var(--icon);stroke-width:2;stroke-linejoin:round;stroke-linecap:round}.button1.upload .icon{--arrow-rotate:45;--arrow-top:0}</style><div class="container-fluid"><div class="row mt-5"><div class="col-md-8 pr-5"><h1 class=" display-1">دانلود های شما !!!</h1></div><div class="col-md-2 align-self-center text-center">"""
    lineb="""<h2 class="display-4">{qualiti}p</h2>""".format(qualiti=quality)
    linec="""</div><div class="col-md-1 mt-2"><style>a{text-decoration:none}.typewriter{--blue:#5C86FF;--blue-dark:#275EFE;--key:#fff;--paper:#EEF0FD;--text:#D3D4EC;--tool:#FBC56C;--duration:3s;position:relative;-webkit-animation:bounce var(--duration) linear infinite;animation:bounce var(--duration) linear infinite}.typewriter .slide{width:92px;height:20px;border-radius:3px;margin-left:14px;-webkit-transform:translateX(14px);transform:translateX(14px);background:-webkit-gradient(linear, left top, left bottom, from(var(--blue)), to(var(--blue-dark)));background:linear-gradient(var(--blue), var(--blue-dark));-webkit-animation:slide var(--duration) ease infinite;animation:slide var(--duration) ease infinite}.typewriter .slide:before, .typewriter .slide:after, .typewriter .slide i:before{content:'';position:absolute;background:var(--tool)}.typewriter .slide:before{width:2px;height:8px;top:6px;left:100%}.typewriter .slide:after{left:94px;top:3px;height:14px;width:6px;border-radius:3px}.typewriter .slide i{display:block;position:absolute;right:100%;width:6px;height:4px;top:4px;background:var(--tool)}.typewriter .slide i:before{right:100%;top:-2px;width:4px;border-radius:2px;height:14px}.typewriter .paper{position:absolute;left:24px;top:-26px;width:40px;height:46px;border-radius:5px;background:var(--paper);-webkit-transform:translateY(46px);transform:translateY(46px);-webkit-animation:paper var(--duration) linear infinite;animation:paper var(--duration) linear infinite}.typewriter .paper:before{content:'';position:absolute;left:6px;right:6px;top:7px;border-radius:2px;height:4px;-webkit-transform:scaleY(0.8);transform:scaleY(0.8);background:var(--text);box-shadow:0 12px 0 var(--text), 0 24px 0 var(--text), 0 36px 0 var(--text)}.typewriter .keyboard{width:120px;height:56px;margin-top:-10px;z-index:1;position:relative}.typewriter .keyboard:before, .typewriter .keyboard:after{content:'';position:absolute}.typewriter .keyboard:before{top:0;left:0;right:0;bottom:0;border-radius:7px;background:linear-gradient(135deg, var(--blue), var(--blue-dark));-webkit-transform:perspective(10px) rotateX(2deg);transform:perspective(10px) rotateX(2deg);-webkit-transform-origin:50% 100%;transform-origin:50% 100%}.typewriter .keyboard:after{left:2px;top:25px;width:11px;height:4px;border-radius:2px;box-shadow:15px 0 0 var(--key), 30px 0 0 var(--key), 45px 0 0 var(--key), 60px 0 0 var(--key), 75px 0 0 var(--key), 90px 0 0 var(--key), 22px 10px 0 var(--key), 37px 10px 0 var(--key), 52px 10px 0 var(--key), 60px 10px 0 var(--key), 68px 10px 0 var(--key), 83px 10px 0 var(--key);-webkit-animation:keyboard var(--duration) linear infinite;animation:keyboard var(--duration) linear infinite}@-webkit-keyframes bounce{85%,92%,100%{-webkit-transform:translateY(0);transform:translateY(0)}89%{-webkit-transform:translateY(-4px);transform:translateY(-4px)}95%{-webkit-transform:translateY(2px);transform:translateY(2px)}}@keyframes bounce{85%,92%,100%{-webkit-transform:translateY(0);transform:translateY(0)}89%{-webkit-transform:translateY(-4px);transform:translateY(-4px)}95%{-webkit-transform:translateY(2px);transform:translateY(2px)}}@-webkit-keyframes slide{5%{-webkit-transform:translateX(14px);transform:translateX(14px)}15%,30%{-webkit-transform:translateX(6px);transform:translateX(6px)}40%,55%{-webkit-transform:translateX(0);transform:translateX(0)}65%,70%{-webkit-transform:translateX(-4px);transform:translateX(-4px)}80%,89%{-webkit-transform:translateX(-12px);transform:translateX(-12px)}100%{-webkit-transform:translateX(14px);transform:translateX(14px)}}@keyframes slide{5%{-webkit-transform:translateX(14px);transform:translateX(14px)}15%,30%{-webkit-transform:translateX(6px);transform:translateX(6px)}40%,55%{-webkit-transform:translateX(0);transform:translateX(0)}65%,70%{-webkit-transform:translateX(-4px);transform:translateX(-4px)}80%,89%{-webkit-transform:translateX(-12px);transform:translateX(-12px)}100%{-webkit-transform:translateX(14px);transform:translateX(14px)}}@-webkit-keyframes paper{5%{-webkit-transform:translateY(46px);transform:translateY(46px)}20%,30%{-webkit-transform:translateY(34px);transform:translateY(34px)}40%,55%{-webkit-transform:translateY(22px);transform:translateY(22px)}65%,70%{-webkit-transform:translateY(10px);transform:translateY(10px)}80%,85%{-webkit-transform:translateY(0);transform:translateY(0)}92%,100%{-webkit-transform:translateY(46px);transform:translateY(46px)}}@keyframes paper{5%{-webkit-transform:translateY(46px);transform:translateY(46px)}20%,30%{-webkit-transform:translateY(34px);transform:translateY(34px)}40%,55%{-webkit-transform:translateY(22px);transform:translateY(22px)}65%,70%{-webkit-transform:translateY(10px);transform:translateY(10px)}80%,85%{-webkit-transform:translateY(0);transform:translateY(0)}92%,100%{-webkit-transform:translateY(46px);transform:translateY(46px)}}@-webkit-keyframes keyboard{5%,12%,21%,30%,39%,48%,57%,66%,75%,84%{box-shadow:15px 0 0 var(--key), 30px 0 0 var(--key), 45px 0 0 var(--key), 60px 0 0 var(--key), 75px 0 0 var(--key), 90px 0 0 var(--key), 22px 10px 0 var(--key), 37px 10px 0 var(--key), 52px 10px 0 var(--key), 60px 10px 0 var(--key), 68px 10px 0 var(--key), 83px 10px 0 var(--key)}9%{box-shadow:15px 2px 0 var(--key), 30px 0 0 var(--key), 45px 0 0 var(--key), 60px 0 0 var(--key), 75px 0 0 var(--key), 90px 0 0 var(--key), 22px 10px 0 var(--key), 37px 10px 0 var(--key), 52px 10px 0 var(--key), 60px 10px 0 var(--key), 68px 10px 0 var(--key), 83px 10px 0 var(--key)}18%{box-shadow:15px 0 0 var(--key), 30px 0 0 var(--key), 45px 0 0 var(--key), 60px 2px 0 var(--key), 75px 0 0 var(--key), 90px 0 0 var(--key), 22px 10px 0 var(--key), 37px 10px 0 var(--key), 52px 10px 0 var(--key), 60px 10px 0 var(--key), 68px 10px 0 var(--key), 83px 10px 0 var(--key)}27%{box-shadow:15px 0 0 var(--key), 30px 0 0 var(--key), 45px 0 0 var(--key), 60px 0 0 var(--key), 75px 0 0 var(--key), 90px 0 0 var(--key), 22px 12px 0 var(--key), 37px 10px 0 var(--key), 52px 10px 0 var(--key), 60px 10px 0 var(--key), 68px 10px 0 var(--key), 83px 10px 0 var(--key)}36%{box-shadow:15px 0 0 var(--key), 30px 0 0 var(--key), 45px 0 0 var(--key), 60px 0 0 var(--key), 75px 0 0 var(--key), 90px 0 0 var(--key), 22px 10px 0 var(--key), 37px 10px 0 var(--key), 52px 12px 0 var(--key), 60px 12px 0 var(--key), 68px 12px 0 var(--key), 83px 10px 0 var(--key)}45%{box-shadow:15px 0 0 var(--key), 30px 0 0 var(--key), 45px 0 0 var(--key), 60px 0 0 var(--key), 75px 0 0 var(--key), 90px 2px 0 var(--key), 22px 10px 0 var(--key), 37px 10px 0 var(--key), 52px 10px 0 var(--key), 60px 10px 0 var(--key), 68px 10px 0 var(--key), 83px 10px 0 var(--key)}54%{box-shadow:15px 0 0 var(--key), 30px 2px 0 var(--key), 45px 0 0 var(--key), 60px 0 0 var(--key), 75px 0 0 var(--key), 90px 0 0 var(--key), 22px 10px 0 var(--key), 37px 10px 0 var(--key), 52px 10px 0 var(--key), 60px 10px 0 var(--key), 68px 10px 0 var(--key), 83px 10px 0 var(--key)}63%{box-shadow:15px 0 0 var(--key), 30px 0 0 var(--key), 45px 0 0 var(--key), 60px 0 0 var(--key), 75px 0 0 var(--key), 90px 0 0 var(--key), 22px 10px 0 var(--key), 37px 10px 0 var(--key), 52px 10px 0 var(--key), 60px 10px 0 var(--key), 68px 10px 0 var(--key), 83px 12px 0 var(--key)}72%{box-shadow:15px 0 0 var(--key), 30px 0 0 var(--key), 45px 2px 0 var(--key), 60px 0 0 var(--key), 75px 0 0 var(--key), 90px 0 0 var(--key), 22px 10px 0 var(--key), 37px 10px 0 var(--key), 52px 10px 0 var(--key), 60px 10px 0 var(--key), 68px 10px 0 var(--key), 83px 10px 0 var(--key)}81%{box-shadow:15px 0 0 var(--key), 30px 0 0 var(--key), 45px 0 0 var(--key), 60px 0 0 var(--key), 75px 0 0 var(--key), 90px 0 0 var(--key), 22px 10px 0 var(--key), 37px 12px 0 var(--key), 52px 10px 0 var(--key), 60px 10px 0 var(--key), 68px 10px 0 var(--key), 83px 10px 0 var(--key)}}@keyframes keyboard{5%,12%,21%,30%,39%,48%,57%,66%,75%,84%{box-shadow:15px 0 0 var(--key), 30px 0 0 var(--key), 45px 0 0 var(--key), 60px 0 0 var(--key), 75px 0 0 var(--key), 90px 0 0 var(--key), 22px 10px 0 var(--key), 37px 10px 0 var(--key), 52px 10px 0 var(--key), 60px 10px 0 var(--key), 68px 10px 0 var(--key), 83px 10px 0 var(--key)}9%{box-shadow:15px 2px 0 var(--key), 30px 0 0 var(--key), 45px 0 0 var(--key), 60px 0 0 var(--key), 75px 0 0 var(--key), 90px 0 0 var(--key), 22px 10px 0 var(--key), 37px 10px 0 var(--key), 52px 10px 0 var(--key), 60px 10px 0 var(--key), 68px 10px 0 var(--key), 83px 10px 0 var(--key)}18%{box-shadow:15px 0 0 var(--key), 30px 0 0 var(--key), 45px 0 0 var(--key), 60px 2px 0 var(--key), 75px 0 0 var(--key), 90px 0 0 var(--key), 22px 10px 0 var(--key), 37px 10px 0 var(--key), 52px 10px 0 var(--key), 60px 10px 0 var(--key), 68px 10px 0 var(--key), 83px 10px 0 var(--key)}27%{box-shadow:15px 0 0 var(--key), 30px 0 0 var(--key), 45px 0 0 var(--key), 60px 0 0 var(--key), 75px 0 0 var(--key), 90px 0 0 var(--key), 22px 12px 0 var(--key), 37px 10px 0 var(--key), 52px 10px 0 var(--key), 60px 10px 0 var(--key), 68px 10px 0 var(--key), 83px 10px 0 var(--key)}36%{box-shadow:15px 0 0 var(--key), 30px 0 0 var(--key), 45px 0 0 var(--key), 60px 0 0 var(--key), 75px 0 0 var(--key), 90px 0 0 var(--key), 22px 10px 0 var(--key), 37px 10px 0 var(--key), 52px 12px 0 var(--key), 60px 12px 0 var(--key), 68px 12px 0 var(--key), 83px 10px 0 var(--key)}45%{box-shadow:15px 0 0 var(--key), 30px 0 0 var(--key), 45px 0 0 var(--key), 60px 0 0 var(--key), 75px 0 0 var(--key), 90px 2px 0 var(--key), 22px 10px 0 var(--key), 37px 10px 0 var(--key), 52px 10px 0 var(--key), 60px 10px 0 var(--key), 68px 10px 0 var(--key), 83px 10px 0 var(--key)}54%{box-shadow:15px 0 0 var(--key), 30px 2px 0 var(--key), 45px 0 0 var(--key), 60px 0 0 var(--key), 75px 0 0 var(--key), 90px 0 0 var(--key), 22px 10px 0 var(--key), 37px 10px 0 var(--key), 52px 10px 0 var(--key), 60px 10px 0 var(--key), 68px 10px 0 var(--key), 83px 10px 0 var(--key)}63%{box-shadow:15px 0 0 var(--key), 30px 0 0 var(--key), 45px 0 0 var(--key), 60px 0 0 var(--key), 75px 0 0 var(--key), 90px 0 0 var(--key), 22px 10px 0 var(--key), 37px 10px 0 var(--key), 52px 10px 0 var(--key), 60px 10px 0 var(--key), 68px 10px 0 var(--key), 83px 12px 0 var(--key)}72%{box-shadow:15px 0 0 var(--key), 30px 0 0 var(--key), 45px 2px 0 var(--key), 60px 0 0 var(--key), 75px 0 0 var(--key), 90px 0 0 var(--key), 22px 10px 0 var(--key), 37px 10px 0 var(--key), 52px 10px 0 var(--key), 60px 10px 0 var(--key), 68px 10px 0 var(--key), 83px 10px 0 var(--key)}81%{box-shadow:15px 0 0 var(--key), 30px 0 0 var(--key), 45px 0 0 var(--key), 60px 0 0 var(--key), 75px 0 0 var(--key), 90px 0 0 var(--key), 22px 10px 0 var(--key), 37px 12px 0 var(--key), 52px 10px 0 var(--key), 60px 10px 0 var(--key), 68px 10px 0 var(--key), 83px 10px 0 var(--key)}}</style><div class="typewriter"><div class="slide"><i></i></div><div class="paper"></div><div class="keyboard"></div></div></div><div class="col-md-1"></div></div></div><div class="container shadow rounded-sm mt-4 mb-5 h4"><div class="row p-0">"""
    return linea+lineb+linec
def dl2():
    return """</div></div> <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.1.1/gsap.min.js"></script><script src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/16327/Physics2DPlugin3.min.js"></script>
    <script>const $ = (s, o = document) => o.querySelector(s); const $$ = (s, o = document) => o.querySelectorAll(s);gsap.registerPlugin(Physics2DPlugin);$$('.button1').forEach(button1 => {let isUpload = button1.classList.contains('upload'), icon = $('.icon', button1), line = $('.line', icon), svgPath = new Proxy({ y: null }, { set(target, key, value) { target[key] = value; if(target.y !== null) { line.innerHTML = getPath(target.y, .25, null); } return true; }, get(target, key) { return target[key]; } }), timeline = gsap.timeline({ paused: true }), interval;svgPath.y = 12;timeline.to(icon, { '--arrow-y': 6, '--arrow-rotate': isUpload ? 70 : 150, ease: "elastic.in(1.1, .8)", duration: .7, onComplete() { particles(icon, 6, 10, 18, -60, -120); } }).to(icon, { '--arrow-y': 0, '--arrow-rotate': isUpload ? 45 : 135, ease: "elastic.out(1.1, .8)", duration: .7 });timeline.to(svgPath, { y: 15, duration: .15 }, .65).to(svgPath, { y: 12, ease: "elastic.out(1.2, .7)", duration: .6 }, .8);button1.addEventListener('mouseover', e => { timeline.restart(); interval = setInterval(() => timeline.restart(), 1500); });button1.addEventListener('mouseout', e => clearInterval(interval));});function getPoint(point, i, a, smoothing) { let cp = (current, previous, next, reverse) => { let p = previous || current, n = next || current, o = { length: Math.sqrt(Math.pow(n[0] - p[0], 2) + Math.pow(n[1] - p[1], 2)), angle: Math.atan2(n[1] - p[1], n[0] - p[0]) }, angle = o.angle + (reverse ? Math.PI : 0), length = o.length * smoothing; return [current[0] + Math.cos(angle) * length, current[1] + Math.sin(angle) * length]; }, cps = cp(a[i - 1], a[i - 2], point, false), cpe = cp(point, a[i - 1], a[i + 1], true); return `C ${cps[0]},${cps[1]} ${cpe[0]},${cpe[1]} ${point[0]},${point[1]}`; }function getPath(update, smoothing, pointsNew) { let points = pointsNew ? pointsNew : [ [5, 12], [12, update], [19, 12] ], d = points.reduce((acc, point, i, a) => i === 0 ? `M ${point[0]},${point[1]}` : `${acc} ${getPoint(point, i, a, smoothing)}`, ''); return `<path d="${d}" />`; }function particles(parent, quantity, x, y, minAngle, maxAngle) { let minScale = .07, maxScale = .5; for(let i = quantity - 1; i >= 0; i--) { let angle = minAngle + Math.random() * (maxAngle - minAngle), scale = minScale + Math.random() * (maxScale - minScale), velocity = 12 + Math.random() * (80 - 60), dot = document.createElement('div'); dot.className = 'dot'; parent.appendChild(dot); gsap.set(dot, { opacity: 1, x: x, y: y, scale: scale }); gsap.timeline({ onComplete() { dot.remove(); } }).to(dot, 1.2, { physics2D: { angle: angle, velocity: velocity, gravity: 20 } }).to(dot, .4, { opacity: 0 }, .8); } }</script>
     </body></html>"""
def dlm():
    return """
      <div class="col-md-12 border-bottom pt-3 pb-3"><div class="row align-items-center"><div class="col-md-1 text-center">{}</div><div class="col-md-2"> <a class="dltr" href="{}" target="__blank"><div class="button1"><div class="icon"><div class="arrow"></div> <svg class="line" viewBox="0 0 24 24"></svg></div> دانلود</div> </a></div><div class="col-md-9 text-center h5">{}</div></div></div>
        """

# Extract Download Link with spicified quality
def mylinks(Downlink,DException):
    mainpage=urlparse(Downlink)
    website="{}://{}".format(mainpage[0],mainpage[1]) 
    al0=BeautifulSoup(requests.get(Downlink).content,"html.parser")
    na=al0.title.string
    na=na.replace("\n","")
    na=na.replace("        ","")
    al=al0.find_all('a')
    li=[]
    for i in al:
        li.append(i.get("href"))
    newlist=[]

    for i in li:
        
        if None == i:
            continue
        elif DException in i:
            if list(i)[0] == '/':
                newlist.append("{}{}".format(website,i))
            else:
                newlist.append(i)
                
    newlist.sort()
    return newlist,na

# aparat play list links
def aparatPlayList(AparatUrl):
    myli=[]
    for i in AparatUrl:
        if "?" in i and list(i)[1]== 'v':
            myli.append("https://www.aparat.com{}".format(i).split("?")[0])
    # remove dublicated item
    myli = list(dict.fromkeys(myli))
    return myli


def Start():
    PlayListLinks=(aparatPlayList(li2))
    print('Links=',len(PlayListLinks))
    chdir(getcwd()+"/")
    f=open("index.html","w")
    f.write(dl1())

    coun=0
    for i in  PlayListLinks:
        coun+=1
        fin=mylinks(i,quality)
        # Download link
        if len(fin[0]) == 0 :
            print("Download Link Not Found Sorry !")
            t="""<div class="col-md-12 border-bottom pt-3 pb-3"><div class="row align-items-center"><div class="col-md-1 text-center">{}</div><div class="col-md-2 text-center"> <a class="dltr" href="{}" target="__blank"><div class="btn btn-lg btn-danger ffm"><div class="icon"><div class="arrow"></div> </div> یافت نشد </div> </a></div><div class="col-md-9 text-center h5">{}</div></div></div>"""
            nam=fin[1]
            print(coun,nam)
            f.write(t.format(str(coun).zfill(3),i,nam))
            continue
        tmp=fin[0][0]
        # Name of Download
        nam=fin[1]
        print(coun,tmp)
        f.write(dlm().format(str(coun).zfill(3),tmp,nam))

    f.write(dl2())
    f.close()
    
Start()