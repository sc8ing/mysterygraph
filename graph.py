import networkx as nx


verts = ["Brenna",
         "Grace",
         "Jacob",
         "EmmaB",
         "Nia",
         "Josh",
         "Liam",
         "Dani",
         "EmmaLl",
         "Julia",
         "Amika",
         "Katherine",
         "Kevin",
         "Vanessa",
         "Lia",
         "Mario",
         "Ben",
         "Sam",
         "Paula"]
edges = [("Brenna", "Grace", "blue"),
         ("Brenna", "Kevin", "orange"),
         ("Grace", "Brenna", "blue"),
         ("Grace", "Josh", "blue"),
         ("Grace", "Jacob", "orange"),
         ("Jacob", "Amika", "blue"),
         ("Jacob", "Liam", "blue"),
         ("Jacob", "Nia", "blue"),
         ("EmmaB", "Nia", "blue"),
         ("EmmaB", "Josh", "orange"),
         ("Nia", "EmmaB", "blue"),
         ("Nia", "Liam", "blue"),
         ("Nia", "EmmaLl", "blue"),
         ("Nia", "Jacob", "blue"),
         ("Josh", "Grace", "blue"),
         ("Josh", "EmmaB", "orange"),
         ("Josh", "EmmaLl", "orange"),
         ("Josh", "Liam", "orange"),
         ("Liam", "Jacob", "blue"),
         ("Liam", "Nia", "blue"),
         ("Liam", "Amika", "blue"),
         ("Liam", "Brenna", "orange"),
         ("Liam", "Josh", "orange"),
         ("Liam", "Kevin", "orange"),
         ("Liam", "Paula", "orange"),
         ("Liam", "Lia", "orange"),
         ("Liam", "EmmaLl", "orange"),
         ("Liam", "EmmaB", "orange"),
         ("Dani", "Liam", "orange"),
         ("EmmaLl", "Dani", "orange"),
         ("EmmaLl", "Nia", "blue"),
         ("EmmaLl", "EmmaB", "orange"),
         ("EmmaLl", "Jacob", "orange"),
         ("EmmaLl", "Liam", "orange"),
         ("EmmaLl", "Brenna", "orange"),
         ("EmmaLl", "Amika", "orange"),
         ("EmmaLl", "Ben", "blue"),
         ("EmmaLl", "Kevin", "orange"),
         ("EmmaLl", "Vanessa", "blue"),
         ("EmmaLl", "Sam", "orange"),
         ("EmmaLl", "Paula", "orange"),
         ("EmmaLl", "Lia", "blue"),
         # ("Julia", "Liam", "orangedotted"),
         ("Julia", "Amika", "orange"),
         ("Julia", "Vanessa", "blue"),
         ("Julia", "Kevin", "blue"),
         ("Amika", "Julia", "orange"),
         ("Amika", "Brenna", "orange"),
         ("Amika", "Jacob", "blue"),
         ("Amika", "EmmaB", "orange"),
         ("Amika", "Nia", "orange"),
         ("Amika", "EmmaLl", "orange"),
         ("Amika", "Katherine", "orange"),
         ("Amika", "Lia", "orange"),
         ("Amika", "Paula", "orange"),
         ("Amika", "Vanessa", "orange"),
         ("Kevin", "Jacob", "orange"),
         ("Kevin", "Liam", "orange"),
         ("Kevin", "Paula", "blue"),
         ("Kevin", "Ben", "blue"),
         ("Kevin", "Mario", "blue"),
         ("Vanessa", "Julia", "blue"),
         ("Vanessa", "Liam", "blue"),
         ("Vanessa", "Nia", "blue"),
         ("Vanessa", "EmmaLl", "blue"),
         ("Vanessa", "Paula", "orange"),
         ("Lia", "Kevin", "blue"),
         ("Lia", "Vanessa", "orange"),
         ("Lia", "EmmaLl", "blue"),
         ("Lia", "Liam", "orange"),
         ("Lia", "Paula", "blue"),
         ("Mario", "Julia", "blue"),
         ("Mario", "Kevin", "blue"),
         ("Mario", "Dani", "blue"),
         ("Mario", "Ben", "blue"),
         ("Ben", "Mario", "blue"),
         ("Ben", "Brenna", "orange"),
         ("Ben", "Kevin", "blue"),
         ("Ben", "Liam", "orange"),
         ("Ben", "Vanessa", "orange"),
         ("Sam", "Mario", "blue"),
         ("Sam", "Ben", "orange"),
         ("Sam", "Liam", "orange"),
         ("Sam", "EmmaLl", "orange"),
         ("Paula", "Lia", "blue")]
         # ("Lia", "AmikaJacob", "orange"),
         # ("Amika", "JacobLiam", "blue"),

# most outbound connections
outcount = {}
for v in verts:
    outcount[v] = 0
for e in edges:
    outcount[e[0]] += 1
maxout = [("", 0)]
for (name, count) in outcount.items():
    if count > maxout[0][1]:
        maxout = [(name, count)]
    elif count == maxout[0][1]:
        maxout.append((name, count))
print("most outgoing overall: {}, {}".format(maxout[0][0], maxout[0][1]))

# most outbound blue
outcount = {}
for v in verts:
    outcount[v] = 0
for e in filter(lambda e: e[2] == "blue", edges):
    outcount[e[0]] += 1
maxout = [("", 0)]
for (name, count) in outcount.items():
    if count > maxout[0][1]:
        maxout = [(name, count)]
    elif count == maxout[0][1]:
        maxout.append((name, count))
print("most outgoing blue: {}, {}".format(maxout[0][0], maxout[0][1]))

# most outbound orange
outcount = {}
for v in verts:
    outcount[v] = 0
for e in filter(lambda e: e[2] == "orange", edges):
    outcount[e[0]] += 1
maxout = [("", 0)]
for (name, count) in outcount.items():
    if count > maxout[0][1]:
        maxout = [(name, count)]
    elif count == maxout[0][1]:
        maxout.append((name, count))
print("most outgoing orange: {}, {}".format(maxout[0][0], maxout[0][1]))

# most inbound
incount = {}
for v in verts:
    incount[v] = 0
for (name, conn, color) in edges:
    incount[conn] += 1
maxin = [("", 0)]
for (name, count) in incount.items():
    if count > maxin[0][1]:
        maxin = [(name, count)]
    elif count == maxin[0][1]:
        maxin.append((name, count))
print("most incoming overall: {}, {}".format(maxin[0][0], maxin[0][1]))

# most inbound blue
incount = {}
for v in verts:
    incount[v] = 0
for (name, conn, color) in filter(lambda e: e[2] == "blue", edges):
    incount[conn] += 1
maxin = [("", 0)]
for (name, count) in incount.items():
    if count > maxin[0][1]:
        maxin = [(name, count)]
    elif count == maxin[0][1]:
        maxin.append((name, count))
print("most incoming blue: {}, {}".format(maxin[0][0], maxin[0][1]))

# most inbound orange
incount = {}
for v in verts:
    incount[v] = 0
for (name, conn, color) in filter(lambda e: e[2] == "orange", edges):
    incount[conn] += 1
maxin = [("", 0)]
for (name, count) in incount.items():
    if count > maxin[0][1]:
        maxin = [(name, count)]
    elif count == maxin[0][1]:
        maxin.append((name, count))
print("most incoming orange: {}, {}".format(maxin[0][0], maxin[0][1]))

G = nx.Graph()
G.add_edges_from(map(lambda e: (e[0], e[1]), edges))
cliques = list(nx.find_cliques(G))
cliques = list(filter(lambda c: len(c) > 2, cliques))
threeways = list(filter(lambda c: len(c) == 3, cliques))
fourways = list(filter(lambda c: len(c) == 4, cliques))
print(threeways)
print(fourways)


# clusters of orange
# most reciprocated connections
