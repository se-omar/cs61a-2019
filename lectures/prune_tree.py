def prune_tree(t, x):
    t.branches = [b for b in t.branches if b.label != x]

    for b in t.branches:
        prune_tree(b, x)
