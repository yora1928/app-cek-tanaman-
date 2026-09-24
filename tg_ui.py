"""TOMAT GROW - Semua template HTML, CSS, dan JS sebagai string."""

CSS = r"""
:root{--hijau:#2e7d32;--hijau-muda:#e8f5e9;--hijau-tua:#1b5e20;--abu-bg:#f4f6f8;
--abu-border:#dfe3e8;--teks:#1f2933;--teks-lembut:#5c6b7a;--merah:#c62828;--kuning:#ef6c00;
--biru:#1565c0;--radius:10px;--shadow:0 1px 3px rgba(0,0,0,.06),0 1px 2px rgba(0,0,0,.04);}
*{box-sizing:border-box}
html,body{margin:0;padding:0;font-family:-apple-system,"Segoe UI",Roboto,Arial,sans-serif;
background:var(--abu-bg);color:var(--teks);font-size:14.5px;line-height:1.5}
a{color:var(--hijau);text-decoration:none}a:hover{text-decoration:underline}
.layout{display:flex;min-height:100vh}
.sidebar{width:230px;background:#fff;border-right:1px solid var(--abu-border);padding:18px 12px;
position:sticky;top:0;height:100vh;overflow-y:auto;flex-shrink:0}
.brand{display:flex;align-items:center;gap:10px;padding:6px 10px 18px;border-bottom:1px solid var(--abu-border);margin-bottom:12px}
.brand-logo{width:36px;height:36px;border-radius:10px;background:var(--hijau);color:#fff;display:flex;
align-items:center;justify-content:center;font-weight:700;font-size:16px}
.brand-text strong{display:block;font-size:14px;letter-spacing:.5px}
.brand-text span{font-size:11px;color:var(--teks-lembut)}
.nav a{display:flex;align-items:center;gap:10px;padding:9px 12px;border-radius:8px;color:var(--teks-lembut);
font-weight:500;font-size:13.5px;margin-bottom:2px}
.nav a:hover{background:var(--abu-bg);text-decoration:none;color:var(--teks)}
.nav a.active{background:var(--hijau-muda);color:var(--hijau-tua);font-weight:600}
.nav .ico{width:18px;text-align:center;font-size:15px}
.content{flex:1;min-width:0;display:flex;flex-direction:column}
.topbar{background:#fff;border-bottom:1px solid var(--abu-border);padding:12px 22px;display:flex;
align-items:center;justify-content:space-between;position:sticky;top:0;z-index:20}
.topbar h1{font-size:17px;margin:0;font-weight:600}
.topbar .user{font-size:13px;color:var(--teks-lembut);display:flex;align-items:center;gap:12px}
.badge-role{background:var(--hijau-muda);color:var(--hijau-tua);padding:2px 9px;border-radius:999px;
font-size:11px;font-weight:600}
.page{padding:22px;max-width:1200px;width:100%}
.card{background:#fff;border:1px solid var(--abu-border);border-radius:var(--radius);padding:18px;
box-shadow:var(--shadow);margin-bottom:16px}
.card h2,.card h3{margin-top:0;font-size:15px;font-weight:600}
.grid{display:grid;gap:14px}
.grid-2{grid-template-columns:repeat(2,1fr)}
.grid-3{grid-template-columns:repeat(3,1fr)}
.grid-4{grid-template-columns:repeat(4,1fr)}
.stat{background:#fff;border:1px solid var(--abu-border);border-radius:var(--radius);padding:14px 16px;box-shadow:var(--shadow)}
.stat .label{font-size:12px;color:var(--teks-lembut);margin-bottom:4px}
.stat .value{font-size:22px;font-weight:700;color:var(--teks)}
.stat .value.green{color:var(--hijau)}.stat .value.red{color:var(--merah)}
.stat .value.orange{color:var(--kuning)}.stat .value.blue{color:var(--biru)}
.btn{display:inline-flex;align-items:center;gap:6px;padding:8px 14px;border-radius:8px;
border:1px solid transparent;cursor:pointer;font-size:13.5px;font-weight:500;font-family:inherit;
background:var(--hijau);color:#fff;transition:filter .15s ease}
.btn:hover{filter:brightness(.94);text-decoration:none}
.btn-outline{background:#fff;color:var(--teks);border-color:var(--abu-border)}
.btn-outline:hover{background:var(--abu-bg)}
.btn-danger{background:var(--merah)}
.btn-sm{padding:5px 10px;font-size:12.5px}
.btn:disabled{opacity:.55;cursor:not-allowed}
.table-wrap{overflow-x:auto}
table.data{width:100%;border-collapse:collapse;font-size:13px;background:#fff}
table.data th,table.data td{padding:9px 11px;text-align:left;border-bottom:1px solid var(--abu-border);white-space:nowrap}
table.data th{background:#f8fafb;font-weight:600;color:var(--teks-lembut);font-size:12px;
text-transform:uppercase;letter-spacing:.3px}
table.data tbody tr:hover{background:#fafcfd}
table.data td.wrap{white-space:normal;min-width:160px}
.form-grid{display:grid;gap:14px;grid-template-columns:repeat(2,1fr)}
.field{display:flex;flex-direction:column;gap:5px}
.field.full{grid-column:1/-1}
.field label{font-size:12.5px;font-weight:500;color:var(--teks-lembut)}
.field input,.field select,.field textarea{padding:8px 11px;border:1px solid var(--abu-border);
border-radius:8px;font-size:13.5px;font-family:inherit;background:#fff;color:var(--teks);width:100%}
.field input:focus,.field select:focus,.field textarea:focus{outline:none;border-color:var(--hijau);
box-shadow:0 0 0 3px rgba(46,125,50,.10)}
.field textarea{resize:vertical;min-height:70px}
.field .hint{font-size:11.5px;color:var(--teks-lembut)}
.toolbar{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin-bottom:14px}
.toolbar .spacer{flex:1}
.toolbar input,.toolbar select{padding:8px 11px;border:1px solid var(--abu-border);border-radius:8px;
font-size:13.5px;font-family:inherit;background:#fff}
.badge{display:inline-block;padding:3px 10px;border-radius:999px;font-size:11.5px;font-weight:600}
.badge.hidup{background:#e8f5e9;color:#2e7d32}
.badge.kurang{background:#fff3e0;color:#ef6c00}
.badge.mati{background:#ffebee;color:#c62828}
.badge.panen{background:#e3f2fd;color:#1565c0}
.modal-backdrop{position:fixed;inset:0;background:rgba(15,23,32,.45);display:none;align-items:center;
justify-content:center;z-index:100;padding:18px}
.modal-backdrop.show{display:flex}
.modal{background:#fff;border-radius:12px;width:100%;max-width:680px;max-height:90vh;overflow-y:auto;
padding:22px;box-shadow:0 12px 40px rgba(0,0,0,.2)}
.modal h3{margin-top:0}
.modal-actions{display:flex;justify-content:flex-end;gap:10px;margin-top:18px;padding-top:14px;
border-top:1px solid var(--abu-border)}
.toast{position:fixed;bottom:22px;right:22px;z-index:200;background:#263238;color:#fff;padding:12px 18px;
border-radius:8px;font-size:13.5px;max-width:340px;box-shadow:0 8px 24px rgba(0,0,0,.25);opacity:0;
transform:translateY(10px);transition:opacity .2s,transform .2s;pointer-events:none}
.toast.show{opacity:1;transform:translateY(0)}
.toast.error{background:#b71c1c}.toast.success{background:#1b5e20}
.timeline{position:relative;padding-left:24px}
.timeline::before{content:"";position:absolute;left:7px;top:4px;bottom:4px;width:2px;background:var(--abu-border)}
.tl-item{position:relative;margin-bottom:16px}
.tl-item::before{content:"";position:absolute;left:-21px;top:4px;width:12px;height:12px;border-radius:50%;
background:var(--hijau);border:2px solid #fff;box-shadow:0 0 0 1px var(--abu-border)}
.tl-item.perawatan::before{background:var(--biru)}
.tl-item.dokumentasi::before{background:var(--kuning)}
.tl-item .tl-date{font-size:11.5px;color:var(--teks-lembut)}
.tl-item .tl-title{font-weight:600;font-size:13.5px}
.tl-item .tl-desc{font-size:12.5px;color:var(--teks-lembut)}
.gallery{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:14px}
.gallery .item{background:#fff;border:1px solid var(--abu-border);border-radius:var(--radius);
overflow:hidden;box-shadow:var(--shadow)}
.gallery .item img{width:100%;height:150px;object-fit:cover;display:block}
.gallery .item .cap{padding:9px 11px;font-size:12.5px}
.gallery .item .cap .tgl{color:var(--teks-lembut);font-size:11.5px}
.chart-box{position:relative;height:280px}
.login-page{min-height:100vh;display:flex;align-items:center;justify-content:center;
background:linear-gradient(160deg,#eef7ef 0%,#f4f6f8 55%);padding:20px}
.login-card{background:#fff;border-radius:14px;padding:34px 30px;width:100%;max-width:380px;
box-shadow:0 12px 40px rgba(0,0,0,.08);border:1px solid var(--abu-border)}
.login-card .logo{width:52px;height:52px;border-radius:14px;background:var(--hijau);color:#fff;
display:flex;align-items:center;justify-content:center;font-weight:700;font-size:20px;margin:0 auto 16px}
.login-card h1{text-align:center;font-size:19px;margin:0 0 4px;letter-spacing:.5px}
.login-card p.sub{text-align:center;font-size:12.5px;color:var(--teks-lembut);margin:0 0 22px}
.login-card .field{margin-bottom:14px}
.login-card .btn{width:100%;justify-content:center;padding:10px}
.flash{padding:10px 14px;border-radius:8px;font-size:13px;margin-bottom:14px}
.flash.danger{background:#ffebee;color:#b71c1c}
.flash.warning{background:#fff8e1;color:#8d6e00}
.empty{text-align:center;padding:40px 18px;color:var(--teks-lembut);font-size:13.5px}
@media(max-width:900px){.grid-4{grid-template-columns:repeat(2,1fr)}.grid-3{grid-template-columns:repeat(2,1fr)}
.form-grid{grid-template-columns:1fr}}
@media(max-width:720px){.layout{flex-direction:column}.sidebar{width:100%;height:auto;position:static;
border-right:none;border-bottom:1px solid var(--abu-border);padding:12px}
.nav{display:flex;overflow-x:auto;gap:4px;padding-bottom:4px}
.nav a{white-space:nowrap;margin-bottom:0}.page{padding:14px}
.grid-4,.grid-3,.grid-2{grid-template-columns:1fr}
.topbar{padding:10px 14px;flex-wrap:wrap;gap:8px}}
"""


JS = r"""
async function api(url, options={}){
  const opts=Object.assign({headers:{}},options);
  if(opts.body&&!(opts.body instanceof FormData)){
    opts.headers['Content-Type']='application/json';
    if(typeof opts.body!=='string')opts.body=JSON.stringify(opts.body);
  }
  const res=await fetch(url,opts);
  if(res.status===401){window.location.href='/login';return;}
  const ct=res.headers.get('content-type')||'';
  if(!ct.includes('application/json')){
    if(!res.ok)throw new Error('Terjadi kesalahan pada server.');
    return res;
  }
  const data=await res.json();
  if(!res.ok)throw new Error(data.error||'Terjadi kesalahan.');
  return data;
}
function toast(msg,type='success'){
  let el=document.querySelector('.toast');
  if(!el){el=document.createElement('div');el.className='toast';document.body.appendChild(el);}
  el.className='toast '+type;el.textContent=msg;
  requestAnimationFrame(()=>el.classList.add('show'));
  clearTimeout(el._t);el._t=setTimeout(()=>el.classList.remove('show'),3200);
}
function esc(s){
  if(s===null||s===undefined)return '';
  return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')
    .replace(/"/g,'&quot;').replace(/'/g,'&#39;');
}
function fmtTanggal(iso){
  if(!iso)return '-';
  const b=['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember'];
  const d=new Date(iso+'T00:00:00');
  if(isNaN(d))return iso;
  return d.getDate()+' '+b[d.getMonth()]+' '+d.getFullYear();
}
function statusBadge(status){
  const m={'hidup':['hidup','Hidup'],'kurang sehat':['kurang','Kurang Sehat'],
    'mati':['mati','Mati'],'panen':['panen','Panen']};
  const [c,l]=m[status]||['hidup',status||'-'];
  return '<span class="badge '+c+'">'+esc(l)+'</span>';
}
function todayISO(){
  const d=new Date();
  const m=String(d.getMonth()+1).padStart(2,'0');
  const day=String(d.getDate()).padStart(2,'0');
  return d.getFullYear()+'-'+m+'-'+day;
}
function openModal(id){document.getElementById(id).classList.add('show');}
function closeModal(id){document.getElementById(id).classList.remove('show');}
function debounce(fn,ms){let t;return(...a)=>{clearTimeout(t);t=setTimeout(()=>fn(...a),ms);};}
document.addEventListener('click',e=>{
  if(e.target.classList&&e.target.classList.contains('modal-backdrop'))e.target.classList.remove('show');
});
"""


TEMPLATES = {}

TEMPLATES["base.html"] = r"""<!DOCTYPE html>
<html lang="id"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{% block title %}TOMAT GROW{% endblock %}</title>
<link rel="stylesheet" href="/static/css/style.css">
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
</head><body>
<div class="layout">
  <aside class="sidebar">
    <div class="brand">
      <div class="brand-logo">TG</div>
      <div class="brand-text"><strong>TOMAT GROW</strong><span>Monitoring Tanaman Tomat</span></div>
    </div>
    <nav class="nav">
      <a href="/dashboard" class="{{ 'active' if active=='dashboard' }}"><span class="ico">▤</span> Dashboard</a>
      <a href="/tanaman" class="{{ 'active' if active=='tanaman' }}"><span class="ico">🌱</span> Data Tanaman</a>
      <a href="/pengukuran" class="{{ 'active' if active=='pengukuran' }}"><span class="ico">📏</span> Pengukuran</a>
      <a href="/perawatan" class="{{ 'active' if active=='perawatan' }}"><span class="ico">💧</span> Perawatan</a>
      <a href="/dokumentasi" class="{{ 'active' if active=='dokumentasi' }}"><span class="ico">📷</span> Dokumentasi</a>
      <a href="/jadwal" class="{{ 'active' if active=='jadwal' }}"><span class="ico">🗓</span> Jadwal</a>
      <a href="/laporan" class="{{ 'active' if active=='laporan' }}"><span class="ico">📄</span> Laporan</a>
      {% if current_user.role in ['admin','pembina'] %}
      <a href="/audit" class="{{ 'active' if active=='audit' }}"><span class="ico">🕘</span> Riwayat</a>
      {% endif %}
      {% if current_user.role=='admin' %}
      <a href="/pengguna" class="{{ 'active' if active=='pengguna' }}"><span class="ico">👥</span> Pengguna</a>
      {% endif %}
    </nav>
  </aside>
  <main class="content">
    <header class="topbar">
      <h1>{% block page_title %}Dashboard{% endblock %}</h1>
      <div class="user">
        <span>{{ current_user.nama }}</span>
        <span class="badge-role">{{ current_user.role }}</span>
        <a class="btn btn-outline btn-sm" href="/logout">Keluar</a>
      </div>
    </header>
    <div class="page">
      {% with messages = get_flashed_messages(with_categories=true) %}
      {% for cat,msg in messages %}<div class="flash {{ cat }}">{{ msg }}</div>{% endfor %}
      {% endwith %}
      {% block content %}{% endblock %}
    </div>
  </main>
</div>
<script src="/static/js/common.js"></script>
{% block scripts %}{% endblock %}
</body></html>"""


TEMPLATES["login.html"] = r"""<!DOCTYPE html>
<html lang="id"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Masuk - TOMAT GROW</title>
<link rel="stylesheet" href="/static/css/style.css">
</head><body>
<div class="login-page"><div class="login-card">
  <div class="logo">TG</div>
  <h1>TOMAT GROW</h1>
  <p class="sub">Sistem Monitoring Pertumbuhan dan Perkembangan Tanaman Tomat</p>
  {% with messages = get_flashed_messages(with_categories=true) %}
  {% for cat,msg in messages %}<div class="flash {{ cat }}">{{ msg }}</div>{% endfor %}
  {% endwith %}
  <form method="POST" action="/login">
    <div class="field"><label for="username">Username</label>
      <input type="text" id="username" name="username" required autofocus></div>
    <div class="field"><label for="password">Password</label>
      <input type="password" id="password" name="password" required></div>
    <button class="btn" type="submit">Masuk</button>
  </form>
</div></div></body></html>"""


TEMPLATES["dashboard.html"] = r"""{% extends "base.html" %}
{% block title %}Dashboard - TOMAT GROW{% endblock %}
{% block page_title %}Dashboard{% endblock %}
{% block content %}
<div class="grid grid-4">
  <div class="stat"><div class="label">Total Tanaman</div><div class="value" id="s-total">-</div></div>
  <div class="stat"><div class="label">Tanaman Sehat</div><div class="value green" id="s-sehat">-</div></div>
  <div class="stat"><div class="label">Bermasalah</div><div class="value orange" id="s-bermasalah">-</div></div>
  <div class="stat"><div class="label">Tanaman Mati</div><div class="value red" id="s-mati">-</div></div>
  <div class="stat"><div class="label">Tinggi Rata-rata (cm)</div><div class="value" id="s-tinggi">-</div></div>
  <div class="stat"><div class="label">Total Bunga</div><div class="value blue" id="s-bunga">-</div></div>
  <div class="stat"><div class="label">Total Buah</div><div class="value blue" id="s-buah">-</div></div>
  <div class="stat"><div class="label">Tanaman Panen</div><div class="value green" id="s-panen">-</div></div>
</div>

<div class="card"><h2>Perkembangan Tinggi Tanaman (Rata-rata)</h2>
  <div class="chart-box"><canvas id="chart-tinggi"></canvas></div></div>

<div class="grid grid-2">
  <div class="card"><h2>Perkembangan Jumlah Daun</h2>
    <div class="chart-box"><canvas id="chart-daun"></canvas></div></div>
  <div class="card"><h2>Perkembangan Bunga &amp; Buah</h2>
    <div class="chart-box"><canvas id="chart-bunga"></canvas></div></div>
</div>

<div class="grid grid-2">
  <div class="card"><h2>Kegiatan Perawatan Terakhir</h2><div id="kegiatan"><div class="empty">Memuat…</div></div></div>
  <div class="card"><h2>Jadwal Hari Ini</h2><div id="jadwal"><div class="empty">Memuat…</div></div></div>
</div>
{% endblock %}
{% block scripts %}
<script>
const charts={};
function buatChart(id,labels,datasets,yl){
  const el=document.getElementById(id); if(!el)return;
  if(charts[id])charts[id].destroy();
  charts[id]=new Chart(el.getContext('2d'),{type:'line',
    data:{labels,datasets},
    options:{responsive:true,maintainAspectRatio:false,
      interaction:{mode:'index',intersect:false},
      plugins:{legend:{position:'bottom',labels:{boxWidth:12,font:{size:11}}}},
      scales:{y:{beginAtZero:true,title:{display:true,text:yl,font:{size:11}},
        grid:{color:'#eef1f4'}},x:{grid:{display:false}}}}});
}
(async function(){
  try{
    const res=await api('/api/dashboard'); const r=res.ringkasan;
    document.getElementById('s-total').textContent=r.total_tanaman;
    document.getElementById('s-sehat').textContent=r.sehat;
    document.getElementById('s-bermasalah').textContent=r.bermasalah;
    document.getElementById('s-mati').textContent=r.mati;
    document.getElementById('s-panen').textContent=r.panen;
    document.getElementById('s-tinggi').textContent=r.tinggi_rata_rata??'-';
    document.getElementById('s-bunga').textContent=r.total_bunga;
    document.getElementById('s-buah').textContent=r.total_buah;

    const kg=document.getElementById('kegiatan');
    if(!res.kegiatan_terakhir.length)kg.innerHTML='<div class="empty">Belum ada catatan.</div>';
    else kg.innerHTML=res.kegiatan_terakhir.map(k=>`
      <div style="padding:8px 0;border-bottom:1px solid var(--abu-border)">
        <div style="font-size:11.5px;color:var(--teks-lembut)">${esc(fmtTanggal(k.tanggal))} • ${esc(k.petugas||'-')}</div>
        <div style="font-weight:600">${esc(k.jenis_kegiatan.replace(/_/g,' '))}</div>
        <div style="font-size:12.5px;color:var(--teks-lembut)">${esc(k.keterangan||'-')}</div>
      </div>`).join('');

    const jh=document.getElementById('jadwal');
    if(!res.jadwal_hari_ini.length)jh.innerHTML='<div class="empty">Tidak ada jadwal hari ini.</div>';
    else jh.innerHTML=res.jadwal_hari_ini.map(j=>`
      <div style="padding:8px 0;border-bottom:1px solid var(--abu-border)">
        <div style="font-weight:600">${esc(j.kegiatan)}</div>
        <div style="font-size:12.5px;color:var(--teks-lembut)">Petugas: ${esc(j.petugas||'-')} • ${esc(j.status)}</div>
      </div>`).join('');

    const g=res.grafik;
    const mk=(l,d,w)=>({label:l,data:d,borderColor:w,backgroundColor:w+'22',
      tension:.3,pointRadius:3,borderWidth:2,spanGaps:true});
    if(!g.labels.length){
      document.querySelectorAll('.chart-box').forEach(b=>b.innerHTML='<div class="empty">Belum ada data pengukuran.</div>');
      return;
    }
    buatChart('chart-tinggi',g.labels,[mk('Tinggi (cm)',g.tinggi,'#2e7d32')],'cm');
    buatChart('chart-daun',g.labels,[mk('Jumlah Daun',g.daun,'#1565c0')],'helai');
    buatChart('chart-bunga',g.labels,[mk('Bunga',g.bunga,'#ef6c00'),mk('Buah',g.buah,'#c62828')],'jumlah');
  }catch(e){toast(e.message,'error');}
})();
</script>
{% endblock %}"""


TEMPLATES["tanaman.html"] = r"""{% extends "base.html" %}
{% block title %}Data Tanaman{% endblock %}
{% block page_title %}Data Tanaman{% endblock %}
{% block content %}
<div class="card">
  <div class="toolbar">
    <input type="text" id="q" placeholder="Cari kode/nama/varietas/lokasi…" style="min-width:260px">
    <select id="f-status">
      <option value="">Semua Status</option><option value="hidup">Hidup</option>
      <option value="kurang sehat">Kurang Sehat</option><option value="mati">Mati</option>
      <option value="panen">Panen</option>
    </select>
    <div class="spacer"></div>
    {% if current_user.can_edit %}<button class="btn" onclick="bukaTambah()">+ Tambah Tanaman</button>{% endif %}
  </div>
  <div class="table-wrap"><table class="data" id="tbl">
    <thead><tr><th>Kode</th><th>Nama</th><th>Varietas</th><th>Tgl Tanam</th><th>Lokasi</th>
      <th>Posisi</th><th>Status</th><th>Aksi</th></tr></thead>
    <tbody><tr><td colspan="8" class="empty">Memuat…</td></tr></tbody>
  </table></div>
</div>

<div class="modal-backdrop" id="modal-form"><div class="modal">
  <h3 id="modal-title">Tambah Tanaman</h3>
  <form onsubmit="return simpan(event)">
    <input type="hidden" id="f-id">
    <div class="form-grid">
      <div class="field"><label>Kode Tanaman *</label><input id="f-kode" required maxlength="50"></div>
      <div class="field"><label>Nama Tanaman *</label><input id="f-nama" required maxlength="120"></div>
      <div class="field"><label>Varietas</label><input id="f-varietas" maxlength="120"></div>
      <div class="field"><label>Tanggal Tanam *</label><input type="date" id="f-tanggal" required></div>
      <div class="field"><label>Lokasi</label><input id="f-lokasi" maxlength="150"></div>
      <div class="field"><label>Posisi</label><input id="f-posisi" maxlength="80"></div>
      <div class="field"><label>Status</label><select id="f-st">
        <option value="hidup">Hidup</option><option value="kurang sehat">Kurang Sehat</option>
        <option value="mati">Mati</option><option value="panen">Panen</option>
      </select></div>
      <div class="field full"><label>Catatan</label><textarea id="f-catatan"></textarea></div>
    </div>
    <div class="modal-actions">
      <button type="button" class="btn btn-outline" onclick="closeModal('modal-form')">Batal</button>
      <button type="submit" class="btn">Simpan</button>
    </div>
  </form>
</div></div>
{% endblock %}
{% block scripts %}
<script>
const CAN_EDIT={{ 'true' if current_user.can_edit else 'false' }};
const IS_ADMIN={{ 'true' if current_user.role=='admin' else 'false' }};
async function muat(){
  const q=document.getElementById('q').value.trim();
  const st=document.getElementById('f-status').value;
  const tb=document.querySelector('#tbl tbody');
  try{
    const res=await api('/api/tanaman?q='+encodeURIComponent(q)+'&status='+encodeURIComponent(st));
    if(!res.data.length){tb.innerHTML='<tr><td colspan="8" class="empty">Belum ada data tanaman.</td></tr>';return;}
    tb.innerHTML=res.data.map(t=>`
      <tr><td><strong>${esc(t.kode_tanaman)}</strong></td><td>${esc(t.nama_tanaman)}</td>
        <td>${esc(t.varietas||'-')}</td><td>${esc(t.tanggal_tanam||'-')}</td>
        <td>${esc(t.lokasi||'-')}</td><td>${esc(t.posisi||'-')}</td>
        <td>${statusBadge(t.status)}</td>
        <td><a class="btn btn-outline btn-sm" href="/tanaman/${t.id}">Detail</a>
          ${CAN_EDIT?`<button class="btn btn-outline btn-sm" onclick='edit(${JSON.stringify(t)})'>Edit</button>`:''}
          ${IS_ADMIN?`<button class="btn btn-danger btn-sm" onclick="hapus(${t.id},'${esc(t.kode_tanaman)}')">Hapus</button>`:''}
        </td></tr>`).join('');
  }catch(e){toast(e.message,'error');}
}
function bukaTambah(){
  document.getElementById('modal-title').textContent='Tambah Tanaman';
  document.querySelector('#modal-form form').reset();
  document.getElementById('f-id').value='';
  document.getElementById('f-tanggal').value=todayISO();
  openModal('modal-form');
}
function edit(t){
  document.getElementById('modal-title').textContent='Edit Tanaman';
  document.getElementById('f-id').value=t.id;
  document.getElementById('f-kode').value=t.kode_tanaman;
  document.getElementById('f-nama').value=t.nama_tanaman;
  document.getElementById('f-varietas').value=t.varietas||'';
  document.getElementById('f-tanggal').value=t.tanggal_tanam||'';
  document.getElementById('f-lokasi').value=t.lokasi||'';
  document.getElementById('f-posisi').value=t.posisi||'';
  document.getElementById('f-st').value=t.status;
  document.getElementById('f-catatan').value=t.catatan||'';
  openModal('modal-form');
}
async function simpan(ev){
  ev.preventDefault();
  const id=document.getElementById('f-id').value;
  const body={kode_tanaman:document.getElementById('f-kode').value.trim(),
    nama_tanaman:document.getElementById('f-nama').value.trim(),
    varietas:document.getElementById('f-varietas').value.trim(),
    tanggal_tanam:document.getElementById('f-tanggal').value,
    lokasi:document.getElementById('f-lokasi').value.trim(),
    posisi:document.getElementById('f-posisi').value.trim(),
    status:document.getElementById('f-st').value,
    catatan:document.getElementById('f-catatan').value.trim()};
  try{
    if(id)await api('/api/tanaman/'+id,{method:'PUT',body});
    else await api('/api/tanaman',{method:'POST',body});
    closeModal('modal-form');toast('Tersimpan.');muat();
  }catch(e){toast(e.message,'error');}
  return false;
}
async function hapus(id,kode){
  if(!confirm('Hapus tanaman '+kode+'? Semua data terkait akan terhapus.'))return;
  try{await api('/api/tanaman/'+id,{method:'DELETE'});toast('Terhapus.');muat();}
  catch(e){toast(e.message,'error');}
}
document.getElementById('q').addEventListener('input',debounce(muat,300));
document.getElementById('f-status').addEventListener('change',muat);
muat();
</script>
{% endblock %}"""


TEMPLATES["tanaman_detail.html"] = r"""{% extends "base.html" %}
{% block title %}Detail Tanaman{% endblock %}
{% block page_title %}Detail Tanaman{% endblock %}
{% block content %}
<div class="card" id="identitas"><div class="empty">Memuat…</div></div>
<div class="card"><h2>Grafik Perkembangan</h2>
  <div class="chart-box"><canvas id="chart-tinggi"></canvas></div>
  <div class="grid grid-2" style="margin-top:16px">
    <div class="chart-box"><canvas id="chart-daun"></canvas></div>
    <div class="chart-box"><canvas id="chart-bunga"></canvas></div>
  </div>
</div>
<div class="card"><h2>Timeline Perkembangan</h2>
  <div id="timeline" class="timeline"><div class="empty">Memuat…</div></div>
</div>
{% endblock %}
{% block scripts %}
<script>
const TID={{ tanaman_id }}; const charts={};
function buatChart(id,labels,ds,yl){
  const el=document.getElementById(id);if(!el)return;
  if(charts[id])charts[id].destroy();
  charts[id]=new Chart(el.getContext('2d'),{type:'line',data:{labels,datasets:ds},
    options:{responsive:true,maintainAspectRatio:false,
      plugins:{legend:{position:'bottom',labels:{boxWidth:12,font:{size:11}}}},
      scales:{y:{beginAtZero:true,title:{display:true,text:yl,font:{size:11}},grid:{color:'#eef1f4'}},
        x:{grid:{display:false}}}}});
}
(async function(){
  try{
    const t=(await api('/api/tanaman/'+TID)).data;
    document.getElementById('identitas').innerHTML=`
      <h2>${esc(t.kode_tanaman)} — ${esc(t.nama_tanaman)}</h2>
      <div class="grid grid-4" style="margin-top:12px">
        <div><div style="font-size:12px;color:var(--teks-lembut)">Varietas</div>
          <div style="font-weight:600">${esc(t.varietas||'-')}</div></div>
        <div><div style="font-size:12px;color:var(--teks-lembut)">Tgl Tanam</div>
          <div style="font-weight:600">${esc(fmtTanggal(t.tanggal_tanam))}</div></div>
        <div><div style="font-size:12px;color:var(--teks-lembut)">Lokasi/Posisi</div>
          <div style="font-weight:600">${esc(t.lokasi||'-')} / ${esc(t.posisi||'-')}</div></div>
        <div><div style="font-size:12px;color:var(--teks-lembut)">Status</div>
          <div>${statusBadge(t.status)}</div></div>
      </div>
      ${t.catatan?`<p style="margin-top:12px;font-size:13px;color:var(--teks-lembut)">${esc(t.catatan)}</p>`:''}`;
    const g=await api('/api/tanaman/'+TID+'/grafik');
    const mk=(l,d,w)=>({label:l,data:d,borderColor:w,backgroundColor:w+'22',
      tension:.3,pointRadius:3,borderWidth:2,spanGaps:true});
    if(!g.labels.length){
      document.querySelectorAll('.chart-box').forEach(b=>b.innerHTML='<div class="empty">Belum ada data pengukuran.</div>');
    }else{
      buatChart('chart-tinggi',g.labels,[mk('Tinggi (cm)',g.tinggi,'#2e7d32')],'cm');
      buatChart('chart-daun',g.labels,[mk('Jumlah Daun',g.daun,'#1565c0')],'helai');
      buatChart('chart-bunga',g.labels,[mk('Bunga',g.bunga,'#ef6c00'),mk('Buah',g.buah,'#c62828')],'jumlah');
    }
    const tl=await api('/api/tanaman/'+TID+'/timeline');
    const el=document.getElementById('timeline');
    if(!tl.data.length)el.innerHTML='<div class="empty">Belum ada riwayat.</div>';
    else el.innerHTML=tl.data.map(i=>`
      <div class="tl-item ${esc(i.tipe)}">
        <div class="tl-date">${esc(fmtTanggal(i.tanggal))} • ${esc(i.tipe)}</div>
        <div class="tl-title">${esc(i.judul)}</div>
        <div class="tl-desc">${esc(i.detail||'')}</div>
      </div>`).join('');
  }catch(e){toast(e.message,'error');}
})();
</script>
{% endblock %}"""


TEMPLATES["pengukuran.html"] = r"""{% extends "base.html" %}
{% block title %}Pengukuran{% endblock %}
{% block page_title %}Data Pengukuran{% endblock %}
{% block content %}
<div class="card">
  <div class="toolbar">
    <select id="filter-tanaman"><option value="">Semua Tanaman</option></select>
    <input type="date" id="f-mulai"><input type="date" id="f-selesai">
    <button class="btn btn-outline btn-sm" onclick="muat()">Filter</button>
    <div class="spacer"></div>
    {% if current_user.can_edit %}<button class="btn" onclick="bukaTambah()">+ Tambah</button>{% endif %}
  </div>
  <div class="table-wrap"><table class="data" id="tbl">
    <thead><tr><th>Tanggal</th><th>Tanaman</th><th>Tinggi</th><th>Daun</th><th>Cabang</th>
      <th>Ø Batang</th><th>Bunga</th><th>Buah</th><th>Catatan</th><th>Aksi</th></tr></thead>
    <tbody><tr><td colspan="10" class="empty">Memuat…</td></tr></tbody>
  </table></div>
</div>

<div class="modal-backdrop" id="modal-form"><div class="modal">
  <h3 id="modal-title">Tambah Pengukuran</h3>
  <form onsubmit="return simpan(event)">
    <input type="hidden" id="f-id">
    <div class="form-grid">
      <div class="field"><label>Tanaman *</label><select id="f-tanaman" required></select></div>
      <div class="field"><label>Tanggal *</label><input type="date" id="f-tanggal" required></div>
      <div class="field"><label>Tinggi (cm)</label><input type="number" step="0.1" min="0" id="f-tinggi"></div>
      <div class="field"><label>Jumlah Daun</label><input type="number" min="0" id="f-daun"></div>
      <div class="field"><label>Jumlah Cabang</label><input type="number" min="0" id="f-cabang"></div>
      <div class="field"><label>Diameter Batang (mm)</label><input type="number" step="0.1" min="0" id="f-diameter"></div>
      <div class="field"><label>Jumlah Bunga</label><input type="number" min="0" id="f-bunga"></div>
      <div class="field"><label>Jumlah Buah</label><input type="number" min="0" id="f-buah"></div>
      <div class="field"><label>Kondisi Daun</label><input id="f-kdaun"></div>
      <div class="field"><label>Kondisi Batang</label><input id="f-kbatang"></div>
      <div class="field"><label>Kondisi Tanah</label><input id="f-ktanah"></div>
      <div class="field full"><label>Catatan</label><textarea id="f-catatan"></textarea></div>
    </div>
    <div class="modal-actions">
      <button type="button" class="btn btn-outline" onclick="closeModal('modal-form')">Batal</button>
      <button type="submit" class="btn">Simpan</button>
    </div>
  </form>
</div></div>
{% endblock %}
{% block scripts %}
<script>
const CAN_EDIT={{ 'true' if current_user.can_edit else 'false' }};
let daftarTanaman=[];
async function muatTanaman(){
  const res=await api('/api/tanaman'); daftarTanaman=res.data;
  const opt=daftarTanaman.map(t=>`<option value="${t.id}">${esc(t.kode_tanaman)} - ${esc(t.nama_tanaman)}</option>`).join('');
  document.getElementById('filter-tanaman').innerHTML='<option value="">Semua Tanaman</option>'+opt;
  document.getElementById('f-tanaman').innerHTML='<option value="">— Pilih —</option>'+opt;
}
function namaTanaman(id){const t=daftarTanaman.find(x=>x.id===id);return t?t.kode_tanaman:'#'+id;}
async function muat(){
  const tid=document.getElementById('filter-tanaman').value;
  const m=document.getElementById('f-mulai').value;
  const s=document.getElementById('f-selesai').value;
  const p=new URLSearchParams();
  if(tid)p.set('tanaman_id',tid); if(m)p.set('mulai',m); if(s)p.set('selesai',s);
  const tb=document.querySelector('#tbl tbody');
  try{
    const res=await api('/api/pengukuran?'+p.toString());
    if(!res.data.length){tb.innerHTML='<tr><td colspan="10" class="empty">Belum ada data.</td></tr>';return;}
    tb.innerHTML=res.data.map(r=>`
      <tr><td>${esc(r.tanggal)}</td><td><strong>${esc(namaTanaman(r.tanaman_id))}</strong></td>
        <td>${r.tinggi_cm??'-'}</td><td>${r.jumlah_daun??'-'}</td><td>${r.jumlah_cabang??'-'}</td>
        <td>${r.diameter_batang_mm??'-'}</td><td>${r.jumlah_bunga??'-'}</td><td>${r.jumlah_buah??'-'}</td>
        <td class="wrap">${esc(r.catatan||'-')}</td>
        <td>${CAN_EDIT?`<button class="btn btn-outline btn-sm" onclick='edit(${JSON.stringify(r)})'>Edit</button>
              <button class="btn btn-danger btn-sm" onclick="hapus(${r.id})">Hapus</button>`:'-'}</td>
      </tr>`).join('');
  }catch(e){toast(e.message,'error');}
}
function bukaTambah(){
  document.getElementById('modal-title').textContent='Tambah Pengukuran';
  document.querySelector('#modal-form form').reset();
  document.getElementById('f-id').value='';
  document.getElementById('f-tanggal').value=todayISO();
  openModal('modal-form');
}
function edit(r){
  document.getElementById('modal-title').textContent='Edit Pengukuran';
  document.getElementById('f-id').value=r.id;
  document.getElementById('f-tanaman').value=r.tanaman_id;
  document.getElementById('f-tanggal').value=r.tanggal;
  document.getElementById('f-tinggi').value=r.tinggi_cm??'';
  document.getElementById('f-daun').value=r.jumlah_daun??'';
  document.getElementById('f-cabang').value=r.jumlah_cabang??'';
  document.getElementById('f-diameter').value=r.diameter_batang_mm??'';
  document.getElementById('f-bunga').value=r.jumlah_bunga??'';
  document.getElementById('f-buah').value=r.jumlah_buah??'';
  document.getElementById('f-kdaun').value=r.kondisi_daun||'';
  document.getElementById('f-kbatang').value=r.kondisi_batang||'';
  document.getElementById('f-ktanah').value=r.kondisi_tanah||'';
  document.getElementById('f-catatan').value=r.catatan||'';
  openModal('modal-form');
}
async function simpan(ev){
  ev.preventDefault();
  const id=document.getElementById('f-id').value;
  const body={tanaman_id:document.getElementById('f-tanaman').value,
    tanggal:document.getElementById('f-tanggal').value,
    tinggi_cm:document.getElementById('f-tinggi').value||null,
    jumlah_daun:document.getElementById('f-daun').value||null,
    jumlah_cabang:document.getElementById('f-cabang').value||null,
    diameter_batang_mm:document.getElementById('f-diameter').value||null,
    jumlah_bunga:document.getElementById('f-bunga').value||null,
    jumlah_buah:document.getElementById('f-buah').value||null,
    kondisi_daun:document.getElementById('f-kdaun').value.trim(),
    kondisi_batang:document.getElementById('f-kbatang').value.trim(),
    kondisi_tanah:document.getElementById('f-ktanah').value.trim(),
    catatan:document.getElementById('f-catatan').value.trim()};
  try{
    if(id)await api('/api/pengukuran/'+id,{method:'PUT',body});
    else await api('/api/pengukuran',{method:'POST',body});
    closeModal('modal-form');toast('Tersimpan.');muat();
  }catch(e){toast(e.message,'error');}
  return false;
}
async function hapus(id){
  if(!confirm('Hapus data ini?'))return;
  try{await api('/api/pengukuran/'+id,{method:'DELETE'});toast('Terhapus.');muat();}
  catch(e){toast(e.message,'error');}
}
document.getElementById('filter-tanaman').addEventListener('change',muat);
(async()=>{await muatTanaman();muat();})();
</script>
{% endblock %}"""


TEMPLATES["perawatan.html"] = r"""{% extends "base.html" %}
{% block title %}Perawatan{% endblock %}
{% block page_title %}Perawatan Tanaman{% endblock %}
{% block content %}
<div class="card">
  <div class="toolbar">
    <select id="filter-tanaman"><option value="">Semua Tanaman</option></select>
    <select id="filter-jenis"><option value="">Semua Jenis</option>
      <option value="penyiraman">Penyiraman</option><option value="pemupukan">Pemupukan</option>
      <option value="penyiangan">Penyiangan</option><option value="pengendalian_hama">Pengendalian Hama</option>
      <option value="pemeriksaan">Pemeriksaan</option><option value="lainnya">Lainnya</option>
    </select>
    <div class="spacer"></div>
    {% if current_user.can_edit %}<button class="btn" onclick="bukaTambah()">+ Catat</button>{% endif %}
  </div>
  <div class="table-wrap"><table class="data" id="tbl">
    <thead><tr><th>Tanggal</th><th>Tanaman</th><th>Jenis</th><th>Petugas</th>
      <th>Keterangan</th><th>Hasil</th><th>Aksi</th></tr></thead>
    <tbody><tr><td colspan="7" class="empty">Memuat…</td></tr></tbody>
  </table></div>
</div>

<div class="modal-backdrop" id="modal-form"><div class="modal">
  <h3 id="modal-title">Catat Perawatan</h3>
  <form onsubmit="return simpan(event)">
    <input type="hidden" id="f-id">
    <div class="form-grid">
      <div class="field"><label>Tanaman *</label><select id="f-tanaman" required></select></div>
      <div class="field"><label>Tanggal *</label><input type="date" id="f-tanggal" required></div>
      <div class="field"><label>Jenis Kegiatan *</label><select id="f-jenis" required>
        <option value="penyiraman">Penyiraman</option><option value="pemupukan">Pemupukan</option>
        <option value="penyiangan">Penyiangan</option><option value="pengendalian_hama">Pengendalian Hama</option>
        <option value="pemeriksaan">Pemeriksaan</option><option value="lainnya">Lainnya</option>
      </select></div>
      <div class="field"><label>Petugas</label><input id="f-petugas" maxlength="120"></div>
      <div class="field full"><label>Keterangan</label><textarea id="f-keterangan"></textarea></div>
      <div class="field full"><label>Hasil</label><textarea id="f-hasil"></textarea></div>
    </div>
    <div class="modal-actions">
      <button type="button" class="btn btn-outline" onclick="closeModal('modal-form')">Batal</button>
      <button type="submit" class="btn">Simpan</button>
    </div>
  </form>
</div></div>
{% endblock %}
{% block scripts %}
<script>
const CAN_EDIT={{ 'true' if current_user.can_edit else 'false' }};
const LB={penyiraman:'Penyiraman',pemupukan:'Pemupukan',penyiangan:'Penyiangan',
  pengendalian_hama:'Pengendalian Hama',pemeriksaan:'Pemeriksaan',lainnya:'Lainnya'};
let daftarTanaman=[];
async function muatTanaman(){
  const res=await api('/api/tanaman');daftarTanaman=res.data;
  const opt=daftarTanaman.map(t=>`<option value="${t.id}">${esc(t.kode_tanaman)} - ${esc(t.nama_tanaman)}</option>`).join('');
  document.getElementById('filter-tanaman').innerHTML='<option value="">Semua Tanaman</option>'+opt;
  document.getElementById('f-tanaman').innerHTML='<option value="">— Pilih —</option>'+opt;
}
function namaTanaman(id){const t=daftarTanaman.find(x=>x.id===id);return t?t.kode_tanaman:'#'+id;}
async function muat(){
  const tid=document.getElementById('filter-tanaman').value;
  const j=document.getElementById('filter-jenis').value;
  const p=new URLSearchParams();if(tid)p.set('tanaman_id',tid);if(j)p.set('jenis',j);
  const tb=document.querySelector('#tbl tbody');
  try{
    const res=await api('/api/perawatan?'+p.toString());
    if(!res.data.length){tb.innerHTML='<tr><td colspan="7" class="empty">Belum ada catatan.</td></tr>';return;}
    tb.innerHTML=res.data.map(r=>`
      <tr><td>${esc(r.tanggal)}</td><td><strong>${esc(namaTanaman(r.tanaman_id))}</strong></td>
        <td>${esc(LB[r.jenis_kegiatan]||r.jenis_kegiatan)}</td><td>${esc(r.petugas||'-')}</td>
        <td class="wrap">${esc(r.keterangan||'-')}</td><td class="wrap">${esc(r.hasil||'-')}</td>
        <td>${CAN_EDIT?`<button class="btn btn-outline btn-sm" onclick='edit(${JSON.stringify(r)})'>Edit</button>
              <button class="btn btn-danger btn-sm" onclick="hapus(${r.id})">Hapus</button>`:'-'}</td>
      </tr>`).join('');
  }catch(e){toast(e.message,'error');}
}
function bukaTambah(){
  document.getElementById('modal-title').textContent='Catat Perawatan';
  document.querySelector('#modal-form form').reset();
  document.getElementById('f-id').value='';
  document.getElementById('f-tanggal').value=todayISO();
  openModal('modal-form');
}
function edit(r){
  document.getElementById('modal-title').textContent='Edit Perawatan';
  document.getElementById('f-id').value=r.id;
  document.getElementById('f-tanaman').value=r.tanaman_id;
  document.getElementById('f-tanggal').value=r.tanggal;
  document.getElementById('f-jenis').value=r.jenis_kegiatan;
  document.getElementById('f-petugas').value=r.petugas||'';
  document.getElementById('f-keterangan').value=r.keterangan||'';
  document.getElementById('f-hasil').value=r.hasil||'';
  openModal('modal-form');
}
async function simpan(ev){
  ev.preventDefault();
  const id=document.getElementById('f-id').value;
  const body={tanaman_id:document.getElementById('f-tanaman').value,
    tanggal:document.getElementById('f-tanggal').value,
    jenis_kegiatan:document.getElementById('f-jenis').value,
    petugas:document.getElementById('f-petugas').value.trim(),
    keterangan:document.getElementById('f-keterangan').value.trim(),
    hasil:document.getElementById('f-hasil').value.trim()};
  try{
    if(id)await api('/api/perawatan/'+id,{method:'PUT',body});
    else await api('/api/perawatan',{method:'POST',body});
    closeModal('modal-form');toast('Tersimpan.');muat();
  }catch(e){toast(e.message,'error');}
  return false;
}
async function hapus(id){
  if(!confirm('Hapus catatan ini?'))return;
  try{await api('/api/perawatan/'+id,{method:'DELETE'});toast('Terhapus.');muat();}
  catch(e){toast(e.message,'error');}
}
document.getElementById('filter-tanaman').addEventListener('change',muat);
document.getElementById('filter-jenis').addEventListener('change',muat);
(async()=>{await muatTanaman();muat();})();
</script>
{% endblock %}"""


TEMPLATES["dokumentasi.html"] = r"""{% extends "base.html" %}
{% block title %}Dokumentasi{% endblock %}
{% block page_title %}Dokumentasi Foto{% endblock %}
{% block content %}
<div class="card">
  <div class="toolbar">
    <select id="filter-tanaman"><option value="">Semua Tanaman</option></select>
    <input type="date" id="f-tanggal">
    <div class="spacer"></div>
    {% if current_user.can_edit %}<button class="btn" onclick="bukaTambah()">+ Unggah Foto</button>{% endif %}
  </div>
  <div class="gallery" id="galeri"><div class="empty">Memuat…</div></div>
</div>

<div class="modal-backdrop" id="modal-form"><div class="modal" style="max-width:520px">
  <h3>Unggah Dokumentasi</h3>
  <form onsubmit="return simpan(event)">
    <div class="form-grid">
      <div class="field"><label>Tanaman *</label><select id="f-tanaman" required></select></div>
      <div class="field"><label>Tanggal *</label><input type="date" id="f-tanggal" required></div>
      <div class="field full"><label>Foto *</label>
        <input type="file" id="f-file" accept="image/png,image/jpeg,image/gif,image/webp" required>
        <span class="hint">JPG/PNG/GIF/WEBP. Maks 5 MB.</span></div>
      <div class="field full"><label>Keterangan</label><textarea id="f-keterangan"></textarea></div>
    </div>
    <div class="modal-actions">
      <button type="button" class="btn btn-outline" onclick="closeModal('modal-form')">Batal</button>
      <button type="submit" class="btn">Unggah</button>
    </div>
  </form>
</div></div>
{% endblock %}
{% block scripts %}
<script>
const CAN_EDIT={{ 'true' if current_user.can_edit else 'false' }};
let daftarTanaman=[];
async function muatTanaman(){
  const res=await api('/api/tanaman');daftarTanaman=res.data;
  const opt=daftarTanaman.map(t=>`<option value="${t.id}">${esc(t.kode_tanaman)} - ${esc(t.nama_tanaman)}</option>`).join('');
  document.getElementById('filter-tanaman').innerHTML='<option value="">Semua Tanaman</option>'+opt;
  document.getElementById('f-tanaman').innerHTML='<option value="">— Pilih —</option>'+opt;
}
function namaTanaman(id){const t=daftarTanaman.find(x=>x.id===id);return t?t.kode_tanaman:'#'+id;}
async function muat(){
  const tid=document.getElementById('filter-tanaman').value;
  const tgl=document.getElementById('f-tanggal').value;
  const p=new URLSearchParams();if(tid)p.set('tanaman_id',tid);
  const gal=document.getElementById('galeri');
  try{
    let res=await api('/api/dokumentasi?'+p.toString());
    let rows=res.data;
    if(tgl)rows=rows.filter(r=>r.tanggal===tgl);
    if(!rows.length){gal.innerHTML='<div class="empty">Belum ada foto.</div>';return;}
    gal.innerHTML=rows.map(r=>`
      <div class="item">
        <a href="/static/uploads/${esc(r.file_foto)}" target="_blank">
          <img src="/static/uploads/${esc(r.file_foto)}" loading="lazy"></a>
        <div class="cap">
          <div class="tgl">${esc(fmtTanggal(r.tanggal))} • ${esc(namaTanaman(r.tanaman_id))}</div>
          <div>${esc(r.keterangan||'-')}</div>
          ${CAN_EDIT?`<button class="btn btn-danger btn-sm" style="margin-top:6px" onclick="hapus(${r.id})">Hapus</button>`:''}
        </div>
      </div>`).join('');
  }catch(e){toast(e.message,'error');}
}
function bukaTambah(){
  document.querySelector('#modal-form form').reset();
  document.getElementById('f-tanggal').value=todayISO();
  openModal('modal-form');
}
async function simpan(ev){
  ev.preventDefault();
  const f=document.getElementById('f-file');
  if(!f.files.length){toast('Pilih file dulu.','error');return false;}
  const fd=new FormData();
  fd.append('tanaman_id',document.getElementById('f-tanaman').value);
  fd.append('tanggal',document.getElementById('f-tanggal').value);
  fd.append('keterangan',document.getElementById('f-keterangan').value.trim());
  fd.append('file_foto',f.files[0]);
  try{await api('/api/dokumentasi',{method:'POST',body:fd});
    closeModal('modal-form');toast('Terunggah.');muat();
  }catch(e){toast(e.message,'error');}
  return false;
}
async function hapus(id){
  if(!confirm('Hapus foto ini?'))return;
  try{await api('/api/dokumentasi/'+id,{method:'DELETE'});toast('Terhapus.');muat();}
  catch(e){toast(e.message,'error');}
}
document.getElementById('filter-tanaman').addEventListener('change',muat);
document.getElementById('f-tanggal').addEventListener('change',muat);
(async()=>{await muatTanaman();muat();})();
</script>
{% endblock %}"""


TEMPLATES["jadwal.html"] = r"""{% extends "base.html" %}
{% block title %}Jadwal{% endblock %}
{% block page_title %}Jadwal Kegiatan{% endblock %}
{% block content %}
<div class="card">
  <div class="toolbar">
    <input type="date" id="f-mulai"><input type="date" id="f-selesai">
    <button class="btn btn-outline btn-sm" onclick="muat()">Filter</button>
    <div class="spacer"></div>
    {% if current_user.role=='admin' %}<button class="btn" onclick="bukaTambah()">+ Tambah Jadwal</button>{% endif %}
  </div>
  <div class="table-wrap"><table class="data" id="tbl">
    <thead><tr><th>Tanggal</th><th>Kegiatan</th><th>Petugas</th><th>Status</th><th>Catatan</th><th>Aksi</th></tr></thead>
    <tbody><tr><td colspan="6" class="empty">Memuat…</td></tr></tbody>
  </table></div>
</div>

<div class="modal-backdrop" id="modal-form"><div class="modal">
  <h3 id="modal-title">Tambah Jadwal</h3>
  <form onsubmit="return simpan(event)">
    <input type="hidden" id="f-id">
    <div class="form-grid">
      <div class="field"><label>Tanggal *</label><input type="date" id="f-tanggal" required></div>
      <div class="field"><label>Kegiatan *</label><input id="f-kegiatan" required maxlength="200"></div>
      <div class="field"><label>Petugas</label><input id="f-petugas" maxlength="120"></div>
      <div class="field"><label>Status</label><select id="f-st">
        <option value="belum">Belum</option><option value="selesai">Selesai</option>
        <option value="batal">Batal</option></select></div>
      <div class="field full"><label>Catatan</label><textarea id="f-catatan"></textarea></div>
    </div>
    <div class="modal-actions">
      <button type="button" class="btn btn-outline" onclick="closeModal('modal-form')">Batal</button>
      <button type="submit" class="btn">Simpan</button>
    </div>
  </form>
</div></div>
{% endblock %}
{% block scripts %}
<script>
const IS_ADMIN={{ 'true' if current_user.role=='admin' else 'false' }};
async function muat(){
  const p=new URLSearchParams();
  const m=document.getElementById('f-mulai').value,s=document.getElementById('f-selesai').value;
  if(m)p.set('mulai',m);if(s)p.set('selesai',s);
  const tb=document.querySelector('#tbl tbody');
  try{
    const res=await api('/api/jadwal?'+p.toString());
    if(!res.data.length){tb.innerHTML='<tr><td colspan="6" class="empty">Belum ada jadwal.</td></tr>';return;}
    const w={belum:'#ef6c00',selesai:'#2e7d32',batal:'#c62828'};
    tb.innerHTML=res.data.map(j=>`
      <tr><td>${esc(fmtTanggal(j.tanggal))}</td><td><strong>${esc(j.kegiatan)}</strong></td>
        <td>${esc(j.petugas||'-')}</td>
        <td><span class="badge" style="background:${w[j.status]}22;color:${w[j.status]}">${esc(j.status)}</span></td>
        <td class="wrap">${esc(j.catatan||'-')}</td>
        <td>${IS_ADMIN?`<button class="btn btn-outline btn-sm" onclick='edit(${JSON.stringify(j)})'>Edit</button>
              <button class="btn btn-danger btn-sm" onclick="hapus(${j.id})">Hapus</button>`:'-'}</td>
      </tr>`).join('');
  }catch(e){toast(e.message,'error');}
}
function bukaTambah(){
  document.getElementById('modal-title').textContent='Tambah Jadwal';
  document.querySelector('#modal-form form').reset();
  document.getElementById('f-id').value='';
  document.getElementById('f-tanggal').value=todayISO();
  openModal('modal-form');
}
function edit(j){
  document.getElementById('modal-title').textContent='Edit Jadwal';
  document.getElementById('f-id').value=j.id;
  document.getElementById('f-tanggal').value=j.tanggal;
  document.getElementById('f-kegiatan').value=j.kegiatan;
  document.getElementById('f-petugas').value=j.petugas||'';
  document.getElementById('f-st').value=j.status;
  document.getElementById('f-catatan').value=j.catatan||'';
  openModal('modal-form');
}
async function simpan(ev){
  ev.preventDefault();
  const id=document.getElementById('f-id').value;
  const body={tanggal:document.getElementById('f-tanggal').value,
    kegiatan:document.getElementById('f-kegiatan').value.trim(),
    petugas:document.getElementById('f-petugas').value.trim(),
    status:document.getElementById('f-st').value,
    catatan:document.getElementById('f-catatan').value.trim()};
  try{
    if(id)await api('/api/jadwal/'+id,{method:'PUT',body});
    else await api('/api/jadwal',{method:'POST',body});
    closeModal('modal-form');toast('Tersimpan.');muat();
  }catch(e){toast(e.message,'error');}
  return false;
}
async function hapus(id){
  if(!confirm('Hapus jadwal ini?'))return;
  try{await api('/api/jadwal/'+id,{method:'DELETE'});toast('Terhapus.');muat();}
  catch(e){toast(e.message,'error');}
}
muat();
</script>
{% endblock %}"""


TEMPLATES["laporan.html"] = r"""{% extends "base.html" %}
{% block title %}Laporan{% endblock %}
{% block page_title %}Generator Laporan PDF{% endblock %}
{% block content %}
<div class="card">
  <h2>Buat Laporan Baru</h2>
  <form onsubmit="return generate(event)">
    <div class="form-grid">
      <div class="field"><label>Judul Laporan *</label>
        <input id="f-judul" value="Laporan Monitoring Pertumbuhan Tanaman Tomat" required></div>
      <div class="field"><label>Nama Kelompok</label><input id="f-kelompok"></div>
      <div class="field"><label>Kelas</label><input id="f-kelas"></div>
      <div class="field"><label>Sekolah</label><input id="f-sekolah"></div>
      <div class="field"><label>Pembina</label><input id="f-pembina"></div>
      <div class="field"><label>Periode Mulai *</label><input type="date" id="f-mulai" required></div>
      <div class="field"><label>Periode Selesai *</label><input type="date" id="f-selesai" required></div>
    </div>
    <div style="margin-top:18px">
      <label style="font-weight:600;font-size:13px">Pilih Tanaman (kosong = semua)</label>
      <div id="daftar-tanaman" style="margin-top:8px;display:flex;flex-wrap:wrap;gap:10px"></div>
    </div>
    <div style="margin-top:18px">
      <label style="font-weight:600;font-size:13px">Jenis Data</label>
      <div style="margin-top:8px;display:flex;flex-wrap:wrap;gap:16px;font-size:13.5px">
        <label><input type="checkbox" id="j-pengukuran" checked> Pengukuran</label>
        <label><input type="checkbox" id="j-perawatan" checked> Perawatan</label>
        <label><input type="checkbox" id="j-dokumentasi" checked> Dokumentasi</label>
        <label><input type="checkbox" id="j-grafik" checked> Grafik</label>
        <label><input type="checkbox" id="j-lampiran" checked> Lampiran</label>
      </div>
    </div>
    <div style="margin-top:22px">
      <button type="submit" class="btn" id="btn-gen">Buat &amp; Unduh Laporan PDF</button>
    </div>
  </form>
</div>

<div class="card">
  <h2>Riwayat Laporan</h2>
  <div class="table-wrap"><table class="data">
    <thead><tr><th>Judul</th><th>Periode</th><th>Oleh</th><th>Waktu</th></tr></thead>
    <tbody id="tbl-riwayat"><tr><td colspan="4" class="empty">Memuat…</td></tr></tbody>
  </table></div>
</div>
{% endblock %}
{% block scripts %}
<script>
async function muatTanaman(){
  const res=await api('/api/tanaman');
  const b=document.getElementById('daftar-tanaman');
  if(!res.data.length){b.innerHTML='<span class="hint">Belum ada tanaman.</span>';return;}
  b.innerHTML=res.data.map(t=>`<label style="font-size:13px">
    <input type="checkbox" class="cb-t" value="${t.id}"> ${esc(t.kode_tanaman)} - ${esc(t.nama_tanaman)}
  </label>`).join('');
}
async function muatRiwayat(){
  try{
    const res=await api('/api/laporan/riwayat');
    const tb=document.getElementById('tbl-riwayat');
    if(!res.data.length){tb.innerHTML='<tr><td colspan="4" class="empty">Belum ada.</td></tr>';return;}
    tb.innerHTML=res.data.map(r=>`
      <tr><td>${esc(r.judul)}</td>
        <td>${esc(r.periode_mulai||'-')} s.d. ${esc(r.periode_selesai||'-')}</td>
        <td>${esc(r.dibuat_oleh||'-')}</td>
        <td>${esc((r.tanggal_dibuat||'').replace('T',' ').slice(0,16))}</td></tr>`).join('');
  }catch(e){toast(e.message,'error');}
}
async function generate(ev){
  ev.preventDefault();
  const btn=document.getElementById('btn-gen');btn.disabled=true;btn.textContent='Membuat…';
  const ids=Array.from(document.querySelectorAll('.cb-t:checked')).map(c=>parseInt(c.value));
  const body={judul:document.getElementById('f-judul').value.trim(),
    kelompok:document.getElementById('f-kelompok').value.trim(),
    kelas:document.getElementById('f-kelas').value.trim(),
    sekolah:document.getElementById('f-sekolah').value.trim(),
    pembina:document.getElementById('f-pembina').value.trim(),
    periode_mulai:document.getElementById('f-mulai').value,
    periode_selesai:document.getElementById('f-selesai').value,
    tanaman_ids:ids,
    jenis:{pengukuran:document.getElementById('j-pengukuran').checked,
      perawatan:document.getElementById('j-perawatan').checked,
      dokumentasi:document.getElementById('j-dokumentasi').checked,
      grafik:document.getElementById('j-grafik').checked,
      lampiran:document.getElementById('j-lampiran').checked}};
  try{
    const res=await fetch('/api/laporan/generate',{method:'POST',
      headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
    if(!res.ok){let m='Gagal membuat laporan.';
      try{const j=await res.json();m=j.error||m;}catch(_){}
      throw new Error(m);}
    const blob=await res.blob();
    const url=URL.createObjectURL(blob);
    const a=document.createElement('a');a.href=url;
    a.download='Laporan_TOMATGROW_'+body.periode_mulai+'_'+body.periode_selesai+'.pdf';
    document.body.appendChild(a);a.click();a.remove();URL.revokeObjectURL(url);
    toast('Laporan dibuat & diunduh.');muatRiwayat();
  }catch(e){toast(e.message,'error');}
  finally{btn.disabled=false;btn.textContent='Buat & Unduh Laporan PDF';}
  return false;
}
(async()=>{
  document.getElementById('f-mulai').value=todayISO().slice(0,8)+'01';
  document.getElementById('f-selesai').value=todayISO();
  await muatTanaman();muatRiwayat();
})();
</script>
{% endblock %}"""


TEMPLATES["users.html"] = r"""{% extends "base.html" %}
{% block title %}Pengguna{% endblock %}
{% block page_title %}Manajemen Pengguna{% endblock %}
{% block content %}
<div class="card">
  <div class="toolbar"><div class="spacer"></div>
    <button class="btn" onclick="bukaTambah()">+ Tambah Pengguna</button></div>
  <div class="table-wrap"><table class="data" id="tbl">
    <thead><tr><th>Nama</th><th>Username</th><th>Role</th><th>Dibuat</th><th>Aksi</th></tr></thead>
    <tbody><tr><td colspan="5" class="empty">Memuat…</td></tr></tbody>
  </table></div>
</div>

<div class="modal-backdrop" id="modal-form"><div class="modal" style="max-width:520px">
  <h3 id="modal-title">Tambah Pengguna</h3>
  <form onsubmit="return simpan(event)">
    <input type="hidden" id="f-id">
    <div class="form-grid">
      <div class="field"><label>Nama Lengkap *</label><input id="f-nama" required maxlength="120"></div>
      <div class="field"><label>Username *</label><input id="f-username" required maxlength="80"></div>
      <div class="field"><label>Password <span id="hint-pw">*</span></label>
        <input type="password" id="f-password" minlength="6" autocomplete="new-password">
        <span class="hint">Minimal 6 karakter.</span></div>
      <div class="field"><label>Role *</label><select id="f-role">
        <option value="anggota">Anggota</option><option value="admin">Admin</option>
        <option value="pembina">Pembina</option></select></div>
    </div>
    <div class="modal-actions">
      <button type="button" class="btn btn-outline" onclick="closeModal('modal-form')">Batal</button>
      <button type="submit" class="btn">Simpan</button>
    </div>
  </form>
</div></div>
{% endblock %}
{% block scripts %}
<script>
async function muat(){
  const tb=document.querySelector('#tbl tbody');
  try{
    const res=await api('/api/users');
    tb.innerHTML=res.data.map(u=>`
      <tr><td><strong>${esc(u.nama)}</strong></td><td>${esc(u.username)}</td>
        <td><span class="badge-role">${esc(u.role)}</span></td>
        <td>${esc((u.created_at||'').slice(0,10))}</td>
        <td><button class="btn btn-outline btn-sm" onclick='edit(${JSON.stringify(u)})'>Edit</button>
          <button class="btn btn-danger btn-sm" onclick="hapus(${u.id})">Hapus</button></td>
      </tr>`).join('');
  }catch(e){toast(e.message,'error');}
}
function bukaTambah(){
  document.getElementById('modal-title').textContent='Tambah Pengguna';
  document.querySelector('#modal-form form').reset();
  document.getElementById('f-id').value='';
  document.getElementById('f-username').disabled=false;
  document.getElementById('f-password').required=true;
  document.getElementById('hint-pw').textContent='*';
  openModal('modal-form');
}
function edit(u){
  document.getElementById('modal-title').textContent='Edit Pengguna';
  document.getElementById('f-id').value=u.id;
  document.getElementById('f-nama').value=u.nama;
  document.getElementById('f-username').value=u.username;
  document.getElementById('f-username').disabled=true;
  document.getElementById('f-password').value='';
  document.getElementById('f-password').required=false;
  document.getElementById('hint-pw').textContent='(kosongkan jika tidak diubah)';
  document.getElementById('f-role').value=u.role;
  openModal('modal-form');
}
async function simpan(ev){
  ev.preventDefault();
  const id=document.getElementById('f-id').value;
  const body={nama:document.getElementById('f-nama').value.trim(),
    role:document.getElementById('f-role').value};
  const pw=document.getElementById('f-password').value;
  if(pw)body.password=pw;
  if(!id){
    body.username=document.getElementById('f-username').value.trim().toLowerCase();
    if(!pw){toast('Password wajib untuk pengguna baru.','error');return false;}
  }
  try{
    if(id)await api('/api/users/'+id,{method:'PUT',body});
    else await api('/api/users',{method:'POST',body});
    closeModal('modal-form');
    document.getElementById('f-username').disabled=false;
    toast('Tersimpan.');muat();
  }catch(e){toast(e.message,'error');}
  return false;
}
async function hapus(id){
  if(!confirm('Hapus pengguna ini?'))return;
  try{await api('/api/users/'+id,{method:'DELETE'});toast('Terhapus.');muat();}
  catch(e){toast(e.message,'error');}
}
muat();
</script>
{% endblock %}"""


TEMPLATES["audit.html"] = r"""{% extends "base.html" %}
{% block title %}Riwayat{% endblock %}
{% block page_title %}Riwayat Perubahan{% endblock %}
{% block content %}
<div class="card">
  <div class="toolbar">
    <select id="f-entitas"><option value="">Semua Entitas</option>
      <option value="tanaman">Tanaman</option><option value="pengukuran">Pengukuran</option>
      <option value="perawatan">Perawatan</option><option value="dokumentasi">Dokumentasi</option>
      <option value="jadwal">Jadwal</option><option value="users">Pengguna</option>
      <option value="laporan">Laporan</option></select>
    <div class="spacer"></div>
  </div>
  <div class="table-wrap"><table class="data">
    <thead><tr><th>Waktu</th><th>Pengguna</th><th>Aksi</th><th>Entitas</th><th>ID</th><th>Deskripsi</th></tr></thead>
    <tbody id="tbody"><tr><td colspan="6" class="empty">Memuat…</td></tr></tbody>
  </table></div>
</div>
{% endblock %}
{% block scripts %}
<script>
const W={create:'#2e7d32',update:'#1565c0',delete:'#c62828',login:'#5c6b7a',logout:'#5c6b7a'};
async function muat(){
  const e=document.getElementById('f-entitas').value;
  const tb=document.getElementById('tbody');
  try{
    const res=await api('/api/audit'+(e?'?entitas='+e:''));
    if(!res.data.length){tb.innerHTML='<tr><td colspan="6" class="empty">Belum ada.</td></tr>';return;}
    tb.innerHTML=res.data.map(r=>`
      <tr><td>${esc((r.waktu||'').replace('T',' ').slice(0,16))}</td>
        <td>${esc(r.username||'-')}</td>
        <td><span class="badge" style="background:${(W[r.aksi]||'#555')}22;color:${W[r.aksi]||'#555'}">${esc(r.aksi)}</span></td>
        <td>${esc(r.entitas)}</td><td>${r.entitas_id??'-'}</td>
        <td class="wrap">${esc(r.deskripsi||'-')}</td></tr>`).join('');
  }catch(e){toast(e.message,'error');}
}
document.getElementById('f-entitas').addEventListener('change',muat);
muat();
</script>
{% endblock %}"""
