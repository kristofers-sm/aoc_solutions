def get_lines(input_str):
        lines = input_str.split('\n')
        if not lines[0]:
                lines = lines[1:]
        return lines

def solution1(input_str):
        lines = get_lines(input_str)
        counts_by_pos = {}

        # Get counts for position
        for line in lines:
                line = lines[0]
                for i in range(len(line)):
                        char = line[i]
                        if not counts_by_pos.get(i):
                                counts_by_post[i] = {0: 0, 1: 0}
                        
                        num = int(char)
                        counts_by_pos[i][num] += 1

        # get max char for each.
        gamma = ['0'] * len(counts_by_pos.items())
        epsilon = ['0'] * len(counts_by_pos.items())
        # for pos, counts in counts_by_pos.items():
        print gamma

def main():
        input_str = '''00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010'''
        print(solution1(input_str))
main()