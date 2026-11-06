match result_sum := int(input()):
    case c if result_sum < 1000:
        print(f"{result_sum:.2f}")
    case c if 1000 <= result_sum < 5000:
        result_sum *= 0.95
        print(f"{result_sum:.2f}")
    case c if 5000 <= result_sum < 10000:
        result_sum *= 0.90
        print(f"{result_sum:.2f}")
    case _:
        result_sum *= 0.85
        print(f"{result_sum:.2f}")