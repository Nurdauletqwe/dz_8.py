'''1'''

# def insertion_sort(num_list):
#     for i in range(1, len(num_list)):
#         a = num_list[i]
#         pos = i
#         while pos > 0 and num_list[pos - 1] > a:
#             num_list[pos] = num_list[pos - 1]
#             pos -= 1
#         num_list[pos] = a


# arr = [1, 4, 2, 3, 4]
# insertion_sort(arr)
# print(arr)

'''2'''


# def find_closest_numbers(nums):
#     nums.sort()
#     closest_pair = [nums[0], nums[1]]
#     min_difference = abs(nums[1] - nums[0])

#     for i in range(1, len(nums) - 1):
#         difference = abs(nums[i+1] - nums[i])
#         if difference < min_difference:
#             min_difference = difference
#             closest_pair = [nums[i], nums[i+1]]

#     return closest_pair


# input_nums = [9, 4, 1, 6]

# result = find_closest_numbers(input_nums)
# print(''.join(map(str, result)))

''''3'''

# import re
# def extract_domains(emails):
#     domains = set()
#     for email in emails:
#         domain = re.search(r'@(\w+\.\w+)', email)
#         if domain:
#             domains.add(domain.group(1))
#     return list(domains)


# # Пример использования:
# emails = ["itstep@gmail.com", "stepit@email.com", "shag@mail.com"]
# domains = extract_domains(emails)
# print(domains)

'''4'''

# import re
# def extract_vowel_words(sentence):
#     vowel_words = re.findall(r'\b[aeiouAEIOU]\w+', sentence)
#     return vowel_words


# sentence = "Messi in 2022 he helped Argentina win the Fédération Internationale de Football Association (FIFA)s World Cup."
# vowel_words = extract_vowel_words(sentence)
# print(vowel_words)
