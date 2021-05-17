
string_1 = [char for char in input()]
string_2 = [char for char in input()]
uncom_seq_counter = 0
comm_seq_counter = 0

for i in range(0, max(len(string_1), len(string_2)), 1):
    if string_1[i:i+1] != string_2[i:i+1]:
        uncom_seq_counter += 1
    else:
        comm_seq_counter += 1

if uncom_seq_counter == 0:
    print(-1)
else:
    print(comm_seq_counter + uncom_seq_counter)
