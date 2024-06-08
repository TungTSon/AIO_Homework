def ex1_F1Score(tp=0, fp=1, fn=1):
    errors = []

    # Check if all inputs are integers
    if not isinstance(tp, int):
        errors.append("tp must be int.")
    if not isinstance(fp, int):
        errors.append("fp must be int.")
    if not isinstance(fn, int):
        errors.append("fn must be int.")
    # Check if all inputs are non-negative
    if (tp <= 0 or fp <= 0 or fn <= 0):
        errors.append("tp, fp, and fn must be greater than or equal to zero.")

    # If there are errors, print them and return
    if errors:
        for error in errors:
            print(error)
        return

    # Calculate the F1 score
    else:
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0
        f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
        print(f"precision = {precision}\n"
              f"recall = {recall}\n"
              f"f1-score = {f1_score}")
        # return f1_score   # turn this ON when doing Multiple Choice, section II


if __name__ == "__main__":
    # Example usage
    ex1_F1Score(tp=2, fp=3, fn=4)  # This should work
    ex1_F1Score(tp='h', fp=1, fn=2)  # This should print an error message for tp
    ex1_F1Score(tp=2, fp=-1, fn=2)  # This should print an error message for fp
    ex1_F1Score(tp=0, fp='O', fn=2)  # This should print error messages for tp and fp

    # Multiple Choice, section II
    # assert round(ex1_F1Score (tp =2, fp =3, fn =5) , 2) == 0.33
    # print(round(ex1_F1Score(tp =2, fp =4, fn =5), 2))