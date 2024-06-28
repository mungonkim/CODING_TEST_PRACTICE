def solution(numbers, direction):
    answer = []

    if direction == "right":
        for i in range(len(numbers)):
            if i == len(numbers) - 1:
                answer.insert(0, numbers[i])
                break
            answer.append(numbers[i])
    elif direction == "left":
        for i in range(len(numbers)):
            if i == len(numbers) -1:
                answer.pop(0)
                answer.append(numbers[i])
                answer.append(numbers[0])
                break
            answer.append(numbers[i])
    return answer
