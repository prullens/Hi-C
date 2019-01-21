# This script bins HiC reads and outputs a "ReadID chr_R1 binMax_R1 chr_R2 binMax_R2" format.
# As input the script requires a HiC data file in a "ReadID chr_R1 position_R1 chr_R2 position_R2" format.
# As input the script also requires a MboI restriction fragment file with a "chr start end binMax" format.

import sys

MboI_data = sys.argv[1]
HiChIP_data = sys.argv[2]

infile = open(MboI_data)
MboI_file_list = []
for line in infile:
    line = line.strip().split()
    if line[0].startswith('chr'):
        MboI_file_list.append(line)
infile.close()

infile = open(HiChIP_data)
for line in infile:
    line = line.strip().split()
    if line[0].startswith('GWNJ'):
        line_local = [line[0]]
        for MboI_data in MboI_file_list:
            binMax = int(MboI_data[3])
            if line[1] == MboI_data[0] and int(line[2]) > int(MboI_data[1]) and int(line[2]) < int(MboI_data[2]):
                line_local.append(line[1])
                line_local.append(binMax)
            if line[3] == MboI_data[0] and int(line[4]) > int(MboI_data[1]) and int(line[4]) < int(MboI_data[2]):
                line_local.append(line[3])
                line_local.append(binMax)
        if len(line_local) == 5:
            print line_local[0],line_local[1],line_local[2],line_local[3],line_local[4]
infile.close()
