# Jobs, Profit, Slot
profit = [15,27,10,100, 150]  #The profitNJobs list is created by zipping together the profit, jobs, and deadline lists. 
#Each element in the profitNJobs list is a tuple containing the profit, job name, and deadline for a particular job.
jobs = ["j1", "j2", "j3", "j4", "j5"]
deadline = [2,3,3,3,4] 
profitNJobs = list(zip(profit,jobs,deadline))
profitNJobs = sorted(profitNJobs, key = lambda x: x[0], reverse = True)
#The key parameter specifies a function that generates a value used for sorting. In this case, lambda x: x[0] is used as the key function.
#The lambda keyword is used to define an anonymous function (a function without a name).
#x is the parameter of the lambda function, representing an element from the profitNJobs list.
#x[0] accesses the first element (profit) of the tuple x.
#The reverse parameter is set to True, indicating that the list should be sorted in descending order.
slot = []
for _ in range(len(jobs)):
    slot.append(0)

profit = 0
ans = []

for i in range(len(jobs)):
    ans.append('null')

for i in range(len(jobs)):
        job = profitNJobs[i]
        #check if slot is occupied
        for j in range(job[2], 0, -1):
            if slot[j] == 0:
                ans[j] = job[1]
                profit += job[0]
                slot[j] = 1
                break
        
print("Jobs scheduled buddy:",ans[1:])
print(profit)
