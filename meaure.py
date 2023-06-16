from rouge import Rouge

def evaluate_rouge(reference_summaries, generated_summaries):
    rouge = Rouge()
    scores = rouge.get_scores(generated_summaries, reference_summaries, avg=True)
    return scores

# Example usage
reference_summaries = ["Reference summary 1", "Reference summary 2", "Reference summary 3"]
generated_summaries = ["Generated summary 1", "Generated summary 2", "Generated summary 3"]

rouge_scores = evaluate_rouge(reference_summaries, generated_summaries)
print(rouge_scores)
