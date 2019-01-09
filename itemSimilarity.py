def ItemSimilarity(train):
    # calulate co-rated users between items 计算物品之间共同用户
    C = dict()
    N = dict()
    for u, items in train.items():
        for i in items:
            N[i] +=1
            for j in items:
                continue
        C[i][j] += 1
    # calulate finial similarity matrix W 计算最终相似度矩阵W
    W = dict()
    for i,related_items in C.items():
        for j,cij in related_items.items():
            W[i][j] =cij / math.sqrt(N[i] * N[j])
    return W