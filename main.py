'''
Created by the authors.
@wallissoncarvalho
@machadoyang
'''

import pandas as pd
import methods
import geoprocessing
import flowsignatures
import clustering

observed_flows = pd.read_pickle(r'data\observed_flows.pkl')
natural_flows = pd.read_pickle(r'data\natural_flows.pkl')
#all_flows = pd.concat([observed_flows,natural_flows],axis=1)
#
#signatures = flowsignatures.all_signatures(all_flows)
#physiographic_data = pd.read_pickle(r'data\physiographic_data.pkl')
#all_parameters = pd.concat([physiographic_data,signatures],axis=1)
#all_parameters['q90'] = all_parameters['q90']/all_parameters['AreaKm2']
#all_parameters['q10'] = all_parameters['q10']/all_parameters['AreaKm2']
#all_parameters['Mean'] = all_parameters['Mean']/all_parameters['AreaKm2']
##
##
#affected_stations = pd.read_pickle(r'data\affected_stations_final.pkl')
#list_affected = ['48460000','48830000','49600000']
#for column in affected_stations.columns:
#    list_affected = list_affected+list(affected_stations[column].dropna())
#
#
#all_parameters=all_parameters.drop(list_affected)
#all_parameters.to_pickle(r'data\all_parameters.pkl')
#
#all_parameters.pop('AreaKm2')
#
#all_parameters = pd.read_pickle(r'data\all_parameters.pkl')

#all_parameters = pd.read_excel(r'data\all_parameters.xlsx', index_col=0)
#all_parameters=all_parameters.drop(45260000)
#correlation = all_parameters.corr(method='spearman')
#all_parameters.pop('Mean')
#all_parameters.pop('CV')
#all_parameters.pop('IBF')
#    
#for column in all_parameters.columns:
#    all_parameters[column] = (all_parameters[column]-all_parameters[column].mean())/all_parameters[column].std()
##
#cluster = clustering.kmeans_ward_evaluation(signatures)
#cluster_points=clustering.kmeans_ward_shape(standard_data_cluster,2,r'shapefiles\Watersheds.shp')
#cluster_points.to_file(r'shapefiles\cluster_points.shp')
