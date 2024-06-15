Create a student dictionary  for n students with the student name as key and their test mark assignment mark and lab mark as values. Do the following computations and display the result.

1.Identify the student with the  highest average score

2.Identify the student who as the highest Assignment marks

3.Identify the student with the Lowest lab marks

4.Identify the student with the lowest average score

Note:

If more than one student has the same score display all the student names



Sample input:

4

James 67 89 56

Lalith 89 45 45

Ram 89 89 89

Sita 70 70 70

Sample Output:

Ram

James Ram

Lalith

Lalith

Code:
def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    n = int(data[0].strip())
    s = {}
    
    for i in range(1, n + 1):
        l = data[i].strip().split()
        name = l[0]
        t = int(l[1])
        a = int(l[2])
        lab = int(l[3])
        s[name] = (t, a, lab)
    
    high_avg = -1
    high_assign = -1
    low_lab = float('inf')
    low_avg = float('inf')
    
    high_avg_students = []
    high_assign_students = []
    low_lab_students = []
    low_avg_students = []
    
    for name, (t, a, lab) in s.items():
        avg = (t + a + lab) / 3
        
        if avg > high_avg:
            high_avg = avg
            high_avg_students = [name]
        elif avg == high_avg:
            high_avg_students.append(name)
            
        if a > high_assign:
            high_assign = a
            high_assign_students = [name]
        elif a == high_assign:
            high_assign_students.append(name)
        
        if lab < low_lab:
            low_lab = lab
            low_lab_students = [name]
        elif lab == low_lab:
            low_lab_students.append(name)
        
        if avg < low_avg:
            low_avg = avg
            low_avg_students = [name]
        elif avg == low_avg:
            low_avg_students.append(name)
    
    high_avg_students.sort()
    high_assign_students.sort()
    low_lab_students.sort()
    low_avg_students.sort()
    
    print(" ".join(high_avg_students))
    print(" ".join(high_assign_students))
    print(" ".join(low_lab_students))
    print(" ".join(low_avg_students))

main()
