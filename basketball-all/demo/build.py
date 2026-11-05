"""static/ → docs/ : FastAPI 없이 GitHub Pages 에서 도는 데모판을 만든다. 실행: python3 demo/build.py"""
import json, os, re, shutil
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out = os.path.join(root, 'docs')
shutil.rmtree(out, ignore_errors=True); os.makedirs(out)
for f in ('manifest.webmanifest', 'sw.js', 'icon.svg'):
    shutil.copy(os.path.join(root, 'static', f), out)
shutil.copytree(os.path.join(root, 'static', 'img'), os.path.join(out, 'img'))
courts = json.load(open(os.path.join(root, 'demo', 'courts.json'), encoding='utf-8'))
backend = open(os.path.join(root, 'demo', 'demo-backend.js'), encoding='utf-8').read().replace('__COURTS__', json.dumps(courts, ensure_ascii=False))
h = open(os.path.join(root, 'static', 'index.html'), encoding='utf-8').read()
css = '.demo{background:#17191d;color:#fff;font-size:12.5px;line-height:1.5;padding:9px 16px;display:flex;gap:10px;align-items:center}.demo span{flex:1}.demo button{color:#ffb59a;font-weight:700;text-decoration:underline;text-underline-offset:3px;white-space:nowrap}'
h = h.replace('</style>', css + '</style>', 1)
h = h.replace('<div class="app">', '<div class="app"><div class="demo"><span>체험용 데모입니다. 입력한 내용은 이 브라우저에만 저장되며 다른 사람과 공유되지 않습니다. "예시"가 붙은 항목은 샘플 데이터입니다.</span><button onclick="if(confirm(\'데모 데이터를 처음 상태로 되돌리시겠습니까?\'))__resetDemo()">초기화</button></div>', 1)
i = h.index('<script>')
h = h[:i] + '<script>\n' + backend + '\n</script>\n' + h[i:]
open(os.path.join(out, 'index.html'), 'w', encoding='utf-8').write(h)
print('built', os.listdir(out))
