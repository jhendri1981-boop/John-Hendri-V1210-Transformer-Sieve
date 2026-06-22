# ==============================================================================
#      SKRIP LAB GENERATOR: JOHN & GEMINI DUMMY FACTORY GENERATOR (V110)
#   TARGET EXECUTION: GENERATING CUSTOM-DIGIT RSA LOCKS FOR STEP-BY-STEP TESTING
# ==============================================================================
import sys
import time
import random

sys.set_int_max_str_digits(30000)

print("=== GERBANG DATA PIPELINE V110: RSA DUMMY ENVELOPE FACTORY ===")
waktu_mulai = time.time()

def is_prime_miller_rabin(n, k=5):
    # Algoritma uji keprimaan Miller-Rabin tingkat sirkuit register hardware
    if n < 2: return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        if n == p: return True
        if n % p == 0: return False
    s, d = 0, n - 1
    while d % 2 == 0:
        s += 1
        d //= 2
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1: continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1: break
        else: return False
    return True

def generate_prime_by_digit(digits):
    # Memaksa generator melahirkan bilangan prima ganjil eksak sesuai panjang digit John
    lower_bound = 10**(digits - 1)
    upper_bound = (10**digits) - 1
    while True:
        p_candidate = random.randint(lower_bound, upper_bound)
        if p_candidate % 2 == 0: p_candidate += 1
        # Syarat Barikade 4 Pilar John: Singkirkan angka ekor 5 dan kelipatan 3 dari hulu!
        if p_candidate % 10 == 5 or p_candidate % 3 == 0: continue
        if is_prime_miller_rabin(p_candidate):
            return p_candidate

# 🪐 💥 INPUT UTAMA JOHN: Silakan tentukan panjang digit faktor prima P dan Q
# Misalkan untuk membuat gembok ~10 Digit, setel panjang_digit_faktor = 5
# Misalkan untuk membuat gembok ~16 Digit, setel panjang_digit_faktor = 8
# Misalkan untuk membuat gembok ~100 Digit (D100), setel panjang_digit_faktor = 50
TARGET_DIGIT_FAKTOR_P_Q = 18

print(f"📡 Request Order Received  : Membuat Kunci P dan Q masing-masing {TARGET_DIGIT_FAKTOR_P_Q}-Digit")
print(f"🚀 Memutar mesin generator kuantum di RAM... Memburu atom prima sejati...")
print("-" * 115)

# Melahirkan sepasang atom prima sejati bebas dari derau ekor 5 dan kelipatan 3 John
true_p = generate_prime_by_digit(TARGET_DIGIT_FAKTOR_P_Q)
true_q = generate_prime_by_digit(TARGET_DIGIT_FAKTOR_P_Q)

# Menjamin P dan Q tidak kembar identik agar tidak merusak topografi kurva
while true_p == true_q:
    true_q = generate_prime_by_digit(TARGET_DIGIT_FAKTOR_P_Q)

# Mengawinkan sepasang atom prima melahirkan gembok induk N Semiprime murni
N_DUMMY = true_p * true_q

def hitung_dr(n):
    sisa = n % 9
    return 9 if sisa == 0 else sisa

print(f"🏆 BERHASIL! GEMBOK DUMMY BERHASIL DIPAHAT SEMPURNA DI MEMORI CPU:")
print("=========================================================================================")
print(f"🔥 INDUK GEMBOK (N) DUMMY  : {N_DUMMY} ({len(str(N_DUMMY))} Digit Desimal)")
print(f"🔥 SIDIK JARI DIGITAL ROOT : DR(N) = {hitung_dr(N_DUMMY)}")
print(f"🔥 TRUE FACTOR PRIMA (P)   : {true_p}")
print(f"🔥 TRUE FACTOR PRIMA (Q)   : {true_q}")
print("=========================================================================================")

# Menyimpan log draf kunci ke berkas folder kerja John
with open("jurnal_gembok_dummy_v110.txt", "w") as f_out:
    f_out.write(f"N_GEMBOK = {N_DUMMY}\nTRUE_P = {true_p}\nTRUE_Q = {true_q}\nDR_N = {hitung_dr(N_DUMMY)}\n")

print(f"🟢 BERKAS KUNCI RAHSIA DISEGEL DI: D:\\Prima\\jurnal_gembok_dummy_v110.txt")
print(f"⏱️  Total Durasi Fabrikasi Mesin V110: {time.time() - waktu_mulai:.4f} detik murni!")
