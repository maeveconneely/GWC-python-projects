import billionaires
import matplotlib.pyplot as plt

list_of_billionaire = billionaires.get_billionaires()

list_of_billionaire.sort(key=lambda e: e["wealth"]["worth in billions"], reverse=True)

wealth = []
num_count = 500

ind = 0
for i in list_of_billionaire:
    wealth.append(i["wealth"]["worth in billions"])
    ind += 1
    if ind == num_count:
        break

plt.plot(range(num_count), wealth)
plt.xlabel("rank")
plt.ylabel("Wealth")
plt.show()
