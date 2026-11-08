def perimeter_rect(width: int, height: int) -> None:
    print(f"Периметр прямоугольника, равен {2 * (width + height)}")


perimeter_rect(*map(int, input().split()))