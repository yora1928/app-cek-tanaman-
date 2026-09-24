"""TOMAT GROW - Generator laporan PDF."""
from io import BytesIO
from datetime import datetime
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (BaseDocTemplate, Frame, Image, PageBreak,
                                PageTemplate, Paragraph, Spacer, Table, TableStyle)
from reportlab.pdfgen import canvas as rl_canvas

HITAM = colors.HexColor("#1a1a1a")
ABU = colors.HexColor("#555555")
GARIS = colors.HexColor("#999999")


class NumberedCanvas(rl_canvas.Canvas):
    def __init__(self, *a, **kw):
        super().__init__(*a, **kw); self._saved = []
    def showPage(self):
        self._saved.append(dict(self.__dict__)); self._startPage()
    def save(self):
        total = len(self._saved)
        for st in self._saved:
            self.__dict__.update(st); self._footer(total); super().showPage()
        super().save()
    def _footer(self, total):
        self.saveState()
        self.setStrokeColor(GARIS); self.setLineWidth(0.4)
        self.line(2.5*cm, 1.7*cm, A4[0]-2.5*cm, 1.7*cm)
        self.setFont("Helvetica", 8.5); self.setFillColor(ABU)
        self.drawString(2.5*cm, 1.2*cm, "TOMAT GROW - Laporan Monitoring Tanaman Tomat")
        self.drawRightString(A4[0]-2.5*cm, 1.2*cm, f"Halaman {self._pageNumber} dari {total}")
        self.restoreState()


def _styles():
    base = getSampleStyleSheet()
    return {
        "judul": ParagraphStyle("judul", parent=base["Title"], fontName="Helvetica-Bold",
                                fontSize=22, leading=28, alignment=TA_CENTER, textColor=HITAM),
        "sub": ParagraphStyle("sub", parent=base["Normal"], fontName="Helvetica",
                              fontSize=12, leading=17, alignment=TA_CENTER, textColor=ABU),
        "bab": ParagraphStyle("bab", parent=base["Heading1"], fontName="Helvetica-Bold",
                              fontSize=13, leading=18, spaceBefore=12, spaceAfter=8, textColor=HITAM),
        "sub2": ParagraphStyle("sub2", parent=base["Heading2"], fontName="Helvetica-Bold",
                               fontSize=11, leading=15, spaceBefore=8, spaceAfter=4, textColor=HITAM),
        "body": ParagraphStyle("body", parent=base["BodyText"], fontName="Helvetica",
                               fontSize=10.5, leading=16, alignment=TA_JUSTIFY, textColor=HITAM),
        "kecil": ParagraphStyle("kecil", parent=base["Normal"], fontName="Helvetica",
                                fontSize=9, leading=13, textColor=ABU),
    }


def _n(v):
    if v is None: return "-"
    if isinstance(v, float): return f"{v:g}"
    return str(v)


def _short(t, limit=45):
    if not t: return "-"
    t = str(t).replace("\n", " ").strip()
    return t if len(t) <= limit else t[:limit-3] + "..."


def _tabel(header, rows, widths=None):
    t = Table([header]+rows, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#e8f5e9")),
        ("TEXTCOLOR", (0,0), (-1,0), HITAM),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTNAME", (0,1), (-1,-1), "Helvetica"),
        ("FONTSIZE", (0,0), (-1,-1), 8.5), ("LEADING", (0,0), (-1,-1), 11),
        ("GRID", (0,0), (-1,-1), 0.4, GARIS),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("ALIGN", (0,0), (-1,0), "CENTER"),
        ("TOPPADDING", (0,0), (-1,-1), 4), ("BOTTOMPADDING", (0,0), (-1,-1), 4),
    ]))
    return t


def _chart(dates, series, judul, ylabel):
    if not dates: return None
    fig, ax = plt.subplots(figsize=(7.0, 3.0), dpi=150)
    for label, vals in series.items():
        ax.plot(dates, vals, marker="o", markersize=3, linewidth=1.4, label=label)
    ax.set_title(judul, fontsize=10, color="#1a1a1a")
    ax.set_ylabel(ylabel, fontsize=9)
    ax.grid(True, linestyle="--", alpha=0.35, linewidth=0.6)
    ax.tick_params(labelsize=8); ax.legend(fontsize=8, frameon=False)
    fig.autofmt_xdate(rotation=30); fig.tight_layout()
    buf = BytesIO(); fig.savefig(buf, format="png", bbox_inches="tight")
    plt.close(fig); buf.seek(0); return buf


def build_laporan(payload):
    meta = payload.get("meta", {})
    tlist = payload.get("tanaman", [])
    pmap = payload.get("pengukuran", {})
    rmap = payload.get("perawatan", {})
    doks = payload.get("dokumentasi", [])
    jenis = payload.get("jenis", {})
    uproot = payload.get("upload_root")

    st = _styles(); story = []

    # --- JUDUL ---
    story.append(Spacer(1, 3.2*cm))
    story.append(Paragraph("TOMAT GROW", st["judul"]))
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph("Sistem Monitoring Pertumbuhan dan Perkembangan Tanaman Tomat", st["sub"]))
    story.append(Spacer(1, 2.0*cm))

    info = [
        ["Nama Kelompok", meta.get("kelompok") or "-"],
        ["Kelas", meta.get("kelas") or "-"],
        ["Sekolah", meta.get("sekolah") or "-"],
        ["Pembina", meta.get("pembina") or "-"],
        ["Periode Proyek", f"{meta.get('periode_mulai') or '-'} s.d. {meta.get('periode_selesai') or '-'}"],
        ["Tanggal Laporan", datetime.now().strftime("%d %B %Y")],
        ["Disusun oleh", meta.get("dibuat_oleh") or "-"],
    ]
    t = Table(info, colWidths=[4.5*cm, 9*cm])
    t.setStyle(TableStyle([
        ("FONTNAME", (0,0), (0,-1), "Helvetica-Bold"),
        ("FONTNAME", (1,0), (1,-1), "Helvetica"),
        ("FONTSIZE", (0,0), (-1,-1), 10.5),
        ("TEXTCOLOR", (0,0), (-1,-1), HITAM),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6), ("TOPPADDING", (0,0), (-1,-1), 6),
        ("LINEBELOW", (0,0), (-1,-1), 0.3, colors.HexColor("#dddddd")),
    ]))
    story.append(t); story.append(PageBreak())

    # --- BAB I ---
    story.append(Paragraph("BAB I&nbsp;&nbsp;PENDAHULUAN", st["bab"]))
    story.append(Paragraph("1.1 Latar Belakang", st["sub2"]))
    story.append(Paragraph(
        "Pemantauan pertumbuhan tanaman tomat merupakan bagian dari pembelajaran berbasis proyek "
        "STEAM. Melalui pencatatan rutin dan terstruktur, siswa memahami hubungan antara perawatan "
        "dan perkembangan tanaman. Laporan ini disusun berdasarkan data yang tercatat pada aplikasi "
        "TOMAT GROW selama periode pengamatan.", st["body"]))
    story.append(Paragraph("1.2 Tujuan", st["sub2"]))
    for i, s in enumerate([
        "Mencatat data pertumbuhan tanaman tomat secara terstruktur.",
        "Mendokumentasikan kegiatan perawatan yang dilakukan.",
        "Menyajikan perkembangan tanaman dalam bentuk tabel dan grafik.",
        "Menjadi bahan evaluasi akhir proyek.",
    ], 1):
        story.append(Paragraph(f"{i}. {s}", st["body"]))
    story.append(Paragraph("1.3 Metode", st["sub2"]))
    story.append(Paragraph(
        "Pengamatan dilakukan berkala terhadap sejumlah tanaman. Data yang dicatat meliputi tinggi, "
        "jumlah daun, cabang, diameter batang, jumlah bunga, jumlah buah, serta kondisi daun/batang/"
        "tanah. Data perawatan dan dokumentasi foto dicatat terpisah. Seluruh data tersimpan di basis "
        "data aplikasi dan diolah menjadi laporan ini.", st["body"]))
    story.append(PageBreak())

    # --- BAB II ---
    story.append(Paragraph("BAB II&nbsp;&nbsp;DATA TANAMAN", st["bab"]))
    if tlist:
        rows = [[str(i), t.get("kode_tanaman"), t.get("nama_tanaman"),
                 t.get("varietas") or "-", t.get("tanggal_tanam") or "-",
                 t.get("lokasi") or "-", t.get("posisi") or "-", t.get("status") or "-"]
                for i, t in enumerate(tlist, 1)]
        story.append(_tabel(["No","Kode","Nama","Varietas","Tgl Tanam","Lokasi","Posisi","Status"],
                            rows, [0.9*cm,1.9*cm,3.2*cm,2.4*cm,2.1*cm,2.4*cm,1.8*cm,1.9*cm]))
    else:
        story.append(Paragraph("Belum ada data tanaman.", st["body"]))
    story.append(PageBreak())

    # --- BAB III ---
    story.append(Paragraph("BAB III&nbsp;&nbsp;HASIL PENGAMATAN", st["bab"]))
    if jenis.get("pengukuran", True):
        for idx, t in enumerate(tlist, 1):
            rows_p = pmap.get(t.get("id"), [])
            story.append(Paragraph(f"3.{idx} Tanaman {t.get('kode_tanaman')} - {t.get('nama_tanaman')}", st["sub2"]))
            if not rows_p:
                story.append(Paragraph("Belum ada data pengukuran.", st["kecil"]))
                story.append(Spacer(1, 0.3*cm)); continue
            rows = [[r.get("tanggal"), _n(r.get("tinggi_cm")), _n(r.get("jumlah_daun")),
                     _n(r.get("jumlah_cabang")), _n(r.get("diameter_batang_mm")),
                     _n(r.get("jumlah_bunga")), _n(r.get("jumlah_buah")),
                     _short(r.get("catatan"))] for r in rows_p]
            story.append(_tabel(["Tgl","Tinggi","Daun","Cabang","Ø Batang","Bunga","Buah","Catatan"],
                                rows, [2.0*cm,1.6*cm,1.1*cm,1.2*cm,1.9*cm,1.1*cm,1.1*cm,5.8*cm]))
            story.append(Spacer(1, 0.35*cm))

    if jenis.get("grafik", True) and tlist:
        story.append(Paragraph("3.G Grafik Perkembangan", st["sub2"]))
        for t in tlist:
            rows_p = pmap.get(t.get("id"), [])
            if len(rows_p) < 2: continue
            dates = [r["tanggal"] for r in rows_p]
            b1 = _chart(dates, {"Tinggi (cm)": [r.get("tinggi_cm") or 0 for r in rows_p],
                                "Jumlah Daun": [r.get("jumlah_daun") or 0 for r in rows_p]},
                        f"Perkembangan {t.get('kode_tanaman')} - Tinggi & Daun", "Nilai")
            if b1:
                story.append(Paragraph(f"Grafik {t.get('kode_tanaman')}", st["kecil"]))
                story.append(Image(b1, width=16*cm, height=6.6*cm))
                story.append(Spacer(1, 0.3*cm))
            b2 = _chart(dates, {"Bunga": [r.get("jumlah_bunga") or 0 for r in rows_p],
                                "Buah": [r.get("jumlah_buah") or 0 for r in rows_p]},
                        f"Perkembangan {t.get('kode_tanaman')} - Bunga & Buah", "Jumlah")
            if b2:
                story.append(Image(b2, width=16*cm, height=6.6*cm))
                story.append(Spacer(1, 0.3*cm))

    if jenis.get("dokumentasi", True) and doks:
        story.append(PageBreak())
        story.append(Paragraph("3.D Dokumentasi Foto", st["sub2"]))
        grid = []; row = []
        for d in doks[:24]:
            path = os.path.join(uproot or "", d.get("file_foto", ""))
            if not os.path.isfile(path): continue
            try: img = Image(path, width=7.2*cm, height=5.4*cm)
            except Exception: continue
            cap = Paragraph(f"{d.get('tanggal')}<br/>{_short(d.get('keterangan'), 60)}", st["kecil"])
            row.append([img, cap])
            if len(row) == 2: grid.append(row); row = []
        if row: grid.append(row)
        for pair in grid:
            cells = []
            for img, cap in pair:
                inner = Table([[img],[cap]], colWidths=[7.6*cm])
                inner.setStyle(TableStyle([("ALIGN",(0,0),(-1,-1),"CENTER"),
                                           ("VALIGN",(0,0),(-1,-1),"TOP"),
                                           ("BOTTOMPADDING",(0,0),(-1,-1),6)]))
                cells.append(inner)
            if len(cells) == 1: cells.append("")
            outer = Table([cells], colWidths=[8.2*cm, 8.2*cm])
            outer.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP")]))
            story.append(outer); story.append(Spacer(1, 0.3*cm))
    story.append(PageBreak())

    # --- BAB IV ---
    story.append(Paragraph("BAB IV&nbsp;&nbsp;PERAWATAN", st["bab"]))
    if jenis.get("perawatan", True):
        kategori = ["penyiraman","pemupukan","penyiangan","pengendalian_hama","pemeriksaan","lainnya"]
        labels = {"penyiraman":"Penyiraman","pemupukan":"Pemupukan","penyiangan":"Penyiangan",
                  "pengendalian_hama":"Pengendalian Hama","pemeriksaan":"Pemeriksaan","lainnya":"Kegiatan Lainnya"}
        ada = False
        for kat in kategori:
            kump = []
            for t in tlist:
                for r in rmap.get(t.get("id"), []):
                    if r.get("jenis_kegiatan") == kat:
                        kump.append((t.get("kode_tanaman"), r))
            if not kump: continue
            ada = True
            story.append(Paragraph(f"4.x {labels[kat]}", st["sub2"]))
            rows = [[k, r.get("tanggal") or "-", r.get("petugas") or "-",
                     _short(r.get("keterangan")), _short(r.get("hasil"))] for k, r in kump]
            story.append(_tabel(["Kode","Tanggal","Petugas","Keterangan","Hasil"],
                                rows, [2.6*cm,2.2*cm,2.8*cm,4.6*cm,4.6*cm]))
            story.append(Spacer(1, 0.3*cm))
        if not ada:
            story.append(Paragraph("Belum ada catatan perawatan.", st["body"]))
    story.append(PageBreak())

    # --- BAB V ---
    story.append(Paragraph("BAB V&nbsp;&nbsp;ANALISIS", st["bab"]))
    story.append(Paragraph(
        "Analisis disusun berdasarkan data yang benar-benar tercatat. Bagian yang datanya belum "
        "cukup tidak disimpulkan secara otomatis.", st["body"]))
    story.append(Spacer(1, 0.3*cm))

    for judul, key in [("Perubahan Tinggi Tanaman","tinggi_cm"),
                       ("Perubahan Jumlah Daun","jumlah_daun"),
                       ("Perkembangan Bunga","jumlah_bunga"),
                       ("Perkembangan Buah","jumlah_buah")]:
        story.append(Paragraph(judul, st["sub2"]))
        rows = []
        for t in tlist:
            rows_p = pmap.get(t.get("id"), [])
            nilai = [r.get(key) for r in rows_p if r.get(key) is not None]
            if len(nilai) >= 2:
                delta = nilai[-1] - nilai[0]
                rows.append([t.get("kode_tanaman"), _n(nilai[0]), _n(nilai[-1]),
                             f"{'+' if delta >= 0 else ''}{round(delta,2)}"])
            else:
                rows.append([t.get("kode_tanaman"), "-", "-", "Data belum cukup"])
        story.append(_tabel(["Kode","Awal","Akhir","Selisih"], rows, [3*cm,3*cm,3*cm,7.2*cm]))
        story.append(Spacer(1, 0.3*cm))

    story.append(Paragraph("Kendala dan Tindakan", st["sub2"]))
    story.append(Paragraph(
        "Kendala dicatat berdasarkan catatan pada kegiatan perawatan dan pengukuran. "
        "Bagian ini dapat dilengkapi manual oleh penyusun laporan.", st["body"]))
    story.append(PageBreak())

    # --- BAB VI ---
    story.append(Paragraph("BAB VI&nbsp;&nbsp;KESIMPULAN", st["bab"]))
    story.append(Paragraph(
        f"Laporan ini merangkum data yang tercatat pada aplikasi TOMAT GROW. Jumlah tanaman yang "
        f"diamati sebanyak {len(tlist)} tanaman. Rincian kondisi akhir setiap tanaman dapat dilihat "
        "pada tabel data tanaman. Kesimpulan menyeluruh disusun berdasarkan data yang tersedia; "
        "apabila data belum mencukupi, penyusun perlu melengkapi pengamatan terlebih dahulu.", st["body"]))
    story.append(PageBreak())

    # --- LAMPIRAN ---
    if jenis.get("lampiran", True):
        story.append(Paragraph("LAMPIRAN", st["bab"]))
        story.append(Paragraph("Lampiran 1 - Tabel Data Pengukuran Lengkap", st["sub2"]))
        for t in tlist:
            rows_p = pmap.get(t.get("id"), [])
            if not rows_p: continue
            story.append(Paragraph(f"Tanaman {t.get('kode_tanaman')}", st["kecil"]))
            rows = [[r.get("tanggal"), _n(r.get("tinggi_cm")), _n(r.get("jumlah_daun")),
                     _n(r.get("jumlah_cabang")), _n(r.get("diameter_batang_mm")),
                     _n(r.get("jumlah_bunga")), _n(r.get("jumlah_buah"))] for r in rows_p]
            story.append(_tabel(["Tanggal","Tinggi","Daun","Cabang","Ø Batang","Bunga","Buah"],
                                rows, [2.7*cm,2.2*cm,1.8*cm,2.0*cm,2.5*cm,1.8*cm,1.8*cm]))
            story.append(Spacer(1, 0.35*cm))

        story.append(Spacer(1, 0.5*cm))
        story.append(Paragraph("Lampiran 2 - Riwayat Kegiatan Perawatan", st["sub2"]))
        all_r = []
        for t in tlist:
            for r in rmap.get(t.get("id"), []):
                all_r.append((r.get("tanggal"), t.get("kode_tanaman"), r.get("jenis_kegiatan"),
                              r.get("petugas"), _short(r.get("keterangan"))))
        all_r.sort(key=lambda x: x[0] or "")
        if all_r:
            story.append(_tabel(["Tanggal","Kode","Jenis","Petugas","Keterangan"],
                                [list(x) for x in all_r],
                                [2.4*cm,2.0*cm,3.2*cm,3.0*cm,5.6*cm]))
        else:
            story.append(Paragraph("Belum ada riwayat kegiatan.", st["kecil"]))

    buf = BytesIO()
    doc = BaseDocTemplate(buf, pagesize=A4, leftMargin=2.5*cm, rightMargin=2.5*cm,
                          topMargin=2.5*cm, bottomMargin=2.2*cm,
                          title=meta.get("judul") or "Laporan TOMAT GROW",
                          author=meta.get("dibuat_oleh") or "TOMAT GROW")
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="normal")
    doc.addPageTemplates([PageTemplate(id="utama", frames=[frame])])
    doc.build(story, canvasmaker=NumberedCanvas)
    buf.seek(0)
    return buf
