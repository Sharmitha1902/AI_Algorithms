import math

def minimax(depth, index, isMaxPlayer, scores, max_depth, alpha, beta):
    
    if depth == max_depth:
        print(f"Reached leaf at depth {depth} with value: {scores[index]}")
        return scores[index]

    if isMaxPlayer:
        highest_score = -math.inf
        print(f"[Maximizer] Evaluating options at depth {depth}...")

        
        for child in range(2):
            score = minimax(
                depth + 1, index * 2 + child, False, scores, max_depth, alpha, beta
            )
            print(f"[Maximizer] At depth {depth}, comparing {score} with {highest_score}")
            highest_score = max(highest_score, score)

            
            alpha = max(alpha, highest_score)
            if alpha >= beta:
                print(f"[Maximizer] Pruned at depth {depth} with α={alpha}, β={beta}")
                break

        print(f"[Maximizer] Chose {highest_score} at depth {depth}")
        return highest_score

    else:
        lowest_score = math.inf
        print(f"[Minimizer] Evaluating options at depth {depth}...")

        
        for child in range(2):
            score = minimax(
                depth + 1, index * 2 + child, True, scores, max_depth, alpha, beta
            )
            print(f"[Minimizer] At depth {depth}, comparing {score} with {lowest_score}")
            lowest_score = min(lowest_score, score)

            
            beta = min(beta, lowest_score)
            if beta <= alpha:
                print(f"[Minimizer] Pruned at depth {depth} with α={alpha}, β={beta}")
                break

        print(f"[Minimizer] Chose {lowest_score} at depth {depth}")
        return lowest_score


max_depth = 3
leaf_scores = [8, -2, 5, 7, 4, -6, 3, 9]  

optimal_outcome = minimax(0, 0, True, leaf_scores, max_depth, -math.inf, math.inf)
print("\nThe optimal outcome is:", optimal_outcome)
