# 5 rəqəmi bir siyahıya daxil edin
nums = []

# İstifadəçidən 5 rəqəm daxil etməsini istəyin
for i in range(5):
    num = int(input("Bir rəqəm daxil edin: "))
    nums.append(num)

# Siyahını sıralayın
nums.sort()

# Sıralanmış siyahını göstərin
print("Sıralanmış siyahı:", nums)
