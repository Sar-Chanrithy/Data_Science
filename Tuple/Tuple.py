# ចាប់ផ្ដើមជាមួយ Tuple ដំបូង
names = ("Sok", "Sokha", "Chanda")

# ==========================================
# 1. ការបន្ថែម (Add)
# ==========================================

# 1.1 បន្ថែម "Vichet" ទៅខាងចុង ដោយប្រើ .append()
temp = list(names)
temp.append("Vichet")
names = tuple(temp)
print(names)
# លទ្ធផល: ('Sok', 'Sokha', 'Chanda', 'Vichet')

# 1.2 បន្ថែម ["Bora", "Dara"] ដោយប្រើ .extend()
temp = list(names)
temp.extend(["Bora", "Dara"])
names = tuple(temp)
print(names)
# លទ្ធផល: ('Sok', 'Sokha', 'Chanda', 'Vichet', 'Bora', 'Dara')

# 1.3 បញ្ចូល "Vireak" នៅ index 1 ដោយប្រើ .insert()
temp = list(names)
temp.insert(1, "Vireak")
names = tuple(temp)
print(names)
# លទ្ធផល: ('Sok', 'Vireak', 'Sokha', 'Chanda', 'Vichet', 'Bora', 'Dara')


# ==========================================
# 2. ការលុប (Remove)
# ==========================================

# 2.1 លុប "Sok" ដោយប្រើ .remove()
temp = list(names)
temp.remove("Sok")
names = tuple(temp)
print(names)
# លទ្ធផល: ('Vireak', 'Sokha', 'Chanda', 'Vichet', 'Bora', 'Dara')

# 2.2 លុបធាតុចុងក្រោយទុកក្នុង last_name ដោយប្រើ .pop()
temp = list(names)
last_name = temp.pop()
names = tuple(temp)
print(names)
print(last_name)
# លទ្ធផល: ('Vireak', 'Sokha', 'Chanda', 'Vichet', 'Bora') និង Dara

# 2.3 លុបធាតុនៅ index 0 ដោយប្រើ .pop(0)
temp = list(names)
temp.pop(0)
names = tuple(temp)
print(names)
# លទ្ធផល: ('Sokha', 'Chanda', 'Vichet', 'Bora')


# ==========================================
# 3. ការរៀបលំដាប់ (Reorder)
# ==========================================

# 3.1 តម្រៀបតាមលំដាប់អក្សរ (A-Z) ដោយប្រើ .sort()
temp = list(names)
temp.sort()
names = tuple(temp)
print(names)
# លទ្ធផល: ('Bora', 'Chanda', 'Sokha', 'Vichet')

# 3.2 ត្រឡប់លំដាប់ពីក្រោយមកមុខវិញ ដោយប្រើ .reverse()
temp = list(names)
temp.reverse()
names = tuple(temp)
print(names)
# លទ្ធផល: ('Vichet', 'Sokha', 'Chanda', 'Bora')