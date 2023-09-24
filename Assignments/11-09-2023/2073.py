class Solution:
	def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
		result = 0
		queue = deque([])
		for index in range(len(tickets)):
			queue.append([tickets[index] , index])
		while len(queue) > 0:
			first_person , index = queue.popleft()
			result = result + 1
			first_person = first_person - 1
			if index == k and first_person == 0:
				return result
			elif first_person != 0:
				queue.append([first_person , index])