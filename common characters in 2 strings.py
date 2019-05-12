def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    # write your logic here
    count1=0
    count2=0
    count3=0
    list1=[]
    for i in range(1,len(patient_medical_speciality_list),2):
        if patient_medical_speciality_list[i]=='P':
            count1=count1+1
        elif patient_medical_speciality_list[i]=='O':
            count2=count2+1 
        else:
            count3=count3+1    
    list1.append(count2)
    list1.append(count1)
    list1.append(count3)
    l=max(list1)
    if l==count1:
        speciality="Pediatrics"
    elif l==count2:
        speciality="Orthopedics"
    else:
        speciality="ENT"
    return speciality

#provide different values in the list and test your program
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)
