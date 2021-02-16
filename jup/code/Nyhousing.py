import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('http://www.jaredlander.com/data/housing.csv')





data.columns = ["Neiborhood", "Class", "Units","YearBuilt", "SqFt", "Income", "IncomeperSqFt",
                "Expence", "ExpencePerSqFt", " NetIncome", "Value", "ValueperSqFt","Boro"]



plt.hist(data['ValueperSqFt'])




ggplot(housing, aes(x = ValueperSqFt)) +
  geom_histogram(binwidth = 10) +labs(x = "Value per Square Foot")

ggplot(housing, aes(x = ValueperSqFt, fill=Boro)) +
  geom_histogram(binwidth = 10) +labs(x = "Value per Square Foot")
ggplot(housing, aes(x= ValueperSqFt, fill=Boro))+
  geom_histogram(binwidth = 10) + labs(x = "Value per Square Foot") +
  facet_wrap(~Boro)

ggplot(housing, aes(x=SqFt)) + geom_histogram()
ggplot(housing, aes(x=Units)) + geom_histogram()
