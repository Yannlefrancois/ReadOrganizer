import BWT_package
import tools_karkkainen_sanders
import argparse
from read import Read
import time
#fichier d'entrée : une seule séquences de génome


"""
Method1 is a function that takes a read and a genome as input and returns a dictionary with the positions of the read in the genome.

:param one_read (object from Read class): a read
:param genome_btw : a genome
:param genome_n: a genome
:param genome_r: a genome
:param genome_suffixe_table: a genome

:return: a dictionary with the positions of the read in the genome
"""
def method1(one_read,genome_btw,genome_n,genome_r,genome_suffixe_table):
    all_pose=set()      #using a set to deal with redundancy easily
    for i in range(0,len(one_read)-arg.k+1):
        all_match=BWT_package.all_occurence(one_read.get_seq()[i:i+arg.k],genome_btw,genome_n,genome_r,genome_suffixe_table)
        for match in all_match:
            all_pose.add(match-i)   # -i to retain only the starting point of the read and not of the patern
    return all_pose


'''
Method0 is a function that takes a read and a genome as input and returns a dictionnary 
whose keys are the position of where pattern of size from the read has been seen the 
genome and the values are the number of occurence corresponding to said position.

:param one_read (object from Read class): a read
:param genome_bwt : the genome burrows wheeler transform
:param genome_n: a dictionnary where the key's are the letter of your genome and the values are the position at wich they appear for the first time in the BWT
:param genome_r: a list the same lengh as the BWT and where the ieme value is the number of time this value as been seen so far in the BWT
:param genome_suffixe_table: a suffixe table

:return: a dictionary with the positions of the read in the genome and the number of occurence the read has been mapped at the position
'''

def method2(one_read,genome_btw,genome_n,genome_r,genome_suffixe_table):
    all_pose=dict()
    for i in range(0,len(one_read)-arg.k+1):
        all_match=BWT_package.all_occurence(one_read.get_seq()[i:i+arg.k],genome_btw,genome_n,genome_r,genome_suffixe_table)
        for match in all_match:
            if match-i in all_pose: # -i for the same reason as method 1
                all_pose[match-i]+=1
            else:
                all_pose[match-i]=1
    return all_pose

'''
best_positions_m1 is the function that choose best position of the read on the genome based 
on where there is the least substitution between the read sequence and the genome. 
Once the best position has been choosen it change the attribut __pos of the read to the best
position and change the attribute __mapped from false to true.


:param one_read (object from Read class): a read
:param genome_seq : the genome sequence as a string
:param all_pose: a list of all position you want evaluated 

:return: nothing
'''

def best_positions_m1(one_read,genome_seq,all_pose):
    a=len(one_read.get_seq())
    best_score=10000
    best_pos=-1
    for pos in all_pose:
        nb_subtitution=0
        genome_seq_substring=genome_seq[pos:pos+a]
        for i in range(len(genome_seq_substring)):
            if one_read.get_seq()[i] != genome_seq_substring[i]:
                nb_subtitution+=1
        if nb_subtitution < best_score:
            best_score=nb_subtitution
            best_pos=pos
    one_read.add_pos(best_pos)

    if one_read.get_pos() != -1:
        one_read.was_mapped()

'''
best_positions_m1 is the function that choose best position of the read on the genome based 
on where pattern of the read have been observed the most in the genome. 
Once the best position has been choosen it change the attribut __pos of the read to the best
position and change the attribute __mapped from false to true.


:param one_read (object from Read class): a read
:param all_pose: a list of all position you want evaluated 

:return: nothing
'''
def best_positions_m2(one_read,all_pose):
    best_pose=-1
    occurence=0
    for pose in all_pose:
        if all_pose[pose] > occurence:
            best_pose=pose
            occurence=all_pose[pose]
    one_read.add_pos(best_pose)
    if one_read.get_pos() != -1:
        one_read.was_mapped()





'''
classic sortiing algorithm, unused in the program because of poor performances.
but we still did it so it stays
'''
def insertion_sort(read_list):
    for i in range(1, len(read_list)):
        for j in range(i-1, -1, -1):
            if read_list[j].get_pos() > read_list[j+1].get_pos():
                read_list[j], read_list[j+1] =  read_list[j+1],read_list[j]
            else :
                break
    return read_list




if __name__=="__main__":
    try :
        parser=argparse.ArgumentParser()
        parser.add_argument("-i", metavar= "reads file in a fasta format", type=argparse.FileType('r'))
        parser.add_argument("-r", metavar= "genome file in a fasta format", type=argparse.FileType('r'))
        parser.add_argument("-o", metavar= "outputfile name", type=str)
        parser.add_argument("-k", metavar= "seed size", type=int)
        parser.add_argument("-m", metavar= "seeding method", type=int)
        arg = parser.parse_args()
        
        if arg.i is None or arg.r is None or arg.k is None or arg.m is None or arg.o is None:
            parser.print_help()
            exit(1)

        with open(arg.r.name,"r") as genome_file:
            a = "".join(genome_file.readlines()[1:]).strip()+"$"
            genome_suffixe_table=tools_karkkainen_sanders.simple_kark_sort(a)
            genome_btw=BWT_package.get_btw(a,genome_suffixe_table)

        genome_n=BWT_package.get_n(genome_btw)
        genome_r=BWT_package.get_r(genome_btw)

        all_reads=[]
        with open(arg.i.name,"r") as read_file:
            b=False
            for line in read_file:
                if line[0] == ">" and b==True:
                    all_reads.append(Read(seq))
                    b=False
                elif line[0] != ">" and b==False:
                    seq=line.strip()
                    b=True
                elif line[0] != ">" and b==True:
                    seq=seq+line
            all_reads.append(Read(seq))
        
        
        for one_read in all_reads:

            if arg.m==1:
                all_pose = method1(one_read,genome_btw,genome_n,genome_r,genome_suffixe_table)
                genome_seq=BWT_package.btw_2_seq(genome_btw,genome_n,genome_r)
                best_positions_m1(one_read,genome_seq,all_pose)

            elif arg.m==2:
                all_pose = method2(one_read,genome_btw,genome_n,genome_r,genome_suffixe_table)
                best_positions_m2(one_read,all_pose)

        del(all_pose)


        last_to_map=[]
        #loop that selects only the read that havent been mapped 
        # so we can try to map their reverse complement sequence
        for one_read in all_reads:
            if  not one_read.get_mapping_status():
                one_read.reverse_complentation()
                last_to_map.append(one_read)

        for one_read in last_to_map:
            all_pose=dict()
            if arg.m==1:
                all_pose = method1(one_read,genome_btw,genome_n,genome_r,genome_suffixe_table)
                genome_seq=BWT_package.btw_2_seq(genome_btw,genome_n,genome_r)
                best_positions_m1(one_read,genome_seq,all_pose)
            elif arg.m==2:
                all_pose = method2(one_read,genome_btw,genome_n,genome_r,genome_suffixe_table)
                best_positions_m2(one_read,all_pose)
        
        del(last_to_map,genome_seq, all_pose)

        all_reads.sort(key= lambda x : x.get_pos())

        with open(arg.o,"w") as outputfile:
            for one_read in all_reads:
                outputfile.write(f'>\n{one_read.get_seq()}\n')

        after_process_time=time.process_time()

        non_map=0
        for read in all_reads:
            if not read.get_mapping_status():
                non_map+=1
    except IOError as e:
        print(e)
        
