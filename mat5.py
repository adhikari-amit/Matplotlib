from matplotlib import pyplot as plt


x=[5,7,8,5,6,7,9,2,3,4,4,4,2,6,3,6,8,6,4,1]
y=[7,4,3,9,1,3,2,5,2,4,8,7,1,6,4,9,7,7,5,1]
colors=[7,5,9,7,5,7,2,5,3,7,1,2,8,1,9,2,5,6,7,5]
sizes=[209,486,391,255,191,315,185,288,174,583,265,965,153,273,193,436,501,397,539,104]
plt.scatter(x,y,s=sizes,c=colors,cmap='Greens',edgecolor='black',alpha=0.75)
cbar=plt.colorbar()
cbar.set_label("Satisfaction")

plt.title("Scatterplot")
plt.tight_layout()
plt.show()