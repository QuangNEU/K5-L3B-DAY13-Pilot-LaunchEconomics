"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

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


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    in_ket_qua_cp1(runs, reqs)
    # TODO CP2 · Nhiệm vụ B: đổi từng yếu tố, ghi vào bảng độ nhạy.
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
