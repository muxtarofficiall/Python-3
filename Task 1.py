# Hədəf rəqəm
target = 13


# Cəhdlərin sayını saxlamaq üçün dəyişən
attempt_count = 0

# İstifadəçinin rəqəmi tapana qədər input almaq üçün while dövrü
while True:
    # İstifadəçidən rəqəm daxil etməsini istəyin
    user_input = int(input("Bir rəqəm daxil edin: "))
    
    # Cəhdləri saymaq üçün sayğacı artırın
    attempt_count += 1
    if (attempt_count) >=10 :
        print("Cehdlerin limitin asmisiniz")
    # Əgər daxil edilən rəqəm hədəfə bərabərdirsə, dövrü dayandırın
    if user_input == target:
        break

# Hədəfi tapdıqdan sonra təbrik mesajı çap edin
print(f"Təbriklər! {attempt_count} cəhddə 13 rəqəmini tapdınız.")
