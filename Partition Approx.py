import numpy as np
import matplotlib.pyplot as plt

#Defining the approximation function
def partition_approx(ratio, n_max):
    sum_list = []
    for i in range(n_max):
        part_sum = (2*i +1)*np.exp((-1)*ratio*i*(i+1))
        sum_list.append(part_sum)
    sum_arr = np.array(sum_list)
    sum_tot = np.sum(sum_arr)
    return sum_tot, sum_arr


#Running function for the different energy ratios w/ n_max of 100

sum_res_1, y_data_1 = partition_approx(0.01,100) #Be = 0.01
sum_res_2, y_data_2 = partition_approx(0.2,100)  #Be = 0.2
sum_res_3, y_data_3 = partition_approx(0.5,100)  #Be = 0.5
sum_res_4, y_data_4 = partition_approx(1,100)    #Be = 1

#Printing Sum Results
print("A ratio of 0.01 has a result of: {res_1}".format(res_1 = sum_res_1))
print("A ratio of 0.2 has a result of: {res_2}".format(res_2 = sum_res_2))
print("A ratio of 0.5 has a result of: {res_3}".format(res_3 = sum_res_3))
print("A ratio of 1 has a result of: {res_4}".format(res_4 = sum_res_4))

#x_data is just 1-100 for sum terms
x_data = np.arange(100)

#Plotting Different Ratios

plt.plot(x_data, y_data_1, label = "Ratio = 0.01")

plt.plot(x_data, y_data_2, label = "Ratio = 0.2")

plt.plot(x_data, y_data_3, label = "Ratio = 0.5")

plt.plot(x_data, y_data_4, label = "Ratio = 1")

#Formatting Graph
plt.xlabel("Sum Index")
plt.ylabel("Value of Sum Term")
plt.title("Terms of Partition Function for Varying Energy Ratios")
plt.legend()
plt.show()