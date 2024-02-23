# from scATAC-benchmarking-main/Real_Data/10x_PBMC_5k/run_clustering_10xpbmc5k.ipynb
# of the additional data 2 from Chen 2019 Assessment of computational methods for the analysis of single-cell ATAC-seq data

def residual_average_gini_index(gene_scores,folder_clusters,
                                housekeeping_genes,marker_genes,
                                min_cells_per_cluster=10):

    #Subset from the main matrix the housekeeping genes and marker genes
    df_matrix_housekeeping=gene_scores.loc[gene_scores.index.intersection(housekeeping_genes),]
    df_matrix_marker=gene_scores.loc[gene_scores.index.intersection(marker_genes),]
    
    #Define a function to compute the Gini score
    def gini(list_of_values):
        sorted_list = sorted(list_of_values)
        height, area = 0, 0
        for value in sorted_list:
            height += value
            area += height - value / 2.
            fair_area = height * len(list_of_values) / 2.
        return (fair_area - area) / fair_area
    
    #Function to calculate Gini value for all the genes
    def calculate_gini(df_matrix, gene_name,clustering_info):
        return gini(get_avg_per_cluster(df_matrix,gene_name,clustering_info,use_log2=False))

    #Function to calculate Gini value for all the genes
    def calculate_gini_values(df_matrix,clustering_info):
        gini_values=[]
        for gene_name in df_matrix.index:
            gini_values.append(calculate_gini(df_matrix, gene_name,clustering_info))
        return gini_values
    
    #Write a function to compute delta difference of the average accessibility in Marker vs Housekeeping and Kolmogorov Smirnov test
    def score_clustering_solution(df_matrix_marker,df_matrix_housekeeping,clustering_info):
        gini_values_housekeeping=calculate_gini_values(df_matrix_housekeeping,clustering_info)
        gini_values_marker=calculate_gini_values(df_matrix_marker,clustering_info)
        statistic,p_value=stats.ks_2samp(gini_values_marker,gini_values_housekeeping)
        
        return  np.mean(gini_values_marker), np.mean(gini_values_housekeeping),np.mean(gini_values_marker)-np.mean(gini_values_housekeeping), statistic,p_value

    #Function to compute the average accessibility value per cluster
    def get_avg_per_cluster(df_matrix, gene_name, clustering_info,use_log2=False):
        N_clusters=len(clustering_info.index.unique())
        avg_per_cluster=np.zeros(N_clusters)
        for idx,idx_cluster in enumerate(sorted(np.unique(clustering_info.index.unique()))):
            if use_log2:
                values_cluster=df_matrix.loc[gene_name,clustering_info.loc[idx_cluster,:].values.flatten()].apply(lambda x:np.log2(x+1))
            else:
                values_cluster=df_matrix.loc[gene_name,clustering_info.loc[idx_cluster,:].values.flatten()]
           
            avg_per_cluster[idx]=values_cluster.mean()
            if avg_per_cluster[idx]>0:
                  avg_per_cluster[idx]=avg_per_cluster[idx]#/values_cluster.std()

        return avg_per_cluster
    

    #Run the method for all the clustering solutions
    
    df_metrics = pd.DataFrame(columns=['Method','Clustering','Gini_Marker_Genes','Gini_Housekeeping_Genes','Difference','KS_statistics','p-value'])    
    
    for clusters_filename in os.listdir(folder_clusters):     
        method = '_'.join(clusters_filename.split('_')[:-1])
        print(method)
        df_clusters = pd.read_csv(os.path.join(folder_clusters,clusters_filename),sep='\\t',index_col=0)
        for clustering_method in df_clusters.columns:
            clustering_info = pd.DataFrame(df_clusters[clustering_method])
            clustering_info['Barcode'] = clustering_info.index
            clustering_info=clustering_info.set_index(clustering_method)
            
            #REMOVE CLUSTERS WITH FEW CELLS
            cluster_sizes=pd.value_counts(clustering_info.index)
            clustering_info=clustering_info.loc[cluster_sizes[cluster_sizes>min_cells_per_cluster].index.values,:]


            mean_gini_marker,mean_gini_housekeeping,mean_gini_difference,statistics,p_value=score_clustering_solution(df_matrix_marker,df_matrix_housekeeping,clustering_info)

            df_metrics = df_metrics.append({'Method': method,'Clustering':clustering_method,
                               'Gini_Marker_Genes':mean_gini_marker,'Gini_Housekeeping_Genes':mean_gini_housekeeping,
                               'Difference':mean_gini_difference,'KS_statistics':statistics,'p-value':p_value},
                              ignore_index=True)  
        
    return df_metrics
