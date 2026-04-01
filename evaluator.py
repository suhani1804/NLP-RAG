from sklearn.metrics.pairwise import cosine_similarity

def cosine(a, b):
    return cosine_similarity([a], [b])[0][0]

class Evaluator:

    def precision_at_k(self, retrieved, relevant, k):
        return len(set(retrieved[:k]) & set(relevant)) / k

    def mrr(self, ranked_lists, relevant):
        score = 0
        for rlist in ranked_lists:
            for i, item in enumerate(rlist):
                if item in relevant:
                    score += 1/(i+1)
                    break
        return score / len(ranked_lists)

    def faithfulness(self, answer, context):
        overlap = sum(1 for w in answer.split() if w in context)
        return overlap / (len(answer.split())+1)