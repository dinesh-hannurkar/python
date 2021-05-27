# total_student= AddStudent.objects.count()
total_student= 20
print("total student=",total_student)

# total_faculty= Addfaculty.objects.count()
total_faculty= 3
print("total total_faculty=",total_faculty)

# if request.method=='POST':
if total_faculty > total_student:
    print('students are less that faculties. so try to add more student or delete faculty')
else:
    total_student_each_faculty=total_student/total_faculty
    print("total_student_each_faculty",int(total_student_each_faculty))

    first_class=[]
    second_class=[]
    third_class=[]
    tmp_list=[]
    faculty_ids=[3,4,2]
    extra_stud_list=[]
        

        # get_student_data=AddStudent.objects.order_by('-created_date')
        # get_faculty_data=Addfaculty.objects.order_by('-created_date')

        # for data in get_faculty_data:
        #     faculty_ids.append(data.id)
        
        # print("faculty id=",faculty_ids)


        # for data in get_student_data:
        #     if data.stud_cgpa < 5.5:
        #         third_class.append(data.id)
        #     elif data.stud_cgpa < 8.0:
        #         second_class.append(data.id)
        #     elif data.stud_cgpa < 10.0:
        #         first_class.append(data.id)

    first_class=[7,5,1,44,21,5]
    second_class=[8,6,4,6,6]
    third_class=[3,2,4,75,68,12,7,45,4]
    final_list=first_class+third_class+second_class

    # print("first class student =",first_class)
    # print("second class student =",second_class)
    # print("3rd class student =",third_class)
    # print("final class student =",final_list)
    

    # print("length first class student =",len(first_class))
    # print(" length second class student =",len(second_class))
    # print(" length 3rd class student =",len(third_class))

    f_class_length=len(first_class)
    s_class_length=len(second_class)
    t_class_length=len(third_class)
    # print("length=",len(final_list))

    xyz=[f_class_length,s_class_length,t_class_length]
    
    xyz.sort()
    max=xyz[-1]
    print("max==",max)

    if f_class_length != max:
        for value in range(max-f_class_length):
            first_class.append(0)
    
    if s_class_length != max:
        for value in range(max-s_class_length):
            second_class.append(0)

    if t_class_length != max:
        for value in range(max-t_class_length):
            third_class.append(0)

    print("first class student =",first_class)
    print("second class student =",second_class)
    print("3rd class student =",third_class)
    print("*********************")


    while max > 0:
        # print("maxxxxxxxxxx=",max)
        # print("first class student =",first_class)
        # print("second class student =",second_class)
        # print("3rd class student =",third_class)

        if first_class[0]==0 and second_class[0]==0 and third_class[0]==0:
            # print("yes",max)
            first_class.remove(first_class[0])
            second_class.remove(second_class[0])
            third_class.remove(third_class[0])

            max=max-1

        elif max==1:
            # print("yes")
            print(third_class)
            if first_class[0]!=0:
                extra_stud_list.append(first_class[0])
            if second_class[0]!=0:
                extra_stud_list.append(second_class[0])
            if third_class[0]!=0:
                extra_stud_list.append(third_class[0])

            for i in range(len(extra_stud_list)):
                stud_id=extra_stud_list[i]
                
                print("A",fac_id,"=",stud_id)
            max=max-1
        elif max >= 2:
            if first_class[0] == 0:
                if second_class[1]==0:
                    if third_class[1]==0:
                        print("first class no student")
                        ###################################
                        # print("first class student =",first_class)
                        # print("second class student =",second_class)
                        # print("3rd class student =",third_class)
                    else:
                        first_class[0]=third_class[1]
                        third_class.remove(third_class[1])
                        third_class.append(0)
                else:
                    # print("Yes")
                    first_class[0]=second_class[1]
                    second_class.remove(second_class[1])
                    second_class.append(0)
                    
            elif second_class[0]==0:
                if third_class[1]==0:
                    if first_class[1]==0:
                        print("Second class no student")
                    else:
                        second_class[0]=first_class[1]
                        first_class.remove(first_class[1])
                        first_class.append(0)
                        
                else:
                    second_class[0]=third_class[1]
                    third_class.remove(third_class[1])
                    third_class.append(0)
            elif third_class[0]==0:
                if second_class[1]==0:
                    if first_class[1]==0:
                        print("Third class no student")
                    else:
                        third_class[0]=first_class[1]
                        first_class.remove(first_class[1])
                        first_class.append(0)
                else:
                    third_class[0]=second_class[1]
                    second_class.remove(second_class[1])
                    second_class.append(0)

            if first_class[0]==0 or second_class[0]==0 or third_class[0]==0:
                if first_class[0]!=0:    
                    tmp_list.append(first_class[0])
                if second_class[0]!=0:
                    tmp_list.append(second_class[0])
                if third_class[0]!=0:
                    tmp_list.append(third_class[0])

                first_class.remove(first_class[0])
                second_class.remove(second_class[0])
                third_class.remove(third_class[0])
                max=max-1
                tmp_list_len=len(tmp_list)
                # print(int(total_student_each_faculty))
                if tmp_list_len >= int(total_student_each_faculty):
                    # print("Tmp list ====",tmp_list)
                    
                 # print("tmp list ====",tmp_list)
                    #datbase insert
                    if len(faculty_ids)>=1:
                        fac_id=faculty_ids[0]
                        faculty_ids.remove(faculty_ids[0])

                    for i in range(int(total_student_each_faculty)):
                        # print("iiiiiiiiiiiiii",i)
                        
                        stud_id=tmp_list[0]
                        tmp_list.remove(tmp_list[0])


                        print("C",fac_id,"=",stud_id)
                else:
                    # print(int(total_student_each_faculty))
                    # print(len(tmp_list))
                    for i in range(len(tmp_list)):
                        # print("iiiiiiiiiiiiii",i)
                        stud_id=tmp_list[0]
                        tmp_list.remove(tmp_list[0])
                        print("B",fac_id,"=",stud_id)

                    first_class.remove(first_class[0])
                    second_class.remove(second_class[0])
                    third_class.remove(third_class[0])
                    max=max-1
            else:
                tmp_list.append(first_class[0])
                tmp_list.append(second_class[0])
                tmp_list.append(third_class[0])

                # print("Adding to list",tmp_list)
                first_class.remove(first_class[0])
                second_class.remove(second_class[0])
                third_class.remove(third_class[0])
                max=max-1

                tmp_list_len=len(tmp_list)
                # print(int(total_student_each_faculty))
                if tmp_list_len >= int(total_student_each_faculty):
                    # print("Tmp list ====",tmp_list)
                    
                # print("tmp list ====",tmp_list)
                    #datbase insert
                    if len(faculty_ids)>=1:
                        fac_id=faculty_ids[0]
                        faculty_ids.remove(faculty_ids[0])

                    for i in range(int(total_student_each_faculty)):
                        # print("iiiiiiiiiiiiii",i) 
                        stud_id=tmp_list[0]
                        tmp_list.remove(tmp_list[0])
                        print("C",fac_id,"=",stud_id)

            f_cls_len=len(first_class)
            s_cls_len=len(second_class)
            t_cls_len=len(third_class)
            
        else:
            print(tmp_list)
            tmp_list.append(first_class[0])
            tmp_list.append(second_class[0])
            tmp_list.append(third_class[0])

            first_class.remove(first_class[0])
            second_class.remove(second_class[0])
            third_class.remove(third_class[0])
            max=max-1

            tmp_list_len=len(tmp_list)
            if tmp_list_len >= total_student_each_faculty:
                print("tmp list ====",tmp_list)
            # print("tmp list ====",tmp_list)
                #datbase insert
                if len(faculty_ids)>=1:
                    fac_id=faculty_ids[0]
                    faculty_ids.remove(faculty_ids[0])
                for i in range(int(total_student_each_faculty)):
                    # print("iiiiiiiiiiiiii",i)
                    stud_id=tmp_list[0]
                    tmp_list.remove(tmp_list[0])
                    print("D",fac_id,"=",stud_id)

            f_cls_len=len(first_class)
            s_cls_len=len(second_class)
            t_cls_len=len(third_class)

            # print("flrn=",f_cls_len)
            # print("slrn=",s_cls_len)
            # print("tlrn=",t_cls_len)
            if f_cls_len==1:
                if first_class[0]!=0:
                    extra_stud_list.append(first_class[0])
                if second_class[0]!=0:
                    extra_stud_list.append(second_class[0])
                if third_class[0]!=0:
                    extra_stud_list.append(third_class[0])

                for i in range(len(extra_stud_list)):
                    stud_id=extra_stud_list[i]
                    
                    print("E",fac_id,"=",stud_id)
                max=max-1
            