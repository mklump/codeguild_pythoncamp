def main():
    candidate_dict = {} #initialize new dictionary

    accept_input = True
    while accept_input:
        print('Candidate name? Or done.')
        candidate_name = input()
        if 'done' == candidate_name:
            break
        if not(candidate_name in candidate_dict):
            candidate_dict[candidate_name] = 1
        else:
            candidate_dict[candidate_name] += 1

    for name in candidate_dict:
        print('Candidate', name, 'has', candidate_dict[name], 'votes.')

    highest_votes = 0
    elected_name = ''
    for name in candidate_dict:
        if highest_votes < candidate_dict[name]:
            highest_votes = candidate_dict[name]
            elected_name = name

    print('The elected name was', elected_name, 'having',
    highest_votes, 'number of votes.')

if __name__ == "__main__":
    sys.exit(int(main() or 0))