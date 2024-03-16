def count_serene_days(X, Y):
    total_days = 7
    stormy_days = int(X)
    overcast_days = int(Y)
    serene_days = total_days - (stormy_days + overcast_days)
    return serene_days
X, Y = input().split()
print(count_serene_days(X, Y))