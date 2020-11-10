import statistics
import random
dice_result=[]
for i in range (0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice_result.append(dice1+dice2)

mean=sum(dice_result)/len(dice_result)
std_deviation=statistics.stdev(dice_result)
median=statistics.median(dice_result)
mode=statistics.mode(dice_result)

print(" mean of the data is {} ".format(mean))
print(" median of the data is {}".format(median))
print("mode of the data is {}".format(mode))
print("standard deviation of the data is {}".format(std_deviation))