def make_collection(tp: str):

    def collect(nums: str) -> list[int] | tuple[int, ...]:
        return [[int(num) for num in nums.split()], tuple(int(num) for num in nums.split())][tp != "list"]

    return collect

maker = make_collection(input())
collection = maker(input())

print(collection)
