#-----------------------------------------------------HOW TO USE-------------------------------------------------------

    #Press f5, to run this module, you will see the resources & the state of the tasks printed before every interrupt
    #The print statements are not part of the execution of the task. It is only placed to illustrate
    #how the shared resource is allowed to be used by 1 task at a time

#----------------------------------------------------------------------------------------------------------------------


#returns true if resource is available
#atomic
def acquire(semaphore):
    if(semaphore[0] == 1):
        semaphore[0] = 0
        return True
    else:
        return False


#releases the resource
#atomic
def release(semaphore):
    if(semaphore[0] == 0):     #calling task has to be within the critical region
        semaphore[0] = 1


#a task which takes in:
#resource, semaphore for that resource, boolean on whether it is chosen to run
#returns its ident when it is killed
def task1(x, semaphore, running):
    while(True):
        yield
        taskIdent = 1
        yield
        while(running):        
            print "Task 1, ------, s=", semaphore, " x=", x     #print not part of task itself. To show state
            yield
            if(acquire(semaphore) == True):                     #enter critical region if available, else block
                print "\n--------- LOCKED BY TASK 1 ---------"
                yield
                reg = x[0]
                print "Task 1, adding, s=", semaphore, " x=", x
                yield
                reg = reg+1
                print "Task 1, adding, s=", semaphore, " x=", x
                yield
                x[0] = reg
                print "Task 1, adding, s=", semaphore, " x=", x, "added!"
                yield
                release(semaphore)
                print "-------- UNLOCKED BY TASK 1 --------\n"
                yield
        yield taskIdent                                         #return ident upon exit


#a task which takes in:
#resource, semaphore for that resource, boolean on whether it is chosen to run
#returns its ident when it is killed
def task2(x, semaphore, running):
    while(True):
        yield
        taskIdent = 2
        yield
        while(running):
            print "Task 2, ------, s=", semaphore, " x=", x     #print not part of task itself. To show state
            yield
            if(acquire(semaphore) == True):                     #enter critical region if available, else block
                print "\n--------- LOCKED BY TASK 2 ---------"
                yield
                reg = x[0]
                print "Task 2, adding, s=", semaphore, " x=", x
                yield
                reg = reg+1
                print "Task 2, adding, s=", semaphore, " x=", x
                yield
                x[0] = reg
                print "Task 2, adding, s=", semaphore, " x=", x, "added!"
                yield
                release(semaphore)      
                print "-------- UNLOCKED BY TASK 2 --------\n"
                yield
        yield taskIdent                                         #return ident upon exit


#a task which takes in:
#resource, semaphore for that resource, boolean on whether it is chosen to run
#returns its ident when it is killed
def task3(x, semaphore, running):
    while(True):
        yield
        taskIdent = 3
        yield
        while(running):
            print "Task 3, ------, s=", semaphore, " x=", x     #print not part of task itself. To show state
            yield
            if(acquire(semaphore) == True):                     #enter critical region if available, else block
                print "\n--------- LOCKED BY TASK 3 ---------"
                yield
                reg = x[0]
                print "Task 3, adding, s=", semaphore, " x=", x
                yield
                reg = reg+1
                print "Task 3, adding, s=", semaphore, " x=", x
                yield
                x[0] = reg
                print "Task 3, adding, s=", semaphore, " x=", x, "added!"
                yield
                release(semaphore)      
                print "-------- UNLOCKED BY TASK 3 --------\n"
                yield
        yield taskIdent                                         #return ident upon exit


#scheduler for 3 tasks, takes in
#resource, semaphore for that resource
#prints final value of x
def scheduler(x, semaphore):
    tasks = [task1(x, semaphore, True),task2(x, semaphore, True), task3(x, semaphore, True)]     #edit 3rd argument of any task, to not run it
    for i in range(61):                                                                          #edit argument of range to increase number of cycles    
        tasks[i%3].next()
    print "END.\n\nx=", x[0]

def main():
    x=[0]     #the shared resource
    semaphore=[1]
    scheduler(x, semaphore)

if __name__ == "__main__":
   main()
