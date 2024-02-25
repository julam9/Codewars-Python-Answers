def solution(number):
    i = 1
    emp_arr = []
    while i < number:   
        if i % 3 == 0 or i % 5 == 0:
            emp_arr.append(i)
        i = i + 1
    return sum(emp_arr)

# testing
solution(5)