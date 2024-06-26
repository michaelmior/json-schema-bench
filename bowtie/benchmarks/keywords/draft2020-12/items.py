import uuid


def get_benchmark():
    name = "items"
    description = (
        "A benchmark for measuring performance of the "
        "implementation for the items keyword."
    )

    max_array_size = 1000000
    array_size = 10000

    benchmarks = []
    while array_size <= max_array_size:
        array = [uuid.uuid4().hex for _ in range(array_size)]

        invalid_at_first = [1] + array[:-1]
        invalid_at_middle = array[:array_size//2] + [1] + array[array_size//2:-1]
        invalid_at_last = array[:-1] + [1]
        valid = array

        benchmarks.append(dict(
            name=f"Array Size - {array_size}",
            description=(
                f"Validating the `items` keyword over array of size {array_size}."
            ),
            schema={
                "type": "array",
                "items": {"type": "string"},
            },
            tests=[
                dict(description="Invalid at First", instance=invalid_at_first),
                dict(description="Invalid at Middle", instance=invalid_at_middle),
                dict(description="Invalid at Last", instance=invalid_at_last),
                dict(description="Valid", instance=valid),
            ],
        ))
        array_size *= 10

    return dict(
        name=name,
        description=description,
        benchmarks=benchmarks,
    )
