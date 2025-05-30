avg = lambda items : sum(items)/len(items)
closest_to = lambda lst,x : min(lst, key=lambda n: abs(n - x))