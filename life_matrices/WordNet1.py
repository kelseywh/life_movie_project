#Kelsey Wheeler
#March 1 2013
#code for WordNet/Semantic Space paper


from nltk.corpus import wordnet as wn
import numpy as np

"""
"not used"
#define all senses of a feature and create a hypernym list for each feature

def define_and_hyper(feature):
	for s in feature:		#s for sense
		print s.name,":",s.definition	#define sense
	#need to append definitions to list
		z = s.name.split(".")[0]	#create string 
		x = z + "." + "n" + "." + "01"	
		y = wn.synset(x)
		a = [y]
		while a!=[]:		#build hypernym list
			print a
	      		a = a[0].hypernyms()
            	#need to append hypernyms to list

#define all senses of a feature; specify part of speech (n/v/a/s)

#spec_sense = wn.synset("feature.n/v/a/s.#")	#without s
#all_senses = wn.synsets("feature")	        	#with s
#all_pos_sense = wn.synsets("feature",wn.pos)   #with s
"""


"""

Building the Matrix	-->

"""

#define variables
    #f = feat_list
    #t = time #as in length of the clip, e.g. 472 seconds
    #tp = timepoint


#create list of timepoints at 2 second intervals
def tp(movie_length):
    tp = range(0,movie_length,2)     #2 for 2 second intervals
    return tp                        #return list of timepoints


#create a matrix of zeros based on list length of features and time
def create_matrix(f_list, timepoint):            #'tp' must be entered as tp(#)
    X = np.zeros((len(f_list),len(timepoint)))   #num of rows: length of feature list
    return X                                        #num columns: num of timepoints

"""
"not used currently..."
#get the index of the feature in feature_list
def get_index(feat_list, wnfeature):
    for i,x in enumerate(feat_list):
        if x == wnfeature:  #unnecessary
            print i
            print x

#create list of tuples in form (index, WN feature)
def set_indices(feat_list):
    for i,x in enumerate(feat_list):
        index_list.append((i,x))
    return index_list

"not used"
#format for a specific sense of a feature
#wn.synset("feature.n/v/a/s.#")
def spec_sense(feature,pos,num):     #enter values in "quotes" as strings
                                     #pos = partofspeech; num = reference #
    string = feature + "." + pos + "." + num
    feature = wn.synset(string)
    return featurespec
"""


"""

Adding features to the Matrix--> lists of features, hypernyms

"""

"""
"not used currently..."
#add a wn compatible feature to a list
def add_wnfeature(feature):   #feature must be entered as a string in "quotes"
    f = wn.synsets(feature)
    if f[0] not in feature_list:
        feature_list.append(f[0])
    #potentially use check_feature() to create this list.
    #would work by popping values off the check_feature list
    #and running them through add_feature. 
    # --> that way they might be in "quotes" already?
    #need to figure out the "quote" issue

"""

#make the features in a list WordNet compatible 
def make_list_wncomp(listname):
    for feature in listname:
        f =  wn.synsets(feature)
        if f[0] not in feature_list:   
            feature_list.append(f[0])
    return feature_list

"""  
"not used"
#create a feature list from check_feature() and add_feature()
def create_featurelist():
    index = 0               #eliminate when using pop() method below
    for i in present:
        f = present[index]  #or, f = present.pop()
        if f not in feature_list:
            add_feature(f)      #returns feature_list
        index+=1
"""


#simple check if a feature is in wn
# --> don't forget to create the lists [missing] and [present]
#should probably rename to check_feature
def check_wn(feature): #feature must be entered in "quotes"
    if wn.synsets(feature) == []:
        missing.append(feature)     #add to a list of missing features
    else:
        present.append(feature)     #add to a list of wn features
    return present


#checks a list using check_wn function
def check_list(listname):
    for i in listname:
        check_wn(i)         #adds features to [present] or [missing] lists
    return present



"not used"
#create a list of hypernyms for all senses
#don't forget to create hyplist
#also, don't forget to define the feature--> wn.synsets("feature")
def hyper_list(f):
    while f!=[]:
        hyplist.append(f[0])    #returns hyplist
        f = f[0].hypernyms()
    return hyplist



#from a list of features, append hypernyms to a list
def find_hypernyms(feat_list):
    for i in feat_list:
        f = [i]
        while f!=[]:
            hyplist.append(f[0])                
            f = f[0].hypernyms()
    return hyplist

#compare 2 lists; append elements of list 1 to list 2
#if they are not already present
def compare_lists(list1,list2):
    for i in list1:
        if i not in list2:
            list2.append(i)
    return list2

#print the definitions of all of the features in a list
def define(feat_list):
    for i in feat_list:
        print i.name,":",i.definition
    return feat_list

#in matrix, change 0s to 1s when a feature is present at that timepoint
def update_matrix(movie_list,matrix_list,matrix_name,time):
    for f in movie_list:
        if f in matrix_list:
            i = matrix_list.index(f)
            matrix_name[i,time] = 1     #consider adjusting time to time/2
    return matrix_name



"""
#check_wn(single feature) or check_list (list of features)
    #--> returns 'present' or 'missing'
#make_list_wncomp
    #--> returns feature_list
#find_hypernyms
    #--> returns hyplist
#compare_lists
    #returns feature_list
"""





"""

The actual code to run!

"""




make_list_wncomp(present)       #makes features WN compatible: wn.synsets('word')
#print "feature_list: ", feature_list         #creates feature_list


find_hypernyms(feature_list)    #finds hypernyms of feature_list features
#print "hyplist: ", hyplist                   #creates hyplist of hypernyms


compare_lists(hyplist,feature_list) #adds hypernyms to the feature_list
#print "feature_list: ", feature_list         #updates feature_list


matrix_list = feature_list      #matrix_list is list of all features
print "matrix_list: ", matrix_list               #feature_list can be cleared and re-used


#tp(movie_length)                #t for timepoints
m_l = tp(466*4)

matrix_name = create_matrix(matrix_list,m_l)   #create a matrix of zeros
    #edit matrix_name           # row/feature X column/timepoint

set_indices(matrix_list)        #creates index_list of tuples (index,feature)



#note to watch out for: some code needs to be changed for each new matrix
#for exmaple, part1, part1_raw_data, seq1, final1, and numbers associated with the length of the movie (seconds)
#lines that require changes are denoted with ###comments



import pickle
part1=pickle.load(file('/home/brain/Desktop/part1_raw_data.pkl'))	### change part1, part1_raw_data
tp_dict=part1['features']						### change part1
#loop over all timepoints and get list of features to update matrix
for time in tp_dict:        #will probably need to rename tp_dict to match movie
     # print "time: ",time

     #clear lists (because using same functions as above^)
     present = []    #but don't clear [missing]
     feature_list = []
     hyplist = []
   

     #check if features are in WN --> append to present or missing
     tp_list = tp_dict[time]
     #print tp_list
       
     timepoint_feature_list = tp_dict[time]
     #print "tp_feature_list: ",timepoint_feature_list

     check_list(timepoint_feature_list)     #returns present
    
     #check_list(tp_list)
     

     #make features WN compatible
     make_list_wncomp(present)
     #print "feature_list: ",feature_list

     #find hypernyms of feature_list
     find_hypernyms(feature_list)
     #print "hyplist: ",hyplist

     #update feature_list to include hypernyms
     compare_lists(hyplist,feature_list)
    
     #print     
     #print "time: ",time
     #print "feature_list: ",feature_list
    
     #print "timepoint_feature_list: ",timepoint_feature_list
     #print "matrix_name: ", matrix_name



     #change 0s to 1s for features present during that timepoint
     update_matrix(feature_list,matrix_list,matrix_name,time)
     #feature_list replaced timepoint_feature_list (might be temporary?)
     #edit matrix_name
     #print
     #print "matrix_list: ",matrix_list


print
print "---------------------------------------------------------"

for f in feature_list:
    #print "f: ",f
    if f in matrix_list:
        i = matrix_list.index(f)
        matrix_name[i,time] = 1

print
#print 'matrix_list: ',matrix_list
#print
print 'matrix_name: ',matrix_name

#final is the final matrix, 60 by 466 (the case for movie 1 code data)
seq1=range(0,466*2,2)					### seq1,  time (466)
final1=matrix_name[:,seq1]				### final1, seq1

#final_dict is the final dictionary, with each key noting the timepoint

final1_dict={}						### final1
for s in range(0,466):					### time (466)
    final1_dict[seq1[s]]=final1[:,s]			###final1_dict, seq1, final1






# len(part2['features'].keys())





"""

seq=range(0,932,2)

final=WN.matrix_name[:,seq]

pickle.dump(final,file('/home/brain/wordnet/WordNet-3.0/final.pkl','w'))


final_dict={}

for s in range(0,466):
    final_dict[seq[s]]=final[:,s]


"""
















