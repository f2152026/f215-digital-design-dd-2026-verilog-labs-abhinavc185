for i in range(1, 65):
    terms = [f"g[{i-1}]"]
    for j in range(1, i):
        p_parts = " & ".join([f"p[{k}]" for k in range(i-1, i-1-j, -1)])
        terms.append(f"({p_parts} & g[{i-1-j}])")
    
    p_all = " & ".join([f"p[{k}]" for k in range(i-1, -1, -1)])
    terms.append(f"({p_all} & cin)")
    
    print(f"  assign #(2) c[{i}] = {' | '.join(terms)};")