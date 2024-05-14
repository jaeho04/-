import math

def gaussian_plume(Q, u, sigma_y, sigma_z, y, z, H):
    if Q <= 0 or u <= 0 or sigma_y <= 0 or sigma_z <= 0 or y <= 0 or z <= 0 or H <= 0:
        raise ValueError("입력 값은 양수여야 합니다.")

    C = Q / (2 * math.pi * u * sigma_y * sigma_z) * math.exp(-y ** 2 / (2 * sigma_y ** 2)) * math.exp(
        -(z - H) ** 2 / (2 * sigma_z ** 2))
    return C

def tnt_equivalent(W_substance, H_substance, H_TNT):
    if W_substance <= 0 or H_substance <= 0 or H_TNT <= 0:
        raise ValueError("입력 값은 양수여야 합니다.")

    W_TNT = W_substance * (H_substance / H_TNT)
    return W_TNT

def bleve_energy(eta, m, delta_H):
    if eta <= 0 or m <= 0 or delta_H <= 0:
        raise ValueError("입력 값은 양수여야 합니다.")

    E = eta * m * delta_H
    return E

def lfl_calculation(lel, vol_percent):
    if lel <= 0 or vol_percent <= 0:
        raise ValueError("입력 값은 양수여야 합니다.")

    LFL = (lel / 100) * vol_percent
    return LFL

def jet_flame_length(C, m, g, d, p, delta_H):
    if C <= 0 or m <= 0 or g <= 0 or d <= 0 or p <= 0 or delta_H <= 0:
        raise ValueError("입력 값은 양수여야 합니다.")

    L = C * ((m ** 2 * g * d ** 2) / (p * delta_H)) ** (1 / 3)
    return L

def main():
    print("안전공학용 계산기")
    print("1. 원추형 확산 모델 (Gaussian Plume Model)")
    print("2. TNT 등가량 계산")
    print("3. BLEVE 에너지 계산")
    print("4. 하한 폭발 한계 (LFL) 계산")
    print("5. 제트 화염 길이 계산")

    choice = int(input("원하는 계산을 선택하세요 (1-5): "))

    if choice == 1:
        Q = float(input("방출율 (Q) [kg/s]: "))
        u = float(input("풍속 (u) [m/s]: "))
        sigma_y = float(input("확산 계수 y (σy) [m]: "))
        sigma_z = float(input("확산 계수 z (σz) [m]: "))
        y = float(input("거리 y [m]: "))
        z = float(input("높이 z [m]: "))
        H = float(input("방출 높이 (H) [m]: "))

        try:
            print("원추형 확산 모델 결과 (농도) [kg/m^3]:", gaussian_plume(Q, u, sigma_y, sigma_z, y, z, H))
        except ValueError as e:
            print(e)

    elif choice == 2:
        W_substance = float(input("물질의 양 (W) [kg]: "))
        H_substance = float(input("물질의 에너지 (H) [J/kg]: "))
        H_TNT = float(input("TNT의 에너지 (H_TNT) [J/kg]: "))

        try:
            print("TNT 등가량 계산 결과 (TNT 등가량) [kg]:", tnt_equivalent(W_substance, H_substance, H_TNT))
        except ValueError as e:
            print(e)

    elif choice == 3:
        eta = float(input("효율 (η) [비율, 예: 0.7]: "))
        m = float(input("액체 질량 (m) [kg]: "))
        delta_H = float(input("증발 잠열 (ΔH) [J/kg]: "))

        try:
            print("BLEVE 에너지 계산 결과 (에너지) [J]:", bleve_energy(eta, m, delta_H))
        except ValueError as e:
            print(e)

    elif choice == 4:
        lel = float(input("하한 폭발 한계 (LEL) [%]: "))
        vol_percent = float(input("부피 백분율 (Vol%) [%]: "))

        # 입력 값 유효성 검사 및 에러 처리
        try:
            print("LFL 계산 결과 (LFL) [%]:", lfl_calculation(lel, vol_percent))
        except ValueError as e:
            print(e)

    elif choice == 5:
        C = float(input("상수 (C): "))
        m = float(input("질량 유속 (m) [kg/s]: "))
        g = float(input("중력 가속도 (g) [m/s^2]: "))
        d = float(input("배출 구경 (d) [m]: "))
        p = float(input("압력 (p) [Pa]: "))
        delta_H = float(input("연소 열 (ΔH) [J/kg]: "))

        try:
            print("제트 화염 길이 계산 결과 (길이) [m]:", jet_flame_length(C, m, g, d, p, delta_H))
        except ValueError as e:
            print(e)

    else:
        print("잘못된 선택입니다. 프로그램을 종료합니다.")

if __name__ == "__main__":
    main()