import sqlite3
conn=sqlite3.connect("TODO_LIST.db") # if not present it will create, if already present it will not
cur=conn.cursor()
conn.execute("CREATE TABLE IF NOT EXISTS USERDETAILS(ID INTEGER PRIMARY KEY AUTOINCREMENT, USERNAME TEXT NOT NULL, PASSWORD TEXT NOT NULL)")
task_table='''
CREATE TABLE IF NOT EXISTS TASK_SCHEDULE(
TID INTEGER PRIMARY KEY AUTOINCREMENT, 
UID INTEGER,
TITLE TEXT NOT NULL,
DESCRIPTION TEXT NOT NULL,
STATUS TEXT DEFAULT "Pending",
DUE_DATE TEXT,
PRIORITY TEXT,
FOREIGN KEY (UID) REFERENCES USERDETAILS(ID)
);
'''
conn.execute(task_table)
conn.commit()

def printing(task):
        print(f"\nTask ID     : {task[0]}")
        print(f"User ID     : {task[1]}")
        print(f"Title       : {task[2]}")
        print(f"Description : {task[3]}")
        print(f"Status      : {task[4]}")
        print(f"Due Date    : {task[5]}")
        print(f"Priority    : {task[6]}\n")


def add_task(uid):
      title=input("\nTitle: ")
      desc=input("Description: ")
      stat=input("Status: ")
      dued=input("Due Date: ")
      pr=input("Priority: ")
      cur.execute("INSERT INTO TASK_SCHEDULE(UID, TITLE, DESCRIPTION, STATUS, DUE_DATE, PRIORITY) VALUES(?,?,?,?,?,?)", (uid, title, desc, stat, dued, pr))
      conn.commit()
      print("Task added successfully!")

def rem_task(uid):
      try:
         tid=int(input("Task ID to remove: "))
      except ValueError:
           print("Invalid Task ID. Please enter a number")
           return
      cur.execute("SELECT * FROM TASK_SCHEDULE WHERE TID=? AND UID=?", (tid, uid))
      task=cur.fetchone()
      if task:
        cur.execute("DELETE FROM TASK_SCHEDULE WHERE TID=? AND UID=?", (tid, uid))
        conn.commit()
        print("Task removed successfully!")
      else:
        print("Task not found or does not belong to this user")

def upd_task(uid):
    try:
        tid = int(input("Task ID to update: "))
    except ValueError:
        print("Invalid Task ID. Please enter a number")
        return

    cur.execute("SELECT * FROM TASK_SCHEDULE WHERE TID=? AND UID=?", (tid, uid))
    task = cur.fetchone()
    if task:
        print("Current Task:", task)
        print("Update Options:\n1. Title\n2. Description\n3. Status\n4. Due-Date\n5. Priority\n")
        ty = input("Type: ")
        if ty == "1":
            title = input("Enter new title: ")
            cur.execute("UPDATE TASK_SCHEDULE SET TITLE=? WHERE TID=? AND UID=?", (title, tid, uid))
        elif ty == "2":
            desc = input("Enter new description: ")
            cur.execute("UPDATE TASK_SCHEDULE SET DESCRIPTION=? WHERE TID=? AND UID=?", (desc, tid, uid))
        elif ty == "3":
            status = input("Enter new status (Pending/Completed/In Progress): ")
            cur.execute("UPDATE TASK_SCHEDULE SET STATUS=? WHERE TID=? AND UID=?", (status, tid, uid))
        elif ty == "4":
            due_date = input("Enter new due date (e.g., YYYY-MM-DD): ")
            cur.execute("UPDATE TASK_SCHEDULE SET DUE_DATE=? WHERE TID=? AND UID=?", (due_date, tid, uid))
        elif ty == "5":
            priority = input("Enter new priority (High/Medium/Low): ")
            cur.execute("UPDATE TASK_SCHEDULE SET PRIORITY=? WHERE TID=? AND UID=?", (priority, tid, uid))
        else:
            print("Invalid option.")
            return
        conn.commit()
        print("Task updated successfully!")
        cur.execute("SELECT * FROM TASK_SCHEDULE WHERE TID=? AND UID=?", (tid, uid))
        res = cur.fetchone()
        printing(res)
    else:
        print("Task not found or does not belong to this user.")

def user_func():
    while True:
        print("\nTODO LIST MAKER")
        print("1. Register\n2. Sign-In\n3. Show details\n0. Exit\n")
        ch=input("Enter choice: ")
        if ch== "1": 
                    user_name=input("Username: ")
                    cur.execute("SELECT * FROM USERDETAILS WHERE USERNAME = ?", (user_name,))
                    if cur.fetchone():
                         print("Username already exists!")
                         continue
                    pas=input("Password: ")
                    cpas=input("Confirm Password: ")
                    if pas==cpas:
                        cur.execute("INSERT INTO USERDETAILS(USERNAME, PASSWORD) VALUES (?,?)", (user_name, pas))
                        conn.commit()
                        print("Registration successful!\n\n")
                    else:
                        print("Passwords are not matching. Try again")
        elif ch== "2":
                    user_name=input("Username: ")
                    pas=input("Password: ")
                    cur.execute("SELECT * FROM USERDETAILS WHERE USERNAME = ? AND PASSWORD = ?", (user_name, pas))
                    row=cur.fetchone()
                    if row:
                        uid=row[0]
                        print("Sign-In successful!\n")
                        print("User-Id: ", uid)
                        while True:
                         print("\nTask Operations:\n0. Show User Details\n1. Add Task\n2. Update Task\n3. Remove Task\n4. Logout\n")
                         op=input("Type: ")
                         if op=="1":
                             add_task(uid)
                         elif op=="2":
                              upd_task(uid)
                         elif op=="3":
                              rem_task(uid)
                         elif op=="4":
                              print("Logged out..")
                              break
                         elif op=="0":
                              print("\n(U_ID, 'Username', 'Password')")
                              cur.execute("SELECT * FROM USERDETAILS WHERE ID=?", (uid,))
                              result=cur.fetchone()
                              print(result)
                              cur.execute("SELECT * FROM TASK_SCHEDULE WHERE UID=?", (uid,))
                              re=cur.fetchall()
                              if re:
                                 print("\nTASKS")
                                 for task in re:
                                      printing(task)
                              else:
                                 print("\nNo tasks found.")
                         else:
                              print("Try again!")
                    else:
                        print("Invalid username or password!")
        elif ch=="0":
              print("Exiting program...\nCOMPLETED!")
              break
        elif ch=="3":
              print("a. User Details\nb. Task Schedule\n")
              inp=input("Choice: ").lower().strip()
              if inp =="a":
                  cur.execute("SELECT * FROM USERDETAILS")
                  result=cur.fetchall()
                  print(result)
              else:
                  cur.execute("SELECT * FROM TASK_SCHEDULE")
                  re=cur.fetchall()
                  if re:
                      print("\nALL TASKS")
                      for task in re:
                          printing(task)
                  else:
                      print("\nNo tasks found.")
        else:
              print("Invalid choice!!")

if __name__=="__main__":
    try:
        user_func()
    finally:
        conn.close()