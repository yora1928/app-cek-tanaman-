"""TOMAT GROW - Core: models, routes, API."""
from datetime import datetime, date, timedelta
from pathlib import Path

from flask import Flask, request, jsonify, render_template, redirect, url_for, flash, send_file, current_app
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_, func
from werkzeug.security import generate_password_hash, check_password_hash

from jinja2 import DictLoader
from tg_ui import TEMPLATES, CSS, JS
from tg_pdf import build_laporan

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "login"


# =====================================================================
# MODELS
# =====================================================================
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(120), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False, default="anggota")
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def set_password(self, raw): self.password_hash = generate_password_hash(raw)
    def check_password(self, raw): return check_password_hash(self.password_hash, raw)
    @property
    def can_edit(self): return self.role in ("admin", "anggota")

    def to_dict(self):
        return {"id": self.id, "nama": self.nama, "username": self.username,
                "role": self.role,
                "created_at": self.created_at.isoformat() if self.created_at else None}


class Tanaman(db.Model):
    __tablename__ = "tanaman"
    id = db.Column(db.Integer, primary_key=True)
    kode_tanaman = db.Column(db.String(50), unique=True, nullable=False, index=True)
    nama_tanaman = db.Column(db.String(120), nullable=False)
    varietas = db.Column(db.String(120))
    tanggal_tanam = db.Column(db.Date, nullable=False)
    lokasi = db.Column(db.String(150))
    posisi = db.Column(db.String(80))
    status = db.Column(db.String(20), default="hidup", nullable=False)
    catatan = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    pengukuran = db.relationship("Pengukuran", backref="tanaman", cascade="all, delete-orphan")
    perawatan  = db.relationship("Perawatan",  backref="tanaman", cascade="all, delete-orphan")
    dokumentasi= db.relationship("Dokumentasi",backref="tanaman", cascade="all, delete-orphan")

    def to_dict(self):
        return {"id": self.id, "kode_tanaman": self.kode_tanaman,
                "nama_tanaman": self.nama_tanaman, "varietas": self.varietas,
                "tanggal_tanam": self.tanggal_tanam.isoformat() if self.tanggal_tanam else None,
                "lokasi": self.lokasi, "posisi": self.posisi, "status": self.status,
                "catatan": self.catatan,
                "created_at": self.created_at.isoformat() if self.created_at else None}


class Pengukuran(db.Model):
    __tablename__ = "pengukuran"
    id = db.Column(db.Integer, primary_key=True)
    tanaman_id = db.Column(db.Integer, db.ForeignKey("tanaman.id", ondelete="CASCADE"), nullable=False, index=True)
    tanggal = db.Column(db.Date, nullable=False, index=True)
    tinggi_cm = db.Column(db.Float)
    jumlah_daun = db.Column(db.Integer)
    jumlah_cabang = db.Column(db.Integer)
    diameter_batang_mm = db.Column(db.Float)
    jumlah_bunga = db.Column(db.Integer)
    jumlah_buah = db.Column(db.Integer)
    kondisi_daun = db.Column(db.String(80))
    kondisi_batang = db.Column(db.String(80))
    kondisi_tanah = db.Column(db.String(80))
    catatan = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {"id": self.id, "tanaman_id": self.tanaman_id,
                "tanggal": self.tanggal.isoformat() if self.tanggal else None,
                "tinggi_cm": self.tinggi_cm, "jumlah_daun": self.jumlah_daun,
                "jumlah_cabang": self.jumlah_cabang, "diameter_batang_mm": self.diameter_batang_mm,
                "jumlah_bunga": self.jumlah_bunga, "jumlah_buah": self.jumlah_buah,
                "kondisi_daun": self.kondisi_daun, "kondisi_batang": self.kondisi_batang,
                "kondisi_tanah": self.kondisi_tanah, "catatan": self.catatan,
                "created_at": self.created_at.isoformat() if self.created_at else None}


class Perawatan(db.Model):
    __tablename__ = "perawatan"
    id = db.Column(db.Integer, primary_key=True)
    tanaman_id = db.Column(db.Integer, db.ForeignKey("tanaman.id", ondelete="CASCADE"), nullable=False, index=True)
    tanggal = db.Column(db.Date, nullable=False, index=True)
    jenis_kegiatan = db.Column(db.String(40), nullable=False)
    petugas = db.Column(db.String(120))
    keterangan = db.Column(db.Text)
    hasil = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {"id": self.id, "tanaman_id": self.tanaman_id,
                "tanggal": self.tanggal.isoformat() if self.tanggal else None,
                "jenis_kegiatan": self.jenis_kegiatan, "petugas": self.petugas,
                "keterangan": self.keterangan, "hasil": self.hasil,
                "created_at": self.created_at.isoformat() if self.created_at else None}


class Dokumentasi(db.Model):
    __tablename__ = "dokumentasi"
    id = db.Column(db.Integer, primary_key=True)
    tanaman_id = db.Column(db.Integer, db.ForeignKey("tanaman.id", ondelete="CASCADE"), nullable=False, index=True)
    tanggal = db.Column(db.Date, nullable=False, index=True)
    file_foto = db.Column(db.String(255), nullable=False)
    keterangan = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {"id": self.id, "tanaman_id": self.tanaman_id,
                "tanggal": self.tanggal.isoformat() if self.tanggal else None,
                "file_foto": self.file_foto, "keterangan": self.keterangan,
                "created_at": self.created_at.isoformat() if self.created_at else None}


class Jadwal(db.Model):
    __tablename__ = "jadwal"
    id = db.Column(db.Integer, primary_key=True)
    tanggal = db.Column(db.Date, nullable=False, index=True)
    kegiatan = db.Column(db.String(200), nullable=False)
    petugas = db.Column(db.String(120))
    status = db.Column(db.String(20), default="belum")
    catatan = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {"id": self.id, "tanggal": self.tanggal.isoformat() if self.tanggal else None,
                "kegiatan": self.kegiatan, "petugas": self.petugas,
                "status": self.status, "catatan": self.catatan}


class Laporan(db.Model):
    __tablename__ = "laporan"
    id = db.Column(db.Integer, primary_key=True)
    judul = db.Column(db.String(200), nullable=False)
    periode_mulai = db.Column(db.Date)
    periode_selesai = db.Column(db.Date)
    dibuat_oleh = db.Column(db.String(120))
    tanggal_dibuat = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {"id": self.id, "judul": self.judul,
                "periode_mulai": self.periode_mulai.isoformat() if self.periode_mulai else None,
                "periode_selesai": self.periode_selesai.isoformat() if self.periode_selesai else None,
                "dibuat_oleh": self.dibuat_oleh,
                "tanggal_dibuat": self.tanggal_dibuat.isoformat() if self.tanggal_dibuat else None}


class AuditLog(db.Model):
    __tablename__ = "audit_log"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="SET NULL"))
    username = db.Column(db.String(80))
    aksi = db.Column(db.String(40), nullable=False)
    entitas = db.Column(db.String(60), nullable=False)
    entitas_id = db.Column(db.Integer)
    deskripsi = db.Column(db.Text)
    waktu = db.Column(db.DateTime, default=datetime.utcnow, index=True)

    def to_dict(self):
        return {"id": self.id, "username": self.username, "aksi": self.aksi,
                "entitas": self.entitas, "entitas_id": self.entitas_id,
                "deskripsi": self.deskripsi,
                "waktu": self.waktu.isoformat() if self.waktu else None}


@login_manager.user_loader
def load_user(user_id): return db.session.get(User, int(user_id))


# =====================================================================
# HELPERS
# =====================================================================
def _parse_date(v):
    if not v: return None
    try: return datetime.strptime(v, "%Y-%m-%d").date()
    except (ValueError, TypeError): return None


def _to_int(v, field, allow_none=True):
    if v in (None, ""): return None if allow_none else 0
    try: n = int(v)
    except (TypeError, ValueError): raise ValueError(f"{field} harus angka bulat.")
    if n < 0: raise ValueError(f"{field} tidak boleh negatif.")
    return n


def _to_float(v, field):
    if v in (None, ""): return None
    try: n = float(v)
    except (TypeError, ValueError): raise ValueError(f"{field} harus angka.")
    if n < 0: raise ValueError(f"{field} tidak boleh negatif.")
    return n


def log_action(aksi, entitas, entitas_id=None, deskripsi=""):
    try:
        db.session.add(AuditLog(
            user_id=getattr(current_user, "id", None),
            username=getattr(current_user, "username", "sistem"),
            aksi=aksi, entitas=entitas, entitas_id=entitas_id,
            deskripsi=(deskripsi or "")[:500]
        ))
        db.session.commit()
    except Exception:
        db.session.rollback()


def _save_upload(fs, folder):
    """Simpan file upload yang tervalidasi."""
    if not fs or not fs.filename: return None
    from werkzeug.utils import secure_filename
    import uuid, os
    name = secure_filename(fs.filename)
    if "." not in name: return None
    ext = name.rsplit(".", 1)[1].lower()
    if ext not in {"png", "jpg", "jpeg", "gif", "webp"}: return None
    head = fs.stream.read(16); fs.stream.seek(0)
    ok = (head.startswith(b"\xff\xd8\xff") or head.startswith(b"\x89PNG") or
          head.startswith(b"GIF8") or (head[:4] == b"RIFF" and head[8:12] == b"WEBP"))
    if not ok: return None
    unique = f"{uuid.uuid4().hex}.{ext}"
    os.makedirs(folder, exist_ok=True)
    fs.save(os.path.join(folder, unique))
    return unique


# =====================================================================
# ROLE DECORATORS (API)
# =====================================================================
def api_login_required(fn):
    from functools import wraps
    @wraps(fn)
    def inner(*a, **kw):
        if not current_user.is_authenticated: return jsonify({"error": "Tidak terautentikasi."}), 401
        return fn(*a, **kw)
    return inner


def api_roles(*roles):
    from functools import wraps
    def wrapper(fn):
        @wraps(fn)
        def inner(*a, **kw):
            if not current_user.is_authenticated: return jsonify({"error": "Tidak terautentikasi."}), 401
            if current_user.role not in roles:
                return jsonify({"error": "Akses ditolak untuk peran Anda."}), 403
            return fn(*a, **kw)
        return inner
    return wrapper


# =====================================================================
# APP FACTORY
# =====================================================================
def create_app(base_dir: Path):
    base_dir = Path(base_dir)
    data_dir = base_dir / "data"
    upload_dir = data_dir / "uploads"
    db_path = data_dir / "tomatgrow.db"
    data_dir.mkdir(parents=True, exist_ok=True)
    upload_dir.mkdir(parents=True, exist_ok=True)

    app = Flask(__name__, static_folder=None)
    app.secret_key = "tomat-grow-local-secret-2024-change-me-" + str(base_dir.name)
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path.as_posix()}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024
    app.config["UPLOAD_FOLDER"] = str(upload_dir)
    app.config["DATA_DIR"] = str(data_dir)
    app.config["SESSION_COOKIE_HTTPONLY"] = True
    app.config["SESSION_COOKIE_SAMESITE"] = "Lax"

    # Jinja dari dict
    app.jinja_loader = DictLoader(TEMPLATES)

    # Static inline
    @app.route("/static/css/style.css")
    def static_css(): return app.response_class(CSS, mimetype="text/css")

    @app.route("/static/js/common.js")
    def static_js(): return app.response_class(JS, mimetype="application/javascript")

    @app.route("/static/uploads/<path:fname>")
    @login_required
    def static_upload(fname):
        from flask import send_from_directory
        return send_from_directory(upload_dir, fname)

    db.init_app(app)
    login_manager.init_app(app)

    register_routes(app)

    with app.app_context():
        db.create_all()
        _bootstrap_admin()

    return app


def _bootstrap_admin():
    if User.query.count() == 0:
        u = User(nama="Administrator", username="admin", role="admin")
        u.set_password("admin123")
        db.session.add(u); db.session.commit()
        print("[TOMAT GROW] Akun admin default -> username: admin | password: admin123")


# =====================================================================
# ROUTES
# =====================================================================
def register_routes(app):

    # ---------------- AUTH ----------------
    @app.route("/login", methods=["GET", "POST"])
    def login():
        if current_user.is_authenticated: return redirect(url_for("dashboard"))
        if request.method == "POST":
            u = User.query.filter_by(username=(request.form.get("username") or "").strip()).first()
            if u and u.check_password(request.form.get("password") or ""):
                login_user(u)
                return redirect(url_for("dashboard"))
            flash("Username atau password salah.", "danger")
        return render_template("login.html")

    @app.route("/logout")
    @login_required
    def logout():
        logout_user(); return redirect(url_for("login"))

    # ---------------- PAGES ----------------
    @app.route("/")
    @login_required
    def index(): return redirect(url_for("dashboard"))

    @app.route("/dashboard")
    @login_required
    def dashboard(): return render_template("dashboard.html", active="dashboard")

    @app.route("/tanaman")
    @login_required
    def page_tanaman(): return render_template("tanaman.html", active="tanaman")

    @app.route("/tanaman/<int:tid>")
    @login_required
    def page_tanaman_detail(tid): return render_template("tanaman_detail.html", active="tanaman", tanaman_id=tid)

    @app.route("/pengukuran")
    @login_required
    def page_pengukuran(): return render_template("pengukuran.html", active="pengukuran")

    @app.route("/perawatan")
    @login_required
    def page_perawatan(): return render_template("perawatan.html", active="perawatan")

    @app.route("/dokumentasi")
    @login_required
    def page_dokumentasi(): return render_template("dokumentasi.html", active="dokumentasi")

    @app.route("/jadwal")
    @login_required
    def page_jadwal(): return render_template("jadwal.html", active="jadwal")

    @app.route("/laporan")
    @login_required
    def page_laporan(): return render_template("laporan.html", active="laporan")

    @app.route("/pengguna")
    @login_required
    def page_pengguna():
        if current_user.role != "admin": return redirect(url_for("dashboard"))
        return render_template("users.html", active="pengguna")

    @app.route("/audit")
    @login_required
    def page_audit():
        if current_user.role not in ("admin", "pembina"): return redirect(url_for("dashboard"))
        return render_template("audit.html", active="audit")

    # ---------------- API AUTH ----------------
    @app.route("/api/auth/me")
    @api_login_required
    def api_me(): return jsonify({"user": current_user.to_dict()})

    # ---------------- API TANAMAN ----------------
    @app.route("/api/tanaman", methods=["GET"])
    @api_login_required
    def api_list_tanaman():
        q = (request.args.get("q") or "").strip()
        st = (request.args.get("status") or "").strip()
        query = Tanaman.query
        if q:
            like = f"%{q}%"
            query = query.filter(or_(Tanaman.kode_tanaman.ilike(like),
                                     Tanaman.nama_tanaman.ilike(like),
                                     Tanaman.varietas.ilike(like),
                                     Tanaman.lokasi.ilike(like)))
        if st: query = query.filter(Tanaman.status == st)
        rows = query.order_by(Tanaman.kode_tanaman.asc()).all()
        return jsonify({"data": [t.to_dict() for t in rows]})

    @app.route("/api/tanaman/<int:tid>", methods=["GET"])
    @api_login_required
    def api_get_tanaman(tid):
        t = db.session.get(Tanaman, tid)
        if not t: return jsonify({"error": "Tanaman tidak ditemukan."}), 404
        return jsonify({"data": t.to_dict()})

    @app.route("/api/tanaman", methods=["POST"])
    @api_roles("admin", "anggota")
    def api_create_tanaman():
        d = request.get_json(silent=True) or {}
        kode = (d.get("kode_tanaman") or "").strip()
        nama = (d.get("nama_tanaman") or "").strip()
        tgl = _parse_date(d.get("tanggal_tanam"))
        st = d.get("status") or "hidup"
        if not kode or not nama: return jsonify({"error": "Kode dan nama tanaman wajib diisi."}), 400
        if not tgl: return jsonify({"error": "Tanggal tanam tidak valid."}), 400
        if st not in ("hidup", "kurang sehat", "mati", "panen"):
            return jsonify({"error": "Status tidak valid."}), 400
        if Tanaman.query.filter_by(kode_tanaman=kode).first():
            return jsonify({"error": "Kode tanaman sudah dipakai."}), 400
        t = Tanaman(kode_tanaman=kode, nama_tanaman=nama, varietas=d.get("varietas"),
                    tanggal_tanam=tgl, lokasi=d.get("lokasi"), posisi=d.get("posisi"),
                    status=st, catatan=d.get("catatan"))
        db.session.add(t); db.session.commit()
        log_action("create", "tanaman", t.id, f"Tambah tanaman {kode}")
        return jsonify({"data": t.to_dict()}), 201

    @app.route("/api/tanaman/<int:tid>", methods=["PUT"])
    @api_roles("admin", "anggota")
    def api_update_tanaman(tid):
        t = db.session.get(Tanaman, tid)
        if not t: return jsonify({"error": "Tanaman tidak ditemukan."}), 404
        d = request.get_json(silent=True) or {}
        if "kode_tanaman" in d:
            k = (d["kode_tanaman"] or "").strip()
            if not k: return jsonify({"error": "Kode tidak boleh kosong."}), 400
            if Tanaman.query.filter(Tanaman.kode_tanaman == k, Tanaman.id != tid).first():
                return jsonify({"error": "Kode sudah dipakai."}), 400
            t.kode_tanaman = k
        if "nama_tanaman" in d: t.nama_tanaman = (d["nama_tanaman"] or "").strip()
        if "varietas" in d: t.varietas = d["varietas"]
        if "tanggal_tanam" in d:
            dd = _parse_date(d["tanggal_tanam"])
            if not dd: return jsonify({"error": "Tanggal tidak valid."}), 400
            t.tanggal_tanam = dd
        for f in ("lokasi", "posisi", "catatan"):
            if f in d: setattr(t, f, d[f])
        if "status" in d:
            if d["status"] not in ("hidup", "kurang sehat", "mati", "panen"):
                return jsonify({"error": "Status tidak valid."}), 400
            t.status = d["status"]
        db.session.commit()
        log_action("update", "tanaman", t.id, f"Update tanaman {t.kode_tanaman}")
        return jsonify({"data": t.to_dict()})

    @app.route("/api/tanaman/<int:tid>", methods=["DELETE"])
    @api_roles("admin")
    def api_delete_tanaman(tid):
        t = db.session.get(Tanaman, tid)
        if not t: return jsonify({"error": "Tanaman tidak ditemukan."}), 404
        kode = t.kode_tanaman
        db.session.delete(t); db.session.commit()
        log_action("delete", "tanaman", tid, f"Hapus tanaman {kode}")
        return jsonify({"ok": True})

    @app.route("/api/tanaman/<int:tid>/timeline")
    @api_login_required
    def api_timeline(tid):
        if not db.session.get(Tanaman, tid): return jsonify({"error": "Tanaman tidak ditemukan."}), 404
        items = []
        for p in Pengukuran.query.filter_by(tanaman_id=tid).all():
            items.append({"tipe": "pengukuran", "tanggal": p.tanggal.isoformat(),
                          "judul": f"Pengukuran: tinggi {p.tinggi_cm or '-'} cm, {p.jumlah_daun or 0} daun",
                          "detail": p.catatan or ""})
        for r in Perawatan.query.filter_by(tanaman_id=tid).all():
            items.append({"tipe": "perawatan", "tanggal": r.tanggal.isoformat(),
                          "judul": f"Perawatan: {r.jenis_kegiatan.replace('_', ' ')}",
                          "detail": r.keterangan or ""})
        for dd in Dokumentasi.query.filter_by(tanaman_id=tid).all():
            items.append({"tipe": "dokumentasi", "tanggal": dd.tanggal.isoformat(),
                          "judul": "Dokumentasi foto", "detail": dd.keterangan or ""})
        items.sort(key=lambda x: x["tanggal"], reverse=True)
        return jsonify({"data": items})

    @app.route("/api/tanaman/<int:tid>/grafik")
    @api_login_required
    def api_grafik(tid):
        rows = Pengukuran.query.filter_by(tanaman_id=tid).order_by(Pengukuran.tanggal.asc(), Pengukuran.id.asc()).all()
        return jsonify({
            "labels": [r.tanggal.isoformat() for r in rows],
            "tinggi": [r.tinggi_cm for r in rows],
            "daun": [r.jumlah_daun for r in rows],
            "bunga": [r.jumlah_bunga for r in rows],
            "buah": [r.jumlah_buah for r in rows],
        })

    # ---------------- API PENGUKURAN ----------------
    @app.route("/api/pengukuran", methods=["GET"])
    @api_login_required
    def api_list_pengukuran():
        q = Pengukuran.query
        tid = request.args.get("tanaman_id")
        if tid: q = q.filter(Pengukuran.tanaman_id == int(tid))
        m = request.args.get("mulai"); s = request.args.get("selesai")
        if m: q = q.filter(Pengukuran.tanggal >= _parse_date(m))
        if s: q = q.filter(Pengukuran.tanggal <= _parse_date(s))
        rows = q.order_by(Pengukuran.tanggal.desc(), Pengukuran.id.desc()).all()
        return jsonify({"data": [r.to_dict() for r in rows]})

    @app.route("/api/pengukuran", methods=["POST"])
    @api_roles("admin", "anggota")
    def api_create_pengukuran():
        d = request.get_json(silent=True) or {}
        tid = d.get("tanaman_id")
        if not tid or not db.session.get(Tanaman, int(tid)):
            return jsonify({"error": "Tanaman tidak ditemukan."}), 400
        tgl = _parse_date(d.get("tanggal"))
        if not tgl: return jsonify({"error": "Tanggal tidak valid."}), 400
        try:
            p = Pengukuran(
                tanaman_id=int(tid), tanggal=tgl,
                tinggi_cm=_to_float(d.get("tinggi_cm"), "Tinggi"),
                diameter_batang_mm=_to_float(d.get("diameter_batang_mm"), "Diameter batang"),
                jumlah_daun=_to_int(d.get("jumlah_daun"), "Jumlah daun"),
                jumlah_cabang=_to_int(d.get("jumlah_cabang"), "Jumlah cabang"),
                jumlah_bunga=_to_int(d.get("jumlah_bunga"), "Jumlah bunga"),
                jumlah_buah=_to_int(d.get("jumlah_buah"), "Jumlah buah"),
                kondisi_daun=d.get("kondisi_daun"), kondisi_batang=d.get("kondisi_batang"),
                kondisi_tanah=d.get("kondisi_tanah"), catatan=d.get("catatan"))
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        db.session.add(p); db.session.commit()
        log_action("create", "pengukuran", p.id, f"Pengukuran tanaman #{tid}")
        return jsonify({"data": p.to_dict()}), 201

    @app.route("/api/pengukuran/<int:pid>", methods=["PUT"])
    @api_roles("admin", "anggota")
    def api_update_pengukuran(pid):
        p = db.session.get(Pengukuran, pid)
        if not p: return jsonify({"error": "Data tidak ditemukan."}), 404
        d = request.get_json(silent=True) or {}
        try:
            if "tanggal" in d:
                tgl = _parse_date(d["tanggal"])
                if not tgl: return jsonify({"error": "Tanggal tidak valid."}), 400
                p.tanggal = tgl
            for f in ("tinggi_cm", "diameter_batang_mm"):
                if f in d: setattr(p, f, _to_float(d[f], f))
            for f in ("jumlah_daun", "jumlah_cabang", "jumlah_bunga", "jumlah_buah"):
                if f in d: setattr(p, f, _to_int(d[f], f))
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        for f in ("kondisi_daun", "kondisi_batang", "kondisi_tanah", "catatan"):
            if f in d: setattr(p, f, d[f])
        db.session.commit()
        log_action("update", "pengukuran", p.id)
        return jsonify({"data": p.to_dict()})

    @app.route("/api/pengukuran/<int:pid>", methods=["DELETE"])
    @api_roles("admin", "anggota")
    def api_delete_pengukuran(pid):
        p = db.session.get(Pengukuran, pid)
        if not p: return jsonify({"error": "Data tidak ditemukan."}), 404
        db.session.delete(p); db.session.commit()
        log_action("delete", "pengukuran", pid)
        return jsonify({"ok": True})

    # ---------------- API PERAWATAN ----------------
    @app.route("/api/perawatan", methods=["GET"])
    @api_login_required
    def api_list_perawatan():
        q = Perawatan.query
        tid = request.args.get("tanaman_id"); jenis = request.args.get("jenis")
        if tid: q = q.filter(Perawatan.tanaman_id == int(tid))
        if jenis: q = q.filter(Perawatan.jenis_kegiatan == jenis)
        rows = q.order_by(Perawatan.tanggal.desc(), Perawatan.id.desc()).all()
        return jsonify({"data": [r.to_dict() for r in rows]})

    @app.route("/api/perawatan", methods=["POST"])
    @api_roles("admin", "anggota")
    def api_create_perawatan():
        d = request.get_json(silent=True) or {}
        tid = d.get("tanaman_id")
        if not tid or not db.session.get(Tanaman, int(tid)):
            return jsonify({"error": "Tanaman tidak ditemukan."}), 400
        jenis = d.get("jenis_kegiatan")
        if jenis not in ("penyiraman", "pemupukan", "penyiangan",
                         "pengendalian_hama", "pemeriksaan", "lainnya"):
            return jsonify({"error": "Jenis kegiatan tidak valid."}), 400
        tgl = _parse_date(d.get("tanggal"))
        if not tgl: return jsonify({"error": "Tanggal tidak valid."}), 400
        r = Perawatan(tanaman_id=int(tid), tanggal=tgl, jenis_kegiatan=jenis,
                      petugas=d.get("petugas"), keterangan=d.get("keterangan"),
                      hasil=d.get("hasil"))
        db.session.add(r); db.session.commit()
        log_action("create", "perawatan", r.id, f"{jenis} tanaman #{tid}")
        return jsonify({"data": r.to_dict()}), 201

    @app.route("/api/perawatan/<int:rid>", methods=["PUT"])
    @api_roles("admin", "anggota")
    def api_update_perawatan(rid):
        r = db.session.get(Perawatan, rid)
        if not r: return jsonify({"error": "Data tidak ditemukan."}), 404
        d = request.get_json(silent=True) or {}
        if "tanggal" in d:
            tgl = _parse_date(d["tanggal"])
            if not tgl: return jsonify({"error": "Tanggal tidak valid."}), 400
            r.tanggal = tgl
        if "jenis_kegiatan" in d:
            if d["jenis_kegiatan"] not in ("penyiraman", "pemupukan", "penyiangan",
                                           "pengendalian_hama", "pemeriksaan", "lainnya"):
                return jsonify({"error": "Jenis tidak valid."}), 400
            r.jenis_kegiatan = d["jenis_kegiatan"]
        for f in ("petugas", "keterangan", "hasil"):
            if f in d: setattr(r, f, d[f])
        db.session.commit()
        log_action("update", "perawatan", r.id)
        return jsonify({"data": r.to_dict()})

    @app.route("/api/perawatan/<int:rid>", methods=["DELETE"])
    @api_roles("admin", "anggota")
    def api_delete_perawatan(rid):
        r = db.session.get(Perawatan, rid)
        if not r: return jsonify({"error": "Data tidak ditemukan."}), 404
        db.session.delete(r); db.session.commit()
        log_action("delete", "perawatan", rid)
        return jsonify({"ok": True})

    # ---------------- API DOKUMENTASI ----------------
    @app.route("/api/dokumentasi", methods=["GET"])
    @api_login_required
    def api_list_dokumentasi():
        q = Dokumentasi.query
        tid = request.args.get("tanaman_id")
        if tid: q = q.filter(Dokumentasi.tanaman_id == int(tid))
        rows = q.order_by(Dokumentasi.tanggal.desc(), Dokumentasi.id.desc()).all()
        return jsonify({"data": [r.to_dict() for r in rows]})

    @app.route("/api/dokumentasi", methods=["POST"])
    @api_roles("admin", "anggota")
    def api_create_dokumentasi():
        tid = request.form.get("tanaman_id")
        if not tid or not db.session.get(Tanaman, int(tid)):
            return jsonify({"error": "Tanaman tidak ditemukan."}), 400
        tgl = _parse_date(request.form.get("tanggal"))
        if not tgl: return jsonify({"error": "Tanggal tidak valid."}), 400
        f = request.files.get("file_foto")
        if not f: return jsonify({"error": "File foto wajib diunggah."}), 400
        name = _save_upload(f, current_app.config["UPLOAD_FOLDER"])
        if not name: return jsonify({"error": "File tidak valid (JPG/PNG/GIF/WEBP)."}), 400
        d = Dokumentasi(tanaman_id=int(tid), tanggal=tgl,
                        file_foto=name, keterangan=request.form.get("keterangan"))
        db.session.add(d); db.session.commit()
        log_action("create", "dokumentasi", d.id)
        return jsonify({"data": d.to_dict()}), 201

    @app.route("/api/dokumentasi/<int:did>", methods=["DELETE"])
    @api_roles("admin", "anggota")
    def api_delete_dokumentasi(did):
        d = db.session.get(Dokumentasi, did)
        if not d: return jsonify({"error": "Data tidak ditemukan."}), 404
        import os
        try:
            path = os.path.join(current_app.config["UPLOAD_FOLDER"], d.file_foto)
            if os.path.isfile(path): os.remove(path)
        except OSError: pass
        db.session.delete(d); db.session.commit()
        log_action("delete", "dokumentasi", did)
        return jsonify({"ok": True})

    # ---------------- API JADWAL ----------------
    @app.route("/api/jadwal", methods=["GET"])
    @api_login_required
    def api_list_jadwal():
        q = Jadwal.query
        m = request.args.get("mulai"); s = request.args.get("selesai")
        if m: q = q.filter(Jadwal.tanggal >= _parse_date(m))
        if s: q = q.filter(Jadwal.tanggal <= _parse_date(s))
        rows = q.order_by(Jadwal.tanggal.asc(), Jadwal.id.asc()).all()
        return jsonify({"data": [r.to_dict() for r in rows]})

    @app.route("/api/jadwal", methods=["POST"])
    @api_roles("admin")
    def api_create_jadwal():
        d = request.get_json(silent=True) or {}
        keg = (d.get("kegiatan") or "").strip()
        if not keg: return jsonify({"error": "Kegiatan wajib diisi."}), 400
        tgl = _parse_date(d.get("tanggal"))
        if not tgl: return jsonify({"error": "Tanggal tidak valid."}), 400
        st = d.get("status") or "belum"
        if st not in ("belum", "selesai", "batal"): return jsonify({"error": "Status tidak valid."}), 400
        j = Jadwal(tanggal=tgl, kegiatan=keg, petugas=d.get("petugas"), status=st, catatan=d.get("catatan"))
        db.session.add(j); db.session.commit()
        log_action("create", "jadwal", j.id, keg)
        return jsonify({"data": j.to_dict()}), 201

    @app.route("/api/jadwal/<int:jid>", methods=["PUT"])
    @api_roles("admin")
    def api_update_jadwal(jid):
        j = db.session.get(Jadwal, jid)
        if not j: return jsonify({"error": "Data tidak ditemukan."}), 404
        d = request.get_json(silent=True) or {}
        if "tanggal" in d:
            tgl = _parse_date(d["tanggal"])
            if not tgl: return jsonify({"error": "Tanggal tidak valid."}), 400
            j.tanggal = tgl
        if "kegiatan" in d: j.kegiatan = (d["kegiatan"] or "").strip()
        if "petugas" in d: j.petugas = d["petugas"]
        if "status" in d:
            if d["status"] not in ("belum", "selesai", "batal"): return jsonify({"error": "Status tidak valid."}), 400
            j.status = d["status"]
        if "catatan" in d: j.catatan = d["catatan"]
        db.session.commit()
        log_action("update", "jadwal", j.id)
        return jsonify({"data": j.to_dict()})

    @app.route("/api/jadwal/<int:jid>", methods=["DELETE"])
    @api_roles("admin")
    def api_delete_jadwal(jid):
        j = db.session.get(Jadwal, jid)
        if not j: return jsonify({"error": "Data tidak ditemukan."}), 404
        db.session.delete(j); db.session.commit()
        log_action("delete", "jadwal", jid)
        return jsonify({"ok": True})

    # ---------------- API DASHBOARD ----------------
    @app.route("/api/dashboard")
    @api_login_required
    def api_dashboard():
        plants = Tanaman.query.all()
        latest = {}
        for p in plants:
            m = (Pengukuran.query.filter_by(tanaman_id=p.id)
                 .order_by(Pengukuran.tanggal.desc(), Pengukuran.id.desc()).first())
            if m: latest[p.id] = m

        total = len(plants)
        sehat = sum(1 for p in plants if p.status == "hidup")
        bermasalah = sum(1 for p in plants if p.status == "kurang sehat")
        mati = sum(1 for p in plants if p.status == "mati")
        panen = sum(1 for p in plants if p.status == "panen")

        vt = [m.tinggi_cm for m in latest.values() if m.tinggi_cm is not None]
        tinggi_rata = round(sum(vt) / len(vt), 2) if vt else None

        total_bunga = sum((m.jumlah_bunga or 0) for m in latest.values())
        total_buah = sum((m.jumlah_buah or 0) for m in latest.values())

        keg = Perawatan.query.order_by(Perawatan.tanggal.desc(), Perawatan.id.desc()).limit(5).all()
        jadwal = Jadwal.query.filter(Jadwal.tanggal == date.today()).order_by(Jadwal.id.asc()).all()

        rows = (db.session.query(Pengukuran.tanggal,
                                 func.avg(Pengukuran.tinggi_cm),
                                 func.avg(Pengukuran.jumlah_daun),
                                 func.sum(Pengukuran.jumlah_bunga),
                                 func.sum(Pengukuran.jumlah_buah))
                .group_by(Pengukuran.tanggal).order_by(Pengukuran.tanggal.asc()).all())

        return jsonify({
            "ringkasan": {
                "total_tanaman": total, "sehat": sehat, "bermasalah": bermasalah,
                "mati": mati, "panen": panen, "tinggi_rata_rata": tinggi_rata,
                "total_bunga": total_bunga, "total_buah": total_buah,
            },
            "kegiatan_terakhir": [k.to_dict() for k in keg],
            "jadwal_hari_ini": [j.to_dict() for j in jadwal],
            "grafik": {
                "labels": [r[0].isoformat() for r in rows],
                "tinggi": [round(r[1], 2) if r[1] is not None else None for r in rows],
                "daun": [round(r[2], 2) if r[2] is not None else None for r in rows],
                "bunga": [int(r[3]) if r[3] is not None else 0 for r in rows],
                "buah": [int(r[4]) if r[4] is not None else 0 for r in rows],
            },
        })

    # ---------------- API USERS ----------------
    @app.route("/api/users", methods=["GET"])
    @api_roles("admin", "pembina")
    def api_list_users():
        rows = User.query.order_by(User.role.asc(), User.nama.asc()).all()
        return jsonify({"data": [u.to_dict() for u in rows]})

    @app.route("/api/users", methods=["POST"])
    @api_roles("admin")
    def api_create_user():
        d = request.get_json(silent=True) or {}
        nama = (d.get("nama") or "").strip()
        uname = (d.get("username") or "").strip().lower()
        pwd = d.get("password") or ""
        role = d.get("role") or "anggota"
        if not nama or not uname or not pwd: return jsonify({"error": "Nama, username, password wajib."}), 400
        if len(pwd) < 6: return jsonify({"error": "Password minimal 6 karakter."}), 400
        if role not in ("admin", "anggota", "pembina"): return jsonify({"error": "Role tidak valid."}), 400
        if User.query.filter_by(username=uname).first(): return jsonify({"error": "Username sudah dipakai."}), 400
        u = User(nama=nama, username=uname, role=role); u.set_password(pwd)
        db.session.add(u); db.session.commit()
        log_action("create", "users", u.id, f"Tambah pengguna {uname}")
        return jsonify({"data": u.to_dict()}), 201

    @app.route("/api/users/<int:uid>", methods=["PUT"])
    @api_roles("admin")
    def api_update_user(uid):
        u = db.session.get(User, uid)
        if not u: return jsonify({"error": "Pengguna tidak ditemukan."}), 404
        d = request.get_json(silent=True) or {}
        if "nama" in d: u.nama = (d["nama"] or "").strip()
        if "role" in d:
            if d["role"] not in ("admin", "anggota", "pembina"): return jsonify({"error": "Role tidak valid."}), 400
            if u.id == current_user.id and d["role"] != "admin":
                return jsonify({"error": "Tidak dapat menurunkan role sendiri."}), 400
            u.role = d["role"]
        if d.get("password"):
            if len(d["password"]) < 6: return jsonify({"error": "Password minimal 6 karakter."}), 400
            u.set_password(d["password"])
        db.session.commit()
        log_action("update", "users", u.id)
        return jsonify({"data": u.to_dict()})

    @app.route("/api/users/<int:uid>", methods=["DELETE"])
    @api_roles("admin")
    def api_delete_user(uid):
        if uid == current_user.id: return jsonify({"error": "Tidak dapat menghapus akun sendiri."}), 400
        u = db.session.get(User, uid)
        if not u: return jsonify({"error": "Pengguna tidak ditemukan."}), 404
        uname = u.username
        db.session.delete(u); db.session.commit()
        log_action("delete", "users", uid, f"Hapus {uname}")
        return jsonify({"ok": True})

    # ---------------- API AUDIT ----------------
    @app.route("/api/audit")
    @api_roles("admin", "pembina")
    def api_audit():
        q = AuditLog.query
        e = request.args.get("entitas")
        if e: q = q.filter(AuditLog.entitas == e)
        limit = min(int(request.args.get("limit", 200)), 500)
        rows = q.order_by(AuditLog.waktu.desc()).limit(limit).all()
        return jsonify({"data": [r.to_dict() for r in rows]})

    # ---------------- API LAPORAN ----------------
    @app.route("/api/laporan/riwayat")
    @api_login_required
    def api_riwayat_laporan():
        rows = Laporan.query.order_by(Laporan.tanggal_dibuat.desc()).limit(50).all()
        return jsonify({"data": [r.to_dict() for r in rows]})

    @app.route("/api/laporan/generate", methods=["POST"])
    @api_login_required
    def api_generate_laporan():
        d = request.get_json(silent=True) or {}
        pm = _parse_date(d.get("periode_mulai"))
        ps = _parse_date(d.get("periode_selesai"))
        if not pm or not ps: return jsonify({"error": "Periode wajib diisi."}), 400
        if ps < pm: return jsonify({"error": "Tanggal selesai tidak boleh lebih awal."}), 400

        ids = d.get("tanaman_ids") or []
        q = Tanaman.query
        if ids: q = q.filter(Tanaman.id.in_([int(i) for i in ids]))
        tlist = q.order_by(Tanaman.kode_tanaman.asc()).all()
        if not tlist: return jsonify({"error": "Tidak ada tanaman yang dipilih."}), 400

        pmap, rmap, doks = {}, {}, []
        for t in tlist:
            pmap[t.id] = [r.to_dict() for r in Pengukuran.query.filter(
                Pengukuran.tanaman_id == t.id,
                Pengukuran.tanggal >= pm, Pengukuran.tanggal <= ps
            ).order_by(Pengukuran.tanggal.asc()).all()]
            rmap[t.id] = [r.to_dict() for r in Perawatan.query.filter(
                Perawatan.tanaman_id == t.id,
                Perawatan.tanggal >= pm, Perawatan.tanggal <= ps
            ).order_by(Perawatan.tanggal.asc()).all()]
            doks.extend([r.to_dict() for r in Dokumentasi.query.filter(
                Dokumentasi.tanaman_id == t.id,
                Dokumentasi.tanggal >= pm, Dokumentasi.tanggal <= ps
            ).order_by(Dokumentasi.tanggal.asc()).all()])

        jenis = d.get("jenis") or {}
        jd = {k: bool(jenis.get(k, True)) for k in ("pengukuran", "perawatan", "dokumentasi", "grafik", "lampiran")}

        meta = {
            "judul": d.get("judul") or "Laporan Monitoring Tanaman Tomat",
            "kelompok": d.get("kelompok"), "kelas": d.get("kelas"),
            "sekolah": d.get("sekolah") or "-", "pembina": d.get("pembina") or "-",
            "periode_mulai": pm.isoformat(), "periode_selesai": ps.isoformat(),
            "dibuat_oleh": current_user.nama,
        }

        try:
            buf = build_laporan({
                "meta": meta,
                "tanaman": [t.to_dict() for t in tlist],
                "pengukuran": pmap, "perawatan": rmap, "dokumentasi": doks,
                "jenis": jd, "upload_root": current_app.config["UPLOAD_FOLDER"],
            })
        except Exception as e:
            current_app.logger.exception("Gagal buat PDF")
            return jsonify({"error": f"Gagal membuat laporan: {e}"}), 500

        rec = Laporan(judul=meta["judul"], periode_mulai=pm, periode_selesai=ps,
                      dibuat_oleh=current_user.nama)
        db.session.add(rec); db.session.commit()
        log_action("create", "laporan", rec.id, meta["judul"])

        fname = f"Laporan_TOMATGROW_{pm}_{ps}.pdf"
        return send_file(buf, mimetype="application/pdf", as_attachment=True, download_name=fname)

    # ---------------- ERROR HANDLERS ----------------
    @app.errorhandler(413)
    def too_large(e): return jsonify({"error": "File terlalu besar (maks 5 MB)."}), 413

    @app.errorhandler(404)
    def nf(e):
        if request.path.startswith("/api/"): return jsonify({"error": "Endpoint tidak ditemukan."}), 404
        return "Halaman tidak ditemukan.", 404
