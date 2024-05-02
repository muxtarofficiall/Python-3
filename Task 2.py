# Sadə ədəd olub-olmadığını yoxlamaq üçün funksiya
def is_prime(num):
    if num <= 1:
        return False
    # 2-dən num-1-ə qədər olan ədədlərdən heç birinə bölünməməlidir
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# 1 ilə 100 arasında olan sadə ədədləri çap etmək üçün for döngəsi
print("1 ilə 100 arasında sadə ədədlər:")
for n in range(1, 101):
    if is_prime(n):
        print(n, end=' ')  # Sadə ədədləri bir sətirdə çap etmək üçün
