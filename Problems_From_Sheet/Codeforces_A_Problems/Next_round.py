no_of_const_and_pos = list(map(int, input().split(" ")))
cont_scores = list(map(int, input().split(" ")))

contestent_no = no_of_const_and_pos[0]
position = no_of_const_and_pos[1]

next_round_participants = 0

for const_score_index in range(contestent_no):
    if cont_scores[const_score_index] > 0:
        if cont_scores[position-1] <= cont_scores[const_score_index]:
            next_round_participants += 1

print(next_round_participants)

# thinking of another solutioto optimize the current one
# result = list(filter(cont_scores, lambda x: x >= position & x > 0))
# print(result)
