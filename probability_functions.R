# Calculate p-values from z-score
z = 2
pvalue_1sided = pnorm(-abs(z))
pvalue_2sided = 2*pnorm(-abs(z))

# Calculate z-score from p-values
z = qnorm(1 - pvalue_1sided)
z = qnorm(1 - pvalue_2sided/2)

# Calculate p-values from t test
data = c(1,2,3,4,5)
t.value = 1
hyp = 3
t.value = (mean(data) - hyp) / (sd(data) / sqrt(length(data))) 
sample_size = length(data)
df = sample_size - 1
p.value = dt(t.value, df=df)

