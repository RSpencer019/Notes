import scipy

p_values = scipy.stats.norm.sf(abs(z_scores)) #one-sided

p_values = scipy.stats.norm.sf(abs(z_scores))*2 #twosided