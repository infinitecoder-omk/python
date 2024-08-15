score_list = input().split()


for n in  range(0,len(score_list)):
    score_list[n] = int(score_list[n])
print(score_list[n])  #simply prints the nth term in this list
heighest_Score = 0

for score in score_list:
    if(score > heighest_Score):
     heighest_Score = score


print(f"the heighest score is :{heighest_Score}")