import numpy as np
import matplotlib.pyplot as plt

def harmonic_mean(values):
    n = len(values)
    sum_reciprocal = sum(1 / value for value in values)
    return n / sum_reciprocal

def geometric_mean(values):
    product = np.prod(values)
    return product ** (1/len(values))

# القيم في المجموعة
values = [3, 4, 6]

# حساب المتوسطات المختلفة
arithmetic_mean = np.mean(values)
geometric_mean_value = geometric_mean(values)
harmonic_mean_value = harmonic_mean(values)

# طباعة المتوسطات
print("المتوسط الحسابي:", arithmetic_mean)
print("المتوسط الهندسي:", geometric_mean_value)
print("المتوسط التوافقي:", harmonic_mean_value)

# إنشاء الرسم البياني
means = [arithmetic_mean, geometric_mean_value, harmonic_mean_value]
mean_names = ['المتوسط الحسابي', 'المتوسط الهندسي', 'المتوسط التوافقي']

plt.figure(figsize=(10, 6))
plt.bar(mean_names, means, color=['blue', 'green', 'red'])
plt.title('مقارنة المتوسطات المختلفة')
plt.ylabel('القيمة')
plt.show()
