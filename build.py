#!/usr/bin/env python3
"""Regenerate all HTML from data.json: python3 build.py"""
import json, html, os
D=os.path.dirname(os.path.abspath(__file__)); os.chdir(D)
DATA=json.load(open('data.json',encoding='utf-8')); S=DATA['shops']
e=html.escape
C={'card':'#7aa2ff','video':'#e7c98a','live':'#2ee6c5'}; L={'card':'商品卡','video':'视频','live':'直播'}
CSS=""":root{--bg:#07080f;--ink:#0d1020;--gl:rgba(255,255,255,.045);--bd:rgba(255,255,255,.09);--tx:#ecebf3;--mu:#8f93ab;--gold:#e7c98a;--gold2:#b8924f;--vio:#8b5cf6;--cy:#22d3ee;--serif:"Didot","Bodoni 72","Bodoni MT","Playfair Display","Noto Serif CJK SC","Songti SC",Georgia,serif;--sans:-apple-system,"SF Pro Display","Inter","Segoe UI","PingFang SC","Microsoft YaHei","Noto Sans CJK SC",sans-serif}
*{box-sizing:border-box}html{background:var(--bg)}body{margin:0;font-family:var(--sans);color:var(--tx);min-height:100vh;background:radial-gradient(900px 500px at 85% -10%,rgba(139,92,246,.22),transparent 60%),radial-gradient(800px 500px at -10% 20%,rgba(34,211,238,.10),transparent 60%),radial-gradient(700px 400px at 50% 110%,rgba(231,201,138,.08),transparent 60%),linear-gradient(180deg,#0a0c18,#06070d);background-attachment:fixed;font-variant-numeric:tabular-nums;-webkit-font-smoothing:antialiased}
a{color:var(--gold);text-decoration:none;transition:color .2s}a:hover{color:#fff3d6}.wrap{max-width:1160px;margin:0 auto;padding:24px 18px 64px}
header.top{position:relative;padding:44px 18px 34px;border-bottom:1px solid var(--bd);overflow:hidden}header.top:after{content:"";position:absolute;left:0;right:0;bottom:-1px;height:1px;background:linear-gradient(90deg,transparent,var(--gold),var(--vio),var(--cy),transparent)}
header.top .in{max-width:1160px;margin:0 auto;position:relative}header.top .in:before{content:"COMPETITIVE INTELLIGENCE · US TIKTOK SHOP";display:block;font-size:11px;letter-spacing:.32em;color:var(--gold);margin-bottom:12px;font-weight:600}
header h1{margin:0 0 10px;font-family:var(--serif);font-weight:700;font-size:clamp(26px,4.2vw,44px);letter-spacing:.01em;line-height:1.15;background:linear-gradient(100deg,#fff 0%,#f3e3bd 45%,#c9b6ff 80%,#9eeaf7 100%);-webkit-background-clip:text;background-clip:text;color:transparent}.upd{font-size:13px;color:var(--mu)}
.card{position:relative;background:linear-gradient(160deg,rgba(255,255,255,.07),rgba(255,255,255,.02));border:1px solid var(--bd);border-radius:18px;backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);box-shadow:0 1px 0 rgba(255,255,255,.06) inset,0 20px 40px -20px rgba(0,0,0,.7);padding:20px;margin-bottom:14px;transition:transform .25s ease,border-color .25s,box-shadow .25s}
.card.row:hover{transform:translateY(-2px);border-color:rgba(231,201,138,.35);box-shadow:0 1px 0 rgba(255,255,255,.08) inset,0 24px 50px -18px rgba(139,92,246,.35)}
.row{display:grid;grid-template-columns:64px 1.6fr 1fr 1fr 1fr 1.15fr 1.8fr 70px;gap:14px;align-items:center}
.hd{font-size:11px;letter-spacing:.14em;color:var(--mu);padding:0 21px 10px;text-transform:uppercase}
.rk{font-family:var(--serif);font-size:34px;font-weight:700;color:#5d6283;line-height:1;text-align:center}
.rk.m1,.rk.m2,.rk.m3{width:52px;height:52px;border-radius:50%;display:grid;place-items:center;font-size:26px;color:#1a1305;position:relative}
.rk.m1{background:radial-gradient(circle at 30% 25%,#fff4cf,#e7c98a 40%,#a87b2d);box-shadow:0 0 24px rgba(231,201,138,.55),0 0 0 2px rgba(231,201,138,.25)}
.rk.m2{background:radial-gradient(circle at 30% 25%,#ffffff,#cfd6e4 40%,#7f889c);box-shadow:0 0 20px rgba(207,214,228,.35),0 0 0 2px rgba(207,214,228,.2)}
.rk.m3{background:radial-gradient(circle at 30% 25%,#ffe1c4,#d39a6a 40%,#8a5330);box-shadow:0 0 20px rgba(211,154,106,.4),0 0 0 2px rgba(211,154,106,.2)}
.card.row.top1{border-color:rgba(231,201,138,.4);background:linear-gradient(160deg,rgba(231,201,138,.12),rgba(139,92,246,.05) 60%,rgba(255,255,255,.02))}
.nm{font-family:var(--serif);font-weight:700;font-size:18px;letter-spacing:.01em}.nm a{color:#fff}.nm a:hover{color:var(--gold)}.sub{font-size:12px;color:var(--mu);margin-top:3px}
.num{font-size:20px;font-weight:800;white-space:nowrap;letter-spacing:-.01em}.go{white-space:nowrap;font-weight:600;font-size:13px}.lbl{display:none;font-size:10px;letter-spacing:.12em;color:var(--mu)}
.badge{display:inline-block;white-space:nowrap;padding:6px 12px;border-radius:999px;font-size:13px;font-weight:800;color:#06070d;box-shadow:0 0 18px -2px var(--g,rgba(255,255,255,.3))}
.sbar{display:flex;height:10px;border-radius:6px;overflow:hidden;background:rgba(255,255,255,.06);gap:2px}.sbar i{display:block;animation:grow 1.1s cubic-bezier(.2,.8,.2,1) both;transform-origin:left}
.leg{font-size:11px;color:var(--mu);margin-top:6px}.leg b{display:inline-block;width:8px;height:8px;border-radius:50%;margin:0 4px 0 8px}.leg b{margin-left:0!important}
.kol{font-size:12px;color:#c4b0ff;margin-top:4px}
.hero{display:flex;flex-wrap:wrap;gap:24px;align-items:center;padding:28px;border-color:rgba(231,201,138,.25);background:linear-gradient(130deg,rgba(231,201,138,.10),rgba(139,92,246,.10) 55%,rgba(34,211,238,.06))}
.hero .rk{width:auto;height:auto;background:none;box-shadow:none;font-size:64px!important;color:transparent;background:linear-gradient(160deg,#fff4cf,#e7c98a 50%,#a87b2d);-webkit-background-clip:text;background-clip:text}
.big{font-size:26px;font-weight:800;padding:12px 22px;border-radius:16px;color:#06070d;box-shadow:0 10px 30px -8px rgba(0,0,0,.6),0 0 30px -6px rgba(255,255,255,.25)}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:14px}.kpis{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.kpi{background:rgba(255,255,255,.035);border:1px solid rgba(255,255,255,.06);border-radius:14px;padding:14px;transition:border-color .2s,transform .2s}.kpi:hover{border-color:rgba(231,201,138,.35);transform:translateY(-1px)}
.kpi .v{font-size:24px;font-weight:800;letter-spacing:-.01em;background:linear-gradient(180deg,#fff,#d9d4e8);-webkit-background-clip:text;background-clip:text;color:transparent}.kpi .k{font-size:11px;color:var(--mu);letter-spacing:.08em;margin-top:2px}
.donut{width:180px;height:180px;border-radius:50%;position:relative;flex:none;box-shadow:0 0 40px -6px rgba(139,92,246,.45);animation:spin 1.2s cubic-bezier(.2,.8,.2,1) both}.donut:after{content:"";position:absolute;inset:34px;background:radial-gradient(circle,#141729,#0b0d18);border-radius:50%;box-shadow:inset 0 0 0 1px rgba(255,255,255,.08)}
.dw{display:flex;gap:28px;align-items:center;flex-wrap:wrap}.pb{margin:14px 0}.pb .t{display:flex;justify-content:space-between;font-size:14px;margin-bottom:6px}.pb .t b{font-size:16px}
.pb .b{height:10px;background:rgba(255,255,255,.06);border-radius:6px;overflow:hidden}.pb .b i{display:block;height:100%;border-radius:6px;animation:grow 1.2s cubic-bezier(.2,.8,.2,1) both;transform-origin:left;box-shadow:0 0 12px rgba(255,255,255,.15)}
h2{font-family:var(--serif);font-size:19px;font-weight:700;margin:0 0 14px;color:#f3e3bd;letter-spacing:.02em}.note{font-size:12px;color:var(--mu);line-height:1.6}
table.info{width:100%;font-size:14px;border-collapse:collapse}table.info td{padding:9px 4px;border-bottom:1px solid rgba(255,255,255,.07)}table.info td:first-child{color:var(--mu);width:40%}
.nav{display:flex;justify-content:space-between;gap:10px;flex-wrap:wrap}.btn{display:inline-block;padding:10px 16px;background:rgba(255,255,255,.05);border:1px solid var(--bd);border-radius:999px;font-size:14px;color:var(--tx);backdrop-filter:blur(10px);transition:all .25s}.btn:hover{border-color:var(--gold);color:var(--gold);box-shadow:0 0 20px -4px rgba(231,201,138,.5)}
.view,main>.wrap{animation:fade .5s ease both}@keyframes fade{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}
@keyframes grow{from{transform:scaleX(0)}to{transform:scaleX(1)}}@keyframes spin{from{transform:rotate(-90deg) scale(.85);opacity:0}to{transform:none;opacity:1}}
@media(prefers-reduced-motion:reduce){*,*:before,*:after{animation:none!important;transition:none!important}}
@media(max-width:820px){.row{grid-template-columns:56px 1fr 1fr;row-gap:12px}.hd{display:none}.lbl{display:block}.row .w{grid-column:2/-1}.rk{grid-row:span 4;align-self:start}.grid2{grid-template-columns:1fr}.kpis{grid-template-columns:1fr 1fr}.big{font-size:20px}.hero .rk{font-size:48px!important}.donut{width:150px;height:150px}.donut:after{inset:28px}.num{font-size:18px}header.top{padding:32px 18px 24px}}"""
def main(s):
    m=max(['card','video','live'],key=lambda x:s[x]); return m
def sbar(s): return '<div class="sbar">'+''.join(f'<i style="width:{s[x]}%;background:{C[x]}"></i>' for x in C)+'</div>'
def href(n,single): return f'#/shop/{n}' if single else f'shop-{n}.html'
def home(single): return '#/' if single else 'index.html'
def head(): return f'<header class="top"><div class="in"><h1>美国 TikTok Shop · 时尚配件 竞品监控</h1><div class="upd">数据更新：{DATA["updated"]}，来源 {DATA["source"]}，每个工作日约 9:00（美东）更新</div></div></header>'
def index(single):
    r=['<div class="wrap"><p class="note">按近 7 天销量排名 · 渠道占比为 28 天成交方式（商品卡/视频/直播）；达人% 为达人带货占比（与店铺自营号为另一维度）</p>',
       '<div class="row hd"><div>排名</div><div>店铺</div><div>7天销量</div><div>28天销量</div><div>28天GMV</div><div>主要出单来源</div><div>商品卡/视频/直播 · 达人%</div><div></div></div>']
    for s in S:
        m=main(s)
        r.append(f'<div class="card row{" top1" if s["rank"]==1 else ""}"><div class="rk{(" m"+str(s["rank"])) if s["rank"]<=3 else ""}">{s["rank"]}</div><div class="w"><div class="nm"><a href="{href(s["rank"],single)}">{e(s["name"])}</a></div><div class="sub">{s["type"]} · 评分 {s["rating"]} · 达人 {s["creators"]:,}</div></div>'
          f'<div><span class="lbl">7天销量</span><span class="num">{s["s7"]}</span></div><div><span class="lbl">28天销量</span><span class="num">{s["s28"]}</span></div><div><span class="lbl">28天GMV</span><span class="num">{s["g28"]}</span></div>'
          f'<div><span class="badge" style="background:{C[m]};--g:{C[m]}">{L[m]} {s[m]:.0f}%</span></div><div class="w">{sbar(s)}<div class="leg">'+''.join(f'<span style="white-space:nowrap;margin-right:8px"><b style="background:{C[x]}"></b>{L[x]} {s[x]}%</span>' for x in C)+f'</div><div class="kol">达人带货 {s["kol"]}%</div></div><div><a class="go" href="{href(s["rank"],single)}">详情 →</a></div></div>')
    return ''.join(r)+'</div>'
def pb(n,v,c): return f'<div class="pb"><div class="t"><span>{n}</span><b>{v}%</b></div><div class="b"><i style="width:{v}%;background:{c}"></i></div></div>'
def detail(s,single):
    m=main(s); n=s['rank']; a=s['card']; b=a+s['video']
    dn=f'conic-gradient({C["card"]} 0 {a}%,{C["video"]} {a}% {b}%,{C["live"]} {b}% 100%)'
    fm='https://www.fastmoss.com/zh/'
    prev=f'<a class="btn" href="{href(n-1,single)}">← #{n-1} {e(S[n-2]["name"])}</a>' if n>1 else '<span></span>'
    nxt=f'<a class="btn" href="{href(n+1,single)}">#{n+1} {e(S[n]["name"])} →</a>' if n<len(S) else '<span></span>'
    k=[('7天销量',s['s7']),('7天GMV',s['g7']),('28天销量',s['s28']),('28天GMV',s['g28']),('累计销量',s['st']),('累计GMV',s['gt'])]
    return f'''<div class="wrap"><div class="nav" style="margin-bottom:14px"><a class="btn" href="{home(single)}">← 返回排行榜</a></div>
<div class="card hero"><div class="rk t" style="font-size:44px">#{n}</div><div style="flex:1;min-width:200px"><div class="nm" style="font-size:24px">{e(s["name"])}</div><div class="sub">{s["type"]} · 近7天销量排名第 {n}</div></div>
<div><div class="big" style="background:{C[m]}">主要靠{L[m]}（{s[m]:.0f}%）</div><div class="kol" style="font-size:14px;margin-top:8px">达人带货占 {s["kol"]}%，店铺自营号占 {s["own"]}%</div></div></div>
<div class="card"><h2>核心指标</h2><div class="kpis">{"".join(f'<div class="kpi"><div class="v">{v}</div><div class="k">{t}</div></div>' for t,v in k)}</div><p class="note">销量/GMV 为 28 天周期，7 天数据来自排行榜。</p></div>
<div class="grid2"><div class="card"><h2>成交方式（28天）</h2><div class="dw"><div class="donut" style="background:{dn}"></div><div>{"".join(f'<div style="margin:6px 0"><b style="display:inline-block;width:10px;height:10px;border-radius:2px;background:{C[x]}"></b> {L[x]} <b>{s[x]}%</b></div>' for x in C)}</div></div></div>
<div class="card"><h2>渠道占比</h2>{pb("商品卡",s["card"],C["card"])}{pb("视频",s["video"],C["video"])}{pb("达人带货",s["kol"],"linear-gradient(90deg,#8b5cf6,#22d3ee)")}{pb("直播",s["live"],C["live"])}<p class="note">注：达人带货是另一维度（达人 vs 店铺自营号），与商品卡/视频/直播不相加。</p></div></div>
<div class="grid2"><div class="card"><h2>🔥 最热商品</h2><div class="nm">{e(s["pname"])}</div><div class="kpis" style="margin-top:12px"><div class="kpi"><div class="v">{s["pprice"]}</div><div class="k">售价</div></div><div class="kpi"><div class="v">{s["psales"]}</div><div class="k">28天销量</div></div><div class="kpi"><div class="v">{s["pgmv"]}</div><div class="k">28天GMV</div></div></div><p><a href="{fm}e-commerce/detail/{s["pid"]}" target="_blank" rel="noopener">在 FastMoss 查看商品 ↗</a></p></div>
<div class="card"><h2>店铺信息</h2><table class="info"><tr><td>店铺 ID</td><td>{s["id"]}</td></tr><tr><td>店铺类型</td><td>{s["type"]}</td></tr><tr><td>官方账号</td><td>{e(s["acct"])}</td></tr><tr><td>店铺评分</td><td>{s["rating"]}</td></tr><tr><td>带货达人数</td><td>{s["creators"]:,}</td></tr></table><p><a href="{fm}shop-marketing/detail/{s["id"]}" target="_blank" rel="noopener">在 FastMoss 查看店铺 ↗</a></p></div></div>
<div class="nav">{prev}{nxt}</div></div>'''
def page(title,body): return f'<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(title)}</title><style>{CSS}</style></head><body>{head()}<main>{body}</main></body></html>'
js='const DATA = '+json.dumps(DATA,ensure_ascii=False,indent=1)+';\n'
open('data.js','w',encoding='utf-8').write(js)
open('index.html','w',encoding='utf-8').write(page('竞品监控排行榜',index(False)))
for s in S: open(f'shop-{s["rank"]}.html','w',encoding='utf-8').write(page(s['name']+' · 竞品详情',detail(s,False)))
views={'/':index(True)}; views.update({f'/shop/{s["rank"]}':detail(s,True) for s in S})
single=f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>TikTok Shop 时尚配件竞品监控</title><style>{CSS}</style></head><body>{head()}<main id="app"></main>
<script>{js}const VIEWS={json.dumps(views,ensure_ascii=False)};
function r(){{var h=location.hash.replace(/^#/,'')||'/';var a=document.getElementById('app');a.className='';void a.offsetWidth;a.innerHTML=VIEWS[h]||VIEWS['/'];a.className='view';window.scrollTo(0,0)}}
addEventListener('hashchange',r);r();</script></body></html>'''
open(os.path.join(D,'..','tk-monitor.html'),'w',encoding='utf-8').write(single)
print('built',len(S),'shops')
