# JAWHER ALKOTAIM

'''
Given a list of names, create a running Python project that sorts it alphabetically,
Python has this functionality built-in, but see if you can do it without using sort()!
Examples:
Input : [“d”,“b”,“a”,“c”,“f”,“h”,“g”,“e”]
Output : [“a”,“b”,“c”,“d”,“e”,“f”,“g”,“h”]
'''

def my_quick_sort(arr: list)->list:

    if len(arr) <= 1:  # To end recursion
        return arr

    pivot = arr.pop()
    grater_than_pivot = [i for i in arr if i > pivot]
    lower_than_pivot = [i for i in arr if i <= pivot]
    return my_quick_sort(lower_than_pivot) + [pivot] + my_quick_sort(grater_than_pivot)


example = []
while(True):
   item =  input('type any thing and click Enter to add one element to the list, or type "end" to get the output: ')
   if item.lower() == 'end':
       break
   example.append(item)

print(f'Output: {my_quick_sort(example)}')