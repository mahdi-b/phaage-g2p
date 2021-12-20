
def parse_cdhit(infile):
    seq_to_clust = {}
    cluster_id = None
    for line in open(infile):
        if line[0]  == ">":
            cluster_id = line.split()[1]
        else:
            data = line.split()
            seq_id = data[2][5:-3].replace("-", "_")
            seq_to_clust[seq_id] = cluster_id
    return seq_to_clust


def replace_val(col_vals, mapping_dict):
    new_vals = []
    for val in col_vals:
        new_vals.append(mapping_dict[val])
    return new_vals

def replace_feature(col_vals, seq_to_clust):
    new_vals = []
    for val in col_vals:
        new_vals.append(seq_to_clust[val])
    return new_vals


# data = pd.read_table("data/ENA_ML_input_ORFs")

# seq_to_clust = parse_cdhit("data/ENA.40.clstr")




# # Replace the long feature_ids
# #### data.replace({'Feature_id': feature_id_to_int})
# # data["feature_number"] = replace_feature(data.Feature_id, seq_to_clust)
# # data.feature_number.astype(int)

# # replace contig ids
# # contig_id_to_int = {y:x for x,y in enumerate(data.contig_id.tolist())}
# #### data.replace({'contig_id': contig_id_to_int})
# # data["contig_number"] = replace_val(data.contig_id, contig_id_to_int)

def get_n_plus_group(group, freq_tuple):
    contig_features = group["feature_number"].values
    others = set(contig_features).difference(freq_tuple)
    if len(others) + len(freq_tuple) == len(contig_features):
        return [freq_tuple + (i, ) for i in others]
    else:
        return []


# subsets = data.groupby("contig_number").apply(lambda x: list(itertools.combinations(x["feature_number"].values, 2)))

# co_occurences = list(itertools.chain(*subsets.values))


# # TODO: Modify to not update the iterable in the loop! 
# for i, co_oc in enumerate(co_occurences):
#     if co_oc[0] > co_oc[1]:
#         co_occurences[i] = (co_oc[1], co_oc[0])

# co_occurences_counts = Counter(co_occurences)


# co_occurences_3 = []
# for freq_tuple, _  in sorted(co_occurences_counts.items(), key=operator.itemgetter(1))[-800:]:
#     subsets_3 = data.groupby("contig_number").apply(get_n_plus_group, freq_tuple=freq_tuple)
#     co_occurences_3 += list(itertools.chain(*subsets_3.values))
# co_occurences_3_counts = Counter(co_occurences_3)


# co_occurences_4 = []
# for freq_tuple, _  in sorted(co_occurences_3_counts.items(), key=operator.itemgetter(1))[-800:]:
#     subsets_4 = data.groupby("contig_number").apply(get_n_plus_group, freq_tuple=freq_tuple)
#     co_occurences_4 += list(itertools.chain(*subsets_4.values))
# co_occurences_4_counts = Counter(co_occurences_4)




