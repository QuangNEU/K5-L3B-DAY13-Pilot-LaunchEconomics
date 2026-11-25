"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from statistics import NormalDist
import pandas as pd
from statsmodels.stats.proportion import proportion_effectsize
from statsmodels.stats.power import NormalIndPower

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CHI_PHI_CO_DINH = 40_000_000  # đồng / tháng (giả định của lab)
SO_YEU_CAU_THANG = 45_000     # yêu cầu hoàn phí / tháng ở quy mô đầy đủ


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, chay_lai, xem_lai, lam_lai, tong, thanh_cong, cps, hoa_don_moi_yc.
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × luong_phut. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    chay_lai = (tien_token + tien_tool)[runs['attempt'] > 1].sum()
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    return {
        'token': tien_token.sum(),
        'tool': tien_tool.sum(),
        'chay_lai': chay_lai,
        'xem_lai': xem_lai,
        'lam_lai': lam_lai,
        'tong': tong,
        'thanh_cong': thanh_cong,
        'cps': tong / thanh_cong,
        'hoa_don_moi_yc': (tien_token.sum() + tien_tool.sum()) / len(reqs),
    }


def in_ket_qua_cp1(runs, reqs):
    """In đầy đủ các bảng kết quả của CP1 (A1, A2, A3, A4)."""
    print('\n=== A1 · Ba phép thử đáp án biết trước (p = 0,8) ===')
    print(f'Tối đa 2 lần chạy       : {so_lan_chay_ky_vong(0.8, 2):.2f}')
    print(f'Chạy đến khi đúng       : {so_lan_chay_ky_vong(0.8):.2f}')
    print(f'Hệ số chi phí, tối đa 3 : {he_so_chi_phi_moi_viec_thanh_cong(0.8, 3):.2f}')

    print('\n=== A2 · Mô hình chi phí từ trace (toàn bộ 1.200 yêu cầu) ===')
    kq = mo_hinh(runs, reqs)
    tong_tool_calls = int(runs['tool_calls'].sum())
    phut_xem_lai = reqs['phut_xem_lai_simulated'].sum()
    phut_lam_lai = reqs['phut_lam_lai_simulated'].sum()
    print(f"{'token':16s} {kq['token']:>14,.0f} đ  [đo từ trace]")
    print(f"{'tool':16s} {kq['tool']:>14,.0f} đ  [đo từ trace, {tong_tool_calls:,} lần gọi]")
    print(f"{'chay_lai (2&3)':16s} {kq['chay_lai']:>14,.0f} đ  [đo từ trace]")
    print(f"{'xem_lai':16s} {kq['xem_lai']:>14,.0f} đ  [simulated, {phut_xem_lai:,.0f} phút]")
    print(f"{'lam_lai':16s} {kq['lam_lai']:>14,.0f} đ  [simulated, {phut_lam_lai:,.0f} phút]")
    print(f"{'tong':16s} {kq['tong']:>14,.0f} đ  [có phần simulated]")
    print(f"{'thanh_cong':16s} {kq['thanh_cong']:>14,d} việc")
    print(f"{'cps':16s} {kq['cps']:>14,.0f} đ  [simulated]")
    print(f"{'hoa_don_moi_yc':16s} {kq['hoa_don_moi_yc']:>14,.1f} đ  [đo từ trace]")

    gap_lan = kq['cps'] / kq['hoa_don_moi_yc']
    ty_trong_xem = kq['xem_lai'] / kq['tong'] * 100
    ty_trong_lam = kq['lam_lai'] / kq['tong'] * 100
    ty_trong_nv = (kq['xem_lai'] + kq['lam_lai']) / kq['tong'] * 100
    khong_tc = len(reqs) - kq['thanh_cong']
    chi_phi_he_thong_moi_yc = (kq['tong'] + khong_tc * BASELINE) / len(reqs)
    print(f'CPS / hóa đơn mỗi yêu cầu           : {gap_lan:.1f}x')
    print(f'Tỉ trọng làm lại / xem lại / giờ NV : {ty_trong_lam:.1f}% / {ty_trong_xem:.1f}% / {ty_trong_nv:.1f}% [simulated]')
    print(f'Chi phí cả hệ thống / yêu cầu       : {chi_phi_he_thong_moi_yc:,.0f} đ ({chi_phi_he_thong_moi_yc / BASELINE:.2f}x của 12.000 đ) [simulated]')

    print('\n=== A3 · Tách theo loại yêu cầu ===')
    print(f"{'Loại':12s} {'Số YC':>7s} {'Thành công':>11s} {'Lần/YC':>8s} {'CPS [sim]':>12s} {'So 12k':>8s}")
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        sub = reqs[reqs['loai'] == loai]
        r = mo_hinh(runs, sub)
        tl_tc = r['thanh_cong'] / len(sub) * 100
        lan_yc = sub['so_lan_chay'].mean()
        print(f"{loai:12s} {len(sub):>7,d} {tl_tc:>10.1f}% {lan_yc:>8.2f} {r['cps']:>11,.0f} đ {r['cps'] / BASELINE:>7.2f}x")

    print('\n--- A3 · Tỉ lệ status == ok theo loại và lần thử (attempt) ---')
    merged = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    merged['is_ok'] = (merged['status'] == 'ok').astype(float)
    piv = merged.pivot_table(index='loai', columns='attempt', values='is_ok', aggfunc='mean') * 100
    piv = piv.reindex(['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac'])
    print(piv.to_string(float_format=lambda x: f'{x:5.1f}%'))

    print('\n=== A4 · Chi phí cố định (phạm vi noi_dia + hang_nang) ===')
    sub_pilot = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    r_pilot = mo_hinh(runs, sub_pilot)
    ty_le_tc_mau = r_pilot['thanh_cong'] / len(reqs)
    print(f"Trong mẫu: {r_pilot['thanh_cong']}/{len(reqs)} việc thành công, tổng biến đổi = {r_pilot['tong']:,.0f} đ, CPS biến đổi = {r_pilot['cps']:,.0f} đ [simulated]")
    print(f"{'Khối lượng':24s} {'Việc TC/tháng':>14s} {'Cố định/việc':>14s} {'CPS+CĐ [sim]':>14s} {'So 12k':>8s}")
    for nhan, kl in [('45.000 yêu cầu/tháng', SO_YEU_CAU_THANG), ('Một nửa khối lượng', SO_YEU_CAU_THANG / 2)]:
        viec_thang = kl * ty_le_tc_mau
        co_dinh_viec = CHI_PHI_CO_DINH / viec_thang
        tong_cps = r_pilot['cps'] + co_dinh_viec
        print(f'{nhan:24s} {viec_thang:>14,.0f} {co_dinh_viec:>13,.0f} đ {tong_cps:>13,.0f} đ {tong_cps / BASELINE:>7.2f}x')


def in_ket_qua_cp2(runs, reqs):
    """In đầy đủ các bảng kết quả của CP2 (B1, B2, B3, B4)."""
    print('\n=== B1 · Bảng độ nhạy (đổi từng yếu tố) ===')
    goc = mo_hinh(runs, reqs)['cps']
    kich_ban = {
        'Giá token gấp đôi':          dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa':     dict(gia_vao=13, gia_ra=65),
        'Tỉ lệ xem lại gấp đôi':      dict(he_so_xem_lai=2),
        'Tỉ lệ xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Số ca làm lại gấp đôi':      dict(he_so_lam_lai=2),
        'Số ca làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương nhân viên tăng 25%':   dict(luong_phut=2500),
        'Chỉ cho chạy tối đa 2 lần':  dict(max_lan_chay=2),
        'Chỉ cho chạy 1 lần':         dict(max_lan_chay=1),
    }
    print(f"{'Kịch bản':28s} {'CPS [sim]':>12s} {'Thay đổi':>10s}")
    print(f"{'Gốc (A2)':28s} {goc:>10,.0f} đ {'0.0%':>10s}")
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        print(f'{ten:28s} {cps:>10,.0f} đ {(cps / goc - 1) * 100:>+9.1f}%')

    print('\n=== B2 · Đổi một cặp và xếp hạng ===')
    cps_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    print(f'Token x2 + Xem lại x2 : {cps_cap:,.0f} đ ({(cps_cap / goc - 1) * 100:+.1f}%) [simulated]')
    print('Xếp hạng 3 yếu tố mạnh nhất: 1. Số ca làm lại · 2. Tỉ lệ xem lại · 3. Lương nhân viên')

    print('\n=== B3 · Giới hạn chạy lại và chi phí cả hệ thống ===')
    print(f"{'Giới hạn':10s} {'Tổng trợ lý [sim]':>18s} {'Không TC':>10s} {'Cả hệ thống [sim]':>18s} {'CPS [sim]':>12s}")
    for k in (1, 2, 3):
        r = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_tc = len(reqs) - r['thanh_cong']
        ca_he_thong = r['tong'] + khong_tc * BASELINE
        print(f"{f'{k} lần':10s} {r['tong']:>16,.0f} đ {khong_tc:>10,d} {ca_he_thong:>16,.0f} đ {r['cps']:>10,.0f} đ")

    print('\n=== B4 · Xem lại 100% (phạm vi noi_dia + hang_nang) ===')
    sub_pilot = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    runs_pilot = runs[runs['request_id'].isin(sub_pilot['request_id'])]
    r_pilot = mo_hinh(runs, sub_pilot)
    so_yc_co_ok = int(runs_pilot.loc[runs_pilot['status'] == 'ok', 'request_id'].nunique())
    so_ca_lam_lai = int((sub_pilot['ket_qua'] == 'lam_lai').sum())
    so_tc_pilot = r_pilot['thanh_cong']
    token_tool_pilot = r_pilot['token'] + r_pilot['tool']
    phut_ll_tb = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    phut_ll_tv = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].median()
    print(f'Số YC trong phạm vi: {len(sub_pilot)}, có ít nhất 1 lần ok: {so_yc_co_ok}, ca làm lại: {so_ca_lam_lai}, thành công: {so_tc_pilot}')
    print(f'Token + tool phạm vi: {token_tool_pilot:,.0f} đ; phút làm lại simulated TB toàn bộ: {phut_ll_tb:.2f} phút (trung vị {phut_ll_tv:.1f})')
    for nhan, phut_ll in [('Giả định đề (9 phút/ca)', 9.0), (f'Thực tế dữ liệu ({phut_ll_tb:.1f} phút/ca)', phut_ll_tb)]:
        tien_xem = so_yc_co_ok * 5 * LUONG_PHUT
        tien_ll = so_ca_lam_lai * phut_ll * LUONG_PHUT
        tong_100 = token_tool_pilot + tien_xem + tien_ll
        cps_100 = tong_100 / so_tc_pilot
        phut_xem_hoa_von = (BASELINE * so_tc_pilot - token_tool_pilot - tien_ll) / (so_yc_co_ok * LUONG_PHUT)
        print(f'  {nhan:34s}: tổng = {tong_100:>10,.0f} đ → CPS = {cps_100:,.0f} đ ({cps_100 / BASELINE:.2f}x) [sim] | hoà vốn xem lại ≤ {phut_xem_hoa_von:.1f} phút')


# ---------- Nhiệm vụ D1 · Cỡ mẫu và thiết kế pilot ----------
def co_mau(p1, p2, alpha=0.05, power=0.80):
    """Cỡ mẫu mỗi nhóm khi so hai tỉ lệ (kiểm định hai phía)."""
    za = NormalDist().inv_cdf(1 - alpha / 2)
    zb = NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    n = (za * math.sqrt(2 * pb * (1 - pb)) + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2
    return math.ceil(n)


def in_ket_qua_cp4(runs, reqs):
    """In kết quả D1 (cỡ mẫu, hệ số thiết kế, power thực tế) và tỉ lệ mở lại hiện tại."""
    print('\n=== D1 · Cỡ mẫu pilot (baseline 0,70; alpha 0,05; power 0,80; ICC 0,02) ===')
    p1, alpha, power, icc = 0.70, 0.05, 0.80, 0.02
    n_5pt = co_mau(p1, 0.75, alpha, power)
    de_75 = 1 + (75 - 1) * icc
    n_nv_75 = math.ceil(n_5pt * de_75)
    so_nv_nhom = math.ceil(n_nv_75 / 75)
    tran_20_nv = 20 / icc
    tran_6_depot = 6 / icc
    n_6pt = co_mau(p1, 0.76, alpha, power)
    m_min_6pt = math.ceil(n_6pt * (1 - icc) / (20 - n_6pt * icc))
    de_6pt = 1 + (m_min_6pt - 1) * icc
    es_5pt = proportion_effectsize(0.70, 0.75)
    power_5pt_o_n859 = NormalIndPower().power(effect_size=es_5pt, nobs1=n_6pt, alpha=alpha, ratio=1.0)

    print(f'a) Chia theo yêu cầu (+5 điểm)           : {n_5pt:,d} yêu cầu / nhóm')
    print(f'b) Theo nhân viên, m = 75                : DE = {de_75:.2f} → {n_nv_75:,d} yc/nhóm → {so_nv_nhom} NV/nhóm ({so_nv_nhom * 2} > 40: không đủ người)')
    print(f'c) 20 nhân viên mỗi nhóm                 : trần c/ICC = {tran_20_nv:,.0f} < {n_5pt:,d} (không đạt +5 điểm)')
    print(f'd) 6 depot mỗi nhóm                      : trần c/ICC = {tran_6_depot:,.0f} < {n_5pt:,d} (loại, dưới 20 cụm/nhóm)')
    print(f'e) Mức chênh 6 điểm ({n_6pt:,d}/nhóm), 20 NV : m ≥ {m_min_6pt:,d} yêu cầu/nhân viên (DE = {de_6pt:.2f})')
    print(f'Đánh đổi (n={n_6pt}, tác động thật +5 điểm): power thực tế ≈ {power_5pt_o_n859:.2f}')

    sub_pilot = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    mo_lai_all = reqs['mo_lai_trong_7_ngay'].mean() * 100
    mo_lai_pilot = sub_pilot['mo_lai_trong_7_ngay'].mean() * 100
    print(f"Tỉ lệ mo_lai_trong_7_ngay hiện tại       : toàn mẫu {mo_lai_all:.2f}% ({int(reqs['mo_lai_trong_7_ngay'].sum())}/{len(reqs)}) | noi_dia+hang_nang {mo_lai_pilot:.2f}% ({int(sub_pilot['mo_lai_trong_7_ngay'].sum())}/{len(sub_pilot)})")


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    in_ket_qua_cp1(runs, reqs)
    in_ket_qua_cp2(runs, reqs)
    in_ket_qua_cp4(runs, reqs)
