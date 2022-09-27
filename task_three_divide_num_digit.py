# JAWHER ALKOTAIM

'''
Create a running Python project to check if all digits of a number divide it; given a
number n, find whether all digits of n divide it or not.
Input : 128
Output : Yes
128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
Input : 130
Output : No
'''

def divisible_by_its_numbers(num):
    try:
        return 'yes' if sum([num % int(i) for i in str(num)]) == 0 else 'no'
    except Exception as e:
        return 'no'


example = int(input('Input: '))
print(f'Output: {divisible_by_its_numbers(example)}')
