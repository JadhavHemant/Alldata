import mysql.connector
class Operations:
    host=""
    user=""
    pas=""
    db=""
    def __init__(self,h,u,p,d):
        self.host=h
        self.user=u
        self.pas=p
        self.db=d
    def Execute(self,type, r, n,e, m, s):
        con=mysql.connector.connect(host=self.host,user=self.user,password=self.pas,database=self.db)
        mycursor=con.cursor()
        if type=="Insert":
            mycursor.execute("insert into students(name,english,maths,science) values('"+n+"',"+str(e)+","+str(m)+","+str(s)+")")
            con.commit()
            return "Student Added Successfully"
        elif type=="Update":
            mycursor.execute("update  students set name='"+n+"', english="+str(e)+", maths="+str(m)+", science="+str(s)+" where rno="+str(r))
            con.commit()
            return "Student Updated Successfully"
        elif type=="Delete":
            mycursor.execute("delete from  students  where rno="+str(r))
            con.commit()
            return "Student Deleted Successfully"
        elif type=="FetchAll":
            mycursor.execute("select * from students")
            data=mycursor.fetchall()
            students=[]
            for d in data:
                st={"rno":d[0],"name":d[1],"english":d[2],"maths":d[3],"science":d[4]}
                students.append(st)
            return students
        elif type=="FetchByRno":
            mycursor.execute("select * from students where rno="+str(r))
            data=mycursor.fetchall()
            d=data[0]
            st={"rno":d[0],"name":d[1],"english":d[2],"maths":d[3],"science":d[4]}

            return st
            
            